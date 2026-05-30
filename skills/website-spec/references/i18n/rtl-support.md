---
title: "RTL and bidirectional text"
category: i18n
status: recommended
updated: "2026-05-29T18:54:03.000Z"
sources:
  - title: "W3C i18n — Structural markup and right-to-left text in HTML"
    url: "https://www.w3.org/International/questions/qa-html-dir"
    publisher: "W3C"
  - title: "W3C i18n — Inline markup and bidirectional text in HTML"
    url: "https://www.w3.org/International/articles/inline-bidi-markup/"
    publisher: "W3C"
  - title: "MDN — CSS logical properties and values"
    url: "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values"
    publisher: "MDN"
licence: CC-BY-4.0
---

# RTL and bidirectional text

> Sites that serve Arabic, Hebrew, Persian, or Urdu must set dir="rtl" and use CSS logical properties so layouts mirror correctly without hard-coded left and right.

## What it is

Right-to-left (RTL) scripts — Arabic, Hebrew, Persian, Urdu, Pashto, Dhivehi, and others — read from right to left. So do their layouts: the logo sits on the right, navigation flows right-to-left, scrollbars are on the left, and progress indicators advance leftwards. Bidirectional ("bidi") text is content that mixes RTL and LTR runs, for example an English brand name embedded inside an Arabic paragraph.

The HTML `dir` attribute declares direction. The Unicode Bidirectional Algorithm handles inline mixing automatically when `dir` is set correctly.

```html
<html lang="ar" dir="rtl">
```

## Why it matters

For roughly half a billion readers, an LTR-only layout looks broken: cramped, misaligned, with arrows and icons pointing the wrong way. Get direction wrong and you also break the bidi algorithm — phone numbers, dates, and Latin brand names appear in the wrong order inside RTL paragraphs. Setting `dir` correctly fixes most of this without any per-element work.

## How to implement

**Set direction on `<html>`.** Use `dir="rtl"` on the root for RTL locales. Set `dir="auto"` on user-generated content (comments, messages) so the browser picks direction from the first strong character.

```html
<html lang="ar" dir="rtl">
<html lang="he" dir="rtl">
<html lang="en" dir="ltr">  <!-- default; explicit is fine -->
```

**Override per element.** A search box that always takes Latin input can stay LTR inside an RTL page:

```html
<input type="search" dir="ltr" name="q">
```

**Use CSS logical properties, not physical ones.** Replace `left`/`right` with `inline-start`/`inline-end`, and `top`/`bottom` with `block-start`/`block-end`. The same stylesheet then works in both directions:

```css
/* Instead of: */
.card { margin-left: 1rem; padding-right: 0.5rem; border-left: 1px solid; }

/* Use: */
.card { margin-inline-start: 1rem; padding-inline-end: 0.5rem; border-inline-start: 1px solid; }
```

The full set includes `margin-inline-*`, `padding-inline-*`, `border-inline-*`, `inset-inline-*`, `text-align: start | end`, and the shorthand `inline-size` / `block-size` instead of `width` / `height` when direction matters.

**Mirror directional icons.** Arrows, chevrons, back buttons, progress bars, and breadcrumbs should mirror in RTL. Use `transform: scaleX(-1)` or supply mirrored SVGs. Do not mirror logos, photos, numerals, or media controls (play stays a right-pointing triangle universally).

**Test bidi inline.** Embed Latin text inside an Arabic paragraph and check digits, punctuation, and parentheses sit correctly.

**Use the right element for unknown or overridden direction.** Three HTML mechanisms exist for inline bidi control, each with a distinct job:

- **`dir="auto"`** on any element — the browser picks direction from the first strong character. The right default for any field that displays user-generated content (comments, usernames, message bodies, search queries).
- **`<bdi>`** — short for "bidi isolation". Wraps a fragment whose direction is unknown so it does not break the surrounding paragraph's bidi algorithm. Use for usernames, titles, and any embedded foreign-language string inside running text: `Mentioned by <bdi>@محمد</bdi> in the thread`.
- **`<bdo dir="ltr">` or `<bdo dir="rtl">`** — force a specific direction regardless of content. Rare; use only when you genuinely need to override the algorithm.

`<bdi>` is the one most sites forget. Without it, an RTL username injected into an LTR template can flip surrounding punctuation and timestamps; the page looks broken and the fix is one element.

For vertical scripts (Japanese, Mongolian) and CJK line breaking, see [writing-modes](/i18n/writing-modes). Direction (`dir`) is about LTR vs RTL; `writing-mode` is about horizontal vs vertical. They are separate axes.

## Common mistakes

- Hard-coding `left:` and `right:` in CSS, then duplicating every rule for `[dir="rtl"]`.
- Forgetting to mirror icons, leaving back-arrows pointing forward.
- Setting `dir="rtl"` only on `<body>` — flexbox, grid, and form widgets read it from `<html>`.
- Reversing numbers manually; the bidi algorithm handles them when `dir` is correct.
- Mirroring logos, code snippets, or telephone numbers, which should stay LTR.
