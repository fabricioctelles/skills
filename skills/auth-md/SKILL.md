---
name: auth-md
description: >
  Generate, validate, and explain `auth.md` files — the open protocol that lets AI agents
  register for services on behalf of users. Use this skill whenever the user wants to make
  their app agent-ready by publishing an `auth.md`, generate Protected Resource Metadata
  (RFC 9728), validate an existing `auth.md` against the protocol specification, implement
  agent registration endpoints, understand how the auth.md protocol works, or configure
  authentication flows for agents. Trigger on mentions of "auth.md", "agent registration",
  "agent auth", "make my app agent-ready", "ID-JAG", "identity_assertion flow",
  "service_auth flow", "protected resource metadata", "claim ceremony", "agentic registration",
  "CIMD", "Client ID Metadata Document", "oauth-id-jag", "agent revocation",
  "agent credential", "agent discovery", "token exchange", "interaction_required",
  "/.well-known/oauth-protected-resource", "/.well-known/oauth-authorization-server",
  "/agent/identity", "/oauth2/token", or any variation of AI agent authentication/registration in APIs.
metadata:
  author: https://ft.ia.br
  version: "2.0"
  date: 2026-06-27
  repository: https://github.com/fabriciotelles/skills
  license: Apache 2.0
---

# auth-md

Generate, validate, and explain the **auth.md** protocol — the open standard that lets AI agents register for services on behalf of users, without signup forms.

---

## Protocol Context

auth.md is a Markdown file published at a service's root (typically `https://service.com/auth.md`) that instructs agents on how to register. It works simultaneously as human-readable documentation and as a discoverable runtime artifact for agents.

The protocol extends RFC 9728 (OAuth 2.0 Protected Resource Metadata) with an `agent_auth` block in the Authorization Server metadata. Registration returns an `identity_assertion` (service-signed JWT) that the agent exchanges at `/oauth2/token` for an `access_token`. Three registration methods are supported:

| Flow | Mechanism | When to use |
|------|-----------|-------------|
| **identity_assertion** | Provider signs an ID-JAG (with `auth_time`) asserting user identity. Service verifies JWKS, returns `identity_assertion`. Agent exchanges at `/oauth2/token`. | Service does JIT provisioning from OIDC/SAML; wants zero-friction registration. |
| **service_auth** | Email hint + browser-based ceremony. Agent receives `user_code` + `verification_uri`; user signs in and types code. Agent polls `/oauth2/token`. | Agents on platforms that can't mint ID-JAGs; self-serve without trust list. |
| **anonymous** | No identity upfront. Immediate `identity_assertion` with pre-claim scopes. Optional deferred claim for scope upgrade. | Agent needs basic access immediately; human ownership binding deferred. |

### Protocol Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/.well-known/oauth-protected-resource` | Discovery — resource metadata (RFC 9728) |
| `/.well-known/oauth-authorization-server` | Discovery — AS metadata with `agent_auth` block |
| `POST /agent/identity` | Registration — dispatches on `type` field |
| `POST /agent/identity/claim` | Claim initiation (anonymous deferred, or re-initiate expired user_code) |
| `POST /oauth2/token` | Token exchange (JWT-bearer grant) + claim polling (claim grant) |
| `POST /oauth2/revoke` | Credential-layer revocation (RFC 7009) |
| `events_endpoint` | Registration-layer revocation (receives SETs, RFC 8935) |

### Token Lifecycle

Registration **never** returns an `access_token` directly. The flow is:

1. Registration → `identity_assertion` (service-signed JWT, reusable until expiry)
2. Exchange → `POST /oauth2/token` with `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` → `access_token`
3. Refresh → re-exchange same `identity_assertion` when access_token expires
4. Expired assertion → restart at registration (Step 3)

### Claim Ceremony (v2 — Browser-Based)

