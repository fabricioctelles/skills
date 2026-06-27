# Protocol Template

Canonical template for generating an `auth.md` file (v2, June 2026). Replace all `{{placeholders}}` with service-specific values. Delete sections for flows the service does not support.

---

## File Structure

An auth.md is organized as a numbered walkthrough the agent follows top to bottom:

1. **Title and intro** — addressed to the agent, declares real hostnames (resource server + auth server)
2. **Step 1 — Discover** — two-hop discovery (PRM → AS metadata)
3. **Step 2 — Pick a method** — decision tree
4. **Step 3 — Register** — one subsection per supported method
5. **Step 4 — Claim ceremony** — browser-based user_code ceremony (if service_auth or anonymous claim)
6. **Step 5 — Exchange the assertion** — POST identity_assertion to /oauth2/token for access_token
7. **Step 6 — Use the access_token** — how to use and refresh
8. **Errors** — error codes table
9. **Revocation** — two-layer revocation model

---

## Complete Template

```markdown
# auth.md

You are an agent. This service supports **agentic registration**: discover → register → (claim if needed) → exchange for an access_token → call API → handle revocation. Follow the steps in order; do not skip ahead.

Examples use placeholder hosts: `{{base_url}}` (the resource server hosting the API you want to call) and `{{auth_server_url}}` (the authorization server that handles registration).

## Step 1 — Discover

Discovery is two hops. The 401 response that pointed you here carries a `WWW-Authenticate` header with the PRM URL:

\```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="{{base_url}}/.well-known/oauth-protected-resource"
\```

### 1a. Fetch the Protected Resource Metadata

\```http
GET /.well-known/oauth-protected-resource
\```

Response:

\```json
{
  "resource": "{{base_url}}/",
  "resource_name": "{{service_name}}",
  "resource_logo_uri": "{{logo_url}}",
  "authorization_servers": ["{{auth_server_url}}/"],
  "scopes_supported": [{{scopes_list}}],
  "bearer_methods_supported": ["header"]
}
\```

### 1b. Fetch the Authorization Server metadata

\```http
GET /.well-known/oauth-authorization-server
\```

Response:

\```json
{
  "resource": "{{base_url}}/",
  "authorization_servers": ["{{auth_server_url}}/"],
  "scopes_supported": [{{scopes_list}}],
  "bearer_methods_supported": ["header"],
  "issuer": "{{auth_server_url}}",
  "token_endpoint": "{{auth_server_url}}/oauth2/token",
  "revocation_endpoint": "{{auth_server_url}}/oauth2/revoke",
  "grant_types_supported": [
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:workos:agent-auth:grant-type:claim"
  ],
  "agent_auth": {
    "skill": "{{auth_md_url}}",
    "identity_endpoint": "{{auth_server_url}}/agent/identity",
    "claim_endpoint": "{{auth_server_url}}/agent/identity/claim",
    "events_endpoint": "{{auth_server_url}}/agent/event/notify",
    "identity_types_supported": [{{identity_types}}],
    "identity_assertion": {
      "assertion_types_supported": [{{assertion_types}}]
    },
    "events_supported": [
      "https://schemas.workos.com/events/agent/auth/identity/assertion/revoked"
    ]
  }
}
\```

## Step 2 — Pick a method

Use this decision tree:

1. **You have a session tied to a user identity and can exchange it for an ID-JAG, audience-bound to this service** → identity_assertion + id-jag.
2. **You have only the user's email** → service_auth. Claim ceremony required.
3. **You have neither** → anonymous. Claim ceremony optional; deferred until the user wants to take ownership.

Before sending: cross-check your choice against the `agent_auth` block. If your type is not in `identity_types_supported`, pick another or stop.

## Step 3 — Register

Before sending an `identity_assertion` or `service_auth` body, surface the service's `resource_name` and `resource_logo_uri` (from Step 1a) and the scope set you'll be acting under, and confirm with the user. Skip this for `anonymous`.

### identity_assertion + id-jag

<!-- DELETE THIS SECTION IF NOT SUPPORTING ID-JAG FLOW -->

Mint the ID-JAG with:
- `aud` = the `resource` from the PRM
- `iss` = your provider's issuer URL (must be on trust list)
- `email_verified: true` OR `phone_number_verified: true`
- Fresh `jti`, near-term `exp` (~5 minutes)
- `auth_time` — epoch seconds when the user last authenticated at your provider. **Required.**

\```http
POST /agent/identity
Content-Type: application/json

{
  "type": "identity_assertion",
  "assertion_type": "urn:ietf:params:oauth:token-type:id-jag",
  "assertion": "<ID-JAG>"
}
\```

Response — no confirmation needed (200):

\```json
{
  "registration_id": "reg_...",
  "registration_type": "identity_assertion",
  "identity_assertion": "<service-signed-jwt>",
  "assertion_expires": "{{assertion_expiry}}",
  "scopes": [{{post_registration_scopes}}]
}
\```

Keep `identity_assertion` and go to Step 5.

Response — confirmation required (401, `interaction_required`):

\```json
{
  "error": "interaction_required",
  "error_description": "...",
  "registration_id": "reg_...",
  "registration_type": "identity_assertion",
  "claim_url": "{{auth_server_url}}/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "...",
  "post_claim_scopes": [{{post_claim_scopes}}],
  "claim": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "{{auth_server_url}}/login?return_to=...",
    "interval": 5
  }
}
\```

Surface `verification_uri` + `user_code` to the user (Step 4b) and poll (Step 4c).

Response — login required (401, `login_required`):

\```json
{
  "error": "login_required",
  "error_description": "auth_time is too old; re-authenticate at the provider.",
  "max_age": 3600
}
\```

Re-authenticate the user at your provider (`prompt=login`) and mint a fresh ID-JAG.

### service_auth

<!-- DELETE THIS SECTION IF NOT SUPPORTING SERVICE_AUTH FLOW -->

\```http
POST /agent/identity
Content-Type: application/json

{
  "type": "service_auth",
  "login_hint": "user@example.com"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_...",
  "registration_type": "service_auth",
  "claim_url": "{{auth_server_url}}/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "{{claim_ttl}}",
  "post_claim_scopes": [{{post_claim_scopes}}],
  "claim": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "{{auth_server_url}}/login?return_to=...",
    "interval": 5
  }
}
\```

No `identity_assertion` yet. Go to Step 4.

### anonymous

<!-- DELETE THIS SECTION IF NOT SUPPORTING ANONYMOUS FLOW -->

\```http
POST /agent/identity
Content-Type: application/json

{
  "type": "anonymous"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_...",
  "registration_type": "anonymous",
  "identity_assertion": "<service-signed-jwt>",
  "assertion_expires": "{{assertion_expiry}}",
  "pre_claim_scopes": [{{pre_claim_scopes}}],
  "claim_url": "{{auth_server_url}}/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "{{claim_ttl}}",
  "post_claim_scopes": [{{post_claim_scopes}}]
}
\```

The `identity_assertion` exchanges at `/oauth2/token` for an access_token with `pre_claim_scopes` immediately (Step 5). To upgrade scopes, go to Step 4.

## Step 4 — Claim ceremony

<!-- DELETE THIS ENTIRE SECTION IF ONLY SUPPORTING identity_assertion WITHOUT interaction_required -->

The end goal: get a signed-in user to confirm a 6-digit `user_code` **you supply them**. The code travels from you → user; the user authenticates to the service and types it into a page the service owns.

### 4a. Get the ceremony materials

For **service_auth** registrations and **interaction_required** responses, you already have the `claim` block from Step 3. Skip to 4b.

For **anonymous** registrations, initiate the ceremony:

\```http
POST /agent/identity/claim
Content-Type: application/json

{
  "claim_token": "clm_...",
  "email": "user@example.com"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_...",
  "claim_attempt_id": "cla_...",
  "status": "initiated",
  "expires_at": "{{claim_attempt_ttl}}",
  "claim_attempt": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "{{auth_server_url}}/login?return_to=...",
    "interval": 5
  }
}
\```

### 4b. Hand off to the user

Surface `verification_uri` and `user_code` to the user in a single message:

> Open this link, sign in (or sign up), and enter this 6-digit code: **123456**
> {{verification_uri}}

The user will:
1. Open `verification_uri`
2. Authenticate with the service (sign in or sign up)
3. Land on the claim page, see their identity displayed, type the `user_code`, and submit

### 4c. Poll for completion

Poll the standard `token_endpoint` (from AS metadata) with the profile-specific claim grant:

\```http
POST /oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:workos:agent-auth:grant-type:claim
&claim_token=<claim_token>
\```

Response while waiting:

\```json
{
  "error": "authorization_pending",
  "error_description": "..."
}
\```

Response on success:

\```json
{
  "access_token": "<token>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "{{scopes}}",
  "identity_assertion": "<service-signed-jwt-v2>",
  "assertion_expires": "{{assertion_expiry}}"
}
\```

Use `access_token` immediately; cache `identity_assertion` for refresh via Step 5.

If the `user_code` window expires:

\```json
{
  "error": "expired_token",
  "error_description": "..."
}
\```

Re-call `POST /agent/identity/claim` with the same `claim_token` and `email` to mint a fresh `user_code`. If that returns `claim_expired`, restart at Step 3.

Honor `interval` (in seconds); on `slow_down` back off.

## Step 5 — Exchange the assertion

POST the `identity_assertion` to the token endpoint with the RFC 7523 JWT-bearer grant:

\```http
POST /oauth2/token
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
&assertion=<identity_assertion>
&resource={{base_url}}/
\```

Response (200):

\```json
{
  "access_token": "<token>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "{{scopes}}"
}
\```

The same `identity_assertion` can be re-used to mint additional access_tokens until it expires. If `/oauth2/token` returns `invalid_grant`, restart at Step 3.

## Step 6 — Use the access_token

Present as a bearer token:

\```http
GET /api/some-resource
Authorization: Bearer <access_token>
\```

**Refresh:** When the access_token expires, re-call Step 5 with the same `identity_assertion`. When the identity_assertion itself expires or `/oauth2/token` returns `invalid_grant`, restart at Step 3. There is no refresh_token — the two-step pattern replaces it.

On 401 for a previously-working access_token: try Step 5 once. If that also fails, restart at Step 1.

Full API reference: `{{api_docs_url}}`

## Errors

| Code | Where | What to do |
|------|-------|------------|
| `anonymous_not_enabled` | `/agent/identity` | Pick another method from Step 2 |
| `service_auth_not_enabled` | `/agent/identity` | Pick another method |
| `issuer_not_enabled` | `/agent/identity` | Provider not on trust list. Pick another method |
| `invalid_request` | `/agent/identity` | Fix body shape, claims, signature, jti, aud problems |
| `interaction_required` (401) | `/agent/identity` (ID-JAG) | Body carries `claim` block; surface to user (Step 4) |
| `login_required` (401) | `/agent/identity` (ID-JAG) | Re-authenticate user at provider, mint fresh ID-JAG |
| `invalid_claim_token` | `/agent/identity/claim` | Restart at Step 3 |
| `claimed_or_in_flight` | `/agent/identity/claim` | Already claimed. Re-read Step 3 response |
| `claim_expired` | `/agent/identity/claim` | Registration expired. Restart at Step 3 |
| `invalid_grant` | `/oauth2/token` | Assertion expired/revoked. Restart at Step 3 |
| `invalid_client` | `/oauth2/token` | client_id not recognized |
| `unsupported_grant_type` | `/oauth2/token` | Use one of the two supported grant types |
| `authorization_pending` | `/oauth2/token` (claim) | User hasn't completed ceremony. Honor `interval` |
| `expired_token` | `/oauth2/token` (claim) | user_code window closed. Re-initiate or restart |
| `slow_down` | `/oauth2/token` (claim) | Add ≥5s to interval and retry |
| `rate_limited` (429) | any | Back off and retry |

## Revocation

Two independent layers:

- **Credential layer (RFC 7009):** POST `token=<access_token>&token_type_hint=access_token` to `{{auth_server_url}}/oauth2/revoke`. Kills one access_token. Identity assertion intact — re-run Step 5.
- **Registration layer (RFC 8935 SET delivery):** Provider POSTs a Security Event Token to `events_endpoint`. Service invalidates identity_assertion and all derived access_tokens. Agent discovers this when `/oauth2/token` returns `invalid_grant` — restart at Step 3.

On 401 for a previously-working access_token: try Step 5 once. If `/oauth2/token` succeeds, credential-layer revocation — fresh access_token works. If `invalid_grant`, registration-layer — restart at Step 3.
```

