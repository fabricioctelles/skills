# Complete Example: auth.md

A working example of an `auth.md` file for the fictional "Acme Notes" service, updated to protocol v2 (June 2026).

---

## Example Context

- **Service:** Acme Notes (collaborative notes app)
- **Resource Server:** `https://api.acmenotes.com`
- **Auth Server:** `https://auth.acmenotes.com`
- **Supported flows:** identity_assertion (ID-JAG), service_auth, anonymous
- **Scopes:** `notes.read`, `notes.write`, `notes.admin`

---

## The File

```markdown
# auth.md

You are an agent. This service supports **agentic registration**: discover → register → (claim if needed) → exchange for an access_token → call API → handle revocation. Follow the steps in order; do not skip ahead.

The resource server is `https://api.acmenotes.com` and the authorization server is `https://auth.acmenotes.com`.

## Step 1 — Discover

Discovery is two hops. The 401 response that pointed you here carries a `WWW-Authenticate` header with the PRM URL:

\```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer resource_metadata="https://api.acmenotes.com/.well-known/oauth-protected-resource"
\```

### 1a. Fetch the Protected Resource Metadata

\```http
GET /.well-known/oauth-protected-resource
\```

Response:

\```json
{
  "resource": "https://api.acmenotes.com/",
  "resource_name": "Acme Notes",
  "resource_logo_uri": "https://acmenotes.com/logo.png",
  "authorization_servers": ["https://auth.acmenotes.com/"],
  "scopes_supported": ["notes.read", "notes.write", "notes.admin"],
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
  "resource": "https://api.acmenotes.com/",
  "authorization_servers": ["https://auth.acmenotes.com/"],
  "scopes_supported": ["notes.read", "notes.write", "notes.admin"],
  "bearer_methods_supported": ["header"],
  "issuer": "https://auth.acmenotes.com",
  "token_endpoint": "https://auth.acmenotes.com/oauth2/token",
  "revocation_endpoint": "https://auth.acmenotes.com/oauth2/revoke",
  "grant_types_supported": [
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:workos:agent-auth:grant-type:claim"
  ],
  "agent_auth": {
    "skill": "https://acmenotes.com/auth.md",
    "identity_endpoint": "https://auth.acmenotes.com/agent/identity",
    "claim_endpoint": "https://auth.acmenotes.com/agent/identity/claim",
    "events_endpoint": "https://auth.acmenotes.com/agent/event/notify",
    "identity_types_supported": ["anonymous", "identity_assertion", "service_auth"],
    "identity_assertion": {
      "assertion_types_supported": [
        "urn:ietf:params:oauth:token-type:id-jag"
      ]
    },
    "events_supported": [
      "https://schemas.workos.com/events/agent/auth/identity/assertion/revoked"
    ]
  }
}
\```

## Step 2 — Pick a method

1. **You have a session tied to a user identity and can exchange it for an ID-JAG** → identity_assertion + id-jag.
2. **You have only the user's email** → service_auth. Claim ceremony required.
3. **You have neither** → anonymous. Claim ceremony optional.

Cross-check against the `agent_auth` block before proceeding.

## Step 3 — Register

Before sending an `identity_assertion` or `service_auth` body, surface "Acme Notes" and its logo to the user and confirm consent. Skip for `anonymous`.

### identity_assertion + id-jag

Mint the ID-JAG with:
- `aud` = `https://api.acmenotes.com/` (from PRM `resource`)
- `auth_time` = epoch seconds of user's last authentication at your provider (**required**)

