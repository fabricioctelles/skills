# Steering: Generate Scan Report

Produce the final deliverable: a structured report of all findings from a scan, in both machine-readable (JSON) and human-readable (Markdown) formats.

## Step 1: Load All Findings

Pull the complete findings set from the scan database:
```bash
python3 scripts/scan_db.py list --scan-dir <dir> --format json > /tmp/findings_raw.json
```

Verify the data includes:
- All triaged findings (confirmed + false-positive + needs-more-info)
- Validated severity for each
- Status (open, fixed, tracked, false-positive)
- Location, category, evidence, and triage rationale

If any findings lack triage data, go back to the `triage` workflow first. Don't report un-triaged findings.

## Step 2: Compute Statistics

Calculate:

**By severity:**
- Critical: count
- High: count
- Medium: count
- Low: count
- Informational: count
- False positives excluded from totals

**By category:**
- Group by CWE or vulnerability class (injection, XSS, auth, crypto, etc.)
- Show count per category

**By location:**
- Which files/directories have the most findings
- Hotspots (files with 3+ findings)

**By status:**
- Open (unresolved)
- Fixed (remediated and verified)
- Tracked (exported to issue tracker)
- False positive (dismissed with rationale)

## Step 3: Generate JSON Report

Structure:
```json
{
  "scan_metadata": {
    "scan_id": "<uuid>",
    "timestamp": "<ISO 8601>",
    "target": "<repository or directory scanned>",
    "tools_used": ["semgrep", "trufflehog", ...],
    "scan_duration_seconds": <int>
  },
  "summary": {
    "total_findings": <int>,
    "by_severity": {"critical": 0, "high": 0, "medium": 0, "low": 0, "informational": 0},
    "by_status": {"open": 0, "fixed": 0, "tracked": 0, "false_positive": 0},
    "by_category": {"CWE-79": 3, "CWE-89": 1, ...}
  },
  "findings": [
    {
      "id": "<finding-id>",
      "title": "<short description>",
      "severity": "<validated severity>",
      "category": "<CWE-XXX>",
      "location": {"file": "<path>", "line": <int>, "function": "<name>"},
      "status": "<open|fixed|tracked|false_positive>",
      "evidence": "<code snippet or trace>",
      "rationale": "<triage reasoning>",
      "tracking_url": "<url if tracked, null otherwise>"
    }
  ]
}
```

Write to: `<scan-dir>/report.json`

## Step 4: Generate HTML Report

The human-readable report is a **self-contained HTML file** (`security-report.html`). Follow the template in `references/report-format.md`.

Key features:
- Dark theme, color-coded severity badges
- Collapsible evidence and remediation sections
- Interactive filter buttons (filter by severity)
- CVE analysis table with exploitability cross-reference
- Pentest results with all tests numbered (P1, P2...)
- Negative results table (what was tested and passed)
- Zero external dependencies — opens offline

Build the HTML by replacing `{{placeholders}}` in the template with actual data. Repeat blocks for each finding/CVE/test.

Write to: `<scan-dir>/security-report.html` (and also repo root for easy access)

## Step 5: Finalize

Run the finalization script to seal both reports and compute integrity hashes:
```bash
python3 scripts/finalize.py --scan-dir <dir>
```

This script:
- Validates both report files exist and are well-formed (JSON valid, HTML parseable)
- Computes SHA-256 hashes of report.json and security-report.html
- Writes a `manifest.json` with file hashes and completion timestamp
- Marks the scan as complete in the database

## Step 6: Present to User

Show:
- The executive summary
- The findings table
- Location of the full report files
- Any findings that still need action (open critical/high)

## Principles

- Reports are for two audiences: machines (JSON) and humans (HTML). Both must be complete.
- The HTML report is self-contained, interactive, and opens offline in any browser.
- False positives go in a collapsible appendix — they prove rigor but shouldn't clutter the main findings.
- Severity in the report is the **validated** severity (cross-referenced against project context), not the scanner's original rating.
- Every recommendation must be specific enough that a developer can act on it without further research.
- The executive summary is for people who won't read the rest. Make it count.
- All pentest tests performed must appear in the report — positive and negative results.
