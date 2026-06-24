#!/usr/bin/env python3
"""SQLite-based security scan database manager."""

import argparse
import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS scans (
    id TEXT PRIMARY KEY,
    repo_path TEXT NOT NULL,
    started_at TEXT NOT NULL,
    sealed_at TEXT,
    status TEXT NOT NULL CHECK(status IN ('active', 'sealed'))
);

CREATE TABLE IF NOT EXISTS findings (
    id TEXT PRIMARY KEY,
    scan_id TEXT NOT NULL REFERENCES scans(id),
    title TEXT NOT NULL,
    severity TEXT NOT NULL CHECK(severity IN ('critical', 'high', 'medium', 'low', 'info')),
    category TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'open'
        CHECK(status IN ('open', 'fixed', 'false-positive', 'accepted-risk', 'tracked')),
    file_path TEXT,
    line_number INTEGER,
    description TEXT,
    evidence TEXT,
    created_at TEXT NOT NULL,
    tracking_url TEXT,
    notes TEXT
);
"""


def _connect(repo: str) -> sqlite3.Connection:
    db_path = Path(repo) / ".security" / "scan.db"
    if not db_path.exists():
        raise SystemExit(f"Database not found: {db_path}")
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def cmd_init(args: argparse.Namespace) -> None:
    """Initialize .security/scan.db and create a new scan record."""
    sec_dir = Path(args.repo) / ".security"
    sec_dir.mkdir(parents=True, exist_ok=True)
    db_path = sec_dir / "scan.db"
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    scan_id = str(uuid.uuid4())
    conn.execute(
        "INSERT INTO scans (id, repo_path, started_at, status) VALUES (?, ?, ?, ?)",
        (scan_id, str(Path(args.repo).resolve()), _now(), "active"),
    )
    conn.commit()
    conn.close()
    print(json.dumps({"scan_id": scan_id, "db": str(db_path)}))


def cmd_add_finding(args: argparse.Namespace) -> None:
    """Insert a finding into the database."""
    conn = _connect(args.repo)
    finding_id = str(uuid.uuid4())
    conn.execute(
        """INSERT INTO findings
           (id, scan_id, title, severity, category, status, file_path, line_number,
            description, evidence, created_at)
           VALUES (?, ?, ?, ?, ?, 'open', ?, ?, ?, ?, ?)""",
        (finding_id, args.scan_id, args.title, args.severity, args.category,
         args.file, args.line, args.description, args.evidence, _now()),
    )
    conn.commit()
    conn.close()
    print(json.dumps({"finding_id": finding_id}))


def cmd_list_findings(args: argparse.Namespace) -> None:
    """List findings as JSON, with optional filters."""
    conn = _connect(args.repo)
    query = "SELECT * FROM findings WHERE scan_id = ?"
    params: list = [args.scan_id]
    if args.severity:
        query += " AND severity = ?"
        params.append(args.severity)
    if args.status:
        query += " AND status = ?"
        params.append(args.status)
    rows = conn.execute(query, params).fetchall()
    conn.close()
    print(json.dumps([dict(r) for r in rows], indent=2))


def cmd_update_status(args: argparse.Namespace) -> None:
    """Update a finding's status and optional tracking metadata."""
    conn = _connect(args.repo)
    parts = ["status = ?"]
    params: list = [args.status]
    if args.tracking_url:
        parts.append("tracking_url = ?")
        params.append(args.tracking_url)
    if args.note:
        parts.append("notes = ?")
        params.append(args.note)
    params.append(args.finding_id)
    conn.execute(f"UPDATE findings SET {', '.join(parts)} WHERE id = ?", params)
    conn.commit()
    conn.close()
    print(json.dumps({"updated": args.finding_id}))


def cmd_stats(args: argparse.Namespace) -> None:
    """Print severity/category/status counts for a scan."""
    conn = _connect(args.repo)
    result: dict = {"by_severity": {}, "by_category": {}, "by_status": {}}
    for col, key in [("severity", "by_severity"), ("category", "by_category"), ("status", "by_status")]:
        rows = conn.execute(
            f"SELECT {col}, COUNT(*) as cnt FROM findings WHERE scan_id = ? GROUP BY {col}",
            (args.scan_id,),
        ).fetchall()
        result[key] = {r[col]: r["cnt"] for r in rows}
    conn.close()
    print(json.dumps(result, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Security scan database manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--repo", required=True)

    p_add = sub.add_parser("add-finding")
    p_add.add_argument("--repo", required=True)
    p_add.add_argument("--scan-id", required=True)
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--severity", required=True, choices=["critical", "high", "medium", "low", "info"])
    p_add.add_argument("--category", required=True)
    p_add.add_argument("--file", required=True)
    p_add.add_argument("--line", type=int, required=True)
    p_add.add_argument("--description", required=True)
    p_add.add_argument("--evidence", required=True)

    p_list = sub.add_parser("list-findings")
    p_list.add_argument("--repo", required=True)
    p_list.add_argument("--scan-id", required=True)
    p_list.add_argument("--severity", choices=["critical", "high", "medium", "low", "info"])
    p_list.add_argument("--status", choices=["open", "fixed", "false-positive", "accepted-risk", "tracked"])

    p_upd = sub.add_parser("update-status")
    p_upd.add_argument("--repo", required=True)
    p_upd.add_argument("--finding-id", required=True)
    p_upd.add_argument("--status", required=True, choices=["open", "fixed", "false-positive", "accepted-risk", "tracked"])
    p_upd.add_argument("--tracking-url")
    p_upd.add_argument("--note")

    p_stats = sub.add_parser("stats")
    p_stats.add_argument("--repo", required=True)
    p_stats.add_argument("--scan-id", required=True)

    args = parser.parse_args()
    {"init": cmd_init, "add-finding": cmd_add_finding, "list-findings": cmd_list_findings,
     "update-status": cmd_update_status, "stats": cmd_stats}[args.command](args)


if __name__ == "__main__":
    main()
