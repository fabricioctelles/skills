# Linting Rules — @google/design.md

> Rule table generated against npm 0.4.0 (git `9bf8eae`, 2026-07-27).
> Sections marked "spec main" follow `google-labs-code/design.md` at
> `db977b3` (2026-11-17) and are **not yet in npm 0.4.0** (npm `latest` as of
> 2026-11-25). Authoritative source at runtime:
> `npx @google/design.md spec --rules-only`.

The linter runs eleven rules against a parsed DESIGN.md. `token-like-ignored`
and `omitted-rules` both ship in 0.4.0. Each rule produces findings at a
fixed severity level.

## Rules Table

| Rule | Severity | What it checks |
|---|---|---|
| `broken-ref` | error | Token references (`{colors.primary}`) that don't resolve to any defined token. Spec main also checks external `@` references (see below) |
| `missing-primary` | warning | Colors are defined but no `primary` color exists — agents will auto-generate one. Spec main also accepts `primary` inside a group (e.g. `colors.brand.primary`); npm 0.4.0 still warns in that case (false positive) |
| `contrast-ratio` | warning | Component `backgroundColor`/`textColor` pairs below WCAG AA minimum (4.5:1) |
| `orphaned-tokens` | warning | Color tokens defined but never referenced by any component |
| `token-summary` | info | Summary of how many tokens are defined in each section |
| `missing-sections` | info | Optional sections (spacing, rounded) absent when other tokens exist |
| `missing-typography` | warning | Colors are defined but no typography tokens exist — agents will use default fonts |
| `section-order` | warning | Sections appear out of the canonical order defined by the spec (spec main adds two sections, see below) |
| `unknown-key` | warning | A top-level YAML key looks like a typo of a known schema key (e.g. `colours:` → `colors:`) |
| `token-like-ignored` | warning | A top-level YAML key looks like a design-token map but is not part of the recognized export schema and will be silently ignored. On npm 0.4.0 this fires for `motion:`; spec main recognizes `motion` |
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
Spec main adds `motion` as a valid omittable section (not yet in npm 0.4.0).

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

Order on spec main (`db977b3`, not yet in npm 0.4.0) — two canonical sections
inserted before Components:

| # | Section | Aliases |
|---|---|---|
| 1–6 | Overview … Shapes | unchanged |
| 7 | Motion & Micro-interaction | Motion & Micro-interactions, Motion |
| 8 | Voice & Content Strategy | |
| 9 | Components | |
| 10 | Do's and Don'ts | |

npm 0.4.0 does not know these headings: it preserves them without error, and
`section-order` does not place them.

## Consumer Behavior for Unknown Content

| Scenario | Behavior |
|---|---|
| Unknown section heading | Preserve; do not error |
| Unknown color token name | Accept if value is valid |
| Unknown typography token name | Accept as valid typography |
| Unknown component property | Accept with warning |
| Unknown motion token name (spec main) | Accept as valid motion |
| Grouped token sub-map (spec main) | Flatten to dot-separated path, e.g. `colors.light.surface` |
| Flat and grouped name collision (spec main) | Error; e.g. `colors.primary-light` vs `colors.primary.light` |
| External `@` reference in prose (spec main) | Preserve; resolve the file on demand |
| External `@` fragment on an unsupported file type (spec main) | Ignore the fragment, use the whole file; not broken |
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

## External `@` references (spec `9ac6eb9`, #180)

Spec main only — **not yet in npm 0.4.0** (0.4.0 neither detects nor checks
them). In prose, an inline code span whose whole content matches
`@<path>[#<fragment>]` is a reference: `<path>` uses `/`, has no whitespace
and ends in a file extension. `@media`, `@font-face` and `@scope/package` have
no extension and are ordinary code; an `@` outside a code span is ignored.

Every path resolves from the directory containing `DESIGN.md`, also when the
reference sits in another referenced file. `broken-ref` then reports:

| Condition | Severity |
|---|---|
| Leading `/` or path that resolves outside the `DESIGN.md` directory | error |
| Target file missing | warning |
| Markdown (`.md`, `.markdown`) heading or HTML (`.html`, `.htm`) `id` / `<!-- COMPONENT: name -->` fragment not found | warning |
| Fragment on any other file type | info (not checked) |

The linter follows Markdown targets transitively (cap: 32 files). Fragments
are matched by heading slug (Markdown) or element id (HTML). `lint` passes the
file path to the linter, so it needs a real path; from stdin (`-`) it has no
base directory and does not check files on disk. Fix by correcting the path
relative to `DESIGN.md`, not by adding `../`.

## Grouped tokens and collisions (spec `db977b3`, #179)

Spec main only for typography groups and the collision check; npm 0.4.0
already accepts nested groups in `colors`, `rounded` and `spacing`. Groups
nest up to 20 levels and flatten to dot paths. A flat hyphenated key and a
nested key that flatten to the same CSS variable name (`colors.primary-light`
and `colors.primary.light` → `--color-primary-light`) is an error, as are
duplicate token paths. Fix by renaming one side.

## Motion tokens (spec `a2e3304`, #182)

Spec main only — **not yet in npm 0.4.0**. Validates `motion:` entries: a
`duration` or `delay` that is not an `ms` value is an error; a
`timingFunction` that is not a CSS easing (`linear`, `ease`, `ease-in`,
`ease-out`, `ease-in-out`, `steps(...)`, `cubic-bezier(...)`) is an error; an
unknown property is a warning. See `token-schema.md`. `token-summary` counts
motion tokens.
