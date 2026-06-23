---
name: auth-md
description: >
  Generate, validate, and explain `auth.md` files — the open protocol that lets AI agents
  register for services on behalf of users. Use this skill whenever the user wants to make
  their app agent-ready by publishing an `auth.md`, generate Protected Resource Metadata
  (RFC 9728), validate an existing `auth.md` against the protocol specification, implement
  agent registration endpoints, understand how the auth.md protocol works, or configure
  authentication flows for agents. Trigger on mentions of "auth.md", "agent registration",
  "agent auth", "make my app agent-ready", "ID-JAG", "agent verified flow",
  "user claimed flow", "protected resource metadata", "OTP claim", "agentic registration",
  "CIMD", "Client ID Metadata Document", "oauth-id-jag", "logout token",
  "agent revocation", "agent credential", "agent discovery",
  "/.well-known/oauth-protected-resource", "/.well-known/oauth-authorization-server",
  "/agent/auth", or any variation of AI agent authentication/registration in APIs.
metadata:
  author: https://ft.ia.br
  version: "1.0"
  date: 2026-03-05
  repository: https://github.com/fabriciotelles/skills
  license: Apache 2.0
---

# auth-md

Generate, validate, and explain the **auth.md** protocol — the open standard that lets AI agents register for services on behalf of users, without signup forms.

---

## Protocol Context

auth.md is a Markdown file published at a service's root (typically `https://service.com/auth.md`) that instructs agents on how to register. It works simultaneously as human-readable documentation and as a discoverable runtime artifact for agents.

The protocol extends RFC 9728 (OAuth 2.0 Protected Resource Metadata) with an `agent_auth` block in the Authorization Server metadata, and defines two primary flows:

| Flow | Mechanism | When to use |
|------|-----------|-------------|
| **Agent Verified** | Provider (OpenAI, Anthropic, Cursor) signs an ID-JAG asserting user identity. Service verifies signature via JWKS and issues credentials synchronously. | Service already does JIT provisioning from OIDC/SAML; wants zero-friction registration. |
| **User Claimed** | OTP-based. Two entrypoints: *anonymous start* (credential immediately, claim later) or *email required* (no credential until OTP verified). | Agents on platforms that can't mint ID-JAGs; self-serve without trust list. |

### Protocol Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/.well-known/oauth-protected-resource` | Discovery — resource metadata (RFC 9728) |
| `/.well-known/oauth-authorization-server` | Discovery — AS metadata with `agent_auth` block |
| `POST /agent/auth` | Registration — dispatches on `type` field |
| `POST /agent/auth/claim` | Claim initiation (anonymous start only) |
| `POST /agent/auth/claim/complete` | OTP verification |
| `POST /agent/auth/revoke` | Revocation (receives logout tokens from providers) |

### Credential Types

- `access_token` — short-lived, no refresh token, re-register with fresh ID-JAG on expiry
- `api_key` — typically no expiry, subject to revocation

---

## Operation Modes

| Parameter | Default | Description |
|-----------|---------|-------------|
| `mode` | `generate` | `generate` = create auth.md + metadata; `validate` = check existing auth.md; `explain` = explain the protocol |
| `validation_level` | `basic` | `basic` = structure + fields + consistency (offline); `full` = basic + live endpoint fetch |
| `flows` | `all` | Which flows to include: `agent_verified`, `user_claimed_anonymous`, `user_claimed_email`, `all` |
| `role` | `app` | Perspective: `app` = service accepting registrations; `provider` = platform minting ID-JAGs |

---

## Workflow: Generate

### 1. Scan the codebase

Look for:
- Existing API routes and authentication patterns
- Defined scopes/permissions
- Framework (Express, Django, Rails, FastAPI, NestJS, etc.)
- Base URL and auth server URL configuration
- Existing authentication middleware
- User models and provisioning mechanisms

### 2. Ask the user only what cannot be inferred

- Which flows to support (agent verified, user claimed anonymous, user claimed email, or combination)
- Credential type preference (`api_key`, `access_token`, or both)
- Pre-claim scopes vs post-claim scopes (if anonymous start)
- Trusted agent providers and trust list policy (if agent verified)
- Whether the service already does JIT provisioning or requires manual onboarding
- Desired rate limiting policy

### 3. Generate artifacts

Produce three artifacts:

**a) `auth.md`** — Markdown file following the protocol template (see `references/protocol-template.md`). Must contain:
- Title and intro addressed to the agent
- Step 1 — Discover (two hops: PRM → AS metadata)
- Step 2 — Pick a method (decision tree)
- Step 3 — Register (one subsection per supported method)
- Step 4 — Claim ceremony (if user claimed)
- Step 5 — Use the credential
- Errors (complete table)
- Revocation

