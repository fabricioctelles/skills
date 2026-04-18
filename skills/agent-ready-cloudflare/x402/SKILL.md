# Implement x402 Payment Protocol

Support agent-native HTTP payments via the
[x402 protocol](https://x402.org)
([docs](https://docs.x402.org), [GitHub](https://github.com/coinbase/x402)).

## Requirements

- Add x402 payment middleware to your API routes
- Use `@x402/express`, `@x402/hono`, or `@x402/next` middleware
- Configure a facilitator URL and wallet address
- Protected routes return HTTP 402 with payment requirements that agents fulfill automatically

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.commerce.x402.status` is `"pass"`.
