---
title: "<meta viewport>"
category: foundations
status: required
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "MDN — Viewport meta tag"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag"
    publisher: "MDN"
  - title: "CSS Device Adaptation Module — viewport meta"
    url: "https://drafts.csswg.org/css-device-adapt/#viewport-meta"
    publisher: "W3C"
  - title: "WCAG 1.4.4 — Resize Text (Level AA)"
    url: "https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html"
    publisher: "W3C"
licence: CC-BY-4.0
---

# <meta viewport>

> Tell mobile browsers to render the page at the device's actual width instead of pretending to be a 980-pixel desktop. One line, and never disable user scaling.

## What it is

The viewport meta tag controls how mobile browsers size and scale the page. The correct value for almost every website is:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

It belongs in `<head>`, alongside the charset and title.

## Why it matters

When mobile browsers first appeared, almost every website on the web was designed for desktop. To avoid showing tiny squashed columns, Safari on iPhone decided to render pages as if the screen were 980 CSS pixels wide and zoom out to fit. That behaviour persists today: without a viewport meta tag, your responsive site is rendered at 980 pixels, then scaled down. The result on a phone is a postage-stamp version of the desktop layout, with text too small to read and tap targets the user has to pinch-zoom to hit.

Setting `width=device-width` tells the browser: "Use the device's actual width as the viewport." `initial-scale=1` sets the initial zoom level to 1:1, so CSS pixels match the browser's idea of a pixel. Together they make responsive CSS (`@media (max-width: 600px)`) work as designed.

This single line is the difference between a site that works on mobile and one that does not. Google has used "mobile-friendliness" as a ranking signal since 2015, and Search uses the mobile version of pages for indexing.

## How to implement

The standard, correct value:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

That is it. Do not add anything else unless you have a specific reason.

You may occasionally see additional keys:

- `viewport-fit=cover` — required for iOS Safari to draw into the safe-area insets (the notch). Add it only if you handle the insets in CSS with `env(safe-area-inset-*)`.
- `interactive-widget=resizes-content` — controls how the on-screen keyboard interacts with the viewport.

What you must **never** do is disable user zooming:

```html
<!-- Do not do this -->
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
```

`user-scalable=no` and `maximum-scale=1` prevent users from pinch-zooming. For anyone with low vision who needs to magnify text — and that is a significant fraction of users — this turns a usable page into an unusable one. It also fails WCAG 1.4.4. There is no good reason to disable zoom on a content site.

## Common mistakes

- Omitting the tag and assuming the site is "responsive enough" — mobile browsers will still render at 980 pixels.
- Copying old snippets that include `user-scalable=no`. Remove it.
- Setting `width=1024` or a fixed pixel value to force a layout. Build a responsive layout instead.
- Using `initial-scale=1.0` (with the trailing zero) — harmless, but `1` is canonical.
- Adding the tag only to some templates. Every HTML page needs it.

## Verification

- View source: confirm the tag is present and contains `width=device-width, initial-scale=1`.
- Open Chrome DevTools, toggle device emulation, and check the layout is not 980 pixels wide and scaled down.
- Try pinch-to-zoom on a real phone. If it does not zoom, you have a `user-scalable=no` somewhere.
- Run Lighthouse — it flags both missing viewport tags and ones that disable zooming.
