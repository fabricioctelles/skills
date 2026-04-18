# Implement ACP Discovery Document

Publish an ACP discovery document so AI agents can discover your
[Agentic Commerce Protocol](https://agenticcommerce.dev) implementation.

## Requirements

- Serve JSON at `/.well-known/acp.json` with HTTP 200
- Include `protocol.name` set to `"acp"` and `protocol.version`
- Include `api_base_url` as an absolute HTTP(S) URL
- Include `transports` as a non-empty array of supported transport types
- Include `capabilities.services` as a non-empty array of offered services

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.commerce.acp.status` is `"pass"`.
