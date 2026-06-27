# Validation Rules

Complete ruleset for validating `auth.md` files against the protocol specification (v2, June 2026).

---

## Level: Basic (Offline)

### Structure Rules

| ID | Rule | Error Message | Severity |
|----|------|---------------|----------|
| S01 | Document starts with `# auth.md` heading | Missing required top-level heading `# auth.md` | 🔴 |
| S02 | Contains `## Step 1 — Discover` section | Missing required section: Step 1 — Discover | 🔴 |
| S03 | Contains `## Step 2 — Pick a method` section | Missing required section: Step 2 — Pick a method | 🔴 |
| S04 | Contains `## Step 3 — Register` section | Missing required section: Step 3 — Register | 🔴 |
| S05 | Contains `## Step 4 — Claim ceremony` section (if service_auth or anonymous with claim) | Missing required section: Step 4 — Claim ceremony (required when service_auth or anonymous claim is supported) | 🔴 |
| S06 | Contains `## Step 5 — Exchange the assertion` section | Missing required section: Step 5 — Exchange the assertion | 🔴 |
| S07 | Contains `## Step 6 — Use the access_token` section | Missing required section: Step 6 — Use the access_token | 🔴 |
| S08 | Contains `## Errors` section | Missing required section: Errors | 🔴 |
| S09 | Contains `## Revocation` section | Missing required section: Revocation | 🔴 |
| S10 | Sections appear in correct order (Step 1 → 2 → 3 → 4 → 5 → 6 → Errors → Revocation) | Sections are out of order. Expected sequence: Step 1, 2, 3, 4, 5, 6, Errors, Revocation | 🟡 |
| S11 | Intro declares real hostnames (resource server and auth server) | Intro should declare real hostnames for resource and auth servers | 🟢 |

### Field Rules

| ID | Rule | Error Message | Severity |
|----|------|---------------|----------|
| F01 | Step 1 contains at least one fenced JSON block with `resource` field | Step 1 must include Protected Resource Metadata JSON with `resource` field | 🔴 |
| F02 | PRM JSON contains `resource_name` | Missing `resource_name` in PRM — agents need this for consent prompts | 🟡 |
| F03 | PRM JSON contains `resource_logo_uri` | Missing `resource_logo_uri` — recommended for consent UX | 🟢 |
| F04 | JSON metadata contains `authorization_servers` array | Missing `authorization_servers` — agents can't discover the auth endpoint | 🟡 |
| F05 | JSON metadata contains `scopes_supported` array with ≥1 scope | Missing or empty `scopes_supported` | 🟡 |
| F06 | AS metadata contains `agent_auth` block | Missing `agent_auth` block in Authorization Server metadata | 🔴 |
| F07 | `agent_auth` contains `identity_endpoint` | Missing `identity_endpoint` in agent_auth block | 🔴 |
| F08 | `agent_auth` contains `identity_types_supported` with ≥1 type | Missing or empty `identity_types_supported` | 🔴 |
| F09 | If `identity_assertion` in identity_types_supported, `assertion_types_supported` must exist | Declared `identity_assertion` support but missing `assertion_types_supported` | 🟡 |
| F10 | Step 3 contains at least one `POST /agent/identity` request example | Step 3 must include at least one registration request example | 🔴 |
| F11 | Errors section contains a table with `Code`, `Where`, and `What to do` columns | Errors section must contain a table with Code, Where, and What to do columns | 🟡 |
| F12 | `agent_auth` contains `skill` pointing to auth.md URL | Missing `skill` field in agent_auth — recommended for discoverability | 🟢 |
| F13 | `agent_auth` contains `events_supported` | Missing `events_supported` — recommended for revocation support | 🟢 |
| F14 | AS metadata contains `token_endpoint` | Missing `token_endpoint` — required for token exchange and claim polling | 🔴 |
| F15 | AS metadata contains `revocation_endpoint` | Missing `revocation_endpoint` — required for credential-layer revocation | 🟡 |
| F16 | AS metadata contains `grant_types_supported` with both required URNs | Missing or incomplete `grant_types_supported` — must include jwt-bearer and claim grant URNs | 🟡 |
| F17 | If `service_auth` or `anonymous` in identity_types_supported, `claim_endpoint` must exist | service_auth/anonymous requires `claim_endpoint` for ceremony initiation | 🟡 |
| F18 | `agent_auth` contains `events_endpoint` | Missing `events_endpoint` — recommended for registration-layer revocation | 🟢 |
| F19 | Step 5 contains `POST /oauth2/token` with jwt-bearer grant | Step 5 must document the token exchange via /oauth2/token | 🔴 |

### Consistency Rules

