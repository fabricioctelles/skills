# 👑 pstack-skill

> Lauren Tan's rigorous engineering workflow — `poteto-mode` and the whole pstack stack — as **one self-contained skill**. No plugin marketplace, no Cursor required, no vendor lock-in. Drop the folder in any agent that reads skills.sh-format skills.

Ported from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by [Lauren Tan (@poteto)](https://x.com/poteto), informed by [open-pstack](https://github.com/ericlitman/open-pstack). MIT-licensed; all credit for the method is hers.

---

## The idea

There is a growing sense that AI writes too much slop code. Throughput without quality is not a goal. **If you want to go fast, go deep first.**

This skill turns a coding agent into a disciplined engineering team. It is not a model or a hosted service — it gives your agent engineering rules, step-by-step workflows, focused procedures, and small local tools. Give it a task in plain language and it will:

- read the task and pick the workflow that fits (one of 23 playbooks);
- learn how the current system works before changing it (`how` / `why`);
- compare competing designs before committing when the choice matters (`architect` / `arena`);
- favor the smallest change that solves the problem;
- have several models try to break important decisions before shipping (`interrogate` / `peer`);
- run the code and check real behavior instead of stopping at "the tests pass";
- carry work through review, CI, and a ready-to-merge PR when asked (`babysit` / `shipping`).

The skill is **sticky**: once invoked it stays on across turns, applying itself when rigor is needed and staying out of the way otherwise. Opt out any time by saying so.

## Plugin vs this skill

| | pstack plugin | pstack-skill |
|---|---|---|
| Install | `/add-plugin pstack`, marketplaces | one folder, any agent |
| Platform | Cursor only | Claude Code, Codex, Cursor, opencode, Kiro, anything reading SKILL.md |
| Models | vendor slugs (`grok-4.6-fast-xhigh`, ...) | roles bound to whatever you have: `worker`, `builder`, `judge`, `peer` |
| Stacks & merges | Graphite cloud agents | plain git + `gh`, subagents in isolated worktrees |
| Multi-model panels | native cloud fan-out | same gates, sequential fresh-context passes when only one model exists |

Nothing essential was removed — Cursor-specific mechanics were translated to platform-agnostic equivalents while preserving the operating method.

## Install

Via [skills.sh](https://skills.sh):

```bash
npx skills add https://github.com/fabricioctelles/skills -s pstack-skill
```

Or manually, copy the folder into your agent's skills directory:

```bash
cp -r skills/pstack-skill .claude/skills/    # or .cursor/skills/, .kiro/skills/, ~/.agents/skills/...
```

## Get started

Two steps, like upstream:

**1. Configure models (optional, once).** Ask your agent:

> Use pstack-skill's setup procedure to configure model roles.

It detects what you can actually run, proposes bindings for the four roles, asks before writing `.agents/pstack-models.md`, and validates every slug against what is runnable. Skip it and everything falls back to your single best model, gracefully.

**2. Start tasks that need rigor with the skill invoked.**

```text
Claude Code / opencode:   /pstack-skill fix the scroll drift on this PR, repro first
Codex / Cursor / Kiro:    Use pstack-skill. Add saved filters to search. Keep it
                          simple, verify in the real app, open a PR.
```

That is the main workflow. The other procedures fire as the playbook needs them, or can be called directly ("run interrogate on this diff").

## Use cases

Every playbook is a file under `playbooks/`; the agent copies its steps verbatim onto a todolist. Where to point it:

### Understand before touching

> /pstack-skill how does the rate limiter work? do we have an n+1?

Investigation, `how`, `why`, `recall` (rebuild recent context), `teach`, `blast-radius` (what could this small change break).

### Build features the right way

> Use pstack-skill: build saved filters behind a flag. Name the data shape first, verify in the real app.

Feature, Prototype (settle design forks by building throwaways, not asking), Refactoring (behavior pinned by characterization tests), Visual parity (pixel-diff driven), Multi-phase plan.

### Fix things scientifically

> /pstack-skill this list takes seconds to load even virtualized. trace it, don't guess.

Bug fix (repro → binary-search root cause → failing-test-first fix), Perf issue (baseline trace, eight strategy families, measured delta), Hillclimb (sustained metric improvement, one hypothesis per iteration, keep-or-revert), Runtime/Trace forensics (leaks, spins, cpuprofiles — diagnosis as deliverable).

### Ship and maintain PRs

> pstack-skill, check on PR 123 — anything outstanding? then land the stack if green.

Babysit (drive PRs to merge-ready: conflicts, threads, flaky CI), Shipping (verify each PR independently, land only the contiguous verified run), Autopilot-full / Autopilot-stack (queues of PRs with one owner each, root swarm-verifies every merge head), Opening a PR (conventional commits, evidence-bearing descriptions).

### Run long, unattended, auditable

> /pstack-skill i'm going to bed. drive the migration until done, leave a trail i can audit at breakfast.

Autonomous run (exit predicate, wake mechanisms, checkpoints), Orchestrate (multi-day programs: briefs, rolling windows, verification ledgers, merge frontiers), Session pickup / Pause safely (resume or suspend cleanly), show-me-your-work (append-only TSV decision trail with cross-review).

### Quality gates

> run interrogate on this diff before we ship it.

Interrogate (adversarial multi-model review with lead judgment), Arena (N candidates, pick base, graft best), Swarm (parallel coverage/races), unslop + technical-writing + no-comments (prose and diff hygiene), TDD (failing test first when cheap).

### Agent tooling

Authoring-a-skill, Eval (blind candidate testing), figure-it-out (designs a bespoke rigorous playbook when none fits), create/maintain verification skill (a scripted way to prove real app behavior, any platform), Worktree cleanup (disk reclaim, safety-gated).

## Model roles

Delegations never name vendors. Four role slugs, each with a capability contract, bound once via config:

| Role | Contract | Typical work |
|---|---|---|
| `worker` | fast, cheap instruction-following | mechanical edits, explorers, swarm workers |
| `builder` | strongest instruction-follower, long context | specified implementation |
| `judge` | deepest reasoning, calibrated prose | synthesis, reviews, cross-judging |
| `peer` | strong reasoner from a **different family** than judge | panel diversity, second opinions |

Bindings live in `.agents/pstack-models.md` (project) or `~/.agents/pstack-models.md` (user):

```
worker:  grok-4-fast
builder: codex:gpt-5.6-high      # prefix = alternative CLI/harness
judge:   claude:opus-5-thinking
peer:    gemini:3.1-pro          # family must differ from judge
```

One model available? All four collapse to it and panels become sequential independent passes on fresh context. Gates are downgraded in execution, never skipped.

## The principles

Twenty-one short rules the orchestrator indexes and cites by name. Full text in `references/principles.md`.

**Core:** laziness protocol · foundational thinking · redesign from first principles · subtract before you add · minimize reader load · outcome-oriented execution · experience first · exhaust the design space · build the lever.
**Architecture:** model the domain · boundary discipline · type system discipline · make operations idempotent · migrate callers then delete legacy APIs · separate before serializing shared state.
**Verification:** prove it works · fix root causes · sequence work into verifiable units.
**Delegation:** guard the context window · never block on the human.
**Meta:** encode lessons in structure.

## Layout

```
pstack-skill/
├── SKILL.md                  ← the orchestrator (agent entry point)
├── playbooks/                ← 23 workflows, steps copied verbatim onto todolists
├── references/
│   ├── principles.md         ← full text of the 21 principles
│   ├── plan.md               ← multi-phase planning reference
│   ├── bugbot-triage.md      ← skeptical triage of bot-review comments
│   └── skills/               ← 21 bundled procedures (how, arena, unslop...)
└── scripts/
    ├── log.sh                ← decision-log helper (TSV, formula-safe)
    └── worktree-audit.sh     ← disk reclaim audit
```

## License

MIT, like upstream. pstack was created by [Lauren Tan](https://x.com/poteto); this adaptation translates Cursor-specific mechanics (plugins, cloud agents, Graphite, `/loop`) to platform-agnostic equivalents and repackages everything as one portable skill.
