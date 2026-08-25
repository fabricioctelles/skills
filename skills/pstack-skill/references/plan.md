# Plan

Produce a phased implementation plan grounded in the **Principles** section of this skill. The plan is the deliverable. Do not implement.

Open a todolist with one item per step below.

## 0. Triage

Skip the plan when the change is one or two files with an obvious approach. Say so and stop.

Plan when the change spans three or more files, introduces architecture, has competing approaches or unclear scope, or the user asked for one.

## 1. Re-read principles

Read the **Principles** section of this skill's SKILL.md end to end, plus `references/principles.md` for the full rule of each principle. The principles govern every plan decision; cross-link them.

## 2. Scope and constraints

State your read of scope and constraints in one paragraph. Ask the user only for genuinely ambiguous intent (the [**never-block-on-the-human**](../references/principles.md#never-block-on-the-human) principle); give concrete options with each open question.

Resolve what is in scope vs explicitly out, technical or platform constraints, patterns to preserve, and the definition of done.

## 3. Explore in subagents

Delegate codebase exploration (the [**guard-the-context-window**](../references/principles.md#guard-the-context-window) principle).

- Prefer general-purpose subagents briefed with this skill's principles index.
- 

Each explorer returns file pointers, conventions, dependencies, test infrastructure, and entry points. No inlined dumps.

## 4. Write the plan

The user specifies where the plan lives.

Single file `NN-slug.md` for small plans. For three or more phases, a directory with `overview.md` plus phase files:

```
NN-slug/
├── overview.md
├── phase-1-scaffold.md
├── phase-2-...md
└── testing.md
```

### Phase sizing

- One function or type plus tests, or one bug fix. Not "one file".
- Two to three files touched, max.
- Prefer eight to ten small phases over three to four large ones to preserve option value (the [**foundational-thinking**](../references/principles.md#foundational-thinking) principle).
- Split if a phase has more than five test cases or three functions.

### Overview file

- **Context.** Problem and why now.
- **Scope.** Included; explicitly excluded.
- **Constraints.** Technical, platform, dependency, pattern.
- **Alternatives.** Two or three approaches sketched, choice and rationale (the [**exhaust-the-design-space**](../references/principles.md#exhaust-the-design-space) principle). Skip when constraints dictate one.
- **Applicable skills.** Domain skills the implementer should invoke, by name.
- **Phases.** Ordered standard-markdown links to phase files.
- **Verification.** Project-level commands.
- **Implementation guidance.** Per section 6.

### Phase files

- Back-link to overview.
- **Goal.** What the phase accomplishes.
- **Changes.** Files affected and the change at a high level. What and why, not how. No code snippets.
- **Data structures.** Name the key types or schemas. One-line sketch only (the [**foundational-thinking**](../references/principles.md#foundational-thinking) principle).
- **Verification.** Per section 6.

Order phases so infrastructure and shared types land first (the [**foundational-thinking**](../references/principles.md#foundational-thinking) principle). Each phase should be independently shippable.

For changes touching existing code, apply the [**redesign-from-first-principles**](../references/principles.md#redesign-from-first-principles) principle: if we'd built this with the new requirement on day one, what would it look like? Redesign holistically; deliver incrementally.

If a phase creates or edits a skill, the phase instructs the implementer to follow the Authoring-a-skill playbook.

## 5. Verification per phase

Each phase needs both:

**Static.** Type check, lint, project tests pass.

**Runtime.** Exercise the feature on the matching surface on the real surface:

- Web UIs: drive the running app (browser automation, CDP, or the project's e2e harness).
- CLIs and TUIs: run the binary through a scripted PTY session.
- Services: exercise the real endpoints.
- No scripted way to reach the touched surface: flag it in the plan.

For bug fixes, the loop is reproduce on the surface, fix, verify on the same surface. Unit tests show a branch behaves a certain way; they do not prove the bug is gone (the [**prove-it-works**](../references/principles.md#prove-it-works) principle).

## 6. Implementation guidance

In the overview, name which orchestrator non-negotiables the implementer must apply, by name:

- the **how** skill over each unfamiliar subsystem before changing it.
- the **interrogate** skill for adversarial review on contested designs before shipping.
- strip slop from each diff before commit; apply [**unslop**](skills/unslop.md) to any prose surface.
- the **show-me-your-work** skill to keep a decision trail when the plan is large enough to need an auditable record.
- the **Babysit** playbook after opening the PR.

## 7. Hand back

Summarize phases, scope boundaries, applicable skills, and verification. Stop. The user decides when implementation starts.
