# Skill Evaluation — aidlc-master

> Evaluated: 2026-08-29
> Source: `skills/aidlc-master/`
> Evaluator: skill-evaluation v2.1.0
> Framework: [Anthropic Skill Best Practices](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) + Matt Pocock's [writing-great-skills](https://www.youtube.com/watch?v=UNzCG3lw6O0)

## Summary

| Metric | Value |
|--------|-------|
| Overall Score | 78.71/100 |
| Grade | B |
| Category | `code-scaffolding-and-templates` |
| Invocation | model-invoked |
| Files | 46 (`SKILL.md` 613 lines; 45 on-demand) |
| Criteria scored / N/A | 15 scored, 3 N/A |

**Standing constraint:** this skill is a deliberate **1:1 mirror** of the upstream AWS AI-DLC rule set
(see `README.md` § Adaptations). Three criteria — conciseness, no-ops, single source of truth — score
below what a from-scratch skill would, because the port is not allowed to rewrite upstream prose. Those
scores are accepted cost, not open defects.

## Scorecard

### Axis 1 — Trigger

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 1 | Invocation design | 2x | 85/100 | Model-invoked is right: the workflow must fire on the upstream trigger phrase "Using AI-DLC, ..." without the user knowing a skill exists (`SKILL.md:39-41`). Context cost is real and permanent — a 956-char description every turn — but the skill is unreachable otherwise. |
| 2 | Description quality | 2x | 82/100 | Leading verb up front, one trigger per branch (name, vocabulary, lifecycle shape), and three explicit exclusions naming the sibling that owns each case (`SKILL.md:3-17`). Loses points for "Runs ... methodology end to end", which restates identity the body already carries, and for a trigger list long enough to blur. |

### Axis 2 — Structure

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 3 | Steps vs. reference clarity | 1x | 90/100 | Every stage is an ordered step list whose first move is `Load all steps from <file>` (e.g. Workspace Detection, `SKILL.md` § INCEPTION), and the loaded file is reference. The two content types never blur. |
| 4 | Branch-aware disclosure & pointers | 2x | 92/100 | Best feature of the port. Four common rules load at start; every stage-specific rule stays behind a pointer that names the stage that needs it. Extensions go further: only `*.opt-in.md` prompts load up front and the full rule file is read *only after the user opts in* (`SKILL.md` § Extensions Loading) — disclosure keyed to a branch that has not been taken yet. |
| 5 | Conciseness | 2x | 62/100 | `SKILL.md` is 613 lines, over the 500-line ceiling. 539 of those are upstream `core-workflow.md`, mirrored by decision; the port adds ~74 (frontmatter, activation contract, resolution order, host-agnostic answering, Gotchas). Reference material is fully disclosed, so this is length, not sprawl — but it is over the bar. |
| 6 | Coherent scope | 1x | 90/100 | One thing: run AI-DLC. Composes rather than absorbing — `README.md` hands off single changes to `pstack-skill`, Kiro loops to `ralph-loop-kiro-specs`, fan-out to `orchestration`. |

### Axis 3 — Steering

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 7 | Leading words | 2x | 85/100 | `ALWAYS` / `CONDITIONAL` / `PLACEHOLDER` on every stage, `MANDATORY` on every non-negotiable, plus `unit of work`, `greenfield`/`brownfield`, `depth`, `INCEPTION`/`CONSTRUCTION`. Used identically in every stage block, and distinctive enough to grep in a trace. |
| 8 | Completion criteria & legwork | 2x | 90/100 | Each stage ends on **Wait for Explicit Approval — DO NOT PROCEED until user confirms**, reinforced by two-level checkbox tracking (plan-level + `aidlc-state.md`) and a mandatory audit entry (`SKILL.md` § Plan-Level Checkbox Enforcement). Binary and checkable; premature completion has almost nowhere to hide. |
| 9 | Gotchas section | 2x | 82/100 | Added by the port (`SKILL.md` § Gotchas): rule-directory resolution, the exploratory-question footgun, code-outside-`aidlc-docs/`, the `audit.md` overwrite trap, resume vs restart. Every one is a failure point observed while building or reading the port. Not 90+ because the list is young — one build cycle of evidence, not many. |
| 10 | Grounded in expertise | 2x | 85/100 | Upstream content is workshop-derived and says so: `references/working-with-aidlc.md` presents its patterns as "drawn from real workshop experience". `common/overconfidence-prevention.md` and `common/error-handling.md` are failure-shaped, not aspirational. |
| 11 | Avoids railroading | 1x | 65/100 | Prescription is the product here — governed lifecycle, blocking gates, `NO EMERGENT BEHAVIOR` — and stage *selection* is genuinely adaptive (`common/depth-levels.md`: "exactly the detail needed for the problem at hand"). But `MANDATORY`/`CRITICAL` saturate the file, and saturation devalues each instance. |

