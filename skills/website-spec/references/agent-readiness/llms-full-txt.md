---
title: "/llms-full.txt"
category: agent-readiness
status: optional
updated: "2026-05-29T09:45:15.000Z"
sources:
  - title: "The /llms.txt proposal"
    url: "https://llmstxt.org/"
    publisher: "llmstxt.org"
  - title: "Is It Agent Ready?"
    url: "https://isitagentready.com/"
    publisher: "Is It Agent Ready?"
licence: CC-BY-4.0
---

# /llms-full.txt

> An extended companion to /llms.txt that concatenates the full markdown content of your key pages into a single file. Useful for small sites, costly for large ones.

## What it is

`/llms-full.txt` is the long companion to [/llms.txt](../agent-readiness/llms-txt.md). Where `llms.txt` is an index of links, `llms-full.txt` concatenates the actual markdown content of those pages into a single file. The convention also originates with the [llmstxt.org](https://llmstxt.org/) proposal.

The idea is that an agent fetches one file and receives your entire documentation in plain markdown, ready to use as context. No crawling, no HTML extraction.

It is optional and emerging. Treat it as a nice-to-have for documentation-heavy sites where the content is reasonably small and stable.

```md
# Example Corp — full content

> All public documentation, concatenated.

---

# Getting started

(full markdown of the getting-started page)

---

# API reference

(full markdown of the API reference)
```

## Why it matters

- One fetch, all the content. No retries, no rate limits per page, no broken links.
- Markdown, not HTML. Agents do not have to strip navigation, ads, or scripts.
- Predictable structure. Pages are separated by horizontal rules and headings.
- Useful as a build artefact for your own retrieval pipelines and embeddings.

The trade-off is size. A large documentation site can easily produce a multi-megabyte file. Agents may refuse to load it, or load only the first slice. If your content does not fit comfortably in a single file, stick with `llms.txt` plus per-page markdown.

## How to implement

- Generate the file at build time. Manually maintaining it is not realistic.
- Concatenate the markdown source of the pages listed in `llms.txt`, in the same order.
- Separate sections with `---` and clear `#` headings. Include the page URL near each heading so agents can cite it.
- Strip front-matter and templating artefacts. Keep prose, headings, code blocks, and lists.
- Watch the size. Many model providers cap context windows; aim to stay well under common limits or split into focused files (`llms-api.txt`, `llms-guides.txt`).
- Serve as `text/markdown` or `text/plain`. Set sensible cache headers — this file changes on every doc update.

## Common mistakes

- Including every page on the site. Curate the same way `llms.txt` does.
- Forgetting to update it. A stale concatenation is harder to spot than a stale index.
- Letting it grow until it is too big to be useful. Split it before that point.
- Serving HTML by accident — check the response is real markdown.

## Verification

- Fetch the file and check the size. Anything over a couple of megabytes is suspect.
- Spot-check a few sections against the live pages they were generated from.
- Re-run the build after major content changes and diff against the previous version.
