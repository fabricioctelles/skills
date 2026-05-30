---
title: "Structured data (JSON-LD)"
category: seo
status: recommended
updated: "2026-05-29T14:13:42.000Z"
sources:
  - title: "Schema.org"
    url: "https://schema.org/"
    publisher: "schema.org"
  - title: "Introduction to structured data markup in Google Search"
    url: "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data"
    publisher: "Google Search Central"
  - title: "JSON-LD 1.1 Specification"
    url: "https://www.w3.org/TR/json-ld11/"
    publisher: "W3C"
  - title: "Yoast — What is structured data?"
    url: "https://yoast.com/what-is-structured-data/"
    publisher: "Yoast"
licence: CC-BY-4.0
---

# Structured data (JSON-LD)

> Machine-readable annotations that describe the content of a page using the schema.org vocabulary. JSON-LD is the format search engines and AI agents expect.

## What it is

Structured data is a set of machine-readable statements that describe what a page is about, using the shared vocabulary at [schema.org](https://schema.org/). The recommended serialisation is JSON-LD: a `<script type="application/ld+json">` block inside `<head>` (or, less commonly, `<body>`).

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What is HSTS?",
  "datePublished": "2026-05-29",
  "author": {
    "@type": "Person",
    "name": "Jane Doe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example",
    "url": "https://example.com"
  }
}
</script>
```

Microdata and RDFa are also accepted, but JSON-LD is the de facto standard because it sits separate from the visible markup.

## Why it matters

Two audiences read it heavily:

- **Search engines** use structured data to power rich results (article cards, breadcrumbs, FAQ accordions, product carousels, knowledge-panel facts). Without it, you get a plain blue link.
- **AI agents and answer engines** rely on it as the ground truth for facts they may quote. A `Person` schema with a `sameAs` linking to your verified profiles is the cleanest way to assert identity.

It is also the most stable contract between a publisher and the rest of the web. The HTML can change; the JSON-LD describes meaning.

## How to implement

Stick to a small set of well-supported types:

- **`WebSite`** — site-wide, on the home page. Include `url` and `name`, and `potentialAction` for sitelinks search if appropriate.
- **`Organization`** or **`Person`** — for the publisher and authors. Include `sameAs` arrays pointing at verified profiles.
- **`BreadcrumbList`** — on every page that has a breadcrumb trail.
- **`Article`** or **`BlogPosting`** — for articles, with `headline`, `datePublished`, `dateModified`, `author`, `image`.
- **`Product`**, **`Offer`**, **`AggregateRating`** — for e-commerce, where eligibility is strict.
- **`FAQPage`** — only when the page genuinely has a Q-and-A list visible to users. Google has restricted FAQ rich results to authoritative publishers; do not stuff fake FAQs.

Rules:

- **Mirror what is visible on the page.** Do not declare facts in JSON-LD that the page does not state. Google calls this "out of sync" data and ignores or penalises it.
- **One graph per page is cleaner than many fragments.** Use `@graph` to nest related entities and `@id` URIs to cross-reference them.
- **Use absolute URLs** in `@id`, `url`, `image`, and `sameAs`.
- **Keep dates in ISO 8601.**
- **Validate.** Schema.org evolves; what is valid one year may be deprecated the next.

## Common mistakes

- Fabricating `aggregateRating` or `Review` to win stars. Google detects this and removes the rich result, sometimes the whole site's eligibility.
- Marking up navigation, footers, or sidebars as if they were the main content.
- Forgetting to update structured data when the page content changes.
- Multiple disagreeing `@type` declarations across plugins or templates on the same page.

## Verification

- Use the [Schema.org validator](https://validator.schema.org/) for spec conformance.
- Use Google's [Rich Results Test](https://search.google.com/test/rich-results) for eligibility.
- Check Search Console's "Enhancements" reports after deployment.
