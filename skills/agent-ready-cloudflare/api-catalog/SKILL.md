# Implement API Catalog

Publish an API catalog for automated discovery per
[RFC 9727](https://www.rfc-editor.org/rfc/rfc9727).

## Requirements

- Serve `/.well-known/api-catalog` with `Content-Type: application/linkset+json` and HTTP 200
- Include a `linkset` array with entries for each API
- Each entry needs an `anchor` URL and link relations: `service-desc` (OpenAPI spec), `service-doc` (docs), and optionally `status` (health endpoint)
- See [RFC 9727 Appendix A](https://www.rfc-editor.org/rfc/rfc9727#appendix-A) for examples

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.apiCatalog.status` is `"pass"`.