The claim ceremony uses RFC 8628-style device authorization:
1. Registration returns `user_code` + `verification_uri` in a `claim` block
2. Agent surfaces both to the user
3. User opens `verification_uri`, signs in to the service, types the 6-digit code
4. Agent polls `POST /oauth2/token` with `grant_type=urn:workos:agent-auth:grant-type:claim` + `claim_token`
5. On success: receives `access_token` + fresh `identity_assertion`

---

## Operation Modes

| Parameter | Default | Description |
|-----------|---------|-------------|
| `mode` | `generate` | `generate` = create auth.md + metadata; `validate` = check existing auth.md; `explain` = explain the protocol |
| `validation_level` | `basic` | `basic` = structure + fields + consistency (offline); `full` = basic + live endpoint fetch |
| `flows` | `all` | Which flows to include: `identity_assertion`, `service_auth`, `anonymous`, `all` |
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

- Which flows to support (identity_assertion, service_auth, anonymous, or combination)
- Pre-claim scopes vs post-claim scopes (if anonymous)
- Trusted agent providers and trust list policy (if identity_assertion)
- Whether the service already does JIT provisioning or requires manual onboarding
- `idJagMaxAuthAgeSeconds` value (default: 3600)
- Desired rate limiting policy

### 3. Generate artifacts

Produce three artifacts:

**a) `auth.md`** — Markdown file following the protocol template (see `references/protocol-template.md`). Must contain:
- Title and intro addressed to the agent
- Step 1 — Discover (two hops: PRM → AS metadata)
- Step 2 — Pick a method (decision tree)
- Step 3 — Register (one subsection per supported method)
- Step 4 — Claim ceremony (if service_auth or anonymous with claim)
- Step 5 — Exchange the assertion (POST /oauth2/token with jwt-bearer grant)
- Step 6 — Use the access_token
- Errors (complete table with all applicable codes)
- Revocation (two layers)

**b) `oauth-protected-resource.json`** — JSON for `/.well-known/oauth-protected-resource` with `resource_name` and `resource_logo_uri`

**c) `oauth-authorization-server.json`** — JSON for `/.well-known/oauth-authorization-server` with:
- `issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`
- Complete `agent_auth` block with `identity_endpoint`, `claim_endpoint`, `events_endpoint`

### 4. Generate implementation guidance

"Next Steps" section with:
- How to serve `auth.md` at the domain root
- How to serve metadata at the well-known paths
- How to add `WWW-Authenticate` header to 401 responses
- Endpoint implementation guidance (without generating framework-specific code unless requested)
- Token exchange implementation at `/oauth2/token`
- Claim page hosting (verification_uri → login → code input → confirm)
- Recommended rate limiting configuration
- Recommended audit events
- Security considerations (token hashing, auth_time validation, replay protection, claim_token handling)

### 5. Generate Agent Provider guide (if role=provider)

When the user is an agent provider (not an app), generate:
- How to mint audience-specific ID-JAGs with `auth_time`
- Token structure (header + payload with required and optional claims)
- How to publish JWKS
- Optionally: how to publish a CIMD (Client ID Metadata Document)
- How to implement revocation (POST SET to events_endpoint)
- How to present consent to the user before asserting identity (using `resource_name` + `resource_logo_uri`)

---

## Workflow: Validate

### 1. Load the auth.md

From a local file path or URL.

### 2. Run validation at the requested level

**Basic (offline):**
- All required headings present (Step 1–6, Errors, Revocation)
- At least one flow documented
- Valid JSON in fenced code blocks for request/response shapes
- AS metadata contains `identity_endpoint`, `token_endpoint`, `grant_types_supported`
- Error table with standard error codes
- Consistency: flows in prose match `identity_types_supported` in metadata JSON
- No unreplaced placeholders

**Full (live):**
- All basic checks, plus:
- Fetch `/.well-known/oauth-protected-resource` from the declared base URL
- Verify `agent_auth` block exists in AS metadata
- Fetch `/.well-known/oauth-authorization-server` and verify consistency
- Check that `identity_endpoint`, `token_endpoint`, `revocation_endpoint` respond (accept 400/401/422, reject 404/405)
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

