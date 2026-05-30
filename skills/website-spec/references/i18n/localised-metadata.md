---
title: "Localised page metadata"
category: i18n
status: recommended
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "Google Search Central — Tell Google about localized versions"
    url: "https://developers.google.com/search/docs/specialty/international/localized-versions"
    publisher: "Google Search Central"
  - title: "schema.org — inLanguage"
    url: "https://schema.org/inLanguage"
    publisher: "schema.org"
  - title: "Open Graph protocol"
    url: "https://ogp.me/"
    publisher: "ogp.me"
  - title: "W3C — Internationalization Quick Tips for the Web"
    url: "https://www.w3.org/International/quicktips/"
    publisher: "W3C"
licence: CC-BY-4.0
---

# Localised page metadata

> Translate every visible string in the head and in structured data — title, meta description, Open Graph fields, JSON-LD names and descriptions, image alt text — not just the body. A localised body with English metadata is a half-translation.

## What it is

Localised metadata means every audience-facing string outside the visible body is translated to match the page's locale: the `<title>`, the meta description, every Open Graph and Twitter Card field, every name and description inside JSON-LD, `alt` text on images, the PWA manifest name, and the Open Graph image itself when it carries text. A page that ships a translated body but English metadata is half-translated — and the English half is what shows up in search results and social previews.

## Why it matters

[hreflang](/i18n/hreflang) tells search engines which URL to surface for which user, but it does not translate anything. A common real-world failure is a French page at `/fr/` that ranks correctly in `google.fr` and then appears in the SERP with an English title and English snippet, because the templating layer only swapped the body. The user sees a foreign-language result, distrusts it, and clicks the competitor.

The same applies to shared links. When someone in São Paulo pastes the Portuguese URL into WhatsApp and the unfurl card is in English, the link looks broken even though the landing page is fine. Screen readers reading `alt="Company logo"` in an otherwise Spanish page jar the listener in exactly the same way.

## How to implement

Every locale needs its own translated version of:

- `<title>` and `<meta name="description">`.
- `<meta property="og:title">`, `og:description`, `og:site_name`, `og:image:alt`.
- `og:locale` set to this page's locale, `og:locale:alternate` listing the others. Open Graph uses underscored tags (`fr_FR`), unlike BCP 47 elsewhere — that mismatch is OGP's quirk.
- `twitter:title`, `twitter:description`, `twitter:image:alt`.
- JSON-LD `name`, `description`, `headline`, `articleSection`, and `inLanguage` (BCP 47, matching the page).
- `alt` text on every `<img>` — translated, not left in the source language.
- `<meta name="application-name">` and any PWA manifest `name` / `short_name`.
- The Open Graph image itself when it contains text — render a per-locale variant rather than reusing one English card.

Set the matching [`lang` on `<html>`](/foundations/html-lang) so assistive tech and crawlers know which language the metadata is in. Use BCP 47 in `lang`, `hreflang`, and `inLanguage` (`fr-FR`); the underscored form (`fr_FR`) only applies to `og:locale`.

```html
<html lang="fr-FR">
<head>
  <title>Spécification du Web — un bon site web fait ces choses</title>
  <meta name="description" content="Un guide indépendant de la plateforme…">
  <meta property="og:title" content="Spécification du Web">
  <meta property="og:description" content="Un guide indépendant…">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:locale:alternate" content="en_GB">
  <meta property="og:image" content="https://example.com/og/fr.png">
  <meta property="og:image:alt" content="Logo de Spécification du Web">
  <link rel="alternate" hreflang="fr-FR" href="https://example.com/fr/">
  <link rel="alternate" hreflang="en-GB" href="https://example.com/en/">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Spécification du Web",
    "description": "Un guide indépendant…",
    "inLanguage": "fr-FR"
  }
  </script>
</head>
```

## Common mistakes

- Translating the body but leaving the head in the source language — the most damaging case, because the head is what search results and unfurl cards display.
- Forgetting `alt` text on images. It is usually the last string translators see, and often the one they never receive.
- Reusing a single Open Graph image with English text on it across every locale. The shareable card stays monolingual even when the page is not.
- Omitting `inLanguage` on JSON-LD. Consumers fall back to guessing from `lang` or content sniffing, and they guess wrong on short pages.
- `og:locale` left as `en_US` on every page because it was copy-pasted from a template.
- Schema `description` fields that quietly duplicate the body text instead of being translated to match the locale.

## Verification

- Fetch each locale's URL and grep the head for any source-language strings that survived.
- Run each locale through Google's Rich Results Test and confirm `inLanguage` is emitted on the structured data.
- Paste the URL into the Facebook Sharing Debugger and LinkedIn Post Inspector — the title, description, and image alt on the card should all match the page's locale.
- Spot-check the SERP with a query like `site:example.com/fr/` and confirm every title and snippet is in French, not English.