\```http
POST /agent/identity
Host: auth.acmenotes.com
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
  "registration_id": "reg_01ABC123DEF456",
  "registration_type": "identity_assertion",
  "identity_assertion": "eyJhbGciOiJFUzI1NiJ9...",
  "assertion_expires": "2026-05-22T14:00:00.000Z",
  "scopes": ["notes.read", "notes.write"]
}
\```

Keep `identity_assertion` and go to Step 5.

Response — confirmation required (401, `interaction_required`):

\```json
{
  "error": "interaction_required",
  "error_description": "ID-JAG email matches an existing account but no delegation on file for (iss, sub).",
  "registration_id": "reg_01ABC123DEF456",
  "registration_type": "identity_assertion",
  "claim_url": "https://auth.acmenotes.com/agent/identity/claim",
  "claim_token": "clm_xYz789AbC012dEf",
  "claim_token_expires": "2026-05-22T13:30:00.000Z",
  "post_claim_scopes": ["notes.read", "notes.write"],
  "claim": {
    "user_code": "847291",
    "expires_in": 600,
    "verification_uri": "https://auth.acmenotes.com/login?return_to=%2Fclaim%3Fclaim_attempt_token%3Dcat_abc123",
    "interval": 5
  }
}
\```

Surface `verification_uri` + `user_code` to the user (Step 4b) and poll (Step 4c).

Response — login required (401, `login_required`):

\```json
{
  "error": "login_required",
  "error_description": "auth_time is 7200s old; max allowed is 3600s. Re-authenticate at the provider.",
  "max_age": 3600
}
\```

Re-authenticate the user at your provider and mint a fresh ID-JAG.

### service_auth

\```http
POST /agent/identity
Host: auth.acmenotes.com
Content-Type: application/json

{
  "type": "service_auth",
  "login_hint": "jane@example.com"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_01DEF789GHI012",
  "registration_type": "service_auth",
  "claim_url": "https://auth.acmenotes.com/agent/identity/claim",
  "claim_token": "clm_aBc123DeF456gHi",
  "claim_token_expires": "2026-05-22T13:30:00.000Z",
  "post_claim_scopes": ["notes.read", "notes.write"],
  "claim": {
    "user_code": "592841",
    "expires_in": 600,
    "verification_uri": "https://auth.acmenotes.com/login?return_to=%2Fclaim%3Fclaim_attempt_token%3Dcat_def456",
    "interval": 5
  }
}
\```

No `identity_assertion` yet. Go to Step 4.

### anonymous

\```http
POST /agent/identity
Host: auth.acmenotes.com
Content-Type: application/json

{
  "type": "anonymous"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_01GHI345JKL678",
  "registration_type": "anonymous",
  "identity_assertion": "eyJhbGciOiJFUzI1NiJ9...",
  "assertion_expires": "2026-05-22T14:00:00.000Z",
  "pre_claim_scopes": ["notes.read"],
  "claim_url": "https://auth.acmenotes.com/agent/identity/claim",
  "claim_token": "clm_mNo345PqR678sTu",
  "claim_token_expires": "2026-05-22T13:30:00.000Z",
  "post_claim_scopes": ["notes.read", "notes.write"]
}
\```

Exchange `identity_assertion` at `/oauth2/token` for an access_token with `pre_claim_scopes` (Step 5). To upgrade scopes, go to Step 4.

## Step 4 — Claim ceremony

### 4a. Get the ceremony materials

For **service_auth** and **interaction_required** responses, you already have the `claim` block. Skip to 4b.

For **anonymous**, initiate:

\```http
POST /agent/identity/claim
Host: auth.acmenotes.com
Content-Type: application/json

{
  "claim_token": "clm_mNo345PqR678sTu",
  "email": "jane@example.com"
}
\```

Response (200):

\```json
{
  "registration_id": "reg_01GHI345JKL678",
  "claim_attempt_id": "cla_001",
  "status": "initiated",
  "expires_at": "2026-05-22T13:40:00.000Z",
  "claim_attempt": {
    "user_code": "374918",
    "expires_in": 600,
    "verification_uri": "https://auth.acmenotes.com/login?return_to=%2Fclaim%3Fclaim_attempt_token%3Dcat_ghi789",
    "interval": 5
  }
}
\```

### 4b. Hand off to the user

Surface to the user:

> Open this link, sign in (or sign up), and enter this 6-digit code: **374918**
> https://auth.acmenotes.com/login?return_to=%2Fclaim%3Fclaim_attempt_token%3Dcat_ghi789

The user signs in to Acme Notes, sees a confirmation page, and types the code.

### 4c. Poll for completion

\```http
POST /oauth2/token
Host: auth.acmenotes.com
Content-Type: application/x-www-form-urlencoded

grant_type=urn:workos:agent-auth:grant-type:claim&claim_token=clm_mNo345PqR678sTu
\```

Response while waiting:

\```json
{
  "error": "authorization_pending",
  "error_description": "User has not completed the claim ceremony yet."
}
\```

Response on success:

\```json
{
  "access_token": "eyJhbGciOiJSUzI1NiJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "notes.read notes.write",
  "identity_assertion": "eyJhbGciOiJFUzI1NiJ9...",
  "assertion_expires": "2026-05-22T15:00:00.000Z"
}
\```

Use `access_token` immediately. Cache `identity_assertion` for refresh via Step 5.

If `user_code` window expires:

\```json
{
  "error": "expired_token",
  "error_description": "The user_code window has closed."
}
\```

Re-call `POST /agent/identity/claim` with same `claim_token` and `email` for a fresh code. If that returns `claim_expired`, restart at Step 3.

## Step 5 — Exchange the assertion

\```http
POST /oauth2/token
Host: auth.acmenotes.com
Content-Type: application/x-www-form-urlencoded

grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=eyJhbGciOiJFUzI1NiJ9...&resource=https://api.acmenotes.com/
\```

Response (200):

\```json
{
  "access_token": "eyJhbGciOiJSUzI1NiJ9...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "notes.read notes.write"
}
\```

Same `identity_assertion` can be re-used until it expires. If `invalid_grant`, restart at Step 3.

## Step 6 — Use the access_token

\```http
GET /api/notes
Host: api.acmenotes.com
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9...
\```

**Refresh:** When access_token expires, re-call Step 5 with same identity_assertion. When identity_assertion expires or Step 5 returns `invalid_grant`, restart at Step 3.

On 401 for a previously-working access_token: try Step 5 once. If that also fails, restart at Step 1.

Full API docs: https://docs.acmenotes.com/

## Errors

| Code | Where | What to do |
|------|-------|------------|
| `anonymous_not_enabled` | `/agent/identity` | Pick another method from Step 2 |
| `service_auth_not_enabled` | `/agent/identity` | Pick another method |
| `issuer_not_enabled` | `/agent/identity` | Provider not on trust list. Pick another method |
| `invalid_request` | `/agent/identity` | Fix body shape, ID-JAG signature/jti/aud problems |
| `interaction_required` (401) | `/agent/identity` (ID-JAG) | Body carries `claim` block; surface to user (Step 4) |
| `login_required` (401) | `/agent/identity` (ID-JAG) | Re-authenticate user at provider, mint fresh ID-JAG |
| `invalid_claim_token` | `/agent/identity/claim` | Restart at Step 3 |
| `claimed_or_in_flight` | `/agent/identity/claim` | Already claimed |
| `claim_expired` | `/agent/identity/claim` | Restart at Step 3 |
| `invalid_grant` | `/oauth2/token` | Assertion expired/revoked. Restart at Step 3 |
| `unsupported_grant_type` | `/oauth2/token` | Use one of the two supported grants |
| `authorization_pending` | `/oauth2/token` (claim) | User hasn't finished. Honor `interval` |
| `expired_token` | `/oauth2/token` (claim) | user_code window closed. Re-initiate or restart |
| `slow_down` | `/oauth2/token` (claim) | Add ≥5s to interval |
| `rate_limited` (429) | any | Back off and retry |

## Revocation

Two independent layers:

- **Credential layer (RFC 7009):** POST `token=<access_token>&token_type_hint=access_token` to `https://auth.acmenotes.com/oauth2/revoke`. Kills one access_token. Identity assertion intact — re-run Step 5.
- **Registration layer (RFC 8935):** Provider POSTs a Security Event Token to `events_endpoint`. Invalidates identity_assertion and all derived access_tokens. Agent discovers via `invalid_grant` at `/oauth2/token` — restart at Step 3.

On 401 for a previously-working access_token: try Step 5 once. If `/oauth2/token` succeeds, credential-layer revocation. If `invalid_grant`, registration-layer — restart at Step 3.
```

---

## Notes on This Example

1. **All three flows** documented — in production, delete sections for unsupported flows
2. **Token exchange step** (Step 5) — registration never returns access_token directly; always returns identity_assertion
3. **Browser-based claim ceremony** — user_code + verification_uri replaces OTP-via-email
4. **`interaction_required` response** — shows the 401 path when ID-JAG email matches existing account without delegation
5. **`login_required` response** — shows `auth_time` freshness enforcement
6. **Two revocation layers** — credential (agent-callable) vs registration (provider-driven)
7. **Claim polling at `/oauth2/token`** — uses profile-specific grant URN to avoid collision with standard RFC 8628