The identity_assertion flow needs to decide which service user a registration represents. Recommended resolution order:

1. **Delegation record match** — if `(iss, sub)` has a delegation on file, route to same user
2. **Verified email match** — if a user exists with same verified email BUT no `(iss, sub)` delegation → `interaction_required` (401) with claim block for user to confirm linking
3. **Verified phone match** — same pattern
4. **No match → JIT** — create a new user per provisioning policy, or refuse

Reject ID-JAGs with neither a verified email nor a verified phone — there's no basis for matching.

---

## Rate Limiting

The `/agent/identity` endpoint is unauthenticated for anonymous registration. Implement two tiers:

1. **Per-IP** (checked first) — prevents a single source from consuming the tenant's budget. Default: 5/hour anonymous, 60/hour identity_assertion.
2. **Per-tenant** (checked second) — global cap across IPs. Default: 100/hour anonymous, 1000/hour identity_assertion.

Also rate-limit `/oauth2/token` polling — enforce `interval` from the claim block, reject with `slow_down` if too fast.

---

## Recommended Audit Events

| Event | When | Data |
|-------|------|------|
| `registration.created` | Successful POST /agent/identity | registration_id, registration_type, iss, sub |
| `registration.interaction_required` | 401 interaction_required | registration_id, iss, sub, matched_user_id |
| `registration.login_required` | 401 login_required | iss, sub, auth_time, max_age |
| `claim.initiated` | /agent/identity/claim called | registration_id, email |
| `claim.completed` | User submitted correct user_code | registration_id, claimed_by_user_id |
| `claim.expired` | user_code window or registration expired | registration_id |
| `token.exchanged` | /oauth2/token jwt-bearer success | registration_id, access_token_id |
| `token.revoked` | /oauth2/revoke called | access_token_id |
| `registration.revoked` | SET processed at events_endpoint | registration_id, iss, sub |

---

## Security Considerations

- **auth_time validation** — `auth_time` is required in ID-JAGs. Service validates against `idJagMaxAuthAgeSeconds`. If too old, returns `login_required` (401) — agent must get user to re-authenticate at provider.
- **claim_token handling** — returned exactly once in the registration response. Agent holds in memory only for ceremony duration. Do not persist past Step 4.
- **Token hashing** — `claim_token` is a bearer secret. Store only SHA-256 hash server-side.
- **Consent UX** — surface `resource_name` and `resource_logo_uri` from PRM to the user before asserting identity. This is the user's only consent gate.
- **Two revocation layers** — credential layer (agent-callable, `/oauth2/revoke`, kills one access_token) vs registration layer (provider-driven SETs at `events_endpoint`, kills identity_assertion + all derived tokens).
- **Replay protection** — cache `jti` values with TTL of at least `exp - iat` + clock skew (typically 6 min).
- **CIMD resolution** — if `client_id` is a URL, fetch as Client ID Metadata Document and verify `jwks_uri`.
- **Bulk revocation** — provide operator-facing mechanism to revoke all outstanding identity_assertions for a tenant.

---

## Error Codes Reference

| Code | Where | Meaning |
|------|-------|---------|
| `anonymous_not_enabled` | `/agent/identity` | Service doesn't accept anonymous |
| `service_auth_not_enabled` | `/agent/identity` | service_auth disabled |
| `issuer_not_enabled` | `/agent/identity` | Provider not on trust list |
| `invalid_request` | `/agent/identity` | Body/claim/signature/jti/aud problems |
| `interaction_required` (401) | `/agent/identity` | ID-JAG matched account, no delegation — claim needed |
| `login_required` (401) | `/agent/identity` | auth_time too old — re-authenticate at provider |
| `invalid_claim_token` | `/agent/identity/claim` | Token wrong or expired |
| `claimed_or_in_flight` | `/agent/identity/claim` | Already claimed or wrong endpoint |
| `claim_expired` | `/agent/identity/claim` | Registration expired |
| `invalid_grant` | `/oauth2/token` | Assertion expired/revoked |
| `invalid_client` | `/oauth2/token` | client_id not recognized |
| `unsupported_grant_type` | `/oauth2/token` | Not jwt-bearer or claim grant |
| `authorization_pending` | `/oauth2/token` (claim) | User hasn't completed ceremony |
| `expired_token` | `/oauth2/token` (claim) | user_code window closed |
| `slow_down` | `/oauth2/token` (claim) | Polling too fast |
| `rate_limited` (429) | any | Back off and retry |

