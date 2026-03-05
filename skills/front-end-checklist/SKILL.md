---
name: front-end-checklist
description: This skill should be used when a developer or team needs to review, validate, or audit front-end code before launching a website or HTML page to production. Triggers on requests such as "run the front-end checklist", "validate my front-end", "check my site before launch", or when the user asks for a structured review of HTML, CSS, JavaScript, accessibility, performance, security, or design quality.
metadata:
  author: https://github.com/thedaviddias/Front-End-Checklist
  version: "1.1"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
---

# Front-End Checklist

Inspired by [Front-End Checklist](https://github.com/thedaviddias/Front-End-Checklist)

## Parameters

| Parameter  | Description                                      | Default                          |
|------------|--------------------------------------------------|----------------------------------|
| `checklist` | Which checklist to run: `frontend`, `performance`, or `design` | Ask the user to choose if not specified |
| `scope`    | Specific sections to focus on (e.g., "CSS", "Accessibility") | All sections of the chosen checklist |

## Workflow

1. If `checklist` is not specified, ask the user to choose one of the following:
   - **Front-End Checklist** (`references/frontend.md`) — best practices for HTML, CSS, JS, accessibility, SEO, and security
   - **Front-End Performance Checklist** (`references/performance.md`) — performance evaluation and optimization tools
   - **Front-End Design Checklist** (`references/design.md`) — design-to-code quality and designer/developer collaboration

2. Load the selected checklist from `references/`.

3. Work through each section of the checklist systematically. For each item:
   - Mark as passed, failed, or not applicable (N/A).
   - For failed items, provide a brief explanation and a recommended fix.
   - Skip items marked N/A with a short justification (e.g., "not a blog, RSS not applicable").

4. If `scope` is specified, focus only on the relevant sections. Otherwise, cover all sections.

5. Present a summary of results grouped by section, showing:
   - Total items checked
   - Items passed / failed / N/A
   - High-priority failures that must be resolved before launch

6. Register the checklist session result in the project's `docs/` folder if applicable.

## Quality Checklist

Before delivering results, verify:

- [ ] All high-priority items (`![High]`) were evaluated without exception.
- [ ] Every failed item includes a concrete corrective action, not just a description of the problem.
- [ ] N/A items are explicitly justified.
- [ ] The summary clearly distinguishes blocking issues (high priority failures) from non-blocking ones.
- [ ] References to tools and documentation from the checklist files are included where relevant.

## Reference Files

- See `references/frontend.md` — Full Front-End Checklist (Head, HTML, CSS, JS, Security, Performance, Accessibility, SEO)
- See `references/performance.md` — Front-End Performance Checklist
- See `references/design.md` — Front-End Design Checklist
- See `references/head.md` — Complete HTML `<head>` element reference
- See `references/favicon.md` — Favicon sizes, formats, and browser compatibility cheat sheet
