---
name: skill-evaluation
description: >
  Evaluate any agent skill against Anthropic's 9 best-practice criteria from
  "Lessons from building Claude Code." Produces a structured markdown scorecard
  with per-criterion notes (0–100), overall score, and prioritized improvement
  actions. Use when the user says "evaluate this skill", "rate this skill",
  "audit skill quality", "how good is this skill", "skill scorecard", "review
  SKILL.md", "skill best practices check", or wants to compare skills against
  the Anthropic framework.
metadata:
  author: ft.ia.br
  version: "1.0.0"
  date: 2026-06-27
  repository: https://github.com/fabriciotelles/skills
  license: Apache-2.0
  category: code-quality-and-review
---

# Skill Evaluation

Evaluate agent skills against the 9 best-practice criteria defined by
Anthropic's Claude Code team.

## Source

[Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Jun 2026

---

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | Path to skill directory or SKILL.md to evaluate | Ask user |
| `output` | Path to write the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side-by-side | None |

---

## Criteria (9)

Each criterion is scored 0–100 based on evidence found in the skill files.

| # | Criterion | Key Question |
|---|-----------|-------------|
| 1 | **Don't state the obvious** | Does the skill focus on information Claude wouldn't know by default? Or does it restate standard knowledge? |
| 2 | **Gotchas section** | Is there an explicit section capturing common failure points, edge cases, and footguns? |
| 3 | **File system & progressive disclosure** | Does the skill use multiple files (references/, scripts/, assets/) with the SKILL.md as a hub? |
| 4 | **Avoids railroading** | Does the skill give Claude flexibility to adapt, or does it over-prescribe exact steps? |
| 5 | **Setup flow** | Does the skill handle first-run setup (config detection, user prompts, missing dependencies)? |
| 6 | **Description written for model trigger** | Is the description a trigger-matching string with concrete phrases, or a human-readable summary? |
| 7 | **Memory mechanism** | Does the skill persist state between runs (logs, config, JSON, SQLite)? |
| 8 | **Scripts & libraries** | Does the skill include executable scripts, helpers, or code Claude can compose with? |
| 9 | **On-demand hooks** | Does the skill define hooks that activate only when the skill is invoked? |

---

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 0 | Not present at all |
| 1–25 | Minimal/token effort, barely addresses the criterion |
| 26–50 | Partially addressed but with significant gaps |
| 51–75 | Solid implementation with room for improvement |
| 76–90 | Strong implementation, minor gaps only |
| 91–100 | Exemplary — would use as a reference for others |

---

## Workflow

1. **Read the target skill** — SKILL.md + list all files in the skill directory (references/, scripts/, assets/, etc.)

2. **For each of the 9 criteria**, examine the skill and assign a score with a 1–2 sentence justification citing specific evidence (file names, section headings, presence/absence of patterns).

3. **Calculate overall score** — weighted average:
   - Criteria 1, 2, 3, 6 → weight 2x (highest impact on skill quality)
   - Criteria 4, 5, 7, 8, 9 → weight 1x

4. **Identify top 3 improvements** — the 3 lowest-scoring criteria with specific actionable recommendations.

5. **Write the scorecard** to the output path.

---

## Output Format

```markdown
# Skill Evaluation — {skill name}

> Evaluated: {date}
> Source: {path}
> Evaluator: skill-evaluation v1.0.0
> Framework: [Anthropic Skill Best Practices](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)

## Summary

| Metric | Value |
|--------|-------|
| Overall Score | {weighted}/100 |
| Grade | {A/B/C/D/F} |
| Files | {count} |
| Has references/ | {yes/no} |
| Has scripts/ | {yes/no} |
| Has gotchas | {yes/no} |

## Scorecard

| # | Criterion | Score | Notes |
|---|-----------|-------|-------|
| 1 | Don't state the obvious | {n}/100 | {justification} |
| 2 | Gotchas section | {n}/100 | {justification} |
| 3 | Progressive disclosure | {n}/100 | {justification} |
| 4 | Avoids railroading | {n}/100 | {justification} |
| 5 | Setup flow | {n}/100 | {justification} |
| 6 | Description for trigger | {n}/100 | {justification} |
| 7 | Memory mechanism | {n}/100 | {justification} |
| 8 | Scripts & libraries | {n}/100 | {justification} |
| 9 | On-demand hooks | {n}/100 | {justification} |

## Grade Scale

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

## Top 3 Improvements

### 1. {criterion name} ({score}/100)

**Problem:** {what's missing or weak}

**Action:** {specific, actionable recommendation}

### 2. {criterion name} ({score}/100)

**Problem:** {what's missing}

**Action:** {recommendation}

### 3. {criterion name} ({score}/100)

**Problem:** {what's missing}

**Action:** {recommendation}

---

*Generated by [skill-evaluation](https://github.com/fabriciotelles/skills) using the [Anthropic skill quality framework](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills).*
```

---

## Comparison Mode

When `compare` is set, produce a side-by-side table:

```markdown
## Comparison: {skill A} vs {skill B}

| Criterion | {A} | {B} | Delta |
|-----------|-----|-----|-------|
| Don't state the obvious | 60 | 85 | +25 |
| Gotchas | 25 | 70 | +45 |
| ... | ... | ... | ... |
| **Overall** | **43** | **72** | **+29** |
```

---

## Quality Checklist

Before delivering the scorecard, verify:

- [ ] All 9 criteria have a score and justification
- [ ] Justifications cite specific files/sections as evidence
- [ ] Overall score uses the weighted formula
- [ ] Top 3 improvements are actionable (not vague)
- [ ] Grade matches the score range
- [ ] Output file is valid markdown
