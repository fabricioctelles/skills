# Implement Universal Commerce Protocol (UCP)

Enable content payments via the Universal Commerce Protocol per the
[UCP Specification](https://ucp.dev/specification/overview/).

## Requirements

- Serve JSON at `/.well-known/ucp` with HTTP 200
- Include `protocol_version`, `services`, `capabilities`, and `endpoints`
- Ensure referenced spec URLs and schemas are reachable

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.commerce.ucp.status` is `"pass"`.
