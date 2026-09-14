#!/usr/bin/env python3
"""Generated Looper runner.

This file executes a resolved loop spec. It intentionally reads only
loop.resolved.json and uses only Python stdlib.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import fnmatch
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any


PASS = "pass"
REVISE = "revise"

DEFAULT_REDACTIONS = [".env", ".env.*", "secrets/**", "**/*.key"]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}


class RunnerError(RuntimeError):
    pass


def utc_now() -> str:
    return _dt.datetime.now(_dt.UTC).replace(microsecond=0).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except OSError as exc:
        raise RunnerError(f"Could not read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RunnerError(f"Could not parse JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise RunnerError(f"{path} must contain a JSON object")
    return data


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ensure_argv(value: Any, field: str) -> list[str]:
    if isinstance(value, list) and value and all(isinstance(item, str) for item in value):
        return value
    raise RunnerError(f"{field} must be a non-empty argv array")


def relative_to_base(path_text: str, base_dir: Path) -> Path:
    path = Path(path_text)
    resolved = path if path.is_absolute() else base_dir / path
    try:
        resolved.resolve().relative_to(base_dir.resolve())
    except ValueError:
        raise RunnerError(
            f"Path {path_text!r} escapes the loop directory {base_dir}; "
            "workspace and context paths must stay inside the loop directory"
        ) from None
    return resolved


def is_redacted(path: Path, base_dir: Path, globs: list[str]) -> bool:
    try:
        rel = path.resolve().relative_to(base_dir.resolve()).as_posix()
    except ValueError:
        rel = path.name
    # Match each pattern against the relative path and every path suffix so
    # bare patterns like ".env" also cover nested files like "config/.env".
    parts = rel.split("/")
    suffixes = {"/".join(parts[i:]) for i in range(len(parts))}
    for pattern in globs:
        normalized = pattern[3:] if pattern.startswith("**/") else pattern
        if any(fnmatch.fnmatch(candidate, normalized) for candidate in suffixes):
            return True
    return False


def run_argv(
    argv: list[str],
    *,
    cwd: Path,
    timeout_sec: int,
    stdin: str = "",
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            argv,
            input=stdin,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            errors="replace",
            cwd=str(cwd),
            timeout=timeout_sec,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        completed = subprocess.CompletedProcess(argv, 124, exc.stdout or "", exc.stderr or "")
        return completed
    except OSError as exc:
        return subprocess.CompletedProcess(argv, 127, "", str(exc))


def call_model(member: dict[str, Any], prompt: str, base_dir: Path) -> str:
    argv = ensure_argv(member.get("invoke"), f"{member.get('id', member.get('cli', 'model'))}.invoke")
    timeout_sec = int(member.get("timeout_sec", 600))
    result = run_argv(argv, cwd=base_dir, timeout_sec=timeout_sec, stdin=prompt)
    if result.returncode != 0:
        raise RunnerError(
            f"Model invocation failed ({' '.join(argv)}): exit {result.returncode}\n{result.stderr}"
        )
    return result.stdout.strip()


def parse_judge_output(text: str) -> dict[str, Any]:
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    candidate = fenced.group(1) if fenced else text.strip()
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return {
            "verdict": REVISE,
            "blocking_issues": ["Judge output was not parseable JSON."],
            "confidence": 0.0,
            "notes": text.strip(),
            "warning": "unparseable_judge_output",
        }
    if not isinstance(parsed, dict):
        return {
            "verdict": REVISE,
            "blocking_issues": ["Judge output was not a JSON object."],
            "confidence": 0.0,
            "notes": text.strip(),
            "warning": "invalid_judge_output",
        }
    verdict = parsed.get("verdict")
    if verdict not in {PASS, REVISE}:
        parsed["verdict"] = REVISE
        parsed.setdefault("blocking_issues", []).append("Judge verdict was not pass or revise.")
    parsed.setdefault("blocking_issues", [])
    parsed.setdefault("confidence", 0.0)
    parsed.setdefault("notes", "")
    return parsed


class Runner:
    def __init__(self, spec_path: Path) -> None:
        self.spec_path = spec_path.resolve()
        self.base_dir = self.spec_path.parent
        self.spec = load_json(self.spec_path)
        self.workspace = relative_to_base(self.spec["workspace"]["dir"], self.base_dir)
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.observability = self.spec.get("observability", {})
        self.run_log_path = self.workspace / self.observability.get("run_log", "run-log.md")
        self.state_path = self.workspace / self.observability.get("state_file", "state.json")
        self.state = self.load_state()
        self.started = time.monotonic()
        # Per-run caches for the scrub layer: flagged-file contents are read
        # once per glob set, surfaced events are logged once per destination.
        self._flagged_cache: dict[tuple[str, ...], list[tuple[str, str]]] = {}
        self._unscrubbable_reported: set[str] = set()
        self._surfaced_events: set[tuple[str, tuple[str, ...]]] = set()

    def load_state(self) -> dict[str, Any]:
        if self.state_path.exists():
            return load_json(self.state_path)
        return {
            "status": "initialized",
            "started_at": utc_now(),
            "iteration": 0,
            "warnings": [],
            "consent": {},
        }

    def save_state(self, **updates: Any) -> None:
        self.state.update(updates)
        self.state["updated_at"] = utc_now()
        write_json(self.state_path, self.state)

    def append_log(self, event: str, **fields: Any) -> None:
        self.run_log_path.parent.mkdir(parents=True, exist_ok=True)
        payload = f" {json.dumps(fields, sort_keys=True)}" if fields else ""
        with self.run_log_path.open("a", encoding="utf-8") as fh:
            fh.write(f"- {utc_now()} `{event}`{payload}\n")

    def enforce_wall_clock(self) -> None:
        budget = self.spec.get("loop_control", {}).get("budget", {})
        wall_clock_min = budget.get("wall_clock_min")
        if wall_clock_min is None:
            return
        if time.monotonic() - self.started > float(wall_clock_min) * 60:
            self.save_state(status="failed", failure="wall_clock_budget_exceeded")
            self.append_log("stop", reason="wall_clock_budget_exceeded")
            raise RunnerError("Wall-clock budget exceeded")

    def no_progress_reached(self, gate_name: str, failures: list[str]) -> bool:
        if not failures:
            self.save_state(no_progress={"count": 0, "signature": "", "gate": gate_name})
            return False
        config = self.spec.get("loop_control", {}).get("no_progress", {})
        threshold = int(config.get("max_stalled_iterations", 2))
        signature = "\n".join(sorted(failures))
        previous = self.state.get("no_progress", {})
        same_gate = previous.get("gate") == gate_name
        same_signature = previous.get("signature") == signature
        count = int(previous.get("count", 0)) + 1 if same_gate and same_signature else 1
        progress = {
            "gate": gate_name,
            "signature": signature,
            "count": count,
            "threshold": threshold,
            "updated_at": utc_now(),
        }
        self.save_state(no_progress=progress)
        if count < threshold:
            return False
        self.append_log("no_progress_detected", gate=gate_name, count=count, failures=failures)
        if config.get("action", "stop") == "human_checkpoint":
            answer = input("No-progress detected. Type 'continue' to allow one more revision: ").strip().lower()
            if answer == "continue":
                progress["count"] = 0
                self.save_state(no_progress=progress)
                self.append_log("no_progress_override", gate=gate_name)
                return False
        self.save_state(status="failed", failure="no_progress_detected", blocking_issues=failures)
        return True

    def criteria(self, ids: list[str]) -> list[dict[str, Any]]:
        by_id = self.spec.get("criteria_by_id", {})
        return [by_id[item] for item in ids]

    def member(self, member_id: str) -> dict[str, Any]:
        return self.spec["council_by_id"][member_id]

    def redactions_for(self, member_id: str) -> list[str]:
        # Defaults always apply; configured egress redactions extend them.
        redactions = list(DEFAULT_REDACTIONS)
        for entry in self.spec.get("privacy", {}).get("egress", []):
            if entry.get("to") == member_id:
                for pattern in entry.get("redact", []):
                    if pattern not in redactions:
                        redactions.append(pattern)
        return redactions

    def all_redaction_globs(self) -> list[str]:
        globs = list(DEFAULT_REDACTIONS)
        for entry in self.spec.get("privacy", {}).get("egress", []):
            for pattern in entry.get("redact", []):
                if pattern not in globs:
                    globs.append(pattern)
        return globs

    def iter_redaction_files(self, globs: list[str]):
        for root, dirs, files in os.walk(self.base_dir):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in files:
                path = Path(root) / name
                if is_redacted(path, self.base_dir, globs):
                    yield path

    def flagged_file_contents(self, globs: list[str]) -> list[tuple[str, str]]:
        """Read flagged files once per glob set; surface the unreadable ones.

        A flagged file the scrub cannot read (too large, not UTF-8) cannot be
        detected if its content leaks, so that blind spot is reported instead
        of silently skipped.
        """
        key = tuple(sorted(globs))
        if key in self._flagged_cache:
            return self._flagged_cache[key]
        contents: list[tuple[str, str]] = []
        for path in self.iter_redaction_files(globs):
            rel = path.relative_to(self.base_dir).as_posix()
            reason = ""
            try:
                if path.stat().st_size > 1_000_000:
                    reason = "larger than 1MB"
                else:
                    secret_text = path.read_text(encoding="utf-8")
                    if secret_text.strip():
                        contents.append((rel, secret_text))
                    continue
            except UnicodeDecodeError:
                reason = "not valid UTF-8"
            except OSError as exc:
                reason = f"unreadable ({exc})"
            if reason and rel not in self._unscrubbable_reported:
                self._unscrubbable_reported.add(rel)
                self.append_log("redaction_unscrubbable", source=rel, reason=reason)
                self.add_state_warning(
                    f"flagged file {rel} is {reason}; its content cannot be "
                    "detected by the scrub layer if it leaks into artifacts"
                )
        self._flagged_cache[key] = contents
        return contents

    def scrub_flagged_content(self, text: str, globs: list[str]) -> tuple[str, list[str]]:
        """Remove content originating from redaction-glob files.

        The flagged files themselves are never read into prompts (path-based
        non-send in gather_context); this second layer catches their content
        when it re-surfaces elsewhere - a cmd context source that printed it,
        or an artifact a model copied it into. Returns the scrubbed text and
        the relative paths whose content was found. Best effort by design,
        erring toward over-redaction: reformatted content or lines shorter
        than 8 characters can survive, and a flagged-file line that
        legitimately appears elsewhere is masked too.
        """
        original = text
        hits: list[str] = []
        for rel, secret_text in self.flagged_file_contents(globs):
            marker = f"[redacted:{rel}]"
            # Detect against the original text so a secret shared by two
            # flagged files attributes both, not just the first replaced.
            lines = [line.strip() for line in secret_text.splitlines() if len(line.strip()) >= 8]
            if secret_text in original or any(line in original for line in lines):
                hits.append(rel)
            text = text.replace(secret_text, marker)
            for line in lines:
                text = text.replace(line, marker)
        return text, hits

    def add_state_warning(self, note: str) -> None:
        warnings = list(self.state.get("warnings", []) or [])
        if note not in warnings:
            warnings.append(note)
            self.save_state(warnings=warnings)

    def surface_redaction(self, where: str, hits: list[str]) -> None:
        if not hits:
            return
        event_key = (where, tuple(hits))
        if event_key not in self._surfaced_events:
            self._surfaced_events.add(event_key)
            self.append_log("redaction_applied", where=where, sources=hits)
        self.add_state_warning(
            f"flagged content from {', '.join(hits)} appeared in {where}; "
            "scrubbed before use"
        )

    def redact_prompt_for_member(self, member_id: str, prompt: str) -> str:
        scrubbed, hits = self.scrub_flagged_content(prompt, self.redactions_for(member_id))
        self.surface_redaction(f"prompt for {member_id}", hits)
        return scrubbed

    def ensure_consent(self, member_id: str) -> None:
        member = self.member(member_id)
        if member.get("local"):
            return
        if self.state.get("consent", {}).get(member_id):
            return
        matching = [
            entry
            for entry in self.spec.get("privacy", {}).get("egress", [])
            if entry.get("to") == member_id
        ]
        # Consent fails closed: a non-local member always needs consent unless
        # every egress entry for it explicitly pre-grants with consent: granted.
        if matching and all(entry.get("consent") == "granted" for entry in matching):
            return
        sends = sorted({item for entry in matching for item in entry.get("sends", [])})
        redactions = self.redactions_for(member_id)
        print()
        print(f"Looper is about to send {', '.join(sends) or 'loop artifacts'} to {member_id}.")
        print(f"CLI: {member.get('cli')} / model: {member.get('model', 'default')}")
        print(f"Redactions: {', '.join(redactions)}")
        for note in self.state.get("warnings", []) or []:
            if f"prompt for {member_id}" in note:
                print(f"Warning: {note}")
        if not matching:
            print("No privacy.egress entry covers this member; consent is required by default.")
        answer = input("Type 'yes' to consent to this first send: ").strip().lower()
        if answer != "yes":
            self.save_state(status="blocked", failure=f"consent_refused:{member_id}")
            raise RunnerError(f"Consent refused for {member_id}")
        consent = dict(self.state.get("consent", {}))
        consent[member_id] = {"granted_at": utc_now(), "sends": sends, "redact": redactions}
        self.save_state(consent=consent)

    def gather_context(self) -> str:
        goal = self.spec["goal"]
        redaction_globs = self.all_redaction_globs()
        chunks: list[str] = []
        for index, source in enumerate(goal.get("context_sources", []), start=1):
            self.enforce_wall_clock()
            if "file" in source:
                try:
                    path = relative_to_base(source["file"], self.base_dir)
                except RunnerError:
                    chunks.append(f"## Context source {index}: {source['file']}\n[blocked: outside loop directory]\n")
                    self.append_log("context", source=source["file"], status="blocked_outside_base")
                    continue
                if is_redacted(path, self.base_dir, redaction_globs):
                    chunks.append(f"## Context source {index}: {source['file']}\n[redacted]\n")
                    self.append_log("context", source=source["file"], status="redacted")
                elif path.exists():
                    chunks.append(f"## Context source {index}: {source['file']}\n{path.read_text(encoding='utf-8')}\n")
                    self.append_log("context", source=source["file"], status="read")
                else:
                    chunks.append(f"## Context source {index}: {source['file']}\n[missing]\n")
                    self.append_log("context", source=source["file"], status="missing")
            elif "cmd" in source:
                argv = ensure_argv(source["cmd"], f"context_sources[{index}].cmd")
                result = run_argv(argv, cwd=self.base_dir, timeout_sec=int(source.get("timeout_sec", 60)))
                # Command output can reproduce flagged-file content (cat, git
                # log, env dumps); scrub it before it enters any prompt.
                block = (
                    f"exit={result.returncode}\nstdout:\n{result.stdout}\n"
                    f"stderr:\n{result.stderr}\n"
                )
                block, hits = self.scrub_flagged_content(block, redaction_globs)
                self.surface_redaction(f"context command output ({' '.join(argv)})", hits)
                chunks.append(f"## Context source {index}: {' '.join(argv)}\n{block}")
                self.append_log("context_cmd", argv=argv, returncode=result.returncode)
        context = "\n".join(chunks).strip()
        write_text(self.workspace / "context.md", context or "No context sources configured.")
        return context

    def host_prompt(self, phase: str, artifact: str = "", review: str = "") -> str:
        goal = self.spec["goal"]
        if phase == "plan":
            return (
                "Draft plan.md for this loop.\n\n"
                f"Goal:\n{goal['statement']}\n\n"
                f"Definition of done:\n{goal['definition_of_done']}\n\n"
                f"Context:\n{(self.workspace / 'context.md').read_text(encoding='utf-8')}\n"
            )
        if phase == "delivery":
            return (
                "Write the next delivery artifact for this loop.\n\n"
                f"Goal:\n{goal['statement']}\n\n"
                f"Definition of done:\n{goal['definition_of_done']}\n\n"
                f"Plan:\n{(self.workspace / 'plan.md').read_text(encoding='utf-8')}\n"
            )
        if phase == "revise":
            return (
                "Revise the artifact to address the review. Return only the revised artifact.\n\n"
                f"Artifact:\n{artifact}\n\nReview:\n{review}\n"
            )
        raise RunnerError(f"Unknown host phase: {phase}")

    def run_host(self, phase: str, target: Path, artifact: str = "", review: str = "") -> None:
        self.enforce_wall_clock()
        self.append_log("host_start", phase=phase, target=target.name)
        output = call_model(self.spec["host"], self.host_prompt(phase, artifact, review), self.base_dir)
        write_text(target, output)
        self.append_log("host_done", phase=phase, target=target.name)

    def run_programmatic(self, criterion: dict[str, Any]) -> dict[str, Any]:
        argv = ensure_argv(criterion["check"], f"{criterion['id']}.check")
        result = run_argv(argv, cwd=self.base_dir, timeout_sec=int(criterion.get("timeout_sec", 300)))
        expect = criterion.get("expect")
        passed = False
        if expect == "exit_zero":
            passed = result.returncode == 0
        elif expect == "exit_nonzero":
            passed = result.returncode != 0
        elif expect == "stdout_contains":
            passed = criterion.get("contains", "") in result.stdout
        self.append_log(
            "programmatic_check",
            criterion=criterion["id"],
            passed=passed,
            returncode=result.returncode,
        )
        return {
            "id": criterion["id"],
            "type": "programmatic",
            "passed": passed,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }

    def judge_prompt(
        self,
        gate_name: str,
        artifact_label: str,
        artifact_text: str,
        criteria: list[dict[str, Any]],
    ) -> str:
        rubric_lines = []
        for criterion in criteria:
            if criterion["type"] == "judge":
                rubric_lines.append(f"- {criterion['id']}: {criterion['rubric']}")
            elif criterion["type"] == "programmatic":
                rubric_lines.append(f"- {criterion['id']}: programmatic check result is included below.")
            elif criterion["type"] == "human":
                rubric_lines.append(f"- {criterion['id']}: human signoff is required separately.")
        return (
            "You are the Looper judge. Return only a fenced JSON object with keys "
            "verdict, blocking_issues, confidence, and notes. verdict must be pass or revise.\n\n"
            f"Gate: {gate_name}\n"
            f"Artifact: {artifact_label}\n\n"
            "Criteria:\n" + "\n".join(rubric_lines) + "\n\n"
            f"Artifact content:\n{artifact_text}\n"
        )

    def run_judge(
        self,
        member_id: str,
        gate_name: str,
        artifact_label: str,
        artifact_text: str,
        criteria: list[dict[str, Any]],
    ) -> dict[str, Any]:
        # Scrub (and surface any leak) before asking for consent, so the
        # consent decision is made with the leak warning already visible.
        prompt = self.redact_prompt_for_member(
            member_id,
            self.judge_prompt(gate_name, artifact_label, artifact_text, criteria),
        )
        self.ensure_consent(member_id)
        output = call_model(self.member(member_id), prompt, self.base_dir)
        verdict = parse_judge_output(output)
        verdict["member"] = member_id
        self.append_log("judge_verdict", gate=gate_name, member=member_id, verdict=verdict.get("verdict"))
        return verdict

    def run_reviewers(
        self,
        gate_name: str,
        artifact_label: str,
        artifact_text: str,
        member_ids: list[str],
    ) -> list[str]:
        notes = []
        for member_id in member_ids:
            member = self.member(member_id)
            if member.get("role") != "reviewer":
                continue
            prompt = (
                "You are a Looper reviewer. Return concise blocking and non-blocking notes. "
                "Do not return a verdict.\n\n"
                f"Gate: {gate_name}\nArtifact: {artifact_label}\n\n{artifact_text}\n"
            )
            prompt = self.redact_prompt_for_member(member_id, prompt)
            self.ensure_consent(member_id)
            notes.append(f"## {member_id}\n\n{call_model(member, prompt, self.base_dir)}")
            self.append_log("reviewer_notes", gate=gate_name, member=member_id)
        return notes

    def human_check(self, criterion: dict[str, Any]) -> dict[str, Any]:
        print()
        print(criterion["prompt"])
        answer = input("Type 'pass' to approve, anything else to request revision: ").strip().lower()
        return {
            "id": criterion["id"],
            "type": "human",
            "passed": answer == PASS,
            "notes": "approved" if answer == PASS else "human requested revision",
        }

    def run_gate(self, gate_name: str, artifact_path: Path, artifact_label: str) -> bool:
        gate = self.spec["gates"][gate_name]
        criteria = self.criteria(gate.get("criteria", []))
        max_revisions = int(gate.get("max_revisions", 0))
        revision = 0
        self.append_log("gate_start", gate=gate_name, artifact=artifact_label)

        while True:
            self.enforce_wall_clock()
            artifact_text = artifact_path.read_text(encoding="utf-8")
            review_parts: list[str] = []
            failures: list[str] = []

            for criterion in criteria:
                if criterion["type"] == "programmatic":
                    result = self.run_programmatic(criterion)
                    review_parts.append(f"## Programmatic {criterion['id']}\n\n```json\n{json.dumps(result, indent=2)}\n```")
                    if not result["passed"]:
                        failures.append(f"Programmatic check failed: {criterion['id']}")
                elif criterion["type"] == "human":
                    result = self.human_check(criterion)
                    review_parts.append(f"## Human {criterion['id']}\n\n{result['notes']}")
                    if not result["passed"]:
                        failures.append(f"Human check failed: {criterion['id']}")

            reviewer_notes = self.run_reviewers(
                gate_name,
                artifact_label,
                artifact_text,
                list(gate.get("members", [])),
            )
            review_parts.extend(reviewer_notes)

            policy = gate.get("verdict_policy")
            verdict: dict[str, Any] | None = None
            if policy == "revise_until_clean" and not failures:
                source = gate.get("verdict_source")
                if source == "human":
                    answer = input(f"Type 'pass' if {artifact_label} is clean: ").strip().lower()
                    verdict = {
                        "verdict": PASS if answer == PASS else REVISE,
                        "blocking_issues": [] if answer == PASS else ["human requested revision"],
                        "confidence": 1.0,
                        "notes": "human verdict",
                    }
                else:
                    verdict = self.run_judge(source, gate_name, artifact_label, artifact_text, criteria)
                review_parts.append(f"## Verdict\n\n```json\n{json.dumps(verdict, indent=2)}\n```")
                if verdict.get("verdict") == REVISE:
                    failures.extend(verdict.get("blocking_issues") or ["Judge requested revision"])

            if policy == "fixed_passes":
                if failures:
                    pass
                elif revision >= max_revisions:
                    return True
                else:
                    failures.append("fixed_passes reviewer pass")

            if not failures:
                self.save_state(status=f"{gate_name}_passed", **{gate_name: {"passed_at": utc_now()}})
                self.append_log("gate_passed", gate=gate_name, artifact=artifact_label)
                return True

            review_text = "\n\n".join(review_parts + ["## Blocking Issues", "\n".join(f"- {item}" for item in failures)])
            review_path = self.workspace / f"review-{gate_name}-{revision + 1}.md"
            write_text(review_path, review_text)
            self.append_log("gate_blocked", gate=gate_name, review=review_path.name, failures=failures)

            if self.no_progress_reached(gate_name, failures):
                return False

            if revision >= max_revisions:
                self.save_state(
                    status="failed",
                    failure=f"{gate_name}_max_revisions_reached",
                    last_review=str(review_path),
                )
                self.append_log("stop", reason=f"{gate_name}_max_revisions_reached")
                return False

            revised = call_model(
                self.spec["host"],
                self.host_prompt("revise", artifact_text, review_text),
                self.base_dir,
            )
            write_text(artifact_path, revised)
            revision += 1
            self.save_state(status=f"{gate_name}_revision_{revision}", last_review=str(review_path))
            self.append_log("revision", gate=gate_name, revision=revision, artifact=artifact_label)

    def run(self) -> int:
        self.save_state(status="running")
        self.append_log("run_start", spec=str(self.spec_path))
        self.gather_context()

        plan_path = self.workspace / "plan.md"
        if not plan_path.exists():
            self.run_host("plan", plan_path)
        if not self.run_gate("plan_gate", plan_path, "plan.md"):
            return 1

        max_iterations = int(self.spec["loop_control"]["max_iterations"])
        for iteration in range(1, max_iterations + 1):
            self.enforce_wall_clock()
            self.save_state(status="delivery", iteration=iteration)
            delivery_path = self.workspace / f"delivery-{iteration}.md"
            self.run_host("delivery", delivery_path)
            if self.run_gate("delivery_gate", delivery_path, delivery_path.name):
                self.save_state(status="passed", final_delivery=str(delivery_path), completed_at=utc_now())
                self.append_log("run_passed", final_delivery=str(delivery_path))
                print(f"Looper run passed. Final delivery: {delivery_path}")
                return 0

        self.save_state(status="failed", failure="max_iterations_reached")
        self.append_log("stop", reason="max_iterations_reached")
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a compiled Looper loop.")
    parser.add_argument(
        "spec_path",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("loop.resolved.json"),
        help="Path to loop.resolved.json (defaults to the file next to run-loop.py).",
    )
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        return Runner(args.spec_path).run()
    except RunnerError as exc:
        print(f"run-loop: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
