---
title: "Sitemap index files"
category: seo
status: recommended
updated: "2026-05-29T19:18:37.253Z"
sources:
  - title: "Sitemaps XML format — sitemap index files"
    url: "https://www.sitemaps.org/protocol.html#index"
    publisher: "sitemaps.org"
  - title: "Manage sitemaps for large sites"
    url: "https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps"
    publisher: "Google Search Central"
licence: CC-BY-4.0
---

# Sitemap index files

> A sitemap of sitemaps. Used when a site has more than 50,000 URLs or wants to split sitemaps by content type for cleaner reporting.

## What it is

A sitemap index is an XML file that lists [other sitemap files](../seo/xml-sitemaps.md). Its root element is `<sitemapindex>` and each child `<sitemap>` has a `<loc>` pointing at a child sitemap, with an optional `<lastmod>`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-articles.xml</loc>
    <lastmod>2026-05-29</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-products.xml</loc>
    <lastmod>2026-05-28</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-images.xml</loc>
    <lastmod>2026-05-29</lastmod>
  </sitemap>
</sitemapindex>
```

Submit the index URL to Search Console. Crawlers will fetch the index, then each child sitemap, then each URL.

## Why it matters

Two reasons to use an index:

1. **Scale.** A single sitemap is capped at 50,000 URLs and 50 MB uncompressed. Once a site exceeds either, the only standard-compliant option is to split into multiple sitemaps and reference them from an index.
2. **Reporting.** Search Console reports submitted-vs-indexed counts per sitemap. Splitting by content type (articles, products, categories, images) lets you see at a glance which section has indexing problems instead of one big number for the whole site.

A site with 500 URLs does not need an index. Adding one anyway is harmless but adds a layer of fetching that gains you nothing.

## How to implement

Split sitemaps by something meaningful:

- **By content type** — `sitemap-posts.xml`, `sitemap-pages.xml`, `sitemap-products.xml`.
- **By language or region** — `sitemap-en.xml`, `sitemap-nl.xml`. Pairs well with `hreflang`.
- **By date** — `sitemap-2025.xml`, `sitemap-2026.xml` for archive-heavy sites.

Rules:

- Up to **50,000 child sitemaps** per index, and the index itself is capped at 50 MB uncompressed.
- Every child sitemap must be on the same host as the index, with limited cross-host exceptions.
- `<lastmod>` on the index entry should reflect the newest `<lastmod>` inside the child sitemap. This lets crawlers skip refetching unchanged sections.
- Reference the index from `robots.txt` and submit only the index in Search Console — do not also submit each child individually.

## Common mistakes

- Pointing the index at child sitemaps on a different host.
- Stale `<lastmod>` on the index while the child sitemap has fresh URLs.
- Splitting arbitrarily (sitemap-1, sitemap-2) so the reporting buckets are meaningless.
- Submitting both the index and each child sitemap, causing duplicate reports.

## Verification

- Fetch the index URL. Confirm the root element is `<sitemapindex>` and each child resolves to a valid sitemap.
- Validate against the sitemaps.org XSD.
- In Search Console, confirm the index shows the expected number of child sitemaps and their per-sitemap indexing stats.
