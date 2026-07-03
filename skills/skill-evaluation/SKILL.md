---
name: skill-evaluation
description: >
  Evaluate any agent skill against a merged framework — Anthropic's Claude Code
  best practices plus Matt Pocock's writing-great-skills methodology — across
  4 axes (Trigger, Structure, Steering, Pruning). Produces a structured
  markdown scorecard (0–100) with per-criterion evidence, a weighted overall
  score, and diagnosed failure modes (premature completion, duplication,
  sediment, sprawl, no-ops, weak steering, buried steps) with prioritized
  fixes. Use when the user says "evaluate this skill", "rate this skill",
  "audit skill quality", "how good is this skill", "skill scorecard", "review
  SKILL.md", "skill best practices check", or wants to compare skills against
  the merged framework.
metadata:
  author: ft.ia.br
  version: "2.0.0"
  date: 2026-07-03
  repository: https://github.com/fabricioctelles/skills
  license: Apache-2.0
  category: code-quality-and-review
---

# Skill Evaluation

Evaluate agent skills against a merged framework: Anthropic's Claude Code
best practices plus Matt Pocock's writing-great-skills methodology. Score
across 4 axes — Trigger, Structure, Steering, Pruning — then diagnose named
failure modes instead of listing generic weak spots.

If you need the vocabulary and tests behind Axes 1, 3, and 4 (leading words,
completion criteria, context pointers, the deletion test, failure-mode
definitions), read `references/mechanics.md` before scoring those axes.

## Source

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026
- "The Missing Manual: How to Write Great Skills" — Matt Pocock, AI Engineer World's Fair 2026 ([video](https://www.youtube.com/watch?v=UNzCG3lw6O0)), and his `writing-great-skills` skill

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | Path to skill directory or SKILL.md to evaluate | Ask user |
| `output` | Path to write the scorecard | `<target>/EVALUATION.md` |
| `compare` | Optional second skill to compare side-by-side | None |

## Criteria

18 criteria: 14 core, scored on every skill, plus 4 conditional criteria
scored only when the skill's category makes them apply — otherwise mark
**N/A** and exclude the criterion from both the numerator and denominator of
the weighted average. Every score is 0–100 with evidence citing file,
section, or line.

### Axis 1 — Trigger (invocation)

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 1 | Invocation design | 2x | Is model-invoked vs. user-invoked deliberate and fitting? Model-invoked pays **context load** (the description loads every turn); user-invoked pays **cognitive load** (the human is the index). A skill that only ever fires by hand should be user-invoked. |
| 2 | Description quality | 2x | Model-invoked: leading word up front, one trigger per branch (synonyms renaming the same branch are duplication), no identity that's redundant with the body. User-invoked (`disable-model-invocation: true`): a human-facing one-liner, no trigger list. Score against the mode the skill actually uses — never penalize a user-invoked skill for lacking trigger phrases. |

### Axis 2 — Structure

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 3 | Steps vs. reference clarity | 1x | Does the skill distinguish ordered steps from on-demand reference? All-reference and all-steps skills are both valid — score clarity, not the mix. Is related material co-located (definition, rules, caveats under one heading)? |
| 4 | Branch-aware disclosure & pointers | 2x | Is material every branch needs inline, and material only some branches need behind a context pointer? Does each pointer's wording say when to follow it ("if you need X, read Y")? A weakly worded pointer to must-have material is a variance bug. |
| 5 | Conciseness (no sprawl) | 2x | Is SKILL.md lean — under 500 lines as a ceiling, smaller is better — with every line earning its context cost? |
| 6 | Coherent scope | 1x | Does the skill do one thing and compose with others, rather than covering too much? |

### Axis 3 — Steering

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 7 | Leading words | 2x | Does the skill use compact, high-prior terms ("vertical slice", "tight", "red") to anchor behavior, repeated consistently? Could any verbose passage collapse into one? |
| 8 | Completion criteria & legwork | 2x | Skills with steps: does each step end on a checkable, exhaustive completion criterion? A vague one invites premature completion. Skills that are pure reference: is there an exhaustiveness bar over the reference itself ("every rule applied")? If neither applies, mark N/A. |
| 9 | Gotchas section | 2x | Is there explicit capture of failure points, edge cases, footguns? |
| 10 | Grounded in expertise | 2x | Does content come from observed failures and real project facts, or generic "best practices"? |
| 11 | Avoids railroading | 1x | Does the skill leave room to adapt — procedures over declarations, defaults over menus — without over-prescribing? |

### Axis 4 — Pruning

| # | Criterion | Weight | Key question |
|---|-----------|--------|---------------|
| 12 | No-ops (deletion test) | 2x | Running the deletion test sentence by sentence: if removing a sentence leaves behavior unchanged, it's a no-op — including restatements of what the model already does by default. Cite line numbers for candidates. |
| 13 | Single source of truth | 1x | Does each meaning live in exactly one place? Duplication between SKILL.md and references/ counts too. |
| 14 | Relevance & sediment | 1x | Are there stale lines, accumulated layers, or material that no longer influences what the skill does? |

