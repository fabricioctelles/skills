---
title: "Maintenance pages and 503"
category: resilience
status: recommended
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "RFC 9110 — HTTP Semantics: 503 Service Unavailable"
    url: "https://www.rfc-editor.org/rfc/rfc9110.html#name-503-service-unavailable"
    publisher: "IETF"
  - title: "RFC 9110 — HTTP Semantics: Retry-After"
    url: "https://www.rfc-editor.org/rfc/rfc9110.html#name-retry-after"
    publisher: "IETF"
  - title: "Google Search Central — How to deal with planned site downtime"
    url: "https://developers.google.com/search/blog/2011/01/how-to-deal-with-planned-site-downtime"
    publisher: "Google Search Central"
licence: CC-BY-4.0
---

# Maintenance pages and 503

> When the site is intentionally offline, return HTTP 503 with a Retry-After header and a page that tells users what is happening and when to come back.

## What it is

A maintenance page is what visitors see during planned downtime — a database migration, a major deploy, a hardware swap. The page itself is only half of the requirement. The other half is the HTTP response: status `503 Service Unavailable` with a `Retry-After` header that tells crawlers and clients when to come back.

```
HTTP/2 503
Retry-After: 3600
Content-Type: text/html; charset=utf-8
```

## Why it matters

A maintenance page that returns `200 OK` is indistinguishable from your real site to a search engine. Googlebot will happily index "We're back in an hour" as the content of every URL on your domain. If the outage lasts a day, you can wake up to a site that ranks for nothing.

`503` is the explicit signal that the server is unavailable on purpose and that the condition is temporary. Crawlers slow down or pause. CDNs may serve stale content from cache. Monitoring tools record an outage instead of a successful response. Browsers and SDKs that respect `Retry-After` back off cleanly.

## How to implement

Configure the edge or load balancer to return the maintenance response, not the application itself — the application is the thing you're taking down.

- Status code: `503`.
- `Retry-After` header: either an integer number of seconds (`Retry-After: 1800`) or an HTTP date (`Retry-After: Wed, 29 May 2026 14:00:00 GMT`). Use the form that matches your confidence in the ETA.
- Body: a single HTML page that loads no external dependencies, no analytics, and no fonts from CDNs that may also be down.
- Tell the user: what is happening, when you expect to be back, and where to get updates (status page, social account).

Most edge providers (Cloudflare, Fastly, Nginx, HAProxy) can serve a static maintenance page with a 503 from a single rule. Allow an admin IP through so you can verify the deploy before lifting the block.

```nginx
# Nginx example
if (-f /etc/nginx/maintenance.flag) {
  return 503;
}
error_page 503 @maintenance;
location @maintenance {
  root /var/www/maintenance;
  rewrite ^.*$ /index.html break;
  add_header Retry-After 1800 always;
}
```

## Common mistakes

- Returning `200 OK` with a "we'll be back soon" message. Search engines treat this as the new content of every URL.
- Returning `503` with no `Retry-After`. Clients have to guess.
- Loading third-party scripts (analytics, chat widgets, fonts) on the maintenance page. Most of them will fail and the page may not render.
- Forgetting to remove the maintenance flag after the deploy and leaving the site at 503 for hours.

## Verification

- `curl -I https://example.com/` returns `HTTP/2 503` and a `Retry-After` header.
- The page renders without the application backend running.
- Status page (if you have one) shows the planned window.
