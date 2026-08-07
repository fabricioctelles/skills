# Output Template

Use the user's language. Preserve this section order, but keep empty prose
brief. Omit the comparison section unless `compare` is supplied.

```markdown
# Agent Plugin Evaluation — {plugin name}

> Verdict: {PASS / PARTIAL / FAIL} — {one-sentence reason}
> Evaluated: {date}
> Source: {path or URL} ({commit when available})
> Standard: Agent Plugins {version} ({status}), retrieved {date}
> Audit mode: static / authorized dynamic checks

## Summary

| Metric | Value |
|---|---|
| Conformance | {PASS / PARTIAL / FAIL} |
| Raw score | {n}/100 |
| Final score | {n}/100 {cap explanation, if any} |
| Grade | {A/B/C/D/F} |
| Portable components | {skills count}, {MCP server count} |
| Client extensions | {namespaces or none} |
| Criteria scored / N/A | {n} / {n} |

## Release blockers

1. **{finding}** — `{file:line or JSON pointer}`; spec §{section}.
   Impact: {official failure boundary}. Fix: {smallest conforming change}.

Write “None found” when the gate is PASS. Do not mix recommendations here.

## Scorecard

| # | Criterion | Weight | Score | Evidence |
|---|---|---:|---:|---|
| 1 | Root package and manifest | 3x | {n}/100 | {citation} |
| ... | ... | ... | ... | ... |
| 18 | Maintenance and release hygiene | 1x | {n}/100 | {citation} |

Use `N/A` plus a reason for conditional criteria.

## Findings by component

### Manifest and package
{findings, including non-fatal deviations}

### Skills
{one row or paragraph per discovered Skill; include conformance and quality}

### MCP servers
{one row or paragraph per server; include transport and failure boundary}

### Client extensions
{portable-vs-client-specific assessment}

### Security and containment
{resolved paths, secret scan, and execution-risk findings; never reveal values;
distinguish suspected from confirmed credentials and state the corroboration}

## Prioritized actions

1. **P0 — {action}.** Evidence: `{file:line}`. Verify by: {check}.
2. **P1 — {action}.** Evidence: `{file:line}`. Verify by: {check}.
3. **P2 — {action}.** Evidence: `{file:line}`. Verify by: {check}.

## Limits

{Anything not executed or verified, unsupported extension specs, network limits,
or ambiguity. State that static safety boundaries were intentional.}
```

## Comparison mode

Append after both independent evaluations:

```markdown
## Comparison — {A} vs {B}

| Metric | {A} | {B} | Delta / winner |
|---|---:|---:|---|
| Conformance | {status} | {status} | {result} |
| Raw score | {n} | {n} | {signed delta} |
| Final score | {n} | {n} | {signed delta} |
| Grade | {grade} | {grade} | {result} |

| # | Criterion | {A} | {B} | Delta |
|---|---|---:|---:|---:|
| 1 | Root package and manifest | {n} | {n} | {signed delta} |
| ... | ... | ... | ... | ... |
| 18 | Maintenance and release hygiene | {n} | {n} | {signed delta} |

### Decision

{Which plugin is more conformant, which has better uncapped design quality,
and which is safer to release. Do not collapse those into one vague winner.}

### Shared and unique actions

- **Both:** {shared action}
- **{A}:** {specific action}
- **{B}:** {specific action}
```