**b) `oauth-protected-resource.json`** — JSON for `/.well-known/oauth-protected-resource`

**c) `oauth-authorization-server.json`** — JSON for `/.well-known/oauth-authorization-server` with the complete `agent_auth` block

### 4. Generate implementation guidance

"Next Steps" section with:
- How to serve `auth.md` at the domain root
- How to serve metadata at the well-known paths
- How to add `WWW-Authenticate` header to 401 responses
- Endpoint implementation guidance (without generating framework-specific code unless requested)
- Recommended rate limiting configuration
- Recommended audit events
- Security considerations (token hashing, OTP entropy, replay protection)

### 5. Generate Agent Provider guide (if role=provider)

When the user is an agent provider (not an app), generate:
- How to mint audience-specific ID-JAGs
- Token structure (header + payload with required and optional claims)
- How to publish JWKS
- Optionally: how to publish a CIMD (Client ID Metadata Document)
- How to implement revocation (POST logout+jwt)
- How to present consent to the user before asserting identity

---

## Workflow: Validate

### 1. Load the auth.md

From a local file path or URL.

### 2. Run validation at the requested level

**Basic (offline):**
- All required headings present (Step 1–5, Errors, Revocation)
- Service name and base URL declared
- At least one flow documented
- Valid JSON in fenced code blocks for request/response shapes
- Error table with standard error codes
- Consistency: flows in prose match `identity_types_supported` in metadata JSON
- Well-formed URLs in code blocks
- No unreplaced placeholders

**Full (live):**
- All basic checks, plus:
- Fetch `/.well-known/oauth-protected-resource` from the declared base URL
- Verify `agent_auth` block exists and is consistent with auth.md
- Fetch `/.well-known/oauth-authorization-server` and verify consistency
- Check that `register_uri`, `claim_uri`, `revocation_uri` respond (accept 400/401/422, reject 404/405)
- Verify API returns 401 with `WWW-Authenticate` containing `resource_metadata`

### 3. Report results

Checklist with ✅/❌ per rule, grouped by category:
- **Structure** — headings and order
- **Fields** — required fields in JSONs
- **Consistency** — cross-references between prose and metadata
- **Format** — valid JSON, valid HTTP, no placeholders
- **Endpoints** (full only) — reachability and correct responses

Include severity: 🔴 Error (agents will fail), 🟡 Warning (degraded experience), 🟢 Info (suggestion).

See `references/validation-rules.md` for the complete ruleset.

---

## Workflow: Explain

When the user wants to understand the protocol without generating or validating:

1. Identify what the user wants to know (overview, specific flow, specific endpoint, security, etc.)
2. Explain using the protocol context above and the references
3. Use text-based sequence diagrams when helpful
4. Point to official documentation when relevant

---

## User Matching and JIT Provisioning

Both flows need to decide which service user a registration represents. Recommended resolution order:

1. **Delegation record match** — if credentials were previously issued for this `(iss, sub)`, route to the same user
2. **Verified email match** — if a user exists with the same verified email, link
3. **Verified phone match** — same pattern
4. **No match → JIT** — create a new user per provisioning policy, or refuse

Reject ID-JAGs with neither a verified email nor a verified phone — there's no basis for matching and no channel for user-facing communications.

---

## Rate Limiting

The `/agent/auth` endpoint is unauthenticated for anonymous registration. Implement two tiers:

1. **Per-IP** (checked first) — prevents a single source from consuming the tenant's budget. Default: 5/hour anonymous, 60/hour identity_assertion.
2. **Per-tenant** (checked second) — global cap across IPs. Default: 100/hour anonymous, 1000/hour identity_assertion.

Use a sliding-window counter with a shared store. Fail open on store errors.

---

## Recommended Audit Events

| Event | When | Data |
|-------|------|------|
| `registration.created` | Successful POST /agent/auth | registration_id, registration_type, iss, sub |
| `claim.requested` | /agent/auth/claim called | registration_id, email |
| `otp.generated` | OTP minted for claim view | registration_id |
| `claim.confirmed` | /agent/auth/claim/complete succeeds | registration_id, claimed_by_user_id |
| `registration.expired` | Unclaimed registration past TTL | registration_id |
| `registration.revoked` | Logout token processed | registration_id, iss, sub |

---

## Security Considerations

