---
name: agent-ready-ai-rules
description: >
  Sub-skill de agent-ready-cloudflare: Implement AI Bot Rules in robots.txt
---
# Implement AI Bot Rules in robots.txt

Add explicit `User-agent` entries for AI crawlers in your robots.txt per
[RFC 9309](https://www.rfc-editor.org/rfc/rfc9309).

## Requirements

- Add `User-agent` blocks for AI search crawlers: `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`. These fetch the pages AI assistants use in their answers, so blocking them affects whether you appear in AI answers
- Add `User-agent` blocks for AI training crawlers: `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `Bytespider`, `Amazonbot`. Blocking these does not affect whether your pages appear in AI search results
- User-triggered fetchers (`ChatGPT-User`, `Claude-User`, `Perplexity-User`) retrieve pages when a user asks; some vendors do not apply robots.txt to them
- Set `Allow` and/or `Disallow` rules matching your content policy
- A `User-agent: *` group with rules also passes, but applies one policy to every crawler. Explicit entries let you treat search and training crawlers differently

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
