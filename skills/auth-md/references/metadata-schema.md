# Metadata Schema

JSON structure reference for the discovery documents and tokens required by the auth.md protocol (v2, June 2026).

---

## Protected Resource Metadata (PRM)

Served at: `{resource_server}/.well-known/oauth-protected-resource`

Defined by [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728).

```json
{
  "resource": "https://api.example.com/",
  "resource_name": "Example Service",
  "resource_logo_uri": "https://example.com/logo.png",
  "authorization_servers": ["https://auth.example.com/"],
  "scopes_supported": ["read", "write", "admin"],
  "bearer_methods_supported": ["header"]
}
```

### Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `resource` | ✅ | string (URL) | Canonical URL of the API. Used as `aud` in ID-JAGs. |
| `resource_name` | ✅ | string | Display name for consent prompts. Surface to user before asserting identity. |
| `resource_logo_uri` | Recommended | string (URL) | Logo for consent UI. Surface alongside `resource_name`. |
| `authorization_servers` | ✅ | string[] | Base URLs of OAuth AS(s). Agent fetches AS metadata from here. |
| `scopes_supported` | ✅ | string[] | All scopes the resource server understands. |
| `bearer_methods_supported` | ✅ | string[] | How credentials are presented. Typically `["header"]`. |

---

## Authorization Server Metadata

Served at: `{authorization_server}/.well-known/oauth-authorization-server`

Combines standard [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) fields with the `agent_auth` profile block.

```json
{
  "resource": "https://api.example.com/",
  "authorization_servers": ["https://auth.example.com/"],
  "scopes_supported": ["read", "write", "admin"],
  "bearer_methods_supported": ["header"],
  "issuer": "https://auth.example.com",
  "token_endpoint": "https://auth.example.com/oauth2/token",
  "revocation_endpoint": "https://auth.example.com/oauth2/revoke",
  "grant_types_supported": [
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:workos:agent-auth:grant-type:claim"
  ],
  "agent_auth": {
    "skill": "https://example.com/auth.md",
    "identity_endpoint": "https://auth.example.com/agent/identity",
    "claim_endpoint": "https://auth.example.com/agent/identity/claim",
    "events_endpoint": "https://auth.example.com/agent/event/notify",
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
```

