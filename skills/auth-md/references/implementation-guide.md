# Server-Side Implementation Guide

Detailed guidance for implementing auth.md protocol endpoints on the backend (v2, June 2026). Covers discovery, registration, claim ceremony, token exchange, revocation, security, rate limiting, and audit events.

---

## Table of Contents

1. [Minimum Implementation](#minimum-implementation)
2. [Discovery Documents](#discovery-documents)
3. [POST /agent/identity — Registration Handler](#post-agentidentity--registration-handler)
4. [ID-JAG Verification](#id-jag-verification)
5. [Claim Ceremony](#claim-ceremony)
6. [POST /oauth2/token — Token Endpoint](#post-oauth2token--token-endpoint)
7. [Revocation](#revocation)
8. [User Matching and JIT Provisioning](#user-matching-and-jit-provisioning)
9. [Rate Limiting](#rate-limiting)
10. [Security](#security)
11. [Audit Events](#audit-events)
12. [Deploy Checklist](#deploy-checklist)

---

## Minimum Implementation

1. Publish `/.well-known/oauth-protected-resource` with `resource_name` and `resource_logo_uri`
2. Publish `/.well-known/oauth-authorization-server` with `issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`, and `agent_auth` block
3. Return `WWW-Authenticate: Bearer resource_metadata="..."` on 401 responses
4. Host `POST /agent/identity` that dispatches on the `type` field
5. For identity_assertion: maintain a trust list and verify ID-JAG signatures via JWKS, validate `auth_time`
6. For service_auth: return `claim` block with `user_code` + `verification_uri`
7. For anonymous: issue `identity_assertion` immediately with pre-claim scopes
8. Host `POST /agent/identity/claim` for deferred claim initiation
9. Implement `POST /oauth2/token` handling both grant types (jwt-bearer exchange + claim polling)
10. Implement `POST /oauth2/revoke` for credential-layer revocation (RFC 7009)
11. Accept SETs at `events_endpoint` for registration-layer revocation (RFC 8935)
12. Record audit events for every state change

---

## Discovery Documents

### Serving the PRM

```
GET /.well-known/oauth-protected-resource
→ 200 OK
→ Content-Type: application/json
```

Must include `resource_name` and `resource_logo_uri` — agents surface these to the user for consent before asserting identity.

Cache aggressively: `Cache-Control: public, max-age=3600`.

### Serving the AS Metadata

```
GET /.well-known/oauth-authorization-server
→ 200 OK
→ Content-Type: application/json
```

Must include standard OAuth fields (`issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`) plus the `agent_auth` block with `identity_endpoint`, `claim_endpoint`, `events_endpoint`.

### WWW-Authenticate Header

On every 401 response from the API:

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://api.service.com/.well-known/oauth-protected-resource"
```

---

## POST /agent/identity — Registration Handler

All registration requests share the same endpoint and dispatch on the `type` field:

```
POST /agent/identity
Content-Type: application/json
```

### Dispatch

| `type` | Flow | Returns |
|--------|------|---------|
| `identity_assertion` | ID-JAG verified | `identity_assertion` (service-signed JWT) |
| `service_auth` | Email hint + browser ceremony | `claim` block (ceremony materials) |
| `anonymous` | No identity | `identity_assertion` + `claim_token` for deferred claim |

### Handler: identity_assertion + id-jag

1. Decode the ID-JAG header to obtain `kid` and `alg`
2. Look up the issuer (`iss`) in the trust list. Reject if unknown → `issuer_not_enabled`
3. Fetch JWKS from the provider (see ID-JAG Verification section for caching)
4. Verify signature → `invalid_request` if fails
5. Validate claims:
   - `aud` matches the `resource` from PRM → `invalid_request`
   - `exp` is in the future → `invalid_request`
   - `iat` not unreasonably in the future (~1-2 min skew)
   - `jti` not seen recently → `invalid_request` (replay)
   - `auth_time` present and within `idJagMaxAuthAgeSeconds` → `login_required` (401) if too old
   - At least `email_verified` or `phone_number_verified` is `true` → `invalid_request`
6. Match or provision the user (see User Matching)
7. Check delegation: if `(iss, sub)` is known OR JIT-provisioned without collision → success
8. If email/phone collision with existing account but no delegation on file → `interaction_required` (401) with `claim` block
9. On success: sign an `identity_assertion` JWT and return it

### Handler: service_auth

1. Validate `login_hint` (email format)
2. Create a registration row with type `service_auth`
3. Generate `claim_token` (returned to agent once), `user_code` (6-digit), `claim_attempt_token` (embedded in verification_uri)
4. Store SHA-256 hashes of `claim_token`
5. Build `verification_uri` pointing to the service's login page with `return_to` parameter
6. Return the registration response with `claim` block containing `user_code`, `verification_uri`, `expires_in`, `interval`

### Handler: anonymous

1. Apply rate limits
2. Create a registration row
3. Sign an `identity_assertion` JWT with pre-claim scopes
4. Generate `claim_token` for deferred claim. Store only SHA-256 hash.
5. Return `identity_assertion` + `claim_token` + pre/post claim scopes

---

## ID-JAG Verification

### Trust List

Maintain a registry of providers. Minimum entry: issuer URL. Richer entries can pin JWKS URI, CIMD URL, or attestation policy.

### JWKS Fetching

- Fetch `{iss}/.well-known/jwks.json` on first use
- Cache per `Cache-Control`, with floor 10 min, ceiling 24h
- On `kid` miss, refetch once before rejecting

### CIMD Resolution

If `client_id` is a URL:
1. Fetch as OAuth Client ID Metadata Document
2. Verify `jwks_uri` matches the one used to verify signature

### auth_time Validation

- `auth_time` is **required** in ID-JAGs
- Compare `now() - auth_time` against `idJagMaxAuthAgeSeconds` (service-configured, e.g., 3600)
- If too old: return `login_required` (401) with `max_age` in the response
- Agent must re-authenticate user at provider and mint fresh ID-JAG

### Replay Protection

- Cache `jti` values with TTL of at least `exp - iat` + clock skew (typically 6 min)
- Reject on collision with `invalid_request`

---

## Claim Ceremony

The v2 claim ceremony is browser-based, borrowing from RFC 8628 device authorization.

### POST /agent/identity/claim (anonymous deferred claim)

1. Hash `claim_token`, look up registration
2. Reject if not found → `invalid_claim_token`, already claimed → `claimed_or_in_flight`, expired → `claim_expired`
3. Generate `user_code` (6-digit), `claim_attempt_token`
4. Build `verification_uri` with embedded `claim_attempt_token`
5. Return `claim_attempt` block with `user_code`, `verification_uri`, `expires_in`, `interval`

### Service-Hosted Claim Page

When the user opens `verification_uri`:
1. Redirect to login if not authenticated
2. After login, show claim page displaying:
   - The user's identity ("You're signed in as jane@example.com")
   - The requesting agent/provider info (from PRM `resource_name`)
   - Input field for the 6-digit code
3. On correct code submission: mark claim as complete, associate registration with user
4. Incorrect code: show error, allow retry (up to limit)

### Claim Completion Flow

When the user submits the correct `user_code` on the claim page:
1. Mark the claim as complete in the database
2. For anonymous: sign a new `identity_assertion` (v2) carrying user claims, superseding the pre-claim one
3. For service_auth: sign the first `identity_assertion` for this registration
4. The next poll at `/oauth2/token` with the claim grant returns the access_token + identity_assertion

---

## POST /oauth2/token — Token Endpoint

Handles two grant types at the same endpoint:

### Grant: urn:ietf:params:oauth:grant-type:jwt-bearer (Token Exchange)

```
POST /oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
&assertion=<identity_assertion>
&resource=<resource_url>  (optional but recommended)
```

Processing:
1. Verify the `identity_assertion` JWT signature (service's own key)
2. Validate `exp` not passed → `invalid_grant` if expired
3. Check assertion not revoked → `invalid_grant` if revoked
4. Mint a fresh `access_token` scoped to the assertion's scopes
5. Return standard OAuth token response

### Grant: urn:workos:agent-auth:grant-type:claim (Claim Polling)

```
POST /oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:workos:agent-auth:grant-type:claim
&claim_token=<claim_token>
```

Processing:
1. Hash `claim_token`, look up registration
2. If claim not yet completed → return `authorization_pending`
3. If user_code window expired → return `expired_token`
4. If polling too fast → return `slow_down`
5. If claim completed → mint access_token + return along with new `identity_assertion`

Why a profile-specific grant URN? So this doesn't collide with services that also implement standard RFC 8628 device authorization at the same token endpoint.

### Error Responses

| Error | HTTP | Condition |
|-------|------|-----------|
| `invalid_grant` | 400 | Assertion expired, revoked, or invalid |
| `invalid_client` | 401 | client_id not recognized |
| `unsupported_grant_type` | 400 | Not one of the two supported grants |
| `authorization_pending` | 400 | Claim polling — user hasn't finished |
| `expired_token` | 400 | user_code window closed |
| `slow_down` | 400 | Polling too fast — add ≥5s |

---

## Revocation

### Credential Layer — POST /oauth2/revoke (RFC 7009)

Agent-callable. Kills one access_token.

```
POST /oauth2/revoke
Content-Type: application/x-www-form-urlencoded

token=<access_token>&token_type_hint=access_token
```

- Return 200 on success (idempotent)
- The underlying `identity_assertion` remains valid — agent can re-exchange for a new access_token

### Registration Layer — Events Endpoint (RFC 8935)

Provider-driven. Receives Security Event Tokens.

```
POST /agent/event/notify
Content-Type: application/secevent+jwt

<SET JWT>
```

Processing:
1. Verify SET signature against issuer's JWKS
2. Enforce `jti` uniqueness
3. Match `events` key to supported schemas
4. For `https://schemas.workos.com/events/agent/auth/identity/assertion/revoked`:
   - Invalidate all identity_assertions for `(iss, sub, aud)`
   - Invalidate all derived access_tokens
5. Return 200 on success, 400 on verification failure

### Bulk Revocation

Provide an operator-facing mechanism to revoke all outstanding identity_assertions and access_tokens for a tenant in one shot — for incident response.

---

## User Matching and JIT Provisioning

Resolution order:

1. **Delegation record match** — if `(iss, sub)` has a delegation on file, route to that user. Strongest identifier.
2. **Verified email match** — if a user exists with same verified email:
   - If delegation exists for `(iss, sub)` → direct match (already covered above)
   - If NO delegation for `(iss, sub)` → `interaction_required` (401). User must confirm linking.
3. **Verified phone match** — same pattern.
4. **No match → JIT** — create a new user per provisioning policy, or refuse.

Reject ID-JAGs with neither verified email nor verified phone.

---

## Rate Limiting

### Two Tiers

| Tier | Checked | Default Anonymous | Default identity_assertion |
|------|---------|-------------------|---------------------------|
| Per-IP | First | 5/hour | 60/hour |
| Per-tenant | Second | 100/hour | 1000/hour |

### Implementation

- Sliding-window counter with shared store
- Fail open on store errors
- Return 429 with `Retry-After` header
- Also rate-limit `/oauth2/token` polling (respect `interval` from claim block, reject with `slow_down`)

---

## Security

### Token Hashing

| Token | Storage | Plaintext leaves server |
|-------|---------|------------------------|
| `claim_token` | SHA-256 hash | Once, in the registration response |
| `user_code` | Stored for comparison | Displayed on claim page when user submits |
| `identity_assertion` | Full JWT stored (or just signature hash for lookup) | In registration response |

### claim_token

- Returned **exactly once** to the agent in the registration response
- Agent holds in memory for ceremony duration — must not persist past Step 4
- High-entropy: prefix `clm_` + 25+ chars base62

### auth_time Enforcement

- Service configures `idJagMaxAuthAgeSeconds` (default: 3600)
- Reject ID-JAGs where `now() - auth_time > idJagMaxAuthAgeSeconds`
- Return `login_required` (401) with `max_age` field

### Consent UX

- Surface `resource_name` and `resource_logo_uri` from PRM to user before identity assertion
- The claim page should display who is requesting access (provider name from CIMD or ID-JAG metadata)

### user_code Security

- 6-digit numeric code
- 10-minute TTL (configurable via `expires_in`)
- Tight retry limits (3-5 attempts) on the claim page
- Code is tied to the `claim_attempt_token` embedded in `verification_uri`

### Replay Protection

- `jti` cache mandatory for ID-JAGs
- `jti` uniqueness enforced for SETs at events_endpoint
- Shared store required for multi-replica deployments

### Trust List Discipline

Treat the trusted-providers list as security-critical configuration. Changes should be audited.

---

## Audit Events

### Recommended Events

| Event | When | Minimum Data |
|-------|------|--------------|
| `registration.created` | Successful POST /agent/identity | registration_id, registration_type, iss, sub (if ID-JAG) |
| `registration.interaction_required` | 401 interaction_required returned | registration_id, iss, sub, matched_user_id |
| `registration.login_required` | 401 login_required returned | iss, sub, auth_time, max_age |
| `claim.initiated` | /agent/identity/claim called | registration_id, email |
| `claim.completed` | User submitted correct user_code | registration_id, claimed_by_user_id |
| `claim.expired` | user_code window or registration expired | registration_id |
| `token.exchanged` | /oauth2/token jwt-bearer success | registration_id, access_token_id |
| `token.revoked` | /oauth2/revoke called | access_token_id |
| `registration.revoked` | SET processed at events_endpoint | registration_id, iss, sub |
| `registration.expired` | Unclaimed registration past TTL | registration_id |

---

## Deploy Checklist

### Before publishing

- [ ] PRM served at `/.well-known/oauth-protected-resource` with `resource_name` and `resource_logo_uri`
- [ ] AS metadata served at `/.well-known/oauth-authorization-server` with `issuer`, `token_endpoint`, `revocation_endpoint`, `grant_types_supported`, and `agent_auth` block
- [ ] `agent_auth` contains `identity_endpoint`, `claim_endpoint`, `events_endpoint`
- [ ] `auth.md` served at the domain root
- [ ] API returns `WWW-Authenticate` header on 401s
- [ ] `POST /agent/identity` dispatches correctly by `type`
- [ ] Trust list configured (if identity_assertion)
- [ ] JWKS fetching with cache (if identity_assertion)
- [ ] `auth_time` validation against `idJagMaxAuthAgeSeconds` (if identity_assertion)
- [ ] `POST /agent/identity/claim` generates user_code + verification_uri (if service_auth/anonymous)
- [ ] Claim page served at verification_uri (login → code input → confirm)
- [ ] `POST /oauth2/token` handles jwt-bearer grant (assertion → access_token)
- [ ] `POST /oauth2/token` handles claim grant (polling → access_token + identity_assertion)
- [ ] `POST /oauth2/revoke` kills access_tokens (RFC 7009)
- [ ] Events endpoint accepts SETs for registration revocation
- [ ] Rate limiting active on `/agent/identity` and `/oauth2/token`
- [ ] claim_token stored as SHA-256 hash
- [ ] Replay protection for `jti` implemented
- [ ] Audit events being recorded

### Recommended tests

- [ ] identity_assertion: valid ID-JAG with fresh auth_time → identity_assertion returned
- [ ] identity_assertion: expired ID-JAG → `invalid_request`
- [ ] identity_assertion: auth_time too old → `login_required` (401)
- [ ] identity_assertion: email collision without delegation → `interaction_required` (401) with claim block
- [ ] identity_assertion: repeated `jti` → `invalid_request` (replay)
- [ ] identity_assertion: unknown issuer → `issuer_not_enabled`
- [ ] service_auth: valid email → registration with claim block (user_code + verification_uri)
- [ ] anonymous: registration → identity_assertion with pre_claim_scopes
- [ ] anonymous: claim initiation → claim_attempt with user_code
- [ ] /oauth2/token jwt-bearer: valid assertion → access_token
- [ ] /oauth2/token jwt-bearer: expired assertion → `invalid_grant`
- [ ] /oauth2/token claim: before completion → `authorization_pending`
- [ ] /oauth2/token claim: after completion → access_token + identity_assertion
- [ ] /oauth2/token claim: after window expires → `expired_token`
- [ ] /oauth2/token claim: too-fast polling → `slow_down`
- [ ] /oauth2/revoke: valid access_token → 200
- [ ] events_endpoint: valid SET → registrations revoked
- [ ] Rate limit exceeded → 429
- [ ] 401 on API → WWW-Authenticate header present
