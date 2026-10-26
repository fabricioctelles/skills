# Token Schema — DESIGN.md Spec (version alpha)

A DESIGN.md file carries machine-readable design tokens in YAML. These are
the normative values that agents use to generate code.

Spec reference: `google-labs-code/design.md` main at commit
[`6e5da53`](https://github.com/google-labs-code/design.md/commit/6e5da5382f41edbba9d73b2c62f33f32e9971f15)
(#178, 2026-10-16). Published CLI: npm `@google/design.md` 0.4.0, which
already lints hybrid files.

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
components:
  <component-name>:
    <token-name>: <string | token reference>
```

## Token Types

| Type | Format | Example |
|---|---|---|
| Color | Any CSS color (hex, `rgb()`, `oklch()`, named) | `"#1A1C1E"`, `"oklch(62% 0.18 250)"` |
| Dimension | number + unit (`px`, `em`, `rem`) | `48px`, `-0.02em` |
| Token Reference | `{path.to.token}` | `{colors.primary}` |
| Typography | object with font properties | See below |

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
