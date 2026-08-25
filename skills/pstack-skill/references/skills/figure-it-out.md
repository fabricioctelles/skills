# Figure it out

No bundled playbook fits? Design one. The deliverable before any code is the workflow itself: phases that scale rigor to the task, run the scientific method, and leave an auditable decision trail. Bias toward more rigor; building the wrong thing costs more than being careful.

Do not reinvent a playbook you have. A focused single-unit task matching Bug fix, Perf, Feature, Visual parity, or Eval routes there. A large or cross-cutting version of one (a migration across many call sites), or work reviewed after stepping away, belongs here even though a single-unit version would be a Feature.

Open a todolist whose first item is reading this skill's Principles index in full, then add the phases below.

## Phase A: Frame

Ground first, then commit. State:

- The definition of done as a falsifiable predicate ([prove-it-works](../principles.md#prove-it-works)).
- Scope quantified: rough units, effort, blockers grounding surfaced. Raise blockers before spending hours, not after fifty doomed commits.
- The rigor level, biased high. One-way doors and high blast radius get more gates and artifacts; reversible low-stakes steps get less.

Present framing and tradeoffs before committing to a long run. Reversible work proceeds ([never-block-on-the-human](../principles.md#never-block-on-the-human)), but a multi-hour run earns one checkpoint.

## Phase B: Design the workflow

Decompose into atomic independently-landable units. Sequence riskiest-unknown-first so option value stays high. Scaffold and verification before features ([foundational-thinking](../principles.md#foundational-thinking)).

- Build the verification harness before the work, baseline captured from pre-change state, so checks read old-value vs new-value.
- For one-way-door design decisions, run the architect procedure with diverse candidates and an independent judge. Skip it for mechanical work whose shape is already concrete; a second arena over a settled design is over-engineering ([laziness-protocol](../principles.md#laziness-protocol)).
- Decide what fans out. Parallelize only across genuine seams; one worker per worktree or branch ([separate-before-serializing-shared-state](../principles.md#separate-before-serializing-shared-state)). Do not over-fan.
- Write the designed phase list down; that list is what the human reviews. Add its steps to the todolist and weave Phase D logging through them as each lands.

## Phase C: Run the loop

Each unit is an experiment: hypothesis, smallest change, measure against the predicate on the real artifact, keep if it advanced, revert if it did not. Verify each unit before starting the next instead of batching checks at the end ([sequence-verifiable-units](../principles.md#sequence-verifiable-units)).

Verify by inspecting artifacts, never self-reports. A check that passes too easily means suspect the observation method before the system; a blank screenshot passes a lazy gate. If a worker games the gate, reset and harden the contract; if the gate itself is wrong, fix the gate in its own change rather than routing around it. Verdicts are VERIFIED, NOT VERIFIED, or INCONCLUSIVE; inconclusive is not a pass.

## Phase D: Keep the audit trail

Log via [show-me-your-work](show-me-your-work.md): one canonical TSV, a row per decision and per unit, evidence as links. This procedure's work usually merits committing the trail so the reviewer reads it in the PR. Prefer evidence from committed scripts a reviewer can re-run.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Encode any recurring correction as a gate, lint rule, check, or script so the win cannot silently regress ([encode-lessons-in-structure](../principles.md#encode-lessons-in-structure)).

**Reply:** the playbook you designed, rigor level and why, trail path, what is verified against the predicate, what remains open.
