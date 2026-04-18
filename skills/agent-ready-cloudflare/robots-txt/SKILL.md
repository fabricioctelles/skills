# Implement robots.txt

Publish a valid robots.txt at your site root per
[RFC 9309](https://www.rfc-editor.org/rfc/rfc9309).

## Requirements

- Serve `/robots.txt` as `text/plain` with HTTP 200
- Include `User-agent` directives with `Allow`/`Disallow` rules
- Reference your sitemap if one exists: `Sitemap: https://example.com/sitemap.xml`

## Cloudflare

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
can manage your robots.txt from the dashboard, including AI-specific bot rules.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discoverability.robotsTxt.status` is `"pass"`.
