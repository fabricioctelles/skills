# Implement AI Bot Rules in robots.txt

Add explicit `User-agent` entries for AI crawlers in your robots.txt per
[RFC 9309](https://www.rfc-editor.org/rfc/rfc9309).

## Requirements

- Add `User-agent` blocks for AI-specific bots: `GPTBot`, `OAI-SearchBot`, `Claude-Web`, `Google-Extended`, `Amazonbot`, `anthropic-ai`, `Bytespider`, `CCBot`, `Applebot-Extended`
- Set `Allow` and/or `Disallow` rules matching your content policy
- A wildcard `User-agent: *` block alone is not sufficient — explicit AI bot entries are required

## Cloudflare

[AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/)
lets you manage AI bot rules from the dashboard without editing robots.txt manually.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.botAccessControl.robotsTxtAiRules.status` is `"pass"`.