---

## Agent Readiness Scanner Check

The [isitagentready.com](https://isitagentready.com) scanner validates auth.md as the `authMd` check. Pass criteria:

1. `/auth.md` served from site root with HTTP 200
2. Content is Markdown with H1 heading containing "auth.md"
3. Optionally validates OAuth Protected Resource Metadata at `/.well-known/oauth-protected-resource`
4. Optionally validates Authorization Server metadata at `/.well-known/oauth-authorization-server`

**To pass the check minimally:**
```markdown
# auth.md

This service accepts AI agent registrations.

## Authentication

Agents can register via POST /agent/identity with a valid ID-JAG.
See below for supported methods.
```

**To pass with full marks (all metadata):**
- Serve `/auth.md` with proper heading
- Publish `/.well-known/oauth-protected-resource` with `resource`, `resource_name`, `resource_logo_uri`, `authorization_servers`, `scopes_supported`, `bearer_methods_supported: ["header"]`
- Publish `/.well-known/oauth-authorization-server` with `issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`, and `agent_auth` block containing `skill`, `identity_endpoint`, `claim_endpoint`, `events_endpoint`, and registration methods

**Scan command:**
```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://YOUR-DOMAIN/","enabledChecks":["authMd"]}' | jq '.checks.discovery.authMd'
```

---

## Quality Checklist

Before delivering output, verify:

- [ ] Generated `auth.md` contains all required steps (1-6) + Errors + Revocation
- [ ] AS metadata includes `issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`
- [ ] `agent_auth` block includes `identity_endpoint`, `claim_endpoint`, `events_endpoint`
- [ ] `identity_types_supported` matches the flows the user chose
- [ ] `scopes_supported` reflects actual API scopes found in codebase
- [ ] Base URLs are consistent between auth.md and metadata JSON
- [ ] Error codes table includes all standard codes for the supported flows
- [ ] Step 5 documents token exchange at `/oauth2/token` with jwt-bearer grant
- [ ] Revocation section documents both layers (credential + registration)
- [ ] No unreplaced placeholder values (`{{...}}`, `<your-...>`, `[YOUR_...]`)
- [ ] Validation report covers all rules for the requested level
- [ ] Rate limiting documented (including /oauth2/token polling)
- [ ] Security considerations included (auth_time, claim_token, consent UX)
- [ ] If role=provider: ID-JAG structure with `auth_time` documented

---

## References

- `references/protocol-template.md` — Complete auth.md template with all sections and placeholders
- `references/validation-rules.md` — Full validation ruleset with error messages and severities
- `references/metadata-schema.md` — JSON schema for PRM, AS metadata, ID-JAG, and identity_assertion
- `references/example-auth-md.md` — Working example of a complete auth.md file (Acme Notes)
- `references/implementation-guide.md` — Server-side implementation guide with token exchange, claim ceremony, revocation, and security

---

## Updating Protocol Knowledge

This skill ships with a snapshot of the auth.md protocol specification (v2, June 2026). When possible, fetch the latest version from:

- Skill Home and Doc Hub: `https://auth-md.com`
- Spec: `https://raw.githubusercontent.com/workos/auth.md/refs/heads/main/AUTH.md`
- Docs overview: `https://workos.com/auth-md/docs`
- Apps guide: `https://workos.com/auth-md/docs/apps`
- Agent providers guide: `https://workos.com/auth-md/docs/agent-providers`
- File anatomy: `https://workos.com/auth-md/docs/auth-md`

If fetch fails, use the bundled `references/` as the source of truth.
