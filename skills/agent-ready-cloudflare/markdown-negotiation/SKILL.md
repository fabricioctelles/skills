# Implement Markdown Content Negotiation

Support `Accept: text/markdown` content negotiation so agents can request
markdown versions of your pages.
See [llmstxt.org](https://llmstxt.org/) and
[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/).

## Requirements

- When a request includes `Accept: text/markdown`, return a markdown representation of the page
- Set `Content-Type: text/markdown` on the response
- HTML remains the default for requests without the markdown accept header
- Include an `x-markdown-tokens` header with the token count if available

## Cloudflare

[Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)
enables this automatically for Cloudflare zones — no application code changes needed.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.contentAccessibility.markdownNegotiation.status` is `"pass"`.
