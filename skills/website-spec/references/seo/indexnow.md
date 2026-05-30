---
title: "IndexNow"
category: seo
status: optional
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "IndexNow protocol"
    url: "https://www.indexnow.org/documentation"
    publisher: "IndexNow"
  - title: "Bing — IndexNow"
    url: "https://www.bing.com/indexnow"
    publisher: "Bing"
  - title: "Yandex — IndexNow"
    url: "https://yandex.com/support/webmaster/indexnow/key.html"
    publisher: "Yandex"
licence: CC-BY-4.0
---

# IndexNow

> An open protocol for telling participating search engines that a URL has changed. One HTTP request pushes Bing, Yandex, Naver, and Seznam to recrawl — Google does not participate.

## What it is

IndexNow is a simple push protocol that lets a site tell search engines a URL has been added, updated, or deleted. The publisher hosts a key file at the site root and sends an HTTP request to a participating endpoint listing the changed URLs. Bing, Yandex, Naver, Seznam, and Yep all consume the same feed; one submission propagates to all of them. Google does **not** participate.

The submission is a single GET or POST:

```http
POST /indexnow HTTP/1.1
Host: api.indexnow.org
Content-Type: application/json

{
  "host": "example.com",
  "key": "abc123...xyz",
  "keyLocation": "https://example.com/abc123xyz.txt",
  "urlList": [
    "https://example.com/articles/csp",
    "https://example.com/articles/hsts"
  ]
}
```

The key file at `https://example.com/abc123xyz.txt` must contain the same key as plain text — that proves you control the host.

## Why it matters

Discovery is the slowest part of indexing. A sitemap tells crawlers what exists; IndexNow tells them what just changed. For news, e-commerce stock changes, and price updates, that gap matters — Bing typically recrawls within minutes of an IndexNow ping versus hours or days from sitemap-only discovery.

It is also a low-effort improvement. A single endpoint covers every participating engine, no per-engine integrations needed.

Google's absence is the limiting factor. If most of your traffic is from Google, IndexNow is a nice-to-have. For markets where Bing, Yandex, or Naver have meaningful share (Russia, South Korea, the Czech Republic, US Bing-driven verticals), the impact is real.

## How to implement

The shape is straightforward:

1. **Generate a key.** 8 to 128 characters, `[a-zA-Z0-9-]`. Pick one and reuse it indefinitely.
2. **Host the key file at the site root.** `https://example.com/<key>.txt`, served as `text/plain`, body equal to the key.
3. **Submit URLs on change.** Fire a request to `https://api.indexnow.org/indexnow` (or directly to Bing's or Yandex's endpoint) after every publish, update, or unpublish event.
4. **Limit volume.** Up to 10,000 URLs per request. Do not send the entire sitemap on every cron tick — submit only what changed since the last call.
5. **Send deletions too.** A 404 or 410 should also be submitted; that is how participating engines learn to drop URLs quickly.

A small wrapper around your CMS publish hook is usually enough. Many SEO plugins (including Yoast) submit automatically.

## Common mistakes

- Submitting URLs that return non-200 statuses you did not mean to publish.
- Re-submitting on every page view rather than only on change.
- Hosting the key file at the wrong path or behind redirects. The key file must return 200 directly.
- Treating IndexNow as a Google signal. Google ignores the protocol — use Search Console's URL Inspection tool for one-off Google submissions.

## Verification

- `curl https://example.com/<key>.txt` should return the key as plain text.
- The endpoint returns `200 OK` on accepted submissions, `202` if quarantined, and `400`/`403`/`422` on errors. Log the response.
- Bing Webmaster Tools shows IndexNow activity under "URL Submission" — confirm the URLs appear there.
