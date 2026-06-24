# Steering: Export Findings to Tracking Systems

Push confirmed findings to external issue trackers (GitHub Issues, GitHub Security Advisories, Jira, Linear) so they're visible to the engineering team and can be assigned/scheduled.

## Step 1: Select Findings to Export

Query the scan database for findings ready to track:
```bash
python3 scripts/scan_db.py list --status confirmed --not-tracked
```

Decide what to export. Typical filters:
- All confirmed findings above a severity threshold (e.g., high+critical)
- All findings from a specific scan
- A hand-picked set by finding ID

Don't export false positives or informational findings to issue trackers — they create noise.

## Step 2: Determine Target System

Identify the project's tracking system:
- **GitHub Issues** — default for open source and most SaaS teams
- **GitHub Security Advisories** — for vulnerabilities that need CVEs or coordinated disclosure
- **Jira** — enterprise, use the project's existing security issue type
- **Linear** — startup teams, use appropriate team and label

Check the project for existing conventions: issue templates, labels (e.g., `security`, `vulnerability`), custom fields, linked projects.

## Step 3: Format the Issue

### Title Format
```
[<SEVERITY>] <Vulnerability Type> in <Location>
```
Examples:
- `[HIGH] SQL Injection in /api/users search endpoint`
- `[CRITICAL] Authentication bypass via JWT algorithm confusion`
- `[MEDIUM] Stored XSS in comment rendering`

Keep titles scannable. Someone triaging a backlog should understand the issue from the title alone.

### Body Structure

```markdown
## Summary
One paragraph: what's wrong, where, and why it matters.

## Finding Details
- **ID:** <finding-id from scan database>
- **Category:** <CWE-XXX / OWASP category>
- **Severity:** <Critical/High/Medium/Low>
- **Location:** `<file:line>` or `<endpoint + parameter>`
- **Detected by:** <tool name or manual review>

## Evidence
<Code snippet showing the vulnerable pattern, or request/response demonstrating the issue>

## Impact
What can an attacker do if this is exploited? Be specific:
- What data is accessible?
- What actions can be performed?
- What's the blast radius?

## Recommended Fix
Brief guidance on the correct remediation approach. Not a full patch — just enough for the developer to understand the direction.

## References
- CWE link
- OWASP page
- Relevant framework documentation for the secure pattern
```

### For GitHub Security Advisories

Additional fields required:
- Affected versions / commits
- CVSS score (calculate from the validated severity + exploitability)
- Patched version (if fix exists)
- Credit (if from bug bounty or external reporter)

## Step 4: Show User for Approval

Before creating anything externally, present the formatted payload:
```
I'm about to create the following issue in <system>:

Title: [HIGH] SQL Injection in /api/users search endpoint
Labels: security, priority-high
Assignee: (none — or suggest based on git blame)

Body:
<full body text>

Approve? (yes/no/edit)
```

Never auto-create external issues without explicit user confirmation. These are visible to teams and may trigger notifications.

## Step 5: Create the Issue

Use the appropriate CLI tool:

**GitHub Issues:**
```bash
gh issue create --title "<title>" --body "<body>" --label "security,<severity>"
```

**GitHub Security Advisory:**
```bash
gh api repos/{owner}/{repo}/security-advisories --method POST --input payload.json
```

**Jira:**
```bash
# Use project-specific Jira CLI or API
curl -X POST "https://<instance>.atlassian.net/rest/api/3/issue" \
  -H "Authorization: Basic <token>" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

**Linear:**
```bash
# Use Linear CLI or GraphQL API
linear issue create --title "<title>" --description "<body>" --team "<team>" --label "Security"
```

Capture the returned URL/ID of the created issue.

## Step 6: Update Scan Database

Link the finding to the external tracker:
```bash
python3 scripts/scan_db.py update-status \
  --finding-id <id> \
  --status tracked \
  --tracking-url <url>
```

## Step 7: Batch Operations

When exporting multiple findings:
- Group related findings into a single issue if they share the same root cause (e.g., "Missing CSRF protection on 8 endpoints" = 1 issue with a checklist)
- Keep unrelated findings as separate issues — don't create mega-issues
- Apply consistent labels and severity tags across the batch

## Principles

- Issues should be actionable. A developer reading it should know what to fix without needing to re-do the analysis.
- Don't over-classify. If in doubt about severity, round down — you can escalate later.
- Include enough evidence that the issue can be verified independently, but don't paste entire exploit chains in public repos.
- For security advisories: coordinate with maintainers on disclosure timeline before publishing.
