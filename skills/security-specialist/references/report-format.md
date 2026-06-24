# Report Format Specification

This document defines the structure of the final human-readable security report generated after a scan is finalized.

---

## Severity Emoji Mapping

| Severity | Emoji | Badge (for inline use) |
|----------|-------|------------------------|
| Critical | 🔴 | `🔴 Critical` |
| High | 🟠 | `🟠 High` |
| Medium | 🟡 | `🟡 Medium` |
| Low | 🟢 | `🟢 Low` |
| Info | ⚪ | `⚪ Info` |

---

## Report Structure

The report is a single markdown file (`report.md`) with the following sections in order:

### 1. Header

```markdown
# Security Scan Report

**Repository:** <repo-name>
**Scan ID:** <uuid>
**Date:** <ISO 8601 date>
**Scanner:** security-specialist agent
```

### 2. Executive Summary

A brief overview containing:
- Total number of findings broken down by severity (e.g. "2 critical, 3 high, 5 medium, 1 low, 2 info")
- One paragraph (3–5 sentences) overall risk assessment
- Whether immediate action is required

Example:

```markdown
## Executive Summary

This scan identified **13 findings**: 2 critical, 3 high, 5 medium, 1 low, and 2 informational. The critical findings — a hardcoded production credential and an unauthenticated admin endpoint — require immediate remediation before the next deployment. The overall security posture is **poor**; the application lacks input validation in several data paths and has no rate limiting on authentication endpoints. Addressing the critical and high findings will substantially reduce attack surface.
```

### 3. Methodology

Describe what was analyzed and how. Keep it factual and concise.

```markdown
## Methodology

- **Scope:** All application source code in `src/`, configuration files, dependency manifests
- **Approach:** Static analysis of data flows, dependency audit against known CVE databases, configuration review against hardening baselines
- **Exclusions:** Third-party vendored code in `vendor/`, test fixtures
- **Limitations:** No dynamic/runtime testing performed. Findings are based on code review only.
```

### 4. Findings Summary Table

A quick-reference table sorted by severity (critical first).

```markdown
## Findings Summary

| | Title | File | Line | Status |
|---|---|---|---|---|
| 🔴 | Hardcoded Stripe secret key | src/services/payment.ts | 12 | open |
| 🔴 | Unauthenticated admin endpoint | src/routes/admin.js | 8 | open |
| 🟠 | SQL Injection in user search | src/routes/users.js | 47 | open |
| 🟡 | Missing Content-Security-Policy | src/middleware/headers.js | 3 | open |
| ⚪ | Consider enabling HSTS preload | nginx.conf | 22 | open |
```

### 5. Detailed Findings

Each finding gets its own subsection:

```markdown
## Detailed Findings

### 🔴 Hardcoded Stripe secret key

**Severity:** Critical
**Category:** Exposure
**File:** `src/services/payment.ts:12`
**Status:** Open

**Description:**
A live Stripe secret key is hardcoded in source. Anyone with repository access can use this key to issue refunds, access customer payment data, and create charges.

**Evidence:**
​```typescript
// src/services/payment.ts:12
const stripe = new Stripe('sk_live_EXAMPLE_KEY_REDACTED_000', {
  apiVersion: '2024-06-20',
});
​```

**Remediation:**
Rotate the key immediately. Move credentials to environment variables or a secrets manager. Add secret patterns to pre-commit hooks.

---
```

Each detailed finding is separated by a horizontal rule (`---`).

### 6. Recommendations

Top 3–5 actionable items prioritized by impact. These are strategic, not per-finding fixes.

```markdown
## Recommendations

1. **Rotate all hardcoded credentials immediately** — The exposed Stripe key is actively exploitable. Rotate, then audit the full codebase for other embedded secrets.
2. **Implement parameterized queries throughout** — Multiple injection points exist because raw SQL is constructed via string concatenation. Adopt an ORM or query builder consistently.
3. **Add authentication middleware to all admin routes** — The admin router has no auth check. Apply the existing `requireAuth` middleware at the router level.
4. **Deploy security headers via middleware** — Add CSP, HSTS, X-Content-Type-Options, and X-Frame-Options. Use a hardening baseline.
5. **Establish a dependency update cadence** — Three dependencies have known CVEs. Set up automated alerts and a monthly review cycle.
```

---

## Formatting Rules

- Use fenced code blocks with language tags for all evidence snippets.
- Never truncate evidence to the point where it loses meaning.
- Keep descriptions factual. Avoid speculative language like "might be exploitable" — either demonstrate it or note the limitation.
- Sort findings by severity descending, then alphabetically within the same severity.
- The report must be self-contained: a reader should understand every finding without consulting external documents.
