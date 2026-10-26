# Linting Rules — @google/design.md

> Generated against npm 0.4.0 (git `9bf8eae`, 2026-07-27). Authoritative
> source at runtime: `npx @google/design.md spec --rules-only`.

The linter runs eleven rules against a parsed DESIGN.md. `token-like-ignored`
and `omitted-rules` both ship in 0.4.0. Each rule produces findings at a
fixed severity level.

## Rules Table

| Rule | Severity | What it checks |
|---|---|---|
| `broken-ref` | error | Token references (`{colors.primary}`) that don't resolve to any defined token |
| `missing-primary` | warning | Colors are defined but no `primary` color exists — agents will auto-generate one |
| `contrast-ratio` | warning | Component `backgroundColor`/`textColor` pairs below WCAG AA minimum (4.5:1) |
| `orphaned-tokens` | warning | Color tokens defined but never referenced by any component |
| `token-summary` | info | Summary of how many tokens are defined in each section |
| `missing-sections` | info | Optional sections (spacing, rounded) absent when other tokens exist |
| `missing-typography` | warning | Colors are defined but no typography tokens exist — agents will use default fonts |
| `section-order` | warning | Sections appear out of the canonical order defined by the spec |
| `unknown-key` | warning | A top-level YAML key looks like a typo of a known schema key (e.g. `colours:` → `colors:`) |
| `token-like-ignored` | warning | A top-level YAML key looks like a design-token map but is not part of the recognized export schema and will be silently ignored |
| `omitted-rules` | info | Validates the optional `omitted` frontmatter list; flags redundant or unknown entries |

## `omitted` frontmatter (0.4.0)

Authors can list skipped categories so expected-missing warnings stay quiet.
Bare strings or objects with a reason:

```yaml
omitted:
  - spacing
  - rounded
  - name: elevation
    reason: not used in this product
```

Unknown names and entries that are not actually omitted produce `omitted-rules`
info findings. Do not invent omitted categories to hide real lint errors.

## Section Order (canonical)

Sections use `##` headings. They can be omitted, but those present must appear
in this order:

| # | Section | Aliases |
|---|---|---|
| 1 | Overview | Brand & Style |
| 2 | Colors | |
| 3 | Typography | |
| 4 | Layout | Layout & Spacing |
| 5 | Elevation & Depth | Elevation |
| 6 | Shapes | |
| 7 | Components | |
| 8 | Do's and Don'ts | |

## Consumer Behavior for Unknown Content

| Scenario | Behavior |
|---|---|
| Unknown section heading | Preserve; do not error |
| Unknown color token name | Accept if value is valid |
| Unknown typography token name | Accept as valid typography |
| Unknown component property | Accept with warning |
| Duplicate section heading | Error; reject the file |

## Exit Codes

- `0` — No errors (warnings/info may be present)
- `1` — Errors found (file is invalid per spec)
- `2` — Input failure (file not found or unreadable) — 0.4.0

## Programmatic API

```typescript
import { lint } from '@google/design.md/linter';

const report = lint(markdownString);
console.log(report.findings);       // Finding[]
console.log(report.summary);        // { errors, warnings, infos }
console.log(report.designSystem);   // Parsed DesignSystemState
```

## Duplicate top-level YAML key (spec `6e5da53`)

Since spec commit `6e5da53` (#178, 2026-10-16) tokens may be split across
front matter and ` ```yaml ` blocks inside `##` sections. Per the spec's
consumer-behavior table, a top-level key defined in more than one block is an
error and the file is rejected (example: `colors` in both front matter and a
code block). Fix by merging all entries of that key into one block.

CLI gap: npm 0.4.0 only emits a **warning** (no rule id), e.g. `Section
'colors' is defined in both frontmatter and code block 1.`, with `errors: 0`.
Treat that warning as a spec error and tell the user to fix it.
