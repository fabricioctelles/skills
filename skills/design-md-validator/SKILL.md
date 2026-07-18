---
name: design-md-validator
description: >
  Validate DESIGN.md files against the official Google specification using the
  `@google/design.md` CLI linter. Works with local files and remote URLs.
  Use when the user wants to lint a DESIGN.md, check spec compliance, find
  broken token references, verify WCAG contrast ratios, diff two versions,
  export tokens to Tailwind or DTCG format, or audit a design system file
  for structural correctness. Trigger on mentions of "validate DESIGN.md",
  "lint DESIGN.md", "check my design.md", "design.md spec compliance",
  "WCAG contrast check", "broken token references", "design token validation",
  "export design tokens", "diff design systems", "design.md audit",
  "@google/design.md", "npx design.md lint", "design system validation",
  "frontmatter tokens", or any request to verify a DESIGN.md file.
metadata:
  author: https://ft.ia.br
  version: "1.1"
  date: 2026-07-18
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  category: product-verification
  upstream:
    spec: https://github.com/google-labs-code/design.md
    cli: https://www.npmjs.com/package/@google/design.md
    stitch-skills: https://github.com/google-labs-code/stitch-skills
---

# design-md-validator

Validate, lint, diff, and export DESIGN.md files using the official Google
`@google/design.md` CLI. Always uses the latest published version from npm —
no vendored copy, always up-to-date with the spec.

---

## When to Use

| Trigger | Action |
|---|---|
| User has a DESIGN.md file and wants validation | `lint` |
| User wants to compare two versions | `diff` |
| User wants to export tokens to Tailwind/DTCG | `export` |
| User wants to see the current spec | `spec` |
| User shares a URL to a raw DESIGN.md | Fetch → `lint` |
| User asks "is my design.md valid?" | `lint` + interpret findings |

---

## Core Commands

All commands use `npx @google/design.md` to ensure the latest version is always
used. Never install globally — `npx` resolves from the public npm registry.

### Lint (validate)

```bash
npx @google/design.md lint DESIGN.md
```

Output: JSON with `findings[]` and `summary { errors, warnings, infos }`.
Exit code 1 if errors found, 0 otherwise.

### Diff (compare versions)

```bash
npx @google/design.md diff DESIGN.md DESIGN-v2.md
```

Output: JSON with token-level changes (added, removed, modified) and regression flag.
Exit codes: `0` no regression, `1` regression (errors in "after" > errors in "before"),
`2` input failure (file not found or unreadable).

### Export (to other formats)

```bash
# Tailwind v3 config
npx @google/design.md export --format json-tailwind DESIGN.md

# Tailwind v4 CSS theme
npx @google/design.md export --format css-tailwind DESIGN.md

# W3C Design Tokens (DTCG)
npx @google/design.md export --format dtcg DESIGN.md

# CSS custom properties (optional --prefix)
npx @google/design.md export --format css-vars DESIGN.md
npx @google/design.md export --format css-vars --prefix ds DESIGN.md
```

`css-vars` is available on main, ships in the next release — if the CLI
rejects the format, npm is still on 0.3.0.

### Spec (output the format specification)

```bash
npx @google/design.md spec
npx @google/design.md spec --rules
npx @google/design.md spec --rules-only --format json
```

---

## Workflow

### 1. Obtain the DESIGN.md

**Local file:**
```bash
npx @google/design.md lint ./DESIGN.md
```

**From URL (fetch first):**
```bash
curl -sL <url> > /tmp/DESIGN.md && npx @google/design.md lint /tmp/DESIGN.md
```

**From stdin:**
```bash
cat DESIGN.md | npx @google/design.md lint -
```

### 2. Discover the Active Rule Set

Before interpreting anything, check which rules the installed CLI actually
runs — the rule set changes between releases, and the bundled references are
a fallback, not the authoritative source:

```bash
npx @google/design.md spec --rules-only --format json
```

### 3. Run Lint

```bash
npx @google/design.md lint --format json DESIGN.md
```

### 4. Interpret Findings

Parse the JSON output and report to the user:

| Severity | Meaning | Action |
|---|---|---|
| `error` | Spec violation — file is invalid | Must fix |
| `warning` | Best practice violation — file is valid but suboptimal | Should fix |
| `info` | Informational — suggestions for improvement | Nice to fix |

### 5. Provide Actionable Fixes

For each finding, explain:
1. What the rule checks
2. Why it matters
3. How to fix it with a concrete code example

### 6. Re-validate After Fixes

After applying fixes, re-run lint to confirm the file passes.

---

## Linting Rules Reference

Load `references/linting-rules.md` for the complete rule table when providing
detailed explanations of lint failures.

---

## Token Schema Quick Reference

Load `references/token-schema.md` for the complete YAML frontmatter schema
when helping users author or fix their frontmatter tokens.

---

## Windows Compatibility

On Windows/PowerShell, the `.md` suffix in the bin name collides with Markdown
file associations. Use the `designmd` alias:

```bash
npx -p @google/design.md designmd lint DESIGN.md
```

---

## Related Official Skills

| Skill | Source | Purpose |
|---|---|---|
| `stitch-design-taste` | google-labs-code/stitch-skills | Generates DESIGN.md for Google Stitch |
| `design-md` (Stitch plugin) | google-labs-code/stitch-skills | Analyzes Stitch projects → DESIGN.md |
| `taste-design` (MCP) | mcpservers.org | MCP server for Stitch design extraction |

Install the official Stitch skill for generation:
```bash
npx skills add https://github.com/google-labs-code/stitch-skills --skill design-md
```

---

## Anti-Patterns

- Never vendor or cache the CLI — always use `npx` for latest spec
- Never manually parse YAML frontmatter when the linter can do it
- Never guess at contrast ratios — let the linter compute them
- Never assume section order is correct — let the linter verify
- Never skip re-validation after fixes
- Never assume the rule set from memory or from the bundled references —
  confirm it at runtime with `spec --rules-only`

---

## Example Session

```
User: validate my DESIGN.md

Agent:
1. Reads the file
2. Runs: npx @google/design.md spec --rules-only --format json
3. Runs: npx @google/design.md lint --format json DESIGN.md
4. Parses output
5. Reports:
   - summary: { errors: 0, warnings: 2, infos: 1 }
   - WARNING: contrast-ratio — button textColor on backgroundColor is 3.8:1 (needs 4.5:1)
   - WARNING: orphaned-tokens — color "accent-muted" defined but never used
   - INFO: token-summary — 5 colors, 3 typography, 2 rounded, 2 spacing
6. Suggests fixes with code
7. Re-runs lint to confirm
```