### Conditional criteria

Score only when the skill's category (from `references/categories.md`) makes
the criterion apply; otherwise mark N/A and drop it from the weighted
average entirely.

| # | Criterion | Weight | Applies to category |
|---|-----------|--------|----------------------|
| 15 | Setup flow | 1x | library-and-api-reference, data-fetching-and-analysis, ci-cd-and-deployment, infrastructure-operations |
| 16 | Memory mechanism | 1x | business-process-automation, data-fetching-and-analysis, runbooks |
| 17 | Scripts & libraries | 1x | product-verification, code-scaffolding-and-templates, code-quality-and-review, data-fetching-and-analysis, infrastructure-operations |
| 18 | On-demand hooks | 1x | code-quality-and-review, ci-cd-and-deployment |

Override this table with judgment, in either direction: score a criterion
for a skill outside these categories when it would clearly benefit (e.g., a
non-`product-verification` skill that obviously needs a helper script), and
mark it N/A even within an applicable category when the pattern doesn't fit
the skill's shape (e.g., a pure-reference vocabulary skill filed under
`code-quality-and-review` has nothing for a hook to enforce). Explain the
override in the scorecard either way.

### Overall score

Weighted average of applicable criteria only:

```
overall = sum(score × weight) / sum(weight)
```

N/A criteria are excluded from both sums — never scored as 0, never counted
as weight.

## Scoring Guide

| Score | Meaning |
|-------|---------|
| 0 | Not present at all |
| 1–25 | Minimal/token effort, barely addresses the criterion |
| 26–50 | Partially addressed but with significant gaps |
| 51–75 | Solid implementation with room for improvement |
| 76–90 | Strong implementation, minor gaps only |
| 91–100 | Exemplary — would use as a reference for others |

## Grade Scale

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

## Workflow

1. **Read the target skill** — SKILL.md, its frontmatter (check for
   `disable-model-invocation`), and every file in the skill directory.
2. **Read `references/mechanics.md`** — the vocabulary and tests Axes 1, 3,
   and 4 depend on, including what makes a context pointer's wording
   effective.
3. **Classify** — use `references/categories.md` and its decision tree to
   assign a category. The category determines which conditional criteria
   apply.
4. **Score all applicable criteria** — specific evidence per criterion; mark
   N/A wherever the conditional table, or your own judgment, says a
   criterion doesn't apply.
5. **Diagnose failure modes** — see below.
6. **Assess bonus patterns** — the 4 carried over from v1, plus a fifth:

   | Bonus | Applies when | What to look for |
   |-------|-------------|-----------------|
   | Validation loops | Skill produces output or modifies state | Instructs the agent to self-check before finalizing |
   | Output templates | Skill generates structured output | Includes a concrete template/example of expected format |
   | Procedures over declarations | Skill teaches a method | Teaches *how to approach* problems, not *what to produce* for one case |
   | Defaults over menus | Skill offers tool/approach choices | Picks a clear default, mentions alternatives briefly |
   | Trace-checkable steering | Skill uses leading words | The leading words are distinctive enough that a user could grep the agent's reasoning traces to confirm the skill actually fired |

   Report each as Present / Absent / N/A.
7. **Compute the weighted score**, assign a grade.
8. **Write the scorecard** to the output path.

## Failure-mode diagnosis

Name the failure mode, cite evidence, prescribe the defense — this replaces
a generic "top improvements" list.

| Mode | Evidence to look for | Defense |
|------|----------------------|---------|
| Premature completion | Vague completion criteria with future steps still visible | Sharpen the completion criterion first; only split by sequence if it's irreducibly vague *and* the rush is actually observed |
| Weak steering | Instruction present but the agent doesn't reliably follow it | Find or strengthen the leading word — one too weak to beat the default is a no-op, so the fix is a stronger word, not a different technique |
| Duplication | Same meaning in 2+ places, including SKILL.md vs. references/ | Collapse to a single source of truth, often via a leading word |
| Sediment | Stale layers, outdated references, dead instructions | Line-by-line relevance check; delete |
| Sprawl | Long even with no duplication or sediment | Disclose reference behind pointers; split by branch or sequence |
| No-ops | Lines that don't change behavior versus the model's default | Sentence-by-sentence deletion test; delete the whole sentence, don't trim words |
| Buried steps | Inline reference so heavy it soaks the steps | Progressive disclosure — push the reference behind a pointer |

After the table, write a **Prioritized Actions** section: 3–5 highest-impact
actions derived directly from the detected failure modes, each citing its
evidence.

Note: **context overload** — too many model-invoked skills competing for
attention in one environment — is a portfolio-level problem, out of scope
for evaluating a single skill. Record the description's context-load cost
when it's notable; don't score the portfolio.

