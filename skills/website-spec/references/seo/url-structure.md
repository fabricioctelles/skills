---
title: "URL structure"
category: seo
status: recommended
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax"
    url: "https://www.rfc-editor.org/rfc/rfc3986"
    publisher: "IETF"
  - title: "URL structure best practices"
    url: "https://developers.google.com/search/docs/crawling-indexing/url-structure"
    publisher: "Google Search Central"
  - title: "URL — Living Standard"
    url: "https://url.spec.whatwg.org/"
    publisher: "WHATWG"
licence: CC-BY-4.0
---

# URL structure

> URLs are the most stable identifier on the web. Keep them lowercase, hyphenated, descriptive, and shallow. Treat them as a public API for your content.

## What it is

A URL is the canonical name for a resource on the web. Its syntax is defined by RFC 3986 and refined for the browser by the WHATWG URL Living Standard. The path component — everything after the host — is where structure choices have the most impact on SEO and usability.

```
https://example.com/articles/web-security/csp
            ^host       ^path
```

## Why it matters

URLs are quoted in chat, pasted into documents, printed on slides, and saved in bookmarks for years. Once a URL is public, it is effectively forever — changing it requires a redirect, and chains of redirects degrade. They also appear under the page title in search results, so a clean, readable URL is a small but real signal of quality to both users and crawlers.

A consistent URL structure also makes analytics, A/B testing, redirect rules, and access controls dramatically simpler.

## How to implement

Treat URLs as a public API:

- **Lowercase only.** RFC 3986 says the path is case-sensitive, so `/About` and `/about` are different URLs. Pick lowercase and enforce a 301 redirect for any uppercase variant.
- **Hyphens, not underscores.** Search engines tokenise on hyphens but not underscores. `web-security` reads as two words; `web_security` reads as one.
- **No trailing whitespace, no encoded spaces.** Replace spaces with hyphens before the URL is ever generated.
- **Descriptive slugs.** `/articles/csp` beats `/articles/12345`. Both work, but the readable one survives social sharing better.
- **Avoid deep nesting.** Aim for three or fewer path segments after the host. Deep URLs (`/section/sub/sub/sub/post`) signal low priority and are hard to refactor.
- **Pick trailing-slash or no-trailing-slash and stick with it.** Both work; mixing creates duplicate-content risk. Use a 301 to enforce the chosen form.
- **Query parameters are for filters, not content.** Canonical content should have a clean path. Parameters are fine for sort order, pagination, and tracking, but the canonical link should strip them.
- **ASCII where possible.** Modern browsers handle IDNs and percent-encoded UTF-8 fine, but non-ASCII URLs break in older tooling, copy-paste, and email clients.

```
Good:  https://example.com/articles/web-security/csp
Bad:   https://example.com/Articles/Web_Security/CSP/?id=12345&utm_source=x
```

## Common mistakes

- Mixed case across the site, with no canonical enforcement.
- Including dates that go stale: `/2023/10/csp` looks outdated by 2026 even if the content has been kept current.
- Session IDs or tracking parameters baked into canonical URLs.
- Renaming URLs every CMS migration. Each rename costs link equity even with redirects.

## Verification

- Crawl the site with a tool like Screaming Frog or a sitemap fetcher. Check for mixed-case duplicates and trailing-slash inconsistencies.
- Confirm 301 redirects enforce the canonical form.
- Check Search Console's Pages report for "Duplicate, Google chose different canonical" — that often points at URL-structure problems.
