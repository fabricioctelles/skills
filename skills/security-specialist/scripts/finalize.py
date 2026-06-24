#!/usr/bin/env python3
"""Seal a security scan and generate final reports."""

import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def _connect(scan_dir: Path) -> sqlite3.Connection:
    db_path = scan_dir / "scan.db"
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}")
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def _get_active_scan(conn: sqlite3.Connection) -> dict:
    row = conn.execute("SELECT * FROM scans WHERE status = 'active' ORDER BY started_at DESC LIMIT 1").fetchone()
    if not row:
        raise SystemExit("No active scan found to seal.")
    return dict(row)


def _seal(conn: sqlite3.Connection, scan_id: str) -> None:
    now = datetime.now(timezone.utc).isoformat()
    conn.execute("UPDATE scans SET sealed_at = ?, status = 'sealed' WHERE id = ?", (now, scan_id))
    conn.commit()


def _export_findings(conn: sqlite3.Connection, scan_id: str, scan_dir: Path) -> list[dict]:
    rows = conn.execute("SELECT * FROM findings WHERE scan_id = ? ORDER BY severity, file_path", (scan_id,)).fetchall()
    findings = [dict(r) for r in rows]
    (scan_dir / "findings.json").write_text(json.dumps(findings, indent=2))
    return findings


def _severity_order(sev: str) -> int:
    return {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}.get(sev, 5)


def _generate_report(findings: list[dict], scan: dict, scan_dir: Path) -> None:
    counts: dict[str, int] = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    total = len(findings)

    lines = ["# Security Scan Report\n"]
    lines.append(f"**Repository:** `{scan['repo_path']}`  ")
    lines.append(f"**Scan ID:** `{scan['id']}`  ")
    lines.append(f"**Started:** {scan['started_at']}  ")
    lines.append(f"**Sealed:** {scan['sealed_at']}\n")

    # Executive summary
    lines.append("## Executive Summary\n")
    if total == 0:
        lines.append("No findings were recorded during this scan.\n")
    else:
        lines.append(f"This scan identified **{total} finding(s)** across the repository:\n")
        for sev in sorted(counts, key=_severity_order):
            emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🔵", "info": "⚪"}.get(sev, "·")
            lines.append(f"- {emoji} **{sev.capitalize()}:** {counts[sev]}")
        lines.append("")
        if counts.get("critical", 0) > 0:
            lines.append("⚠️  Critical findings require immediate attention before deployment.\n")

    # Findings table
    if findings:
        lines.append("## Findings Overview\n")
        lines.append("| # | Severity | Category | File | Status | Title |")
        lines.append("|---|----------|----------|------|--------|-------|")
        for i, f in enumerate(sorted(findings, key=lambda x: _severity_order(x["severity"])), 1):
            loc = f"`{f['file_path']}:{f['line_number']}`" if f["file_path"] else "—"
            lines.append(f"| {i} | {f['severity']} | {f['category']} | {loc} | {f['status']} | {f['title']} |")
        lines.append("")

    # Detailed findings
    if findings:
        lines.append("## Detailed Findings\n")
        for i, f in enumerate(sorted(findings, key=lambda x: _severity_order(x["severity"])), 1):
            lines.append(f"### {i}. {f['title']}\n")
            lines.append(f"- **Severity:** {f['severity']}")
            lines.append(f"- **Category:** {f['category']}")
            lines.append(f"- **Status:** {f['status']}")
            if f["file_path"]:
                lines.append(f"- **Location:** `{f['file_path']}:{f['line_number']}`")
            if f["tracking_url"]:
                lines.append(f"- **Tracking:** {f['tracking_url']}")
            lines.append(f"\n{f['description']}\n")
            if f["evidence"]:
                lines.append("**Evidence:**\n")
                lines.append(f"```\n{f['evidence']}\n```\n")

    (scan_dir / "report.md").write_text("\n".join(lines))


def _write_integrity(scan_dir: Path) -> str:
    content = (scan_dir / "findings.json").read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    (scan_dir / "integrity.sha256").write_text(f"{digest}  findings.json\n")
    return digest


def main() -> None:
    parser = argparse.ArgumentParser(description="Seal scan and generate reports")
    parser.add_argument("--scan-dir", required=True, help="Path to .security/ directory")
    args = parser.parse_args()

    scan_dir = Path(args.scan_dir).resolve()
    conn = _connect(scan_dir)
    scan = _get_active_scan(conn)
    _seal(conn, scan["id"])
    scan["sealed_at"] = datetime.now(timezone.utc).isoformat()

    findings = _export_findings(conn, scan["id"], scan_dir)
    _generate_report(findings, scan, scan_dir)
    digest = _write_integrity(scan_dir)
    conn.close()

    total = len(findings)
    counts = {}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    print(f"Scan sealed: {scan['id']}")
    print(f"Findings: {total} total — " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items(), key=lambda x: _severity_order(x[0]))))
    print(f"Reports: {scan_dir / 'report.md'}, {scan_dir / 'findings.json'}")
    print(f"Integrity: {digest}")


if __name__ == "__main__":
    main()
