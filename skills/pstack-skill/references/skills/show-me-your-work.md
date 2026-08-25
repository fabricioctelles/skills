# Show me your work

For work a human reviews after the fact, a decision trail lets them reconstruct what was decided, why, on what evidence, without rerunning the work or reading the transcript. One canonical TSV log.

## The format

Header row: `ts<TAB>phase<TAB>decision<TAB>why<TAB>evidence<TAB>result`. One row per decision or checkpoint. Cells stay single-line; evidence is a pointer (commit SHA, PR number, `file:line`, artifact path), never prose.

Start a clean log with `scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <result>` (relative to this skill's root). It stamps `ts`, writes the header on first use, strips tabs and newlines, and neutralizes leading `=`, `+`, `-`, `@` so opening the log in a spreadsheet cannot trigger formula execution from attacker-controlled cells.

Write each entry the way you would tell a teammate: plain words, concrete actions, no AI speak ([unslop](unslop.md) applies to log text).

Log decision points and checkpoints, not every action: a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker surfaced, a gate fixed. For loop runs, one row per iteration. Skip the trivial and self-evident.

## Where it lives

Default: a working artifact, not committed. Keep it at `decisions.tsv` in the work dir, or `.audit/<task-slug>.tsv` when several efforts run at once, gitignored. Commit it only when the work is ambitious enough that a reviewer needs the trail to trust the result: large ports, multi-week migrations, anything where confidence must be shown rather than assumed. A committed log renders as a table in the PR.

## Rules

- One row is one decision. If it does not fit one line, the decision is not crisp yet.
- Append-only. A wrong call gets a new superseding row. Never edit or delete history.
- Prefer evidence produced by committed scripts over hand-made one-offs, so a reviewer can re-run it ([encode-lessons-in-structure](../principles.md#encode-lessons-in-structure)).

## Audit the log against the run

Before handing back: every row maps to a real action; each evidence pointer resolves and shows what the row claims; forks, pivots, and abandoned approaches that shaped the work are logged; padding dropped. Fix the log, not the story.

## Cross-model review of the trail

Spawn a reviewer on a different model family than the one that did the work (an independent fresh-context pass when only one model exists). It reads the trail and flags: decisions with weak or absent evidence, verification claimed without proof, choices risky in hindsight, gaps a casual skim would miss. Every reply for a run that produced a trail ends with an "Attention" section led by `reviewed by <model>` and listing flags by row. "No flags" is valid; omitting the section is not.
