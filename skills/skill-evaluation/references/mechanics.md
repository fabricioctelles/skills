# Mechanics: Predictability, Invocation, Hierarchy, Steering, Failure Modes

Reference for scoring Axes 1, 3, and 4 of the skill-evaluation rubric — a
deliberately self-contained condensation of Matt Pocock's `writing-great-skills`
GLOSSARY, kept in-skill so the evaluator runs anywhere without that skill
installed (sync manually if the upstream GLOSSARY changes). Not a tutorial:
look a bolded term up here rather than re-deriving it.

## 1. Root virtue: Predictability

A skill exists to wrangle determinism out of a stochastic system.
**Predictability** is the agent taking the same *process* every run, not
producing the same output — a brainstorming skill should predictably diverge;
its tokens vary, its behavior doesn't. Every criterion in the rubric is a lever
on this one virtue: conciseness, steering, and pruning are symptoms of
predictability, not separate virtues competing with it.

## 2. Invocation trade-off

Two invocation modes, each paying a different cost:

- **Model-invoked** (default; no `disable-model-invocation`): keeps a
  description the agent reads every turn. Pays permanent **context load** —
  tokens and attention spent on every turn — in exchange for autonomous
  firing and reachability by other skills.
- **User-invoked** (`disable-model-invocation: true`): the description is
  stripped from the agent's reach; only a human typing the skill's name can
  fire it, and no other skill can reach it either. Zero context load, but
  spends **cognitive load** — the human becomes the index of which skills
  exist and when to reach for each.

Pick model-invocation only when the agent must reach the skill on its own, or
another skill must reach it. A skill that only ever fires by hand should be
user-invoked and carry no trigger scaffolding it doesn't need. When
user-invoked skills multiply past what a human can remember, a **router
skill** — one user-invoked skill naming the others and when to reach for each
— cures the accumulated cognitive load. That fix operates at the portfolio
level, not the single-skill level this evaluation scores.

## 3. Content types & hierarchy

A skill mixes two content types freely: **steps** (ordered actions, each
ending on a **completion criterion**) and **reference** (definitions, rules,
facts consulted on demand). All-steps, all-reference, and mixed skills are
equally valid — neither shape is a smell.

The **information hierarchy** ranks material by how immediately the agent
needs it: in-skill step, then in-skill reference, then reference disclosed
behind a **context pointer** in a linked file. Material every **branch** (a
distinct way the skill is invoked) needs belongs inline; material only some
branches need belongs behind a pointer — branching is the disclosure test. A
pointer's *wording*, not its target, decides whether the agent reaches it and
how reliably; a must-have target behind weak wording is a variance bug, and
the fix is sharper wording, tried before pulling the material back inline.

**Co-location** governs what sits beside a piece of content once placed: a
concept's definition, rules, and caveats belong under one heading, not
scattered, so reading one part brings its neighbors with it.

## 4. Steering

**Leading words** are compact, pretrained concepts (*tight*, *red*, *lesson*)
the agent thinks with while executing. Repeated consistently, they recruit
priors the model already holds and anchor a region of behavior in the fewest
tokens — cheaper and stickier than spelling the same quality out in prose. A
leading word works twice: in the body it anchors execution (the same behavior
fires every time the word appears); in the description it anchors invocation.
It is also **trace-checkable** — distinctive enough that its appearance in the
agent's reasoning traces confirms the skill actually shaped behavior.

A completion criterion must be *checkable* (can the agent tell done from
not-done?) and, where it matters, *exhaustive* ("every X accounted for", not
"produce a list"). A vague criterion invites **premature completion** —
attention slipping to being done rather than to the work. The exhaustiveness
demand also binds flat reference with no steps: "every rule applied" drives
thorough **legwork** over a checklist the same way a sharp step criterion
drives it over an action.

Skills should **avoid railroading**: procedures the agent adapts, not
declarations of exact output; defaults with brief alternatives, not
exhaustive menus.

## 5. Failure modes

- **Premature completion** — ending a step before it's genuinely done.
  Defense, in order: sharpen the completion criterion first (cheap, local);
  only if it's irreducibly vague *and* the rush is actually observed, split
  the sequence so later steps are hidden.
- **Duplication** — the same meaning in more than one place. Costs
  maintenance and tokens, and inflates that meaning's rank past its real
  weight. Fix: collapse to a **single source of truth**, often via a leading
  word.
- **Sediment** — stale layers that accumulate because adding feels safe and
  removing feels risky. The default fate of any skill without a pruning
  discipline.
- **Sprawl** — a skill simply too long, independent of whether lines are
  stale or duplicated. Cure: disclose reference behind pointers, split by
  branch or sequence so each path carries only what it needs.
- **No-op** — a line that changes nothing because the model already does it
  by default. The test: does it change behavior versus the default? Apply
  the **deletion test** sentence by sentence, not paragraph by paragraph — if
  removing the sentence leaves behavior unchanged, delete the whole sentence,
  don't trim words from it. A weak leading word (*be thorough* when the agent
  is already thorough-ish) is a no-op; the fix is a stronger word
  (*relentless*), not a different technique.
- **Weak steering** — an instruction is present but the agent doesn't
  reliably follow it. Usually a leading word too weak to beat the default, or
  no leading word at all where a verbose passage is trying to do its job.

**Relevance vs. no-op**: relevance asks whether a line still bears on the
task; no-op asks whether it changes behavior. A line can be relevant (right
topic) and still be a no-op (the model would do it anyway) — run both checks,
they don't imply each other.
