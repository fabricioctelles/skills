# Swarm

Fan out N parallel workers, drain them, return one report. Workers may cover separate slices, race the same brief, or mix both. Use for coverage matrices, races, gauntlets, and exploration partitions.

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape: partition into disjoint slices, race N workers on identical briefs, or mix. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive from the shape. N is total workers, not a concurrency limit.
4. Pick worker models up front; name each arm's model in a race.
5. Give each worker its own writable output when it writes: its own worktree, branch, or `/tmp/swarm-<slug>/worker-<n>/`.

## Phase B: Fan out

Spawn all N workers in one message, background. Every brief stands alone: goal, scope, exact slice or race arm, how to verify, what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence.

A worker that drops out: proceed with N-1 and note it.

## Phase C: Aggregate

For coverage, every required slice needs a result. For a race, apply the selection rule declared in Phase A. Never paste raw worker dumps: keep a compact result table, one-line evidenced issues, explicit gaps and dropouts.

## Phase D: Report

One consolidated report: the table, issue one-liners, gaps or dropouts, and the race rule when used.