## Output Format

```markdown
# Skill Evaluation — {skill name}

> Evaluated: {date}
> Source: {path}
> Evaluator: skill-evaluation v2.0.0
> Framework: [Anthropic Skill Best Practices](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) + Matt Pocock's [writing-great-skills](https://www.youtube.com/watch?v=UNzCG3lw6O0)

## Summary

| Metric | Value |
|--------|-------|
| Overall Score | {weighted}/100 |
| Grade | {A/B/C/D/F} |
| Category | {category} |
| Invocation | {model-invoked / user-invoked} |
| Files | {count} |
| Criteria scored / N/A | {n} scored, {m} N/A |

## Scorecard

### Axis 1 — Trigger

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 1 | Invocation design | 2x | {n}/100 | {evidence} |
| 2 | Description quality | 2x | {n}/100 | {evidence} |

### Axis 2 — Structure

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 3 | Steps vs. reference clarity | 1x | {n}/100 | {evidence} |
| 4 | Branch-aware disclosure & pointers | 2x | {n}/100 | {evidence} |
| 5 | Conciseness | 2x | {n}/100 | {evidence} |
| 6 | Coherent scope | 1x | {n}/100 | {evidence} |

### Axis 3 — Steering

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 7 | Leading words | 2x | {n}/100 | {evidence} |
| 8 | Completion criteria & legwork | 2x | {n/100 or N/A} | {evidence} |
| 9 | Gotchas section | 2x | {n}/100 | {evidence} |
| 10 | Grounded in expertise | 2x | {n}/100 | {evidence} |
| 11 | Avoids railroading | 1x | {n}/100 | {evidence} |

### Axis 4 — Pruning

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 12 | No-ops (deletion test) | 2x | {n}/100 | {evidence with line citations} |
| 13 | Single source of truth | 1x | {n}/100 | {evidence} |
| 14 | Relevance & sediment | 1x | {n}/100 | {evidence} |

### Conditional criteria

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 15 | Setup flow | 1x | {n/100 or N/A} | {evidence or reason for N/A} |
| 16 | Memory mechanism | 1x | {n/100 or N/A} | {evidence or reason for N/A} |
| 17 | Scripts & libraries | 1x | {n/100 or N/A} | {evidence or reason for N/A} |
| 18 | On-demand hooks | 1x | {n/100 or N/A} | {evidence or reason for N/A} |

## Failure Modes Detected

| Mode | Evidence | Root cause | Defense |
|------|----------|------------|---------|
| {mode, or a single row "None detected"} | {file:line} | {cause} | {defense} |

## Prioritized Actions

### 1. {action}

**Evidence:** {file:line or section}

**Fix:** {specific recommendation}

### 2. {action}

**Evidence:** {file:line or section}

**Fix:** {specific recommendation}

(3–5 total, each tied to a detected failure mode)

## Bonus Patterns

| Pattern | Status | Notes |
|---------|--------|-------|
| Validation loops | {Present/Absent/N/A} | {detail} |
| Output templates | {Present/Absent/N/A} | {detail} |
| Procedures over declarations | {Present/Absent/N/A} | {detail} |
| Defaults over menus | {Present/Absent/N/A} | {detail} |
| Trace-checkable steering | {Present/Absent/N/A} | {detail} |

## Grade Scale

{copy the Grade Scale table from the Grade Scale section above}

---

*Generated by [skill-evaluation](https://github.com/fabricioctelles/skills) v2.0.0, merging the [Anthropic skill quality framework](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) with Matt Pocock's [writing-great-skills](https://www.youtube.com/watch?v=UNzCG3lw6O0) methodology.*
```

## Comparison Mode

When `compare` is set, produce a side-by-side table across all 18 criteria.
Leave a cell N/A rather than scoring it 0, and exclude N/A rows from the
Overall row's weighted math for that skill.

```markdown
## Comparison: {skill A} vs {skill B}

| # | Criterion | {A} | {B} | Delta |
|---|-----------|-----|-----|-------|
| 1 | Invocation design | 60 | 85 | +25 |
| 2 | Description quality | 25 | 70 | +45 |
| ... | ... | ... | ... | ... |
| 15 | Setup flow | N/A | 80 | — |
| **Overall** | | **43** | **72** | **+29** |
```

## Quality Checklist

Before delivering the scorecard, verify:

- [ ] All applicable criteria (up to 18) have a score and evidence citation
- [ ] Every N/A is justified by the skill's category, or an explained override
- [ ] Failure modes cite file:line evidence, or the table reads "None detected"
- [ ] The weighted average excludes N/A criteria from both sum and count
- [ ] Prioritized actions are derived from the detected failure modes, not generic advice
- [ ] Bonus patterns (5) are assessed as Present/Absent/N/A
- [ ] Grade matches the score range
- [ ] Output file is valid markdown
