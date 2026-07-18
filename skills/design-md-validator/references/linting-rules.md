# Linting Rules — @google/design.md

> Generated against npm 0.3.0 + main as of 2026-07-18. Authoritative source at
> runtime: `npx @google/design.md spec --rules-only`.

The linter runs nine rules against a parsed DESIGN.md in the published npm
0.3.0 release; a tenth rule (`token-like-ignored`) has merged on main and
ships in the next release. Each rule produces findings at a fixed severity
level.

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
| `token-like-ignored` | warning | **Next release (on main since 2026-06-15, not in npm 0.3.0).** Warns when a top-level YAML key looks like a design-token map but is not part of the recognized export schema and will be silently ignored |

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

## Programmatic API

```typescript
import { lint } from '@google/design.md/linter';

const report = lint(markdownString);
console.log(report.findings);       // Finding[]
console.log(report.summary);        // { errors, warnings, infos }
console.log(report.designSystem);   // Parsed DesignSystemState
```
