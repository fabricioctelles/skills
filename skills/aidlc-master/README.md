# 🏛️ aidlc-master

> AWS's **AI-DLC** (AI-Driven Development Life Cycle) as **one self-contained skill**. No per-IDE
> installation, no copying rule files into `.kiro/`, `.amazonq/`, `CLAUDE.md` or
> `.github/copilot-instructions.md`. Drop the folder into any agent that reads skills.sh-format
> skills and say *"Using AI-DLC, ..."*.

Ported from [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) — rule set version
**1.0.1**, upstream commit
[`e49341db`](https://github.com/awslabs/aidlc-workflows/commit/e49341dbeb8af82758dd85e96ed7fe9bcf38a447)
(the last commit touching the ported paths; repository HEAD at port time was `af650cf9`).
Licensed **MIT No Attribution** — attribution is not required, and is given anyway. All credit for
the methodology is AWS's.

---

## The idea

AI-DLC is a governed software lifecycle for AI coding agents: three phases, explicit human approval
gates between stages, a complete audit trail, and every artifact written to `aidlc-docs/`. It is the
opposite of vibe coding — the agent proposes an execution plan, you approve it, and each stage stops
for review before the next one starts.

The workflow is **adaptive**: only the stages that add value run. A one-file bug fix and a
multi-service greenfield build go through the same machinery at different depths.

```text
INCEPTION (what & why)          CONSTRUCTION (how)              OPERATIONS
├── Workspace Detection  ALWAYS ├── per unit:                   └── placeholder
├── Reverse Engineering  brownf │   ├── Functional Design  COND
├── Requirements Analysis ALWAYS│   ├── NFR Requirements   COND
├── User Stories         COND   │   ├── NFR Design         COND
├── Workflow Planning    ALWAYS │   ├── Infrastructure Dsg  COND
├── Application Design   COND   │   └── Code Generation   ALWAYS
└── Units Generation     COND   └── Build and Test        ALWAYS
```

Optional **extensions** (security baseline, property-based testing, resiliency baseline) are offered
as opt-ins during Requirements Analysis. Only the opt-in prompts load up front; a full extension rule
file is read only if you accept it. Once accepted, its rules are blocking constraints.

## Using it

```text
Using AI-DLC, build a REST API that ...
Using AI-DLC, add multi-tenant support to this codebase
```

The skill then displays the welcome message once, detects greenfield vs brownfield, and starts. For
brownfield projects it reverse-engineers the existing code into design docs before touching anything.

Optional but recommended for anything non-trivial: write a **vision** document and a **technical
environment** document first — see `references/inputs/inputs-quickstart.md`, with guides and both
minimal and full examples.

Two habits worth learning early (`references/working-with-aidlc.md` has the rest):

- Prefix exploratory questions with **"Do not update any documents."** Otherwise the agent reads the
  question as a change request and rewrites design docs.
- Answers go into the generated question files. `aidlc-docs/audit.md` is append-only and holds the
  complete raw record of every prompt and response.

**Not the right skill for**: a single focused change, a code review, a PR, or debugging → use
`pstack-skill`. Autonomous loops over Kiro specs → `ralph-loop-kiro-specs`. Plain subagent
orchestration → `orchestration`.

## Layout

| Path | Upstream origin | Note |
| --- | --- | --- |
| `SKILL.md` | `aidlc-rules/aws-aidlc-rules/core-workflow.md` | near-literal + adaptations A1–A4, A6 |
| `references/common/` (11) | `aws-aidlc-rule-details/common/` | 1:1 (A5 in `process-overview.md`) |
| `references/inception/` (7) | `aws-aidlc-rule-details/inception/` | 1:1 |
| `references/construction/` (6) | `aws-aidlc-rule-details/construction/` | 1:1 |
| `references/operations/` (1) | `aws-aidlc-rule-details/operations/` | 1:1 |
| `references/extensions/` (6) | `aws-aidlc-rule-details/extensions/` | 1:1 — 3 baselines + 3 opt-ins |
| `references/working-with-aidlc.md` | `docs/WORKING-WITH-AIDLC.md` | 1:1, renamed |
| `references/generated-docs-reference.md` | `docs/GENERATED_DOCS_REFERENCE.md` | 1:1, renamed |
| `references/inputs/` (9) | `docs/writing-inputs/` | 1:1, flattened |
| `UPSTREAM_COMMIT` | — | reviewed upstream reference |
| `scripts/check-upstream.sh` | — | upstream sync tooling |
| `EVALUATION.md` | — | quality scorecard (`skill-evaluation`) |

Everything except `SKILL.md` loads on demand.

## Adaptations

The port is a 1:1 mirror. These six deviations are the complete list — anything else the sync
tooling reports is drift, not intent.

| # | Where | Change |
| --- | --- | --- |
| **A1** | `SKILL.md` | Skill frontmatter added (`name`, trigger-oriented `description`, `metadata` with the upstream pin). Does not exist upstream. |
| **A2** | `SKILL.md` § *Rule Details Loading* | Resolution order keeps the four project-local IDE paths (so an organization's customized rules still win) and appends **`references/` inside this skill** as the guaranteed fallback. Also lists the three bundled non-rule references. |
| **A3** | `SKILL.md` header | `OVERRIDES all other built-in workflows` is scoped to *while this skill is active*, with an explicit activation/opt-out contract. |
| **A4** | `SKILL.md` § *Host-agnostic answering* | The question file stays mandatory and canonical. A host agent with a native structured multiple-choice prompt may mirror the question inline, then write the chosen letter back into the `[Answer]:` tag. No proprietary tool names appear anywhere in the skill. |
| **A5** | `references/common/process-overview.md` | The "duplication is intentional" note points at this skill's `README.md` instead of the upstream repository README. |
| **A6** | `SKILL.md` § *Gotchas* | New section: failure points specific to running AI-DLC from a skill rather than an installed rule set — which rule directory won, the exploratory-question footgun, code outside `aidlc-docs/`, the `audit.md` overwrite trap, resume vs restart. Upstream has no equivalent because it does not need one. |

Deliberately not ported: `scripts/aidlc-evaluator/` (the upstream CI evaluation framework),
`docs/ADMINISTRATIVE_GUIDE.md` and `docs/DEVELOPERS_GUIDE.md` (upstream repo operations).

## Staying in sync

```bash
./scripts/check-upstream.sh check          # any upstream change since UPSTREAM_COMMIT?
./scripts/check-upstream.sh mirror-diff    # is references/ still a 1:1 mirror?
./scripts/check-upstream.sh review-prompt  # generates the port-review prompt for an agent
./scripts/check-upstream.sh accept <sha>   # record the reviewed commit (human decision)
```

`check` exits 0 when there is nothing new, 10 when there is. `mirror-diff` exits 0 on a clean mirror
and 10 with a diff — expect exactly one hunk, the A5 note. Syncing means **replacing** the reference
file with the upstream version and reapplying the relevant adaptation; never rewrite, condense, or
translate upstream prose. `UPSTREAM_COMMIT` only advances through `accept`, after human review.
