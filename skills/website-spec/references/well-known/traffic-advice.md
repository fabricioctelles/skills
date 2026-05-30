---
title: "/.well-known/traffic-advice"
category: well-known
status: optional
updated: "2026-05-29T17:54:33.000Z"
sources:
  - title: "Traffic Advice — formal specification"
    url: "https://buettner.github.io/private-prefetch-proxy/traffic-advice.html"
    publisher: "Jeremy Roman (editor) / Private Prefetch Proxy community"
  - title: "private-prefetch-proxy on GitHub — traffic-advice.md"
    url: "https://github.com/buettner/private-prefetch-proxy/blob/main/traffic-advice.md"
    publisher: "Private Prefetch Proxy community"
  - title: "IANA — Well-Known URIs Registry"
    url: "https://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml"
    publisher: "IANA"
  - title: "Private Prefetch Proxy"
    url: "https://developer.chrome.com/blog/private-prefetch-proxy"
    publisher: "Chrome for Developers"
licence: CC-BY-4.0
---

# /.well-known/traffic-advice

> A JSON file that tells private prefetch proxies — most notably Chrome's — whether to send prefetch traffic to your origin, and at what fraction. Optional opt-out / throttle mechanism, provisionally registered with IANA.

## What it is

`/.well-known/traffic-advice` is a JSON document that tells private prefetch proxies — most notably Chrome's [Private Prefetch Proxy](https://developer.chrome.com/blog/private-prefetch-proxy) — whether (and how much) to send prefetch traffic to your origin on a user's behalf. By default a proxy assumes consent. This file lets you refuse, or throttle to a fraction.

The body is a JSON array of advice objects, served as `application/trafficadvice+json`:

```json
[
  {"user_agent": "prefetch-proxy", "disallow": true}
]
```

Each object has a `user_agent` and either `disallow: true` (refuse traffic) or `fraction` (a value between 0 and 1, the share of traffic to allow). A proxy picks the most-specific match — its own brand name (e.g. `"ExamplePrivatePrefetchProxy"`), the generic class `"prefetch-proxy"`, or the wildcard `"*"`. The first identity that appears in the proxy's own self-identification list wins.

The convention was authored by Jeremy Roman at Google and is provisionally registered with IANA. Outside Chrome's Private Prefetch Proxy, no major implementer has adopted it yet.

## Why it matters

Most sites should never need this file. A prefetched response improves [Core Web Vitals](../performance/core-web-vitals.md) for the user who clicks through, and the proxy itself caches per HTTP semantics so origin load stays low. Reasons to override the default:

- **Origin under load.** Drop `fraction` during a launch or news spike to thin out speculative requests without affecting real traffic.
- **Log hygiene.** Proxy-sourced prefetches still hit access logs even though they bypass client-side analytics. Disallow to keep raw counts clean.
- **Bandwidth-billed infra.** Origins on per-byte billing may want a fraction below 1, or `disallow` outright.

If none of those apply, ship nothing here — a missing file is the correct signal for "default behaviour is fine".

## How to implement

```http
GET /.well-known/traffic-advice HTTP/1.1
Host: example.com

HTTP/1.1 200 OK
Content-Type: application/trafficadvice+json
Cache-Control: public, max-age=3600

[
  {"user_agent": "prefetch-proxy", "fraction": 0.5}
]
```

- **`Content-Type: application/trafficadvice+json` is mandatory.** Any other value (including `application/json`) is treated as no advice and the proxy uses its default.
- **Cache lifetime.** The spec suggests a minimum freshness of 10 minutes and a maximum of 48 hours; agents default to 30 minutes when no `Cache-Control` is set. Pick a value short enough that posture changes propagate within an operationally reasonable window.
- **Match ordering.** List the broadest advice first (`"prefetch-proxy"`), then narrower per-implementer exceptions. A proxy walks its own identity list and takes the earliest match.
- **Status codes.** Return `200` with JSON, or omit the file. `429` and `503` signal back-pressure — the proxy will pause and retry later. Any other non-OK status is treated as "no advice".

## Common mistakes

- Returning `application/json` instead of `application/trafficadvice+json`. The spec requires the dedicated media type and proxies ignore anything else.
- Using `fraction: 0` to opt out. `disallow: true` is the documented refusal; `fraction: 0` works but is the wrong vocabulary.
- Forgetting the wildcard. To affect every prefetch proxy (not only Chrome's), include an entry with `"user_agent": "*"`.
- Treating absence as a bug. A missing file is the correct "default behaviour" signal — only ship the file when you have a reason to override.

## Verification

```
curl -I https://example.com/.well-known/traffic-advice
curl -s https://example.com/.well-known/traffic-advice | jq .
```

Confirm `Content-Type: application/trafficadvice+json` and a sensible `Cache-Control`. The body should parse as a JSON array; each entry should have a string `user_agent` and one of `disallow: true` or a numeric `fraction` between 0 and 1.
