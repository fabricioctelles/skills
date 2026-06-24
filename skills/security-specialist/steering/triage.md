# Steering: Triage Findings

Intake a batch of security findings from any source (SARIF, scanner JSON, bug bounty reports, prior scan DB entries) and produce validated, deduplicated, severity-rated findings ready for action.

## Step 1: Ingest and Normalize

Load all input findings into a common internal format. Each normalized finding must have:

- `id`: unique identifier (generate one if source doesn't provide)
- `title`: short description of the issue
- `category`: CWE number or OWASP category (e.g., CWE-79, A03:2021-Injection)
- `location`: file path + line number (or URL + parameter for dynamic findings)
- `source`: which tool/report produced this (semgrep, snyk, burp, manual, etc.)
- `original_severity`: what the source assigned
- `raw_snippet`: relevant code or request/response excerpt
- `description`: what the finding claims is wrong

Run:
```bash
python3 scripts/scan_db.py import --format <sarif|json|csv|manual> --input <path>
```

This writes normalized findings into the scan database. Verify import count matches expectation.

## Step 2: Deduplicate

Same vulnerability reported by multiple tools = one finding. Dedup criteria:
- Same file + same line range (±5 lines) + same CWE = duplicate
- Same endpoint + same parameter + same vulnerability class = duplicate
- Different manifestations of the same root cause = group under one finding, note variants

Run:
```bash
python3 scripts/scan_db.py dedup --scan-dir <dir>
```

Review the dedup report. If the tool merged things that are actually distinct, split them manually.

## Step 3: Contextual Assessment

For each unique finding, answer these questions **by reading the actual code**:

1. **Is it real?** Does the vulnerable pattern actually exist at that location? Scanners hallucinate. Read the file.
2. **Is it reachable?** Can user-controlled input actually reach the vulnerable code path? Trace backwards from the sink to any entry point.
3. **Are there mitigations?** WAF rules, input validation earlier in the chain, framework-level protections, CSP headers — anything that reduces or eliminates exploitability.
4. **What's the blast radius?** If exploited: data loss? RCE? privilege escalation? Information disclosure only? Account takeover?
5. **What's the attack complexity?** Does exploitation require authentication? Specific race conditions? Social engineering?

## Step 4: Assign Validated Severity

Do NOT blindly accept the scanner's severity. Recalculate using:

| Severity | Criteria |
|----------|----------|
| **Critical** | RCE, auth bypass, mass data exfil, no mitigations, reachable from unauthenticated context |
| **High** | SQLi/XSS with clear exploit path, privilege escalation, SSRF to internal services |
| **Medium** | Exploitable but requires auth, limited blast radius, or partial mitigations exist |
| **Low** | Theoretical risk, defense-in-depth issue, requires unlikely preconditions |
| **Informational** | Best practice violation, no direct exploitability, hardening recommendation |

If a scanner says "Critical" but the finding is behind authentication + rate limiting + the data exposed is non-sensitive → it's Medium at best.

## Step 5: Record Triage Decisions

For each finding, record:
```
finding_id: <id>
validated_severity: <critical|high|medium|low|informational>
verdict: <confirmed|false-positive|needs-validation>
rationale: <2-3 sentences explaining WHY this severity, what you checked>
```

Run:
```bash
python3 scripts/scan_db.py triage \
  --finding-id <id> \
  --severity <level> \
  --verdict <confirmed|false-positive|needs-validation> \
  --rationale "explanation here"
```

## Step 6: Produce Triage Summary

After all findings are triaged, generate the summary:
```bash
python3 scripts/scan_db.py triage-summary --scan-dir <dir>
```

Output includes:
- Total findings ingested vs. unique vs. false positives
- Breakdown by validated severity
- List of findings needing deeper validation (verdict = needs-validation)
- Recommended priority order for remediation

## Key Principles

- Scanner severity is a suggestion, not a verdict. Your job is to validate.
- A finding you can't trace to reachable code is `needs-validation`, not `confirmed`.
- False positives are fine — document why and move on. Don't waste time on them.
- When in doubt about exploitability, escalate to the `validation` workflow.
- Group related findings (e.g., 15 instances of the same missing input validation) — fix the pattern, not each instance individually.
