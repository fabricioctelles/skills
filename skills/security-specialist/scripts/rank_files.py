#!/usr/bin/env python3
"""Rank repository files by security relevance for analysis prioritization."""

import argparse
import json
import subprocess
from pathlib import Path

SKIP_DIRS = {"node_modules", "vendor", ".git", "__pycache__", "dist", "build", ".next", "coverage", ".venv", "venv"}
SKIP_PATTERNS = {"test", "tests", "spec", "specs", "__tests__", "fixtures", "mocks", "generated"}

HIGH_KEYWORDS = ("auth", "login", "session", "token", "password", "secret", "crypto", "permission")
MEDIUM_HIGH_KEYWORDS = ("api", "handler", "controller", "route", "endpoint", "middleware")
MEDIUM_KEYWORDS = ("config", "env", "settings", "database", "migration")

CODE_EXTENSIONS = {".py", ".js", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".rb", ".php", ".c", ".cpp", ".h", ".cs", ".yml", ".yaml", ".toml", ".json", ".env"}


def _should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    return bool(parts & SKIP_PATTERNS)


def _score(path: str) -> tuple[int, str]:
    low = path.lower()
    for kw in HIGH_KEYWORDS:
        if kw in low:
            return 5, f"contains '{kw}' — security-sensitive"
    for kw in MEDIUM_HIGH_KEYWORDS:
        if kw in low:
            return 4, f"contains '{kw}' — attack surface"
    for kw in MEDIUM_KEYWORDS:
        if kw in low:
            return 3, f"contains '{kw}' — configuration"
    return 1, "general code"


def cmd_from_repo(args: argparse.Namespace) -> None:
    """Walk repo and score all code files."""
    repo = Path(args.repo).resolve()
    results = []
    for f in repo.rglob("*"):
        if not f.is_file() or f.suffix not in CODE_EXTENSIONS:
            continue
        rel = f.relative_to(repo)
        if _should_skip(rel):
            continue
        priority, reason = _score(str(rel))
        results.append({"path": str(rel), "priority": priority, "reason": reason})
    results.sort(key=lambda x: -x["priority"])
    Path(args.out).write_text(json.dumps(results, indent=2))
    print(f"Ranked {len(results)} files → {args.out}")


def cmd_from_diff(args: argparse.Namespace) -> None:
    """Rank files changed between two git refs."""
    repo = Path(args.repo).resolve()
    result = subprocess.run(
        ["git", "diff", "--name-only", args.base, args.head],
        capture_output=True, text=True, cwd=str(repo), check=True,
    )
    results = []
    for line in result.stdout.strip().splitlines():
        rel = Path(line)
        if _should_skip(rel) or rel.suffix not in CODE_EXTENSIONS:
            continue
        priority, reason = _score(line)
        results.append({"path": line, "priority": priority, "reason": reason})
    results.sort(key=lambda x: -x["priority"])
    Path(args.out).write_text(json.dumps(results, indent=2))
    print(f"Ranked {len(results)} changed files → {args.out}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank files by security relevance")
    sub = parser.add_subparsers(dest="command", required=True)

    p_repo = sub.add_parser("from-repo")
    p_repo.add_argument("--repo", required=True)
    p_repo.add_argument("--out", required=True)

    p_diff = sub.add_parser("from-diff")
    p_diff.add_argument("--repo", required=True)
    p_diff.add_argument("--base", required=True)
    p_diff.add_argument("--head", required=True)
    p_diff.add_argument("--out", required=True)

    args = parser.parse_args()
    {"from-repo": cmd_from_repo, "from-diff": cmd_from_diff}[args.command](args)


if __name__ == "__main__":
    main()
