---
title: "International URL structure"
category: i18n
status: recommended
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "Google Search Central — Managing multi-regional and multilingual sites"
    url: "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"
    publisher: "Google Search Central"
  - title: "W3C i18n — When should I use language negotiation?"
    url: "https://www.w3.org/International/questions/qa-when-lang-neg"
    publisher: "W3C"
  - title: "RFC 3986 — Uniform Resource Identifier (URI): Generic Syntax"
    url: "https://www.rfc-editor.org/rfc/rfc3986"
    publisher: "IETF"
licence: CC-BY-4.0
---

# International URL structure

> Pick a single URL pattern for multilingual or multi-regional content — country-code top-level domain, subdomain, or subdirectory — and stick with it. Optionally localise the slugs too.

## What it is

When a site serves more than one language or region, every localised page needs its own stable URL. Three patterns are in common use, all compatible with [hreflang](/i18n/hreflang) and standard crawling:

```
ccTLD:        https://example.de/
Subdomain:    https://de.example.com/
Subdirectory: https://example.com/de/
```

A fourth pattern — a query parameter such as `https://example.com/?loc=de` — exists in the wild but is explicitly discouraged by Google for geotargeting because the locale is not part of the resource identity. Treat it as out of scope.

## Why it matters

The URL pattern is the foundation everything else in your internationalisation stack annotates. [hreflang](/i18n/hreflang), [sitemap hreflang entries](/i18n/sitemap-hreflang), the [language switcher](/i18n/language-switcher), canonical tags, and analytics segmentation all reference the same URLs. Change the pattern later and every one of those has to be rebuilt, with 301 redirects to preserve link equity.

The pattern also signals locality to users and search engines. A `.de` domain reads as German to a visitor before the page loads. A `/de/` path reads as "the German section of an international site". Neither is wrong; they communicate different things.

## How to implement

Pick one of the three patterns for the whole site:

| Pattern | Geotargeting | Server location | Infra cost | Perceived locality |
|---|---|---|---|---|
| ccTLD (`example.de`) | Automatic by TLD | Anywhere | High — separate domains, certificates, DNS | Strongest |
| Subdomain (`de.example.com`) | Set per host in Search Console | Anywhere | Medium — DNS + certificate per locale | Medium |
| Subdirectory (`example.com/de/`) | Set per path in Search Console | Anywhere | Low — one domain, one certificate | Weakest |

Choose by what dominates the decision:

- **Strong country presence and budget for separate operations:** ccTLD. Best signal of locality, hardest to consolidate authority across locales.
- **One brand, distinct regional teams or stacks:** subdomain. Geotargeting is per-host in Search Console.
- **One brand, shared codebase, fastest to ship:** subdirectory. Authority concentrates on a single domain; geotargeting is per-path.

Then:

- **Pair every canonical URL with [hreflang](/i18n/hreflang).** The URL pattern identifies the resource; hreflang tells search engines which locale it serves.
- **Localise the slug where it adds clarity.** `/about/` to `/sobre/` is helpful for Spanish readers; `/api/v1/` is not worth translating. Consistency matters more than translation: localise all slugs in a section, or none.
- **Keep slug rules from the general [URL structure](/seo/url-structure) page.** Lowercase, hyphenated, ASCII-where-possible, stable.
- **Set the locale from the URL, not from the `Accept-Language` header.** The W3C recommends against silent language negotiation because it breaks sharing — see [avoid auto geo redirects](/i18n/avoid-auto-geo-redirects).

## Common mistakes

- Mixing patterns within one site (`example.com/de/` for German, `fr.example.com` for French). Pick one.
- Using a query parameter (`?lang=de`, `?country=de`) as the locale identifier. Search engines treat it as the same URL.
- Using a country code as a language indicator: `/uk/` for English-language content served to the UK is fine as a *region* path, but should not be confused with the BCP 47 language tag (`en-GB`).
- Redirecting the root URL based on IP — see [avoid auto geo redirects](/i18n/avoid-auto-geo-redirects). Serve a language picker or an `x-default` page instead.
- Localising slugs inconsistently, so half the German site lives at `/de/about/` and half at `/de/uber-uns/`.
