---
title: "The <title> element"
category: foundations
status: required
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "HTML Living Standard — The title element"
    url: "https://html.spec.whatwg.org/multipage/semantics.html#the-title-element"
    publisher: "WHATWG"
  - title: "MDN — <title>: The Document Title element"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title"
    publisher: "MDN"
  - title: "WCAG 2.4.2 — Page Titled (Level A)"
    url: "https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html"
    publisher: "W3C"
  - title: "Google — Influencing your title links in search results"
    url: "https://developers.google.com/search/docs/appearance/title-link"
    publisher: "Google Search Central"
licence: CC-BY-4.0
---

# The <title> element

> Every HTML document must have exactly one non-empty <title> element inside <head>. It is used by browsers, search engines, screen readers, social previews, and AI agents.

## What it is

The `<title>` element is a required child of `<head>` that names the document. It is the only HTML element with no markup inside it — only text. There must be exactly one per page.

```html
<title>Setting up CSP · The Website Specification</title>
```

## Why it matters

- **Browsers** show the title in the tab, the window, the bookmark, and the history entry.
- **Search engines** use it as the default link text in results (Google may rewrite it, but a good `<title>` is rewritten less).
- **Screen readers** announce the title when the page loads, so it is the first thing a non-sighted user hears.
- **Social platforms** fall back to it when no `<meta property="og:title">` is set.
- **AI agents** use it as the canonical short description of the page.

Missing or empty titles are a WCAG 2.4.2 Level A failure — the lowest accessibility bar there is.

## How to implement

Write the title for the page, not for the site:

- **Page-specific first, site name second**, separated by a delimiter such as `·`, `—`, or `|`.
- **Front-load the unique part.** Truncation in search results and tabs hides the end of the string.
- **50–60 characters** is a reasonable target. Google typically displays around 600 pixels of width.
- **One per page, unique per page.** Two pages with the same title is a quality signal that they are duplicates.
- **No keyword stuffing.** Write what the page is about.

The order matters when the tab is narrow:

```html
<!-- Good: unique part first -->
<title>HSTS · Security · The Website Specification</title>

<!-- Worse: site name eats the tab -->
<title>The Website Specification — Security — HSTS</title>
```

For the homepage, the site name on its own is fine:

```html
<title>The Website Specification</title>
```

## Common mistakes

- Empty `<title></title>`. Browsers show the URL; screen readers announce nothing useful.
- Identical titles across many pages (often the site name only).
- Titles set in JavaScript after first paint — search crawlers and social scrapers may not run JS.
- Putting the title in `<body>` instead of `<head>`.

## Verification

- View source. `<title>` must be inside `<head>` and contain non-whitespace text.
- Open the page in a narrow tab. Check the unique part is visible.
- Run [`curl -s https://example.com | grep -i '<title'`](https://curl.se) and confirm it is set without JavaScript.
- Test with a screen reader (VoiceOver, NVDA). It should announce the title on load.