### Top-Level OAuth Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `issuer` | ✅ | string (URL) | Canonical issuer URL of this AS. Validate `iss` claim of any token the AS signs against this. |
| `token_endpoint` | ✅ | string (URL) | Where agents exchange identity assertions for access_tokens (Step 5) and poll during claim ceremony (Step 4c). |
| `revocation_endpoint` | ✅ | string (URL) | Where agents POST to revoke an access_token ([RFC 7009](https://datatracker.ietf.org/doc/html/rfc7009)). |
| `grant_types_supported` | ✅ | string[] | Grant types accepted at `token_endpoint`. Must include `urn:ietf:params:oauth:grant-type:jwt-bearer` (token exchange) and `urn:workos:agent-auth:grant-type:claim` (claim polling). |

### `agent_auth` Block Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `skill` | Recommended | string (URL) | URL of the auth.md file. |
| `identity_endpoint` | ✅ | string (URL) | POST endpoint for registration (Step 3). |
| `claim_endpoint` | Conditional | string (URL) | POST endpoint for claim initiation. Required if `service_auth` or `anonymous` supported. |
| `events_endpoint` | Recommended | string (URL) | Receives Security Event Tokens ([RFC 8417](https://datatracker.ietf.org/doc/html/rfc8417)) from providers for registration-layer revocation. |
| `identity_types_supported` | ✅ | string[] | `"anonymous"`, `"identity_assertion"`, `"service_auth"`, or combination. |
| `identity_assertion` | Conditional | object | Required if `"identity_assertion"` in identity_types_supported. |
| `identity_assertion.assertion_types_supported` | ✅ (if identity_assertion) | string[] | `"urn:ietf:params:oauth:token-type:id-jag"`. |
| `events_supported` | Recommended | string[] | Event schemas this service can ingest (currently revocation). Informational. |

### identity_types → Flow Mapping

| `identity_types_supported` | Flow | Ceremony |
|---|---|---|
| `identity_assertion` | ID-JAG verified by provider | None (unless `interaction_required`) |
| `service_auth` | Email hint, browser-based ceremony | RFC 8628-style: user_code + verification_uri |
| `anonymous` | No identity upfront | Optional deferred claim |

---

## ID-JAG Token (Identity Assertion JWT Authorization Grant)

Defined by [draft-ietf-oauth-identity-assertion-authz-grant](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant).

### Header

```json
{
  "typ": "oauth-id-jag+jwt",
  "alg": "ES256",
  "kid": "<provider-key-id>"
}
```

### Payload

```json
{
  "iss": "https://api.agent-provider.com",
  "sub": "<opaque-user-identifier>",
  "aud": "https://api.example.com",
  "client_id": "<issuer-url-or-cimd-url>",
  "jti": "<unique-token-id>",
  "iat": 1716400000,
  "exp": 1716400300,
  "auth_time": 1716399000,
  "email": "user@example.com",
  "email_verified": true,
  "amr": ["mfa"],
  "name": "Jane Smith",
  "phone_number": "+15553805188",
  "phone_number_verified": false,
  "resource": "https://api.example.com",
  "agent_platform": "cursor",
  "agent_context_id": "chat-abc123"
}
```

### Required Claims

| Claim | Description |
|-------|-------------|
| `iss` | Provider's issuer URL (must be on service's trust list) |
| `sub` | Opaque user identifier at the provider |
| `aud` | Service's `resource` URL from the PRM |
| `client_id` | Provider identity (issuer URL or CIMD URL) |
| `jti` | Unique token ID for replay protection |
| `iat` | Issuance time (epoch seconds) |
| `exp` | Expiration (typically iat + 5 minutes) |
| `auth_time` | Epoch seconds when the user last authenticated at the provider. **Required.** Service rejects ID-JAGs whose auth_time is older than its `idJagMaxAuthAgeSeconds` window. |
| `email` + `email_verified: true` OR `phone_number` + `phone_number_verified: true` | At least one verified contact required |

### Optional Claims

| Claim | Description |
|-------|-------------|
| `amr` | Authentication methods reference (e.g., `["mfa"]`) |
| `name` | User's display name |
| `phone_number` | User's phone number |
| `phone_number_verified` | Whether phone is verified |
| `resource` | Resource server URL (informational) |
| `agent_platform` | Agent platform (e.g., `"cursor"`, `"chatgpt"`) |
| `agent_context_id` | Agent context/chat ID |

---

## Client ID Metadata Document (CIMD)

Optional document that decouples provider identity from signing keys. Defined by [draft-ietf-oauth-client-id-metadata-document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/).

Hosted at the URL used as `client_id` in the ID-JAG.

```json
{
  "client_id": "https://api.agent-provider.com/agent-auth.json",
  "client_name": "Agent Provider",
  "logo_uri": "https://agent-provider.com/logo.png",
  "client_uri": "https://agent-provider.com",
  "tos_uri": "https://agent-provider.com/tos",
  "policy_uri": "https://agent-provider.com/privacy",
  "token_endpoint_auth_method": "private_key_jwt",
  "jwks_uri": "https://agent-provider.com/.well-known/jwks.json",
  "scope": "openid email profile"
}
```

---

## Identity Assertion JWT (Service-Signed)

After successful registration, the service returns an `identity_assertion` — a JWT signed by the service that the agent exchanges at `/oauth2/token` for an access_token.

The identity_assertion is:
- Reusable until it expires (`assertion_expires`)
- Exchanged via `POST /oauth2/token` with `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`
- Replaced by a fresh one after claim ceremony completion (v2 carries user claims)

---

## Registration Response Shapes

### identity_assertion + id-jag (no confirmation needed)

```json
{
  "registration_id": "reg_...",
  "registration_type": "identity_assertion",
  "identity_assertion": "<service-signed-jwt>",
  "assertion_expires": "2026-05-04T13:00:00.000Z",
  "scopes": ["read", "write"]
}
```

### identity_assertion + id-jag (interaction_required — 401)

```json
{
  "error": "interaction_required",
  "error_description": "...",
  "registration_id": "reg_...",
  "registration_type": "identity_assertion",
  "claim_url": "https://auth.example.com/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "...",
  "post_claim_scopes": ["read", "write"],
  "claim": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "https://auth.example.com/login?return_to=...",
    "interval": 5
  }
}
```

### service_auth

```json
{
  "registration_id": "reg_...",
  "registration_type": "service_auth",
  "claim_url": "https://auth.example.com/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "2026-05-21T17:31:25.994Z",
  "post_claim_scopes": ["read", "write"],
  "claim": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "https://auth.example.com/login?return_to=...",
    "interval": 5
  }
}
```

### anonymous

```json
{
  "registration_id": "reg_...",
  "registration_type": "anonymous",
  "identity_assertion": "<service-signed-jwt>",
  "assertion_expires": "2026-05-04T13:00:00.000Z",
  "pre_claim_scopes": ["read"],
  "claim_url": "https://auth.example.com/agent/identity/claim",
  "claim_token": "clm_...",
  "claim_token_expires": "2026-05-21T17:26:32.915Z",
  "post_claim_scopes": ["read", "write"]
}
```

### Claim Ceremony Initiation (anonymous → POST /agent/identity/claim)

```json
{
  "registration_id": "reg_...",
  "claim_attempt_id": "cla_...",
  "status": "initiated",
  "expires_at": "2026-05-21T17:31:25.994Z",
  "claim_attempt": {
    "user_code": "123456",
    "expires_in": 600,
    "verification_uri": "https://auth.example.com/login?return_to=...",
    "interval": 5
  }
}
```

### Token Exchange Response (POST /oauth2/token — JWT-bearer grant)

```json
{
  "access_token": "<token>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write"
}
```

### Claim Polling Success (POST /oauth2/token — claim grant)

```json
{
  "access_token": "<token>",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "read write",
  "identity_assertion": "<service-signed-jwt-v2>",
  "assertion_expires": "2026-05-21T18:31:25.994Z"
}
```

---

## Error Response Shape

```json
{
  "error": "<error_code>",
  "error_description": "<human-readable description>"
}
```

---

## Revocation

Two independent layers:

### Credential Layer (RFC 7009) — Agent-Callable

```http
POST /oauth2/revoke
Content-Type: application/x-www-form-urlencoded

token=<access_token>&token_type_hint=access_token
```

Kills one access_token. 200 on success, idempotent. The `identity_assertion` remains intact — re-run Step 5 for a fresh access_token.

### Registration Layer (RFC 8935 SET delivery) — Provider-Driven

Provider POSTs a Security Event Token (`Content-Type: application/secevent+jwt`) to the service's `events_endpoint`. The service invalidates the identity_assertion and all derived access_tokens.

Agent discovers this when `/oauth2/token` returns `invalid_grant` — restart at Step 3.

### SET Payload

```json
{
  "iss": "https://api.agent-provider.com",
  "sub": "<opaque-user-identifier>",
  "aud": "https://auth.example.com",
  "jti": "<unique-identifier>",
  "iat": 1716400000,
  "events": {
    "https://schemas.workos.com/events/agent/auth/identity/assertion/revoked": {}
  }
}
```

### Processing

1. Verify signature against the issuer's JWKS (same trust path as ID-JAG verification)
2. Enforce `jti` uniqueness for replay protection
3. Find all identity_assertions and access_tokens for `(iss, sub, aud)` and invalidate them
4. Return 200 on success, 400 on verification failure
