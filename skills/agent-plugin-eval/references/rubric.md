# Agent Plugin Evaluation Rubric

Score each applicable criterion from 0–100 and multiply by its weight. Mark a
conditional criterion `N/A` only when the relevant component is absent; exclude
N/A from numerator and denominator. Cite concrete `file:line`, JSON pointer, or
resolved-path evidence for every score.

## Scale

| Score | Meaning |
|---|---|
| 0 | Missing or wholly broken |
| 1–25 | Token attempt; major requirements unmet |
| 26–50 | Partial implementation with serious gaps |
| 51–75 | Functional, with meaningful improvements needed |
| 76–90 | Strong; minor gaps |
| 91–100 | Exemplary and release-ready |

## Axis 1 — Portable conformance

| # | Criterion | Weight | Key question |
|---|---|---:|---|
| 1 | Root package and manifest | 3x | Is there exactly one regular root `plugin.json`, with all resolved package paths contained? |
| 2 | Schema, required fields, and name | 3x | Does the manifest target a supported canonical schema and satisfy every fatal required-field/name rule? |
| 3 | Closed metadata model | 2x | Are top-level and author fields closed, optional types correct, and metadata internally accurate? |
| 4 | Fixed discovery and version coherence | 2x | Are standard components only in fixed locations, with matching spec versions and correct filesystem kinds? |

## Axis 2 — Components and integration

| # | Criterion | Weight | Applies when | Key question |
|---|---|---:|---|---|
| 5 | Agent Skills conformance | 2x | At least one Skill is discovered | Does every immediate Skill satisfy the Agent Skills format and containment rules? |
| 6 | Agent Skills quality | 1x | At least one Skill is discovered | Are triggers, instructions, resources, validation, and progressive disclosure useful and precise? Aggregate all Skills; identify outliers. |
| 7 | MCP configuration conformance | 2x | `mcp.json` exists | Are the closed top level and every server variant valid under the matching schema? |
| 8 | MCP runtime portability | 2x | At least one stdio server exists | Are command, args, cwd, env, placeholders, bundled executables, and dependencies deterministic across installations? |
| 9 | Remote MCP transport quality | 2x | At least one remote server exists | Are URL, TLS, headers, transport choice, redirect assumptions, and authentication boundaries safe and portable? |
| 10 | Extension isolation | 1x | Client-specific data/files exist | Are extensions correctly reverse-domain namespaced without masquerading as portable core? |

## Axis 3 — Safety and resilience

| # | Criterion | Weight | Key question |
|---|---|---:|---|
| 11 | Path containment | 3x | Do symlinks, commands, working directories, and package-relative references remain within their required roots after resolution? |
| 12 | Secrets and least exposure | 3x | Are visible manifests/configs free of credentials and unnecessarily sensitive literals? Are suspected values redacted in the report? |
| 13 | Component independence | 2x | Can valid Skills and MCP entries remain useful when an unrelated component is absent, invalid, unsupported, or unavailable? |
| 14 | Static audit safety | 1x | Can reviewers and clients inspect/install the package without executing hidden setup, hooks, or side effects? |

## Axis 4 — Product quality

| # | Criterion | Weight | Key question |
|---|---|---:|---|
| 15 | Cohesion and portable value | 2x | Do the components form one understandable plugin and deliver meaningful value on conformant clients? |
| 16 | Discoverability and documentation | 1x | Do description, version, repository, license, keywords, and user guidance make purpose, trust, setup, and limits clear? |
| 17 | Validation evidence | 2x | Are schemas, Skills, scripts, and MCP behavior covered by safe reproducible checks or fixtures? Do tests exercise failure boundaries? |
| 18 | Maintenance and release hygiene | 1x | Are versions, dependencies, generated artifacts, executable bits, ignored files, and client extensions intentional and maintainable? |

## Weighted result and gates

Compute the uncapped weighted score:

```text
raw = sum(score × weight) / sum(applicable weights)
```

Then apply the conformance gate from `spec-checklist.md`:

| Gate | Cap | Meaning |
|---|---:|---|
| PASS | none | No normative violation found |
| PARTIAL | 59 | At least one non-fatal deviation or invalid/skipped component |
| FAIL | 39 | Plugin-level fatal failure, root-manifest escape, or confirmed credential |

Grades use the final capped score: A 80–100, B 60–79, C 40–59, D 20–39,
F 0–19. Always report both raw and final scores when a cap applies.

## Comparison rules

- Score each plugin independently, including its N/A denominator and gate.
- Use final score for the headline delta; show raw delta separately when either
  plugin is capped.
- Compare conformance statuses directly; do not imply that a numerical lead can
  compensate for a release blocker.
- Distinguish shared weaknesses from plugin-specific regressions and end with a
  per-plugin action list.
