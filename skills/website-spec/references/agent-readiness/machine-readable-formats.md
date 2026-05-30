---
title: "Machine-readable formats"
category: agent-readiness
status: recommended
updated: "2026-05-29T09:45:15.000Z"
sources:
  - title: "RSS 2.0 Specification"
    url: "https://www.rssboard.org/rss-specification"
    publisher: "RSS Advisory Board"
  - title: "JSON Feed 1.1"
    url: "https://www.jsonfeed.org/version/1.1/"
    publisher: "JSON Feed"
  - title: "Is It Agent Ready?"
    url: "https://isitagentready.com/"
    publisher: "Is It Agent Ready?"
licence: CC-BY-4.0
---

# Machine-readable formats

> Offer JSON, RSS, or plain markdown endpoints alongside HTML where it makes sense. Agents and feed readers prefer typed data over scraped HTML.

## What it is

A machine-readable format is a representation of your content designed to be consumed by software rather than rendered for humans. HTML is the universal default, but for lists, feeds, and structured records it is the wrong shape. JSON, RSS, Atom, and plain markdown are better.

Most sites already publish one without thinking about it: `sitemap.xml`. Adding a feed and an optional JSON endpoint covers the cases agents and aggregators care about most.

```xml
<!-- /feed -->
<rss version="2.0">
  <channel>
    <title>Example Corp Blog</title>
    <link>https://example.com/blog</link>
    <description>Notes on building things.</description>
    <item>
      <title>Setting up CSP</title>
      <link>https://example.com/blog/csp</link>
      <pubDate>Tue, 12 May 2026 10:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>
```

```json
// /index.json
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "Example Corp Blog",
  "home_page_url": "https://example.com/blog",
  "feed_url": "https://example.com/index.json",
  "items": [
    {
      "id": "https://example.com/blog/csp",
      "url": "https://example.com/blog/csp",
      "title": "Setting up CSP",
      "date_published": "2026-05-12T10:00:00Z",
      "content_html": "<p>...</p>"
    }
  ]
}
```

## Why it matters

- Agents that need a list of recent posts can fetch one URL instead of scraping a paginated index.
- Feed readers, archive tools, and notification services have decades of support for RSS and Atom.
- JSON Feed is friendlier to modern toolchains and easier to extend.
- For documentation, exposing a `.md` next to each `.html` gives agents the source without HTML extraction.

The cost is small and the upside compounds: every consumer that does not have to parse HTML is one less source of bad quotes.

## How to implement

- **Sitemap.** Every site should have one — see [XML sitemaps](../seo/xml-sitemaps.md).
- **A feed.** Publish RSS 2.0 or Atom at a discoverable URL such as `/feed`, `/feed.xml`, or `/rss.xml`. Optionally publish a JSON Feed at `/feed.json` or `/index.json`. Link both from `<head>`:

  ```html
  <link rel="alternate" type="application/rss+xml" title="Blog" href="/feed.xml">
  <link rel="alternate" type="application/json" title="Blog" href="/feed.json">
  ```

- **Markdown sources.** For documentation, serve `page.md` alongside `page.html` — see [Per-page Markdown source endpoints](../agent-readiness/markdown-source-endpoints.md) for the full pattern, including `Accept: text/markdown` content negotiation done correctly with `Vary: Accept`.
- **Content negotiation.** Powerful, but easy to misuse. Always set `Vary: Accept` on every representation, otherwise caches will pin the wrong one for every subsequent visitor. When the formats are very different (HTML vs JSON), distinct URLs are usually simpler.
- **Stable schemas.** Once published, treat the field names as a contract — same rule as URLs.

## Common mistakes

- Truncating feed items to a one-line teaser. If you want agents to quote you fairly, give them the full content.
- Forgetting to update `pubDate` or `date_published`, so readers think nothing has changed.
- Letting the feed go stale because the CMS export broke quietly. Monitor it.
- Mixing absolute and relative URLs inside feed items. Use absolute everywhere.

## Verification

- Validate RSS at [validator.w3.org/feed](https://validator.w3.org/feed/).
- Validate JSON Feed against the [spec](https://www.jsonfeed.org/version/1.1/).
- Subscribe to your own feed in a reader and confirm new posts appear.
