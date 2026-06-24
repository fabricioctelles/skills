# Finding Format Specification

This document defines the canonical structure of a security finding. Every finding produced by the security-specialist agent MUST conform to this schema.

---

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | UUID v4 | yes | Unique identifier for this finding |
| `scan_id` | UUID v4 | yes | Foreign key to the parent scan session |
| `title` | string | yes | Concise vulnerability name (≤ 80 chars). Describe what and where. |
| `severity` | enum | yes | One of: `critical`, `high`, `medium`, `low`, `info` |
| `category` | enum | yes | One of: `injection`, `xss`, `auth`, `crypto`, `exposure`, `config`, `dependency`, `logic`, `other` |
| `status` | enum | yes | One of: `open`, `fixed`, `false-positive`, `accepted-risk`, `tracked` |
| `file_path` | string | yes | Repository-relative path to the affected file (e.g. `src/api/users.py`) |
| `line_number` | integer | yes | Line number where the vulnerability is located or originates |
| `description` | string | yes | 2–4 sentences explaining what the vulnerability is and why it matters |
| `evidence` | string | yes | Proof: code snippet, data flow trace, or proof-of-concept |
| `remediation` | string | no | Suggested fix or mitigation strategy |
| `tracking_url` | string | no | URL to an external issue tracker (Jira, GitHub Issue, GitLab Issue, etc.) |
| `notes` | string | no | Free-text triage notes added during review |
| `created_at` | string | yes | ISO 8601 timestamp of when the finding was recorded |

---

## Field Constraints

- **title**: Should follow the pattern `"<Vulnerability Type> in <location/feature>"`. Avoid generic titles like "Security Issue Found".
- **severity**: Assign per `severity-policy.md`. Do not guess — apply the decision criteria.
- **category**: Choose the most specific match. Use `other` only when no category fits.
- **status**: Initial findings are always `open`. Other statuses are set during triage or remediation.
- **file_path**: Always relative to repository root. No leading slash. Use forward slashes regardless of OS.
- **line_number**: Points to the most relevant line. For multi-line issues, use the first affected line.
- **evidence**: Must be concrete. Include the actual code, the trace, or the request/response. Never write "vulnerability exists here" without showing it.

---

## Examples

### Example 1: SQL Injection

```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scan_id": "f0e1d2c3-b4a5-6789-0123-456789abcdef",
  "title": "SQL Injection in user search endpoint",
  "severity": "high",
  "category": "injection",
  "status": "open",
  "file_path": "src/routes/users.js",
  "line_number": 47,
  "description": "User-supplied search parameter is concatenated directly into a SQL query without sanitization or parameterization. An authenticated user can extract arbitrary data from the database, including other users' credentials and PII.",
  "evidence": "```javascript\n// src/routes/users.js:47\nconst query = `SELECT * FROM users WHERE name LIKE '%${req.query.search}%'`;\nconst results = await db.raw(query);\n```\nPayload: `search=' UNION SELECT password FROM users--` returns all password hashes.",
  "remediation": "Use parameterized queries. Replace with: `db('users').where('name', 'like', `%${search}%`)` or use prepared statements with bound parameters.",
  "tracking_url": null,
  "notes": null,
  "created_at": "2026-06-24T03:15:00Z"
}
```

### Example 2: Hardcoded API Key

```json
{
  "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "scan_id": "f0e1d2c3-b4a5-6789-0123-456789abcdef",
  "title": "Hardcoded Stripe secret key in payment service",
  "severity": "critical",
  "category": "exposure",
  "status": "open",
  "file_path": "src/services/payment.ts",
  "line_number": 12,
  "description": "A live Stripe secret key is hardcoded in source. Anyone with repository access can use this key to issue refunds, access customer payment data, and create charges. The key prefix confirms this is a production credential.",
  "evidence": "```typescript\n// src/services/payment.ts:12\nconst stripe = new Stripe('sk_live_EXAMPLE_KEY_REDACTED_000', {\n  apiVersion: '2024-06-20',\n});\n```",
  "remediation": "1. Rotate the exposed key immediately in the Stripe dashboard. 2. Move the key to environment variables or a secrets manager. 3. Add secret patterns to a pre-commit secret scanner.",
  "tracking_url": "https://gitlab.example.com/project/-/issues/142",
  "notes": "Key confirmed active via Stripe API check (read-only test). Rotation is urgent.",
  "created_at": "2026-06-24T03:15:22Z"
}
```
