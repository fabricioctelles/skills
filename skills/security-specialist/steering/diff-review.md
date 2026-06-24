# Security-Focused Diff Review

## Purpose

Review a code diff (PR, commit range, branch comparison) for security regressions. Lighter and faster than a full scan — scoped strictly to what changed.

## Step 1: Obtain the Diff

Identify what you're reviewing:
- PR: the full diff between base and head
- Commit: single commit's changeset
- Branch comparison: `git diff base..head`

Read the diff in its entirety. Don't skip files — even test changes can reveal security assumptions.

## Step 2: Understand Context

Before hunting bugs, understand intent:
- What feature/fix does this change implement?
- What's the PR description / commit message saying?
- Which components are touched?

This prevents false positives from misunderstanding purpose.

## Step 3: Map Changed Attack Surface

Identify which changes affect security-relevant areas:

| Change Type | Security Relevance |
|---|---|
| New HTTP route/endpoint | New attack surface — needs auth + input validation check |
| Modified auth logic | Possible bypass, privilege escalation |
| New user input accepted | Injection, XSS, path traversal surface |
| Database query changes | SQL/NoSQL injection |
| File I/O changes | Path traversal, TOCTOU |
| Dependency added/updated | Known CVEs, supply chain risk |
| Config/env changes | Secret exposure, permissive settings |
| Error handling changes | Information disclosure |
| Crypto changes | Weak algorithms, key mishandling |
| Logging changes | Sensitive data in logs |

## Step 4: Security Regression Checklist

For each changed file, check:

### Input Handling
- [ ] New inputs validated before use?
- [ ] Existing validation still applies after refactor?
- [ ] Type coercion handled safely?
- [ ] Size/length limits enforced?

### Authentication & Authorization
- [ ] New endpoints require auth?
- [ ] Permission checks not accidentally removed?
- [ ] Auth bypass possible through new code paths?
- [ ] Token/session handling unchanged or improved?

### Data Exposure
- [ ] No secrets added to code (API keys, passwords, tokens)
- [ ] No sensitive data in new log statements
- [ ] Error messages don't leak internals
- [ ] New API responses don't over-expose data

### Dependencies
- [ ] New deps checked for known CVEs
- [ ] Version pinned (not floating ranges)
- [ ] Dep source is legitimate (not typosquat)

### Crypto & Secrets
- [ ] No hardcoded keys or salts
- [ ] Crypto usage correct (proper modes, IV handling, key derivation)
- [ ] Secrets accessed through proper secret management

## Step 5: Produce Findings

For each issue, document:

```
### [SEVERITY] Title

**File:** path/to/file.ext L42-48
**Change:** What was modified
**Issue:** What's wrong, specifically
**Attack:** How this gets exploited
**Fix:** Concrete remediation

Evidence:
\`\`\`
<the vulnerable code from the diff>
\`\`\`
```

## Step 6: Assess Severity in Context

Diff review severity considers:
- Is this code deployed yet? (PR = pre-deploy, post-merge = live)
- Does existing infrastructure mitigate? (WAF, rate limiting, network isolation)
- Is the vulnerable path reachable without auth?
- What data is at risk?

Don't inflate severity. A medium finding behind two auth gates isn't critical just because the code pattern looks bad.

## Step 7: Summary Verdict

End with a clear recommendation:

- **APPROVE** — no security issues found
- **APPROVE WITH NOTES** — informational findings, no blockers
- **REQUEST CHANGES** — security issues that must be fixed before merge
- **BLOCK** — critical vulnerability, must not merge

Include the finding count by severity and the single most important issue if requesting changes.

## Output Format

Deliver as markdown. Structure:
1. One-line verdict (approve/block/changes needed)
2. Scope summary (files reviewed, what the change does)
3. Findings (if any), ordered by severity
4. Notes (informational observations, future concerns)

## Notes

- Review test files too — they often reveal what the developer thinks the security boundary is (and where they're wrong).
- Deleted code matters. Removed validation, removed auth checks, removed error handling — these are findings.
- If the diff touches auth or crypto and you can't fully assess impact from the diff alone, say so. Recommend a broader review.
