---
name: agent-ready-mpp
description: >
  Sub-skill de agent-ready-cloudflare: Implement MPP Payment Discovery
---
# Implement MPP Payment Discovery

Publish an OpenAPI document with MPP payment discovery metadata so AI agents
can discover your payable endpoints via the
[Machine Payment Protocol](https://mpp.dev)
([spec](https://paymentauth.org/draft-payment-discovery-00.txt)).

## Requirements

- Serve `/openapi.json` at the site root with HTTP 200
- Include `x-payment-info` extensions on payable operations
- Each `x-payment-info` must declare `intent` (charge or session), `method` (tempo, stripe, lightning, card), and `amount`
- Optionally include `currency`, `description`, and top-level `x-service-info` with categories

## Example

```json
{
  "openapi": "3.1.0",
  "info": { "title": "My API", "version": "1.0" },
  "paths": {
    "/api/generate": {
      "post": {
        "x-payment-info": {
          "intent": "charge",
          "method": "stripe",
          "amount": "0.01",
          "currency": "USD",
          "description": "Generate content"
        }
      }
    }
  }
}
```

## Validate

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.commerce.mpp.status` is `"pass"`.

## References

- [Machine Payment Protocol](https://mpp.dev)
- [Payment Discovery Spec](https://paymentauth.org/draft-payment-discovery-00.txt)