### Axis 4 — Pruning

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 12 | No-ops (deletion test) | 2x | 55/100 | `Log any user input during this phase in audit.md` appears once per stage — 14 near-identical lines that a single global rule (already present in § Prompts Logging Requirements) covers. Same for `Load reverse engineering artifacts (if brownfield)`, repeated per stage. Upstream text; the mirror keeps it. |
| 13 | Single source of truth | 1x | 52/100 | The three-phase lifecycle is described in full three times: `SKILL.md`, `references/common/process-overview.md`, `references/common/welcome-message.md` — plus a fourth pass in `references/common/terminology.md`. Upstream labels this duplication INTENTIONAL (`process-overview.md:5`) because each serves a different audience; the cost is real regardless. |
| 14 | Relevance & sediment | 1x | 68/100 | Low sediment for its size — the port is one commit old and pinned to a known upstream SHA. The Operations phase is an empty placeholder occupying a full phase slot (`references/operations/operations.md`, 19 lines), which reads as structure waiting for content. |

### Conditional criteria

| # | Criterion | Weight | Score | Notes |
|---|-----------|--------|-------|-------|
| 15 | Setup flow | 1x | N/A | No credentials, endpoints, or config. The skill is self-contained by design — the whole point of the port is that setup disappears. |
| 16 | Memory mechanism | 1x | N/A | Not applicable as the rubric means it (a skill-local log accumulating across runs). The workflow's state lives in the *user's* project (`aidlc-docs/aidlc-state.md` + append-only `audit.md`), which is the artifact, not skill memory. |
| 17 | Scripts & libraries | 1x | 88/100 | `scripts/check-upstream.sh` — `check` / `mirror-diff` / `review-prompt` / `accept`. `mirror-diff` extracts the pinned upstream tree and diffs it against `references/`, so the port's central claim is *machine-verifiable*, not asserted. Guards against a wrong `UPSTREAM_COMMIT` (rejects a reference that does not touch the ported paths) and refuses to advance the pin without a human running `accept`. |
| 18 | On-demand hooks | 1x | N/A | Nothing here to enforce on file-write or commit — the skill's gates are conversational approvals, not lint-shaped rules. |

## Trigger Eval

**Skipped — no agent access.** This session operates under an instruction not to spawn subagents unless
the user asks, so the 10-prompt sub-agent test was not run. The prompts below are recorded as a
regression set for the next run with agent access.

### Prompts to test

| # | Prompt | Expected |
|---|--------|----------|
| 1 | Using AI-DLC, build a REST API for library loans | should-trigger |
| 2 | I want to run this project as a governed lifecycle: requirements, then stories, then units of work, then code | should-trigger |
| 3 | Reverse engineer this codebase into architecture and design docs before we change anything | should-trigger |
| 4 | Where does the aidlc-state file go and what's in it? | should-trigger |
| 5 | Set up a full inception phase for this greenfield service, with approval gates I sign off on | should-trigger |
| 6 | Fix the off-by-one in `paginate()` and add a test | should-not-trigger |
| 7 | Review this PR and tell me what's wrong with it | should-not-trigger |
| 8 | Run kiro-cli in a loop until the spec tasks are done | should-not-trigger |
| 9 | Fan out four subagents to search the codebase for dead imports | should-not-trigger |
| 10 | Write the requirements for a new checkout page | should-not-trigger (generic; a model handles it unaided) |

Prompt 10 is the sharpest test: it uses AI-DLC-adjacent vocabulary ("requirements") for work that needs
no lifecycle. If it triggers, the description's vocabulary branch is too greedy.

## Failure Modes Detected

