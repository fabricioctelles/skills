# Implement OAuth Protected Resource Metadata

Publish OAuth Protected Resource Metadata so agents can discover how to
authenticate per [RFC 9728](https://www.rfc-editor.org/rfc/rfc9728).

## Requirements

- Serve JSON at `/.well-known/oauth-protected-resource` with HTTP 200
- Include `resource` (your resource identifier URL)
- Include `authorization_servers` (array of OAuth/OIDC issuer URLs)
- Optionally include `scopes_supported`
- Optionally return `WWW-Authenticate` with `resource_metadata` on 401 responses

## Cloudflare

Use [Workers](https://developers.cloudflare.com/workers/) to serve the
metadata endpoint and [Access](https://developers.cloudflare.com/cloudflare-one/)
as the authorization server.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.oauthProtectedResource.status` is `"pass"`.
