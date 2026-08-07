#!/usr/bin/env python3
"""Static Agent Plugins 1.0.0 inspector; never executes plugin code.

The scanner finds one plugin root in a repository, checks high-confidence
manifest/MCP/path rules, and emits evidence leads. Human review remains
required for Agent Skill quality, client extensions, and contextual findings.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import urlsplit


PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
PLUGIN_FIELDS = {
    "$schema", "name", "version", "description", "author", "homepage",
    "repository", "license", "keywords", "extensions",
}
NAME_RE = re.compile(r"^(?=.{1,64}$)[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
NAMESPACE_RE = re.compile(r"^[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+$")
SKILL_NAME_RE = re.compile(r"^(?=.{1,64}$)[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
SECRET_KEY_RE = re.compile(
    r"(?:authorization|api[-_]?key|access[-_]?token|(?:^|[-_])token(?:$|[-_])|secret|password|passwd)", re.I
)
HEADER_NAME_RE = re.compile(r"^[!#$%&'*+.^_`|~0-9A-Za-z-]+$")


class Report:
    def __init__(self, target: Path) -> None:
        self.target = str(target)
        self.root: Path | None = None
        self.findings: list[dict[str, str]] = []
        self.skills = 0
        self.mcp_servers = 0
        self.extensions: list[str] = []

    def add(self, severity: str, code: str, path: str, message: str, spec: str) -> None:
        self.findings.append({
            "severity": severity,
            "code": code,
            "path": path,
            "message": message,
            "spec": spec,
        })

    @property
    def gate(self) -> str:
        severities = {item["severity"] for item in self.findings}
        if "fatal" in severities or "security" in severities:
            return "FAIL"
        if "partial" in severities:
            return "PARTIAL"
        return "PASS"

    def payload(self) -> dict[str, Any]:
        counts: dict[str, int] = {}
        for finding in self.findings:
            key = finding["severity"]
            counts[key] = counts.get(key, 0) + 1
        return {
            "target": self.target,
            "plugin_root": str(self.root) if self.root else None,
            "spec_version": "1.0.0",
            "gate": self.gate,
            "counts": counts,
            "inventory": {
                "skills": self.skills,
                "mcp_servers": self.mcp_servers,
                "extension_namespaces": self.extensions,
            },
            "findings": self.findings,
            "notice": "Static evidence leads only; confirm in source before scoring.",
        }


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root)) or "."
    except ValueError:
        return str(path)


def plugin_candidates(target: Path) -> list[Path]:
    if (target / "plugin.json").exists() or (target / "plugin.json").is_symlink():
        return [target]
    found: list[Path] = []
    for base, dirs, files in os.walk(target, followlinks=False):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv"}]
        base_path = Path(base)
        if "plugin.json" in files or (base_path / "plugin.json").is_symlink():
            found.append(base_path)
    return sorted(set(found))


def load_json(path: Path, report: Report, severity: str, code: str, spec: str) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.add(severity, code, str(path), f"Cannot parse JSON: {exc}", spec)
        return None


def contained(path: Path, root: Path) -> bool:
    try:
        path.resolve(strict=False).relative_to(root.resolve(strict=True))
        return True
    except (OSError, ValueError):
        return False


def check_symlinks(root: Path, report: Report) -> None:
    for base, dirs, files in os.walk(root, followlinks=False):
        for name in [*dirs, *files]:
            path = Path(base) / name
            if path.is_symlink() and not contained(path, root):
                report.add(
                    "partial", "PATH_ESCAPE", relative(path, root),
                    "Symlink resolves outside the plugin root.", "§4.1",
                )


def valid_name(name: Any) -> bool:
    return (
        isinstance(name, str)
        and bool(NAME_RE.fullmatch(name))
        and "--" not in name
        and ".." not in name
    )


def check_manifest(root: Path, report: Report) -> dict[str, Any] | None:
    path = root / "plugin.json"
    if not path.is_file() or not contained(path, root):
        report.add("fatal", "MANIFEST_MISSING", "plugin.json", "Root plugin.json is not a contained regular file.", "§4.1, §5.1")
        return None
    data = load_json(path, report, "fatal", "MANIFEST_JSON", "§5.2")
    if data is None:
        return None
    if not isinstance(data, dict):
        report.add("fatal", "MANIFEST_OBJECT", "plugin.json", "Manifest top level must be an object.", "§5.2")
        return None
    if data.get("$schema") != PLUGIN_SCHEMA:
        report.add("fatal", "PLUGIN_SCHEMA", "plugin.json#/$schema", f"Expected canonical Agent Plugins 1.0.0 schema {PLUGIN_SCHEMA}.", "§5.2")
    if not valid_name(data.get("name")):
        report.add("fatal", "PLUGIN_NAME", "plugin.json#/name", "Name violates the 1-64 character lowercase naming constraints.", "§5.3, §5.5")
    for key in sorted(set(data) - PLUGIN_FIELDS):
        report.add("partial", "UNKNOWN_MANIFEST_FIELD", f"plugin.json#/{key}", "Unknown top-level field is non-conforming and must be reported and ignored.", "§5.2")

    string_fields = {"version", "description", "homepage", "repository", "license"}
    for key in sorted(string_fields & set(data)):
        if not isinstance(data[key], str):
            report.add("fatal", "METADATA_TYPE", f"plugin.json#/{key}", "Metadata field must be a string.", "§5.4")
    if "keywords" in data and not (
        isinstance(data["keywords"], list)
        and all(isinstance(item, str) for item in data["keywords"])
    ):
        report.add("fatal", "KEYWORDS_TYPE", "plugin.json#/keywords", "keywords must be an array of strings.", "§5.4")
    if "author" in data:
        author = data["author"]
        if not isinstance(author, dict):
            report.add("fatal", "AUTHOR_TYPE", "plugin.json#/author", "author must be an object.", "§5.4")
        else:
            extra = set(author) - {"name", "email", "url"}
            if extra or any(not isinstance(value, str) for value in author.values()):
                report.add("fatal", "AUTHOR_FIELDS", "plugin.json#/author", "author may contain only string name, email, and url fields.", "§5.4")
    if "extensions" in data:
        extensions = data["extensions"]
        if not isinstance(extensions, dict):
            report.add("partial", "EXTENSIONS_OBJECT", "plugin.json#/extensions", "Non-object extensions is reported and ignored.", "§8.1")
        else:
            for namespace, value in extensions.items():
                report.extensions.append(namespace)
                if not NAMESPACE_RE.fullmatch(namespace):
                    report.add("partial", "EXTENSION_NAMESPACE", f"plugin.json#/extensions/{namespace}", "Extension key is not a clear reverse-domain namespace.", "§8")
                if not isinstance(value, dict):
                    report.add("partial", "EXTENSION_VALUE", f"plugin.json#/extensions/{namespace}", "Extension namespace value must be an object for a conforming package.", "§8.1")
    return data


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return None
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None
    result: dict[str, str] = {}
    body = lines[1:end]
    i = 0
    while i < len(body):
        line = body[i]
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            key, raw = match.groups()
            if raw in {">", "|", ">-", "|-", ">+", "|+"}:
                parts: list[str] = []
                i += 1
                while i < len(body) and (not body[i].strip() or body[i][0].isspace()):
                    parts.append(body[i].strip())
                    i += 1
                result[key] = "\n".join(parts).strip()
                continue
            result[key] = raw.strip("'\"")
        i += 1
    return result


def check_skills(root: Path, report: Report) -> None:
    skills = root / "skills"
    if not skills.exists() and not skills.is_symlink():
        return
    if not skills.is_dir() or not contained(skills, root):
        report.add("partial", "SKILLS_KIND", "skills", "Present skills path is not a contained directory.", "§6.2")
        return
    for child in sorted(skills.iterdir()):
        skill_file = child / "SKILL.md"
        if not child.is_dir() or not skill_file.is_file():
            continue
        report.skills += 1
        if not contained(skill_file, root):
            report.add("partial", "SKILL_ESCAPE", relative(skill_file, root), "Discovered SKILL.md resolves outside the plugin root.", "§4.1, §7.1")
            continue
        frontmatter = parse_frontmatter(skill_file)
        if frontmatter is None:
            report.add("partial", "SKILL_FRONTMATTER", relative(skill_file, root), "SKILL.md lacks parseable YAML frontmatter; run an Agent Skills validator.", "§7.1")
            continue
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if not name or not description:
            report.add("partial", "SKILL_REQUIRED", relative(skill_file, root), "Skill frontmatter is missing name or description.", "§7.1")
        if name and (not SKILL_NAME_RE.fullmatch(name) or "--" in name):
            report.add("partial", "SKILL_NAME_FORMAT", relative(skill_file, root), "Skill name violates Agent Skills naming constraints.", "§7.1 / Agent Skills")
        if len(description) > 1024:
            report.add("partial", "SKILL_DESCRIPTION", relative(skill_file, root), "Skill description exceeds 1024 characters.", "§7.1 / Agent Skills")
        if name and name != child.name:
            report.add("partial", "SKILL_NAME", relative(skill_file, root), "Skill frontmatter name does not match its immediate directory.", "§7.1")


def looks_like_secret(key: str, value: str) -> bool:
    if not SECRET_KEY_RE.search(key) or not value.strip():
        return False
    return "${" not in value and not re.search(r"(?:example|placeholder|replace|dummy|public)", value, re.I)


def check_stdio(name: str, server: dict[str, Any], root: Path, report: Report) -> None:
    pointer = f"mcp.json#/mcpServers/{name}"
    allowed = {"type", "command", "args", "env", "cwd"}
    if set(server) - allowed:
        report.add("partial", "MCP_STDIO_FIELDS", pointer, "stdio entry contains fields outside its closed variant.", "§7.2.1")
    command = server.get("command")
    if not isinstance(command, str) or not command:
        report.add("partial", "MCP_COMMAND", pointer + "/command", "stdio command must be a non-empty executable token.", "§7.2.1")
    elif "${" in command or (not command.startswith("./") and any(ch.isspace() for ch in command)) or command.startswith("../"):
        report.add("partial", "MCP_COMMAND_TOKEN", pointer + "/command", "command must be one bare or ./ plugin-relative token without placeholder expansion.", "§7.2.1")
    elif command.startswith("./") and not contained(root / command[2:], root):
        report.add("partial", "MCP_COMMAND_ESCAPE", pointer + "/command", "Plugin-relative command resolves outside the plugin root.", "§4.1, §7.2.1")
    args = server.get("args")
    if args is not None and not (isinstance(args, list) and all(isinstance(v, str) for v in args)):
        report.add("partial", "MCP_ARGS", pointer + "/args", "args must be an array of strings.", "§7.2.1")
    env = server.get("env")
    if env is not None:
        if not isinstance(env, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in env.items()):
            report.add("partial", "MCP_ENV", pointer + "/env", "env must be an object of string values.", "§7.2.1")
        else:
            for key, value in env.items():
                if key in {"PLUGIN_ROOT", "PLUGIN_DATA"}:
                    report.add("partial", "MCP_RESERVED_ENV", pointer + f"/env/{key}", "Reserved plugin environment variables are client-supplied.", "§9.2")
                if looks_like_secret(key, value):
                    report.add("warning", "POSSIBLE_SECRET", pointer + f"/env/{key}", "Possible embedded credential in visible env config (value redacted); confirm before assigning FAIL.", "§9.2")
    cwd = server.get("cwd")
    if cwd is not None:
        valid_form = isinstance(cwd, str) and (
            cwd.startswith("./")
            or cwd == "${PLUGIN_ROOT}" or cwd.startswith("${PLUGIN_ROOT}/")
            or cwd == "${PLUGIN_DATA}" or cwd.startswith("${PLUGIN_DATA}/")
        )
        if not valid_form:
            report.add("partial", "MCP_CWD", pointer + "/cwd", "cwd is not a permitted plugin/data-rooted form.", "§7.2.1")
        elif cwd.startswith("./") and not contained(root / cwd[2:], root):
            report.add("partial", "MCP_CWD_ESCAPE", pointer + "/cwd", "cwd resolves outside the plugin root.", "§4.1, §7.2.1")


def is_loopback(host: str | None) -> bool:
    if host == "localhost":
        return True
    if not host:
        return False
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def check_remote(name: str, server: dict[str, Any], report: Report) -> None:
    pointer = f"mcp.json#/mcpServers/{name}"
    if set(server) - {"type", "url", "headers"}:
        report.add("partial", "MCP_REMOTE_FIELDS", pointer, "Remote entry contains fields outside its closed variant.", "§7.2.1")
    raw_url = server.get("url")
    valid = isinstance(raw_url, str)
    try:
        parsed = urlsplit(raw_url) if valid else None
        hostname = parsed.hostname if parsed else None
        userinfo = bool(parsed and (parsed.username or parsed.password))
    except ValueError:
        parsed = None
        hostname = None
        userinfo = False
    if not valid or parsed is None or parsed.scheme not in {"http", "https"} or not hostname or userinfo or parsed.fragment:
        report.add("partial", "MCP_URL", pointer + "/url", "Remote URL must be absolute HTTP(S), without userinfo or fragment.", "§7.2.1")
    elif parsed.scheme == "http" and not is_loopback(hostname):
        report.add("partial", "MCP_TLS", pointer + "/url", "Non-loopback MCP endpoint must use HTTPS.", "§7.2.1")
    headers = server.get("headers")
    if headers is not None:
        if not isinstance(headers, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in headers.items()):
            report.add("partial", "MCP_HEADERS", pointer + "/headers", "headers must be an object of strings.", "§7.2.1")
        else:
            lowered: set[str] = set()
            for key, value in headers.items():
                if not HEADER_NAME_RE.fullmatch(key) or "\r" in value or "\n" in value:
                    report.add("partial", "MCP_HEADER_SYNTAX", pointer + f"/headers/{key}", "Header name or value is not a valid HTTP field.", "§7.2.1")
                if key.lower() in lowered:
                    report.add("partial", "MCP_HEADER_DUPLICATE", pointer + "/headers", "Header names duplicate case-insensitively.", "§7.2.1")
                lowered.add(key.lower())
                if looks_like_secret(key, value):
                    report.add("warning", "POSSIBLE_SECRET", pointer + f"/headers/{key}", "Possible embedded credential in visible headers (value redacted); confirm before assigning FAIL.", "§7.2.1")


def check_mcp(root: Path, report: Report) -> None:
    path = root / "mcp.json"
    if not path.exists() and not path.is_symlink():
        return
    if not path.is_file() or not contained(path, root):
        report.add("partial", "MCP_KIND", "mcp.json", "Present mcp.json is not a contained regular file.", "§6.2")
        return
    data = load_json(path, report, "partial", "MCP_JSON", "§7.2.2")
    if data is None:
        return
    if not isinstance(data, dict):
        report.add("partial", "MCP_OBJECT", "mcp.json", "MCP top level must be an object.", "§7.2.1")
        return
    if set(data) != {"$schema", "mcpServers"}:
        report.add("partial", "MCP_TOP_LEVEL", "mcp.json", "MCP top level must contain exactly $schema and mcpServers.", "§7.2.1")
    if data.get("$schema") != MCP_SCHEMA:
        report.add("partial", "MCP_SCHEMA", "mcp.json#/$schema", f"Expected canonical matching schema {MCP_SCHEMA}.", "§7.2.1, §10.1")
    servers = data.get("mcpServers")
    if not isinstance(servers, dict):
        report.add("partial", "MCP_SERVERS", "mcp.json#/mcpServers", "mcpServers must be an object.", "§7.2.1")
        return
    report.mcp_servers = len(servers)
    for name, server in servers.items():
        pointer = f"mcp.json#/mcpServers/{name}"
        if not isinstance(server, dict):
            report.add("partial", "MCP_SERVER_OBJECT", pointer, "Server entry must be an object.", "§7.2.1")
            continue
        server_type = server.get("type")
        if server_type == "stdio":
            check_stdio(name, server, root, report)
        elif server_type in {"streamable-http", "sse"}:
            check_remote(name, server, report)
        else:
            report.add("partial", "MCP_SERVER_TYPE", pointer + "/type", "Unknown or missing MCP transport type.", "§7.2.1")


def inspect(target: Path) -> Report:
    report = Report(target)
    if not target.is_dir():
        report.add("fatal", "TARGET", str(target), "Target is not a directory.", "Package model")
        return report
    candidates = plugin_candidates(target)
    if len(candidates) != 1:
        report.add("fatal", "PLUGIN_ROOT_AMBIGUOUS", str(target), f"Expected exactly one plugin root; found {len(candidates)}.", "§4, §5.1")
        return report
    root = candidates[0].resolve(strict=True)
    report.root = root
    check_symlinks(root, report)
    check_manifest(root, report)
    check_skills(root, report)
    check_mcp(root, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    report = inspect(args.target.expanduser().resolve(strict=False))
    payload = report.payload()
    if args.as_json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"gate: {payload['gate']}")
        print(f"plugin root: {payload['plugin_root'] or 'unresolved'}")
        print(f"skills: {payload['inventory']['skills']}")
        print(f"MCP servers: {payload['inventory']['mcp_servers']}")
        for item in payload["findings"]:
            print(f"[{item['severity'].upper()}] {item['code']} {item['path']}: {item['message']} ({item['spec']})")
    return {"PASS": 0, "PARTIAL": 1, "FAIL": 2}[report.gate]


if __name__ == "__main__":
    sys.exit(main())
