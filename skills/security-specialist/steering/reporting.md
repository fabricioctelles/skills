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

## Step 4: Generate Markdown Report

Structure the markdown report with these sections:

### 4.1 Executive Summary
- 3-5 sentences. What was scanned, what was found, what's the overall risk posture.
- Lead with the most critical finding if one exists.
- State clearly: "X critical, Y high findings require immediate attention."

### 4.2 Methodology
- What tools were run (with versions if available)
- What was in scope (directories, languages, specific threat models)
- What was out of scope
- Whether dynamic testing was performed or static-only

### 4.3 Findings Summary Table

```markdown
| # | Severity | Category | Location | Status |
|---|----------|----------|----------|--------|
| 1 | Critical | CWE-89 | api/users.py:42 | Open |
| 2 | High | CWE-79 | templates/search.html:15 | Fixed |
```

Sort by severity (critical first), then by status (open first).

### 4.4 Detailed Findings

For each confirmed finding (not false positives):
```markdown
### SEC-001: SQL Injection in User Search

**Severity:** Critical
**Category:** CWE-89 (SQL Injection)
**Location:** `src/api/users.py:42`
**Status:** Open

**Description:**
User-controlled input from the `q` query parameter is concatenated directly into a SQL query without parameterization.

**Evidence:**
\`\`\`python
query = f"SELECT * FROM users WHERE name LIKE '%{request.args.get('q')}%'"
db.execute(query)
\`\`\`

**Impact:**
Full database read/write access. Attacker can extract all user records, modify data, or potentially achieve RCE via database features (xp_cmdshell, COPY FROM PROGRAM).

**Recommendation:**
Use parameterized queries via the ORM or prepared statements.
```

### 4.5 Recommendations

Prioritized list:
1. Immediate actions (critical/high open findings)
2. Short-term improvements (medium findings, systemic patterns)
3. Long-term hardening (defense-in-depth, tooling, process improvements)

Include specific, actionable guidance — not generic "improve security." Name the file, the pattern, and the fix direction.

### 4.6 False Positives (Appendix)

Brief list of dismissed findings with one-line rationale each. This shows the work was thorough and prevents re-reporting.

Write to: `<scan-dir>/report.md`

## Step 5: Finalize

Run the finalization script to seal both reports and compute integrity hashes:
```bash
python3 scripts/finalize.py --scan-dir <dir>
```

This script:
- Validates both report files exist and are well-formed
- Computes SHA-256 hashes of report.json and report.md
- Writes a `manifest.json` with file hashes and completion timestamp
- Marks the scan as complete in the database

## Step 6: Present to User

Show:
- The executive summary
- The findings table
- Location of the full report files
- Any findings that still need action (open critical/high)

## Principles

- Reports are for two audiences: machines (JSON) and humans (Markdown). Both must be complete.
- False positives go in an appendix — they prove rigor but shouldn't clutter the main findings.
- Severity in the report is the **validated** severity, not the scanner's original rating.
- Every recommendation must be specific enough that a developer can act on it without further research.
- The executive summary is for people who won't read the rest. Make it count.
