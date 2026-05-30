---
title: "hreflang in XML sitemaps"
category: i18n
status: optional
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "Google Search Central — Tell Google about localized versions"
    url: "https://developers.google.com/search/docs/specialty/international/localized-versions"
    publisher: "Google Search Central"
  - title: "sitemaps.org — XML sitemap protocol"
    url: "https://www.sitemaps.org/protocol.html"
    publisher: "sitemaps.org"
  - title: "BCP 47 — Tags for Identifying Languages"
    url: "https://www.rfc-editor.org/info/bcp47"
    publisher: "IETF"
licence: CC-BY-4.0
---

# hreflang in XML sitemaps

> Declare language and regional alternates inside the XML sitemap with xhtml:link instead of in the HTML head. Easier to maintain at scale and keeps localisation metadata separate from content.

## What it is

The sitemap form of [hreflang](/i18n/hreflang). Instead of declaring language and regional alternates with `<link rel="alternate" hreflang="...">` in every HTML head, you list them once per URL inside the XML sitemap using the `<xhtml:link>` element. The namespace `xmlns:xhtml="http://www.w3.org/1999/xhtml"` is declared on the root `<urlset>`. The signal sent to search engines is identical to the inline form — only the delivery mechanism changes.

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/en/page</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/page"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/seite"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/page"/>
  </url>
  <url>
    <loc>https://example.com/de/seite</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/page"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/seite"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/page"/>
  </url>
  <url>
    <loc>https://example.com/fr/page</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/page"/>
    <xhtml:link rel="alternate" hreflang="de" href="https://example.com/de/seite"/>
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/en/page"/>
  </url>
</urlset>
```

## Why it matters

On a large multilingual site, declaring hreflang inline becomes painful. A cluster of ten locales means ten `<link>` elements in every page's head, every locale, every template — eleven with `x-default`. Adding an eleventh locale touches every template and every cached page. Moving the declaration to the sitemap keeps page HTML clean, centralises localisation metadata in one machine-generated file, and lets you add or remove a locale by regenerating one document.

The signal is equivalent. Google, Bing and Yandex all read `<xhtml:link>` entries from the sitemap as authoritative alternates.

## How to implement

- **Pick one delivery method per site.** Use either inline [hreflang](/i18n/hreflang) in the HTML head, the HTTP `Link` header, or sitemap `<xhtml:link>` — not several at once on the same URLs. Mixed signals get ignored or produce conflicts.
- **Declare the namespace.** Add `xmlns:xhtml="http://www.w3.org/1999/xhtml"` on the root `<urlset>`.
- **Group all alternates inside each `<url>`.** Every `<url>` entry lists every alternate URL in the group, including itself. The bidirectional rule still applies: if A lists B, B must list A.
- **Self-reference always.** Each URL must include a `<xhtml:link>` pointing at itself with its own `hreflang`. Omitting it invalidates the entire cluster.
- **Add `x-default`.** Point it at the language selector or the default-region landing page.
- **Use BCP 47 tags.** Language (`en`, `de`), or language plus region (`en-GB`, `pt-BR`). Never a country code on its own.
- **Reach for the sitemap when** you have many locales, many pages, or generate alternates from the same source that already generates the sitemap. Reach for inline `<link>` when you don't ship an XML sitemap, or when alternates differ from how the sitemap is built.

## Common mistakes

- Forgetting the `xmlns:xhtml` namespace declaration — the entries parse but search engines ignore them.
- Listing only the "other" languages and skipping the self-reference.
- Shipping both inline `<link rel="alternate">` and sitemap `<xhtml:link>` for the same URLs, with different sets.
- Pointing alternates at non-canonical URLs, redirects, or 404s.
- Splitting a language cluster across multiple sitemap files — keep all alternates of a URL inside the same `<url>` entry.

## Verification

- Fetch the sitemap and confirm the `xhtml` namespace is declared on `<urlset>`.
- Pick one URL and confirm every alternate listed there reciprocally lists it back.
- Use Search Console's International Targeting report (or equivalent) to confirm clusters are detected without "no return tags" errors.
