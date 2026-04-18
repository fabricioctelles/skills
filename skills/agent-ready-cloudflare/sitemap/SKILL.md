# Implement sitemap.xml

Publish an XML sitemap at your site root per the
[Sitemaps protocol](https://www.sitemaps.org/protocol.html).

## Requirements

- Serve `/sitemap.xml` as valid XML with HTTP 200
- List canonical `<url><loc>` entries for your public pages
- Keep it updated when content is published or removed
- Reference it from robots.txt: `Sitemap: https://example.com/sitemap.xml`

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discoverability.sitemap.status` is `"pass"`.
