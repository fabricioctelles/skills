# Implement Content Signals

Declare AI content usage preferences in your robots.txt using
[Content Signals](https://contentsignals.org/)
([IETF draft](https://datatracker.ietf.org/doc/draft-romm-aipref-contentsignals/)).

## Requirements

- Add `Content-Signal` directives to your robots.txt under the relevant `User-agent` block
- Declare preferences for `ai-train`, `search`, and `ai-input`
- Example: `Content-Signal: ai-train=no, search=yes, ai-input=no`

## Cloudflare

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
supports Content Signals configuration from the dashboard.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.botAccessControl.contentSignals.status` is `"pass"`.