- **Token hashing** — `claim_token`, `claim_view_token`, and OTP are bearer secrets with no proof of possession. Store only SHA-256 hashes. Plaintext leaves the server exactly once.
- **OTP entropy + TTL** — use CSPRNG. Default TTL ≤10 min with tight retry limits.
- **Replay protection** — cache `jti` values with TTL of at least `exp - iat` + clock skew (typically 6 min).
- **CIMD resolution** — if `client_id` is a URL, fetch as OAuth Client ID Metadata Document and verify `jwks_uri` matches the one used to verify the signature.
- **Key reuse across claim boundary** — for anonymous, the in-place permission swap means anyone who captured the key pre-claim retains access post-claim. Offer forced-rotation as an opt-in.
- **Bulk revocation** — provide an operator-facing mechanism to revoke all outstanding agent credentials for a tenant in one shot.

---

## Agent Readiness Scanner Check

The [isitagentready.com](https://isitagentready.com) scanner validates auth.md as the `authMd` check. Pass criteria:

1. `/auth.md` served from site root with HTTP 200
2. Content is Markdown with H1 heading containing "auth.md" (e.g., `# auth.md` or `# Example auth.md`)
3. Optionally validates OAuth Protected Resource Metadata at `/.well-known/oauth-protected-resource`
4. Optionally validates Authorization Server metadata at `/.well-known/oauth-authorization-server`

**Scanner does NOT:**
- Probe `POST /agent/auth` (passive scan only)
- Require OAuth metadata to pass (self-contained auth.md is sufficient)

**To pass the check minimally:**
```markdown
# auth.md

This service accepts AI agent registrations.

## Authentication

Agents can register via POST /agent/auth with a valid ID-JAG.
See below for supported methods and credential types.
```

**To pass with full marks (all metadata):**
- Serve `/auth.md` with proper heading
- Publish `/.well-known/oauth-protected-resource` with `resource`, `authorization_servers`, `scopes_supported`, `bearer_methods_supported: ["header"]`
- Publish `/.well-known/oauth-authorization-server` with `issuer`, `agent_auth` block containing `skill`, `register_uri`, and registration methods

**Scan command:**
```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://YOUR-DOMAIN/","enabledChecks":["authMd"]}' | jq '.checks.discovery.authMd'
```

### Flow Metadata Fields (per scanner SKILL.md)

For each flow the scanner may look for:

| Flow | Required in AS metadata |
|------|------------------------|
| **ID-JAG** | `identity_types_supported: ["identity_assertion"]`, `identity_assertion.assertion_types_supported` with `urn:ietf:params:oauth:token-type:id-jag`, credential types. Optional: `revocation_uri`, `events_supported` |
| **Verified email** | `identity_assertion.assertion_types_supported` with `verified_email`, credential types, `claim_uri` |
| **Anonymous** | `identity_types_supported: ["anonymous"]`, `anonymous.credential_types_supported`, `claim_uri` |

---

## Quality Checklist

Before delivering output, verify:

- [ ] Generated `auth.md` contains all required steps + Errors + Revocation
- [ ] JSON metadata includes valid `agent_auth` block with all required fields
- [ ] `identity_types_supported` matches the flows the user chose
- [ ] `scopes_supported` reflects actual API scopes found in codebase
- [ ] Base URLs are consistent between auth.md and metadata JSON
- [ ] Error codes table includes all standard codes for the supported flows
- [ ] No unreplaced placeholder values (`{{...}}`, `<your-...>`, `[YOUR_...]`)
- [ ] Validation report covers all rules for the requested level
- [ ] Rate limiting documented or mentioned in next steps
- [ ] Security considerations included in next steps
- [ ] If role=provider: ID-JAG structure and JWKS documented

---

## References

- `references/protocol-template.md` — Complete auth.md template with all sections and placeholders
- `references/validation-rules.md` — Full validation ruleset with error messages and severities
- `references/metadata-schema.md` — JSON schema for Protected Resource Metadata, AS metadata, and ID-JAG
- `references/example-auth-md.md` — Working example of a complete auth.md file (Acme Notes)
- `references/implementation-guide.md` — Server-side implementation guide with security, rate limiting, and audit events

---

## Updating Protocol Knowledge

This skill ships with a snapshot of the auth.md protocol specification (v1, May 2026). When possible, fetch the latest version from:

- Skill Home and Doc Hub: `https://auth-md.com`
- Spec: `https://raw.githubusercontent.com/workos/auth.md/refs/heads/main/AUTH.md`
- Docs overview: `https://workos.com/auth-md/docs`
- Apps guide: `https://workos.com/auth-md/docs/apps`
- Agent providers guide: `https://workos.com/auth-md/docs/agent-providers`
- File anatomy: `https://workos.com/auth-md/docs/auth-md`

If fetch fails, use the bundled `references/` as the source of truth.
