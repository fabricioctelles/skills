---
title: "Image and video sitemap extensions"
category: seo
status: optional
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "Image sitemaps"
    url: "https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps"
    publisher: "Google Search Central"
  - title: "Video sitemaps and alternatives"
    url: "https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps"
    publisher: "Google Search Central"
  - title: "Sitemaps XML format"
    url: "https://www.sitemaps.org/protocol.html"
    publisher: "sitemaps.org"
licence: CC-BY-4.0
---

# Image and video sitemap extensions

> Optional XML extensions that add image and video metadata to sitemap entries. Useful when media is loaded by JavaScript or hosted on a CDN that crawlers cannot reach by following links.

## What it is

Sitemaps support extensions for declaring images and videos associated with each page. They use additional XML namespaces alongside the standard `urlset`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://example.com/articles/csp</loc>
    <image:image>
      <image:loc>https://cdn.example.com/csp-hero.jpg</image:loc>
    </image:image>
    <image:image>
      <image:loc>https://cdn.example.com/csp-diagram.png</image:loc>
    </image:image>
  </url>
</urlset>
```

The video extension is similar (`xmlns:video`) and supports more metadata: `title`, `description`, `thumbnail_loc`, `content_loc`, and `player_loc`.

## Why it matters

Crawlers normally find images by parsing the HTML of pages they fetch. That is usually enough. The extensions only earn their keep when:

- **Media is loaded by JavaScript** and not in the initial HTML.
- **Media lives on a different host** (a CDN or media subdomain) that crawlers do not visit independently.
- **You publish a lot of original photography or video** and want crawlers to discover updates quickly.

For most marketing sites, plain `<img>` and `<video>` elements with good `alt` text and `<source>` declarations are enough. The extensions are an optimisation, not a baseline.

## How to implement

For images:

- Up to **1,000 images per `<url>` entry**.
- Each `<image:image>` needs only `<image:loc>`. Other fields (`caption`, `title`, `geo_location`, `license`) are accepted by some crawlers but are not widely used.
- Use the canonical image URL — the one the page actually loads. CDN URLs are fine.

For videos:

- Each `<video:video>` needs `thumbnail_loc`, `title`, `description`, and one of `content_loc` or `player_loc`.
- Keep titles under 100 characters and descriptions under 2,048.
- Add `duration` in seconds where possible.

For both, prefer to **add them to existing page sitemaps** rather than create a separate image or video sitemap. That keeps the relationship between page and media explicit. If volume is too high, split into a dedicated `sitemap-images.xml` and reference it from your sitemap index.

## Common mistakes

- Listing images that are not actually used on the page in `<loc>`. Crawlers cross-check.
- Pointing `<image:loc>` at a redirect or a 404.
- Forgetting the `xmlns:image` or `xmlns:video` namespace declaration on `<urlset>`.
- Treating these as a ranking lever. They help discovery, not ranking.

## Verification

- Validate the sitemap against the extension XSDs.
- In Search Console, check the Sitemaps report for parsed image and video counts.
- Test that each `<image:loc>` returns `200 OK` with an image `Content-Type`.