| ID | Rule | Error Message | Severity |
|----|------|---------------|----------|
| C01 | Flows documented in Step 3 match `identity_types_supported` in metadata | Mismatch: Step 3 documents flows not declared in metadata (or vice versa) | 🟡 |
| C02 | If only identity_assertion flow without claim: Step 4 may be absent | Step 4 present but only identity_assertion flow without claim is supported | 🟡 |
| C03 | `identity_endpoint` path matches the POST path in Step 3 examples | Registration endpoint in metadata doesn't match the POST path in Step 3 | 🟡 |
| C04 | `claim_endpoint` path matches the POST path in Step 4 examples (if present) | Claim endpoint in metadata doesn't match the POST path in Step 4 | 🟡 |
| C05 | Scopes in response examples are subset of `scopes_supported` | Response example contains scopes not listed in `scopes_supported` | 🟡 |
| C06 | `resource` URL is consistent across all JSON blocks | Different `resource` URLs found in metadata blocks — must be consistent | 🟡 |
| C07 | All URLs use HTTPS scheme | Non-HTTPS URL found — all endpoints must use HTTPS | 🟡 |
| C08 | Error codes in table match standard protocol error codes (see list below) | Non-standard error code found | 🟡 |
| C09 | `aud` in ID-JAG examples matches the `resource` from PRM | ID-JAG `aud` example doesn't match the resource URL | 🟡 |
| C10 | `assertion_types_supported` includes types used in Step 3 examples | Step 3 uses assertion types not declared in metadata | 🟡 |
| C11 | `token_endpoint` in metadata matches the `/oauth2/token` path used in Steps 4c and 5 | Token endpoint in metadata doesn't match the POST path in Steps 4c/5 | 🟡 |
| C12 | `grant_types_supported` includes `urn:ietf:params:oauth:grant-type:jwt-bearer` | Missing jwt-bearer grant in grant_types_supported — required for token exchange | 🟡 |
| C13 | `grant_types_supported` includes `urn:workos:agent-auth:grant-type:claim` (if claim ceremony exists) | Missing claim grant in grant_types_supported — required for ceremony polling | 🟡 |

### Format Rules

| ID | Rule | Error Message | Severity |
|----|------|---------------|----------|
| X01 | All JSON in fenced code blocks is valid JSON | Invalid JSON in fenced code block at section: {section} | 🟡 |
| X02 | HTTP request examples use valid HTTP method + path | Invalid HTTP request format. Expected: METHOD /path | 🟡 |
| X03 | No unreplaced placeholder patterns (`{{...}}`, `<your-...>`, `[YOUR_...]`) | Unreplaced placeholder found: {placeholder} | 🟡 |
| X04 | Fenced code blocks have language hint (`http`, `json`) | Code block missing language hint — agents use these to identify request shapes | 🟢 |

---

## Level: Full (Live)

All Basic rules, plus:

### Endpoint Rules

| ID | Rule | Error Message | Severity |
|----|------|---------------|----------|
| E01 | `GET {base_url}/.well-known/oauth-protected-resource` returns 200 with valid JSON | Protected Resource Metadata endpoint not reachable or returns invalid response | 🔴 |
| E02 | PRM response contains `authorization_servers` pointing to AS with `agent_auth` block | No `agent_auth` block discoverable through PRM → AS metadata chain | 🔴 |
| E03 | `GET {auth_server}/.well-known/oauth-authorization-server` returns 200 with valid JSON | Authorization Server metadata endpoint not reachable | 🔴 |
| E04 | AS metadata `agent_auth` block matches declarations in auth.md | Live AS metadata `agent_auth` block differs from auth.md declarations | 🟡 |
| E05 | `identity_endpoint` accepts POST (returns 400/401/422, not 404/405) | Registration endpoint returns 404 or 405 — not implemented | 🔴 |
| E06 | `claim_endpoint` accepts POST (if service_auth or anonymous supported) | Claim endpoint returns 404 or 405 — not implemented | 🔴 |
| E07 | `token_endpoint` accepts POST (returns 400/401, not 404/405) | Token endpoint returns 404 or 405 — not implemented | 🔴 |
| E08 | `revocation_endpoint` accepts POST (returns 200/400, not 404/405) | Revocation endpoint returns 404 or 405 — not implemented | 🟡 |
| E09 | API base URL returns 401 with `WWW-Authenticate` header containing `resource_metadata` | API does not return WWW-Authenticate header with resource_metadata on 401 | 🟡 |

---

## Standard Protocol Error Codes

Complete list of error codes the Errors table should cover (per supported flows):

### Registration Endpoint (`/agent/identity`)
- `anonymous_not_enabled`
- `service_auth_not_enabled`
- `issuer_not_enabled`
- `invalid_request` (body shape, missing claims, signature, jti, aud, unverified identity)
- `interaction_required` (401) — ID-JAG matched account but no (iss,sub) delegation
- `login_required` (401) — auth_time missing or older than max_age
- `rate_limited` (429)

### Claim Endpoint (`/agent/identity/claim`)
- `invalid_claim_token`
- `claimed_or_in_flight`
- `claim_expired`

### Token Endpoint (`/oauth2/token`)
- `invalid_grant` — assertion expired/revoked/replayed
- `invalid_client`
- `unsupported_grant_type`
- `authorization_pending` — claim polling, user hasn't completed
- `expired_token` — user_code window closed
- `slow_down` — polling too fast

### All Endpoints
- `rate_limited` (429)

---

## Validation Report Format

```markdown
# Validation Report — auth.md

**File:** {path_or_url}
**Level:** {basic|full}
**Date:** {timestamp}

## Summary

- ✅ {n} rules passed
- ❌ {n} rules failed
- ⚠️ {n} warnings

## Structure

| Status | ID | Rule |
|--------|-----|-------|
| ✅ | S01 | Heading `# auth.md` present |
| ❌ | S06 | Step 5 section missing |

## Fields
...

## Consistency
...

## Format
...

## Endpoints (full only)
...
```