---

## Placeholder Reference

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{base_url}}` | API base URL (resource server) | `https://api.acme.com` |
| `{{service_name}}` | Human-readable service name | `Acme Notes` |
| `{{logo_url}}` | Service logo URL | `https://acme.com/logo.png` |
| `{{auth_server_url}}` | Authorization server base URL | `https://auth.acme.com` |
| `{{auth_md_url}}` | URL where auth.md is hosted | `https://acme.com/auth.md` |
| `{{scopes_list}}` | JSON array of scope strings | `"notes.read", "notes.write"` |
| `{{identity_types}}` | Supported identity types | `"anonymous", "identity_assertion", "service_auth"` |
| `{{assertion_types}}` | Supported assertion types | `"urn:ietf:params:oauth:token-type:id-jag"` |
| `{{pre_claim_scopes}}` | Scopes before claim (anonymous) | `"notes.read"` |
| `{{post_claim_scopes}}` | Scopes after claim | `"notes.read", "notes.write"` |
| `{{post_registration_scopes}}` | Scopes after ID-JAG registration | `"notes.read", "notes.write"` |
| `{{assertion_expiry}}` | Identity assertion expiry (ISO) | `2026-05-22T13:00:00.000Z` |
| `{{claim_ttl}}` | Claim token expiration (ISO) | `2026-05-22T12:00:00.000Z` |
| `{{claim_attempt_ttl}}` | Claim attempt expiration | `2026-05-22T12:10:00.000Z` |
| `{{api_docs_url}}` | Link to full API docs | `https://docs.acme.com/` |

---

## Generation Rules

1. **Keep the file concise and high-signal** — anything the agent doesn't need to register or operate belongs in main documentation, not in auth.md
2. **Use fenced code blocks with language hints** (`http`, `json`) so agents can extract templates unambiguously
3. **Declare real hostnames in the intro** — resource server and auth server — so the agent knows which host each example targets
4. **Delete sections for unsupported flows** — don't leave empty sections or "N/A" markers
5. **The PRM is authoritative** — if anything in auth.md conflicts with the PRM, the PRM wins
6. **Token exchange is always required** — registration never returns an access_token directly; always returns an identity_assertion that must be exchanged at `/oauth2/token`
