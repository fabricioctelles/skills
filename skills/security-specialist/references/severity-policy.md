# Severity Policy

Practical decision criteria for assigning severity to security findings. Apply this policy consistently — do not assign severity based on gut feeling.

---

## Severity Levels

### Critical

The vulnerability allows an attacker to fully compromise the system, its data, or its users with minimal effort and no special access.

**Assign critical when:**
- Remote code execution (RCE) is achievable
- Authentication can be bypassed entirely, granting full access
- PII, credentials, or payment data is directly exposed or exfiltrable
- Supply chain compromise: malicious dependency, tampered build artifact, or poisoned CI pipeline
- Pre-authentication exploitation — no account or privileges required

**Examples:**
- Unauthenticated endpoint that returns all user records with passwords
- Deserialization vulnerability allowing arbitrary command execution
- Hardcoded production credentials (database, payment processor, admin tokens)
- Dependency with an actively exploited RCE CVE

---

### High

The vulnerability enables significant damage but requires slightly more effort or minimal access (low-privilege account).

**Assign high when:**
- SQL injection or XSS that enables session hijacking or credential theft
- Privilege escalation from normal user to admin
- SSRF that reaches internal services, metadata endpoints, or private networks
- Significant data exposure (not full breach, but sensitive records accessible)
- Authentication flaws that weaken but don't fully bypass access control
- File upload allowing server-side execution

**Examples:**
- Stored XSS in a comment field that steals admin session cookies
- IDOR allowing any authenticated user to read other users' private data
- SSRF reaching cloud metadata endpoint (`169.254.169.254`)
- JWT signature not verified, allowing role escalation

---

### Medium

The vulnerability has real security impact but is limited in scope, requires chaining, or affects non-critical paths.

**Assign medium when:**
- Stored XSS that cannot access session tokens (HttpOnly cookies in place)
- Information disclosure: stack traces, internal file paths, software versions
- Missing security headers (CSP, X-Frame-Options) on sensitive pages
- Weak cryptography in non-critical paths (e.g., MD5 for non-password hashing)
- CSRF on state-changing but non-critical actions
- Open redirect usable for phishing

**Examples:**
- Error page leaks full stack trace including internal IP addresses
- No CSP header on pages that render user-generated content
- Password reset token generated with insufficient entropy (but short-lived)
- CSRF on profile display name change (not on password/email change)

---

### Low

The issue has minimal direct security impact but represents a gap in defense-in-depth or hygiene.

**Assign low when:**
- Verbose error messages revealing framework version or minor internals
- Missing rate limiting on non-critical endpoints
- Minor misconfigurations with no direct exploit path
- Dependencies with CVEs that have no practical exploit in this context
- Cookie without `Secure` flag in a development-only path
- Directory listing enabled but exposing only public assets

**Examples:**
- Server responds with `X-Powered-By: Express` header
- No rate limit on the "forgot password" endpoint (but tokens are single-use and short-lived)
- Dependency has a CVE for a function the project never calls
- CORS allows `*` on a public read-only API with no auth

---

### Info

Not a vulnerability. An observation, best-practice recommendation, or note for future hardening.

**Assign info when:**
- Best practice not followed but no exploitable condition exists
- Code quality issue with security implications (e.g., error handling inconsistency)
- Suggestion for future improvement (e.g., "consider adding Subresource Integrity")
- Informational notes about architecture or trust boundaries

**Examples:**
- Recommend enabling HSTS preload (HSTS is already present, just not preloaded)
- Suggest adding `integrity` attributes to CDN script tags
- Note that logging does not capture failed authentication attempts

---

## Don't Overcall

Common mistakes that inflate severity beyond what the evidence supports:

| Mistake | Why it's wrong | Correct severity |
|---------|---------------|-----------------|
| Reflected XSS behind authentication marked as critical | Requires social engineering of an already-authenticated user; session cookies are HttpOnly | Medium (or High if cookies are accessible) |
| Missing HSTS marked as critical | HSTS absence alone doesn't enable exploitation; it's defense-in-depth | Low (or Medium if the site handles sensitive auth flows over HTTP) |
| Dependency CVE with no reachable code path marked as high | If the vulnerable function is never called, there's no exploit | Low or Info |
| Missing rate limiting on login marked as high | Only matters if there's no account lockout, no CAPTCHA, and passwords are weak | Low (escalate to Medium if no compensating controls exist) |
| Information disclosure of software version marked as high | Version numbers alone don't enable attack; they help an attacker enumerate but require a corresponding vulnerability | Low |
| Self-XSS (user can only attack themselves) marked as medium | No impact on other users; no realistic attack scenario | Info |
| CORS misconfiguration on a public API with no auth | If the API is intentionally public and has no user context, CORS is irrelevant | Info |

**The rule:** Severity reflects *demonstrated impact*, not *theoretical worst case*. If you can't articulate the realistic attack scenario and its consequences in 2 sentences, you're probably overcalling.

---

## Severity Decision Flowchart

1. **Can an unauthenticated attacker achieve RCE, full data breach, or complete auth bypass?** → Critical
2. **Can a low-privilege attacker steal sessions, escalate privileges, or access significant sensitive data?** → High
3. **Is there real but limited impact (scoped data leak, partial XSS, missing hardening on sensitive pages)?** → Medium
4. **Is it a hygiene gap with no direct exploit path in this context?** → Low
5. **Is it purely advisory with no current exploitability?** → Info

When in doubt between two levels, ask: "Can I demonstrate concrete harm to a user or the system?" If yes, go with the higher level. If not, go lower.
