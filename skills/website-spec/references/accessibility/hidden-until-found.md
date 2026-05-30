---
title: "Hidden until found"
category: accessibility
status: recommended
updated: "2026-05-29T16:40:22.000Z"
sources:
  - title: "HTML Standard — The hidden attribute"
    url: "https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute"
    publisher: "WHATWG"
  - title: "MDN — hidden global attribute"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden"
    publisher: "MDN"
  - title: "Chrome for Developers — hidden=until-found and the beforematch event"
    url: "https://developer.chrome.com/articles/hidden-until-found"
    publisher: "Google"
licence: CC-BY-4.0
---

# Hidden until found

> Use hidden="until-found" (or content-visibility: hidden) for collapsible content so that browser find-in-page, assistive tech, and search engines can still reach the text and auto-expand it.

## What it is

`hidden="until-found"` is a value of the global `hidden` attribute defined in the HTML Standard. An element marked this way renders as if hidden — it takes up no visible space — but the browser's find-in-page (Ctrl/Cmd+F), the fragment-directive scroll-to-text, and `scrollIntoView()` still walk through it. When a match is found inside, the browser fires a `beforematch` event on the element, removes the `hidden` attribute, and scrolls the match into view.

Under the hood it is implemented through `content-visibility: hidden`, which behaves the same way: skipped for rendering, still reachable for find-in-page. Anything you can do with the attribute you can do with the CSS property — pick whichever fits your component.

## Why it matters

- `display: none` removes content from the accessibility tree and from find-in-page entirely. Accordion or tab patterns that hide panels with `display: none` are invisible to a user who knows the exact phrase they want.
- Find-in-page is a primary accessibility tool. Keyboard users, screen-reader users, users with cognitive disabilities, and anyone skimming a long document rely on it to locate content directly.
- Search engines and AI crawlers vary in how they treat content hidden with `display: none`. `hidden="until-found"` keeps the text in the DOM and reachable, which is the honest signal: this is real content, just collapsed by default.

## How to implement

Mark each collapsed panel and listen for `beforematch` so your widget state stays in sync:

```html
<button aria-expanded="false" aria-controls="panel-1">Shipping</button>
<div id="panel-1" hidden="until-found">
  We ship worldwide within 48 hours…
</div>
```

```js
const panel = document.getElementById('panel-1');
panel.addEventListener('beforematch', () => {
  const button = document.querySelector('[aria-controls="panel-1"]');
  button.setAttribute('aria-expanded', 'true');
  // remove any matching collapsed class on the button or panel
});
```

The CSS equivalent, for components that already have their own toggle class:

```css
.accordion-panel[data-collapsed] {
  content-visibility: hidden;
}
```

**Prefer `<details>/<summary>` where you can.** For the everyday "click a heading to expand a panel" pattern, the native disclosure element gives you focus management, keyboard handling, and find-in-page reachability with zero JavaScript. Reach for `hidden="until-found"` when you need a custom widget that `<details>` cannot model — a search-driven FAQ, a complex tab strip, an off-screen mega-menu that must still be findable.

## Common mistakes

- Using `display: none` on accordion panels and then wondering why users cannot find the content they remember reading. Switch the closed state to `hidden="until-found"`.
- Using `hidden="until-found"` for content that should be permanently hidden — error messages, off-screen utility nodes, suppressed admin tools. Use plain `hidden` or `display: none` instead.
- Forgetting to update `aria-expanded` and the visual chevron state in the `beforematch` handler. The panel opens but the button still claims it is collapsed.
- Treating it as a layout primitive. The element still participates in DOM order and document outline — it is hidden, not removed.

## Verification

- Open the page in Chrome or Edge. Press Ctrl/Cmd+F and search for a phrase that lives inside a collapsed panel. The browser should auto-scroll and reveal it.
- Repeat with a panel that uses `display: none`. The search should fail, confirming the regression you are avoiding.
- Tab through the widget with a screen reader (VoiceOver, NVDA, JAWS) and confirm the panel announces correctly once expanded.
- Inspect the element in DevTools after a match — the `hidden` attribute should be gone, the `beforematch` listener should have fired, and `aria-expanded` should read `true`.
