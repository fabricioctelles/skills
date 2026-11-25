# Token Schema — DESIGN.md Spec (version alpha)

A DESIGN.md file carries machine-readable design tokens in YAML. These are
the normative values that agents use to generate code.

Spec reference: `google-labs-code/design.md` main at commit
[`db977b3`](https://github.com/google-labs-code/design.md/commit/db977b3c1d1f309269f43d5d17ae828d54bd6ae3)
(#179, 2026-11-17). Published CLI: npm `@google/design.md` 0.4.0 (npm
`latest` as of 2026-11-25), which already lints hybrid files (#178, spec
`6e5da53`). Items marked "spec main" below are **not yet in npm 0.4.0**; the
git release 0.4.1 (2026-11-06, no tag, not on npm) adds only the DTCG fix and
zod v4.

## Where Tokens Live

Tokens may be embedded in two ways:

1. **YAML front matter** — at the top of the file, opened and closed by a
   line containing exactly `---`.
2. **Interleaved YAML code blocks** — fenced ` ```yaml ` blocks placed inside
   the relevant `##` section.

Both may be used in the same document (hybrid), e.g. `name` and
`description` in the front matter and `colors` / `typography` in blocks
inside their sections. All blocks are parsed and merged into one token tree.
Each top-level schema key may be defined **at most once** across the whole
document — defining the same top-level key in two blocks (e.g. `colors` in
both front matter and a code block) is an error and the file is rejected.

## Top-Level Schema

```yaml
version: <string>          # optional, current: "alpha"
name: <string>             # required
description: <string>      # optional
colors:
  <token-name>: <Color>
typography:
  <token-name>: <Typography>
rounded:
  <scale-level>: <Dimension>
spacing:
  <scale-level>: <Dimension | number>
motion:                    # spec main (#182), not yet in npm 0.4.0
  <token-name>: <Motion>
components:
  <component-name>:
    <token-name>: <string | token reference>
```

Spec main (#179) also lets `colors`, `typography`, `rounded` and `spacing`
hold optional nested group sub-maps (see Grouped Tokens).

## Token Types

| Type | Format | Example |
|---|---|---|
| Color | Any CSS color (hex, `rgb()`, `oklch()`, named) | `"#1A1C1E"`, `"oklch(62% 0.18 250)"` |
| Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `-0.02em` |
| Token Reference | `{path.to.token}` | `{colors.primary}` |
| Duration | number + `ms` (spec main) | `100ms`, `250ms` |
| Typography | object with font properties | See below |
| Motion | object with `duration`, `delay`, `timingFunction` (spec main) | See Motion |

## Typography Object

```yaml
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.02em
    fontFeature: "ss01"        # optional
    fontVariation: "wght 700"  # optional
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.5
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: 500
    letterSpacing: 0.05em
```

Required fields per entry: `fontFamily`, `fontSize`.
Optional fields: `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation`.

The DTCG export always emits `lineHeight` and `letterSpacing` (default
`0px`), since the DTCG typography type requires them — git release 0.4.1,
not on npm (0.4.0 drops unquoted numeric `lineHeight`).

## Colors

```yaml
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
  on-tertiary: "#FFFFFF"     # contrast pair for tertiary
```

The `primary` color is expected by the linter. Its absence triggers a
`missing-primary` warning.

## Rounded (border-radius scale)

```yaml
rounded:
  sm: 4px
  md: 8px
  lg: 16px
```

## Spacing

```yaml
spacing:
  sm: 8px
  md: 16px
  lg: 32px
```

## Motion (spec main, not yet in npm 0.4.0)

Spec `a2e3304` (#182). Purpose-named tokens rather than raw speed labels;
recommended names: `state-change`, `surface-enter`, `surface-exit`. Unknown
names are accepted.

```yaml
motion:
  state-change:
    duration: 100ms
    delay: 0ms
    timingFunction: ease-out
  surface-enter:
    duration: 250ms
    delay: 0ms
    timingFunction: cubic-bezier(0.2, 0, 0, 1)
```

| Property | Type | Meaning |
|---|---|---|
| `duration` | Duration (`ms`) | how long the transition takes |
| `delay` | Duration (`ms`) | wait before it starts |
| `timingFunction` | string | `linear`, `ease`, `ease-in`, `ease-out`, `ease-in-out`, `steps(...)`, `cubic-bezier(...)` |

The matching prose section is `## Motion & Micro-interaction` (also
"Motion & Micro-interactions", "Motion"): what moves, duration rhythm,
easing intent (entering decelerates, leaving accelerates), and restraint
(honor `prefers-reduced-motion`; prefer `transform` and `opacity`). On
npm 0.4.0 a `motion:` key raises `token-like-ignored` and is not exported.
Spec main exports it to `json-tailwind` as `transitionDuration`,
`transitionDelay` and `transitionTimingFunction`.

## Voice & Content Strategy (spec main, not yet in npm 0.4.0)

Spec `679d301` (#183). A prose-only section — no tokens. It covers tone of
voice, capitalization, terminology, button and action labels, empty /
loading / error states, and numbers, dates and units. It sits after Motion
and before Components in the section order.

```markdown
## Voice & Content Strategy

- **Tone of voice:** Precise, calm, and utilitarian.
- **Capitalization:** Sentence case everywhere.
- **Button and action labels:** Verb phrase naming the outcome ("Save changes"), never "OK".
```

## Components

Components map a name to a group of sub-token properties:

```yaml
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary-container}"
```

### Valid Component Properties

`backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`,
`height`, `width`.

### Variants

Hover, active, pressed states are separate entries with a related key name:
`button-primary-hover`, `button-primary-active`.

## Token References

References use curly braces with dot notation:

```yaml
components:
  card:
    backgroundColor: "{colors.neutral}"    # resolves to #F7F5F2
    rounded: "{rounded.md}"                # resolves to 8px
```

Broken references (pointing to undefined tokens) trigger a `broken-ref` error.

Since npm 0.3.0 (PR #103), token groups support nested sub-levels in the
token YAML — e.g. `colors.brand.primary` — and references use the full
dotted path to the leaf token: `{colors.brand.primary}`.

## Grouped Tokens

Spec `db977b3` (#179) documents groups for all four categories. npm 0.4.0
already handles `colors`, `rounded` and `spacing`; **typography groups,
`primary` found inside a group, and the collision check are spec main, not
yet in npm 0.4.0**.

```yaml
colors:
  primary: "#647D66"          # mode-agnostic roles stay at the top level
  light:
    surface: "#FAFDF7"
    on-surface: "#1A1C19"
  dark:
    surface: "#10130E"
    on-surface: "#E2E4DE"
typography:
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
  sm:
    headline-lg:
      fontFamily: Public Sans
      fontSize: 32px
  lg:
    headline-lg:
      fontFamily: Public Sans
      fontSize: 48px
```

- Groups are organizational only; `light`, `dark`, `sm`, `md`, `lg`, `xl`
  are conventions (theme mode, responsive breakpoints), not reserved words.
- Tokens flatten to `<category>.<group>.<token>`; depth limit 20.
- References use the full path to a leaf: `{colors.light.surface}`,
  `{typography.sm.headline-lg}`. A reference to a group (`{colors.light}`)
  is invalid, except composite typography references inside `components`.
- A flat key and a nested key that flatten to the same CSS variable name
  (`colors.primary-light` and `colors.primary.light`) is an error.

## External References (spec main, not yet in npm 0.4.0)

Spec `9ac6eb9` (#180). In prose, `` `@components/button.html#button-primary` ``
(inline code span, `/` path, file extension, optional `#fragment`) points to
a file that elaborates the design system, typically from `## Components`.
Paths resolve from the `DESIGN.md` directory. Rules and severities live in
`linting-rules.md`.

```markdown
- **Buttons** → `@components/button.html` — `button-primary`, `button-secondary`
```

## File Structure Summary (front matter only)

```
---                         ← YAML front matter start
name: "My Design System"
colors: ...
typography: ...
rounded: ...
spacing: ...
components: ...
---                         ← YAML front matter end

## Overview                 ← Markdown prose sections
...
## Colors
...
## Typography
...
```

Hybrid layout (front matter + interleaved blocks):

````markdown
---
version: alpha
name: Daylight Prestige
description: Editorial design system with high-contrast neutrals.
---

## Colors

The palette is rooted in high-contrast neutrals and a single accent color.

```yaml
colors:
  primary: "#1A1C1E"
  secondary: "#6C7278"
  tertiary: "#B8422E"
```

## Typography

```yaml
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
```
````

The tokens are the normative values. The prose provides context for how to
apply them.