| Mode | Evidence | Root cause | Defense |
|------|----------|------------|---------|
| No-ops | `SKILL.md`, the 14 per-stage `Log any user input ... in audit.md` lines; § Prompts Logging Requirements already states it globally | Upstream repeats the global rule per stage for local salience | Accepted. The mirror decision forbids editing upstream prose; the duplication is load-bearing for upstream's own users, who read one stage at a time. |
| Duplication | Lifecycle described in `SKILL.md`, `common/process-overview.md`, `common/welcome-message.md`, `common/terminology.md` | Upstream declares it INTENTIONAL (`process-overview.md:5`) — different audiences per file | Accepted, and now documented: `README.md` § Adaptations records that the triplication is inherited, so a future reader does not "fix" it and break the mirror. |
| Sprawl | `SKILL.md` 613 lines vs 500 ceiling | 539 inherited + 74 added | Partly defensible. The added 74 lines are the ones worth defending line by line — the Gotchas block earns its space; the host-agnostic answering block was already tightened from 14 lines to 9. |
| Sediment | `references/operations/operations.md` — a 19-line placeholder for a whole phase | Upstream ships Operations unimplemented | Dismissed as a port defect. It is upstream's roadmap, correctly mirrored, and `SKILL.md` labels the stage PLACEHOLDER so no run wastes a turn on it. |
| Premature completion | Not found — every stage gate is "DO NOT PROCEED until user confirms" plus a checkbox update in the same interaction | — | — |
| Weak steering | Not found in the port's own additions; § Gotchas uses concrete failures rather than exhortation | — | — |
| Buried steps | Not found — heavy reference is behind pointers, and no stage block exceeds ~10 lines | — | — |

## Prioritized Actions

### 1. Re-run the trigger eval with agent access, watching prompt 10

**Evidence:** Trigger Eval section — skipped this run. `SKILL.md:3-17` claims a vocabulary branch
("workflow planning", "aidlc-docs", "units of work") that has never been tested against adjacent
requests.

**Fix:** Run the 10 recorded prompts in sub-agent sessions. If prompt 10 or 6 triggers, narrow the
vocabulary branch to phrases that only exist inside AI-DLC (`aidlc-docs`, `aidlc-state`, `units of
work`) and drop the generic ones ("workflow planning", "requirements analysis").

### 2. Let the Gotchas section earn its 2x weight over time

**Evidence:** `SKILL.md` § Gotchas — five entries, all from a single build cycle.

**Fix:** After each real AI-DLC run, add any new failure point that cost a turn. Target the specific
shape upstream lacks: what breaks when the rules live in a skill instead of an IDE rule directory.

### 3. Keep the mirror claim machine-checked, not asserted

**Evidence:** `scripts/check-upstream.sh mirror-diff` currently returns exactly one hunk — the A5 note.

**Fix:** Run `mirror-diff` before every commit that touches `references/`. One hunk is the pass
condition; anything else is drift. Advance `UPSTREAM_COMMIT` only via `accept`, after review.

### 4. Do not pay down conciseness by editing upstream prose

**Evidence:** Criteria 5, 12, 13 — all three drags trace to inherited text.

**Fix:** The only legitimate reductions are in the port's own ~74 lines. If the length becomes a real
problem in practice, the answer is a different fidelity decision (condensed port), taken explicitly —
not silent trimming that breaks `mirror-diff`.

## Bonus Patterns

| Pattern | Status | Notes |
|---------|--------|-------|
| Validation loops | Present | Content validation before any file write (`SKILL.md` § Content Validation → `common/content-validation.md`), extension-compliance summary at each stage completion, and `mirror-diff` as a validation loop over the port itself. |
| Output templates | Present | Audit log entry format inline in `SKILL.md`; question file format in `common/question-format-guide.md`; full generated tree in `references/generated-docs-reference.md`; vision and tech-env templates with minimal and full examples in `references/inputs/`. |
| Procedures over declarations | Present | Stage selection is a procedure with assessment criteria ("Analyze request complexity and scope … Default to inclusion for borderline cases"), and `common/depth-levels.md` sets detail level by problem characteristics rather than by rule. |
| Defaults over menus | Present | ALWAYS stages are the default path; conditional stages carry Execute IF / Skip IF tests rather than asking the user to choose a shape. The host-answering rule also picks a default (file) and mentions the alternative (inline mirror) in one clause. |
| Trace-checkable steering | Present | `INCEPTION`, `unit of work`, `aidlc-docs`, `Wait for Explicit Approval`, `brownfield` — if none of these appear in a trace, the skill did not fire. |

## Grade Scale

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| B | 60–79 | Good skill, minor improvements needed |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

---

*Generated by [skill-evaluation](https://github.com/fabricioctelles/skills) v2.1.0, merging the [Anthropic skill quality framework](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) with Matt Pocock's [writing-great-skills](https://www.youtube.com/watch?v=UNzCG3lw6O0) methodology.*
