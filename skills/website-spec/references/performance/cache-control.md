---
title: "Cache-Control headers"
category: performance
status: required
updated: "2026-05-29T12:14:17.000Z"
sources:
  - title: "RFC 9111 — HTTP Caching"
    url: "https://www.rfc-editor.org/rfc/rfc9111"
    publisher: "IETF"
  - title: "MDN — Cache-Control"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control"
    publisher: "MDN"
  - title: "MDN — HTTP caching"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching"
    publisher: "MDN"
  - title: "MDN — Vary"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary"
    publisher: "MDN"
licence: CC-BY-4.0
---

# Cache-Control headers

> Cache-Control tells browsers and CDNs how long to keep a response. Use immutable + max-age=31536000 for fingerprinted assets and short or no-cache for HTML.

## What it is

`Cache-Control` is an HTTP response header that governs how, where, and for how long a response may be stored and reused. It is defined in RFC 9111 and replaces the older `Expires` and `Pragma` headers.

```http
Cache-Control: public, max-age=31536000, immutable
```

Key directives:

- `public` — any cache may store it (CDN, proxy, browser).
- `private` — only the user's browser may store it.
- `no-cache` — store, but revalidate before reuse.
- `no-store` — do not store at all.
- `max-age=<seconds>` — fresh for this many seconds.
- `s-maxage=<seconds>` — same, but only for shared caches (CDNs).
- `immutable` — promise that the body will never change, so the browser can skip revalidation.
- `stale-while-revalidate=<seconds>` — serve stale while fetching a fresh copy in the background.

## Why it matters

A correct cache policy is the cheapest possible performance win. Repeat visitors download nothing for cached assets. CDNs absorb traffic before it reaches your origin. Without it, every page view re-fetches the same CSS, JS, and images. With it, the second visit can be near-instant.

`no-cache` is also a privacy tool: it forces revalidation of HTML so users see your latest content, while still allowing 304s.

## How to implement

**Fingerprinted assets — cache forever.** If the URL contains a content hash (`app.4f3a2b.js`), the body cannot change. Cache aggressively:

```http
Cache-Control: public, max-age=31536000, immutable
```

`immutable` matters: without it, Firefox revalidates on reload even with `max-age` set.

**HTML — short or no cache.** Pages change often and rarely have fingerprinted URLs. Use:

```http
Cache-Control: public, max-age=0, must-revalidate
```

or, for highly dynamic pages:

```http
Cache-Control: no-store
```

Pair with `ETag` so revalidation is cheap.

**Per-user content — private.** Anything personalised needs `private` to prevent shared caches from leaking one user's data to another.

**Set `Vary` correctly.** If the response varies by `Accept-Encoding` or `Accept-Language`, set `Vary` accordingly. Missing `Vary` causes a CDN to serve gzip to a client that asked for brotli.

## Common mistakes

- No `Cache-Control` at all. Browsers then use heuristic caching, which is unpredictable.
- `max-age=31536000` on HTML. Users get stale pages and you can't fix bugs without changing the URL.
- `no-cache` mistaken for "do not cache". It only means "revalidate first". Use `no-store` to actually prevent storage.
- Missing `Vary: Accept-Encoding` when serving brotli/gzip via a CDN.
- Fingerprinted URL without `immutable` — Firefox will still revalidate on reload.

## Verification

- `curl -I https://example.com/app.4f3a2b.js` — confirm `Cache-Control` is set.
- DevTools → Network → Size column shows "(memory cache)" or "(disk cache)" for cached resources.
- Webhint and Lighthouse flag inefficient cache policy.
