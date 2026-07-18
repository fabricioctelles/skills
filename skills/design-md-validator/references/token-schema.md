# Token Schema — DESIGN.md Spec (version alpha)

The YAML front matter in a DESIGN.md file contains machine-readable design
tokens. These are the normative values that agents use to generate code.

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
frontmatter — e.g. `colors.brand.primary` — and references use the full
dotted path to the leaf token: `{colors.brand.primary}`.

## File Structure Summary

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

The tokens are the normative values. The prose provides context for how to
apply them.
