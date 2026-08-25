# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end, pick the strongest as base, graft the best ideas from the losers into it, verify the synthesis. Use when one attempt at a non-trivial artifact would lock in the wrong shape.

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The candidates receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate produces.
2. Derive the rubric: 3-6 concrete gradeable criteria. "Adds a --dry-run flag that skips writes", not "code is correct". Candidates see only the task; the rubric is the picker's tool.
3. Pick the runners. Different models when available (diversity is signal); more runners when the arena covers multiple design directions; same model N times when work is generation-bound rather than judgment-sensitive.
4. Assign output paths. Each candidate writes to its own location (a git worktree where possible, otherwise `/tmp/arena-<slug>/candidate-<n>/`). Shared output paths are shared mutable state and fail [separate-before-serializing-shared-state](../principles.md#separate-before-serializing-shared-state).

## Phase B: Fan out

Spawn all N subagents in one message, background, each with the task, the shared grounding path, its own output path. Each returns both the artifact and a short rationale naming alternatives considered and rejected. Without rationales you cannot tell principled structure from accident, which breaks grafting.

A candidate that fails to produce output: proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all candidates complete, spawn one read-only judge on a model different from the parent's family when possible. It sees rubric plus candidates by sanitized path label, scores each criterion, recommends a base with rationale. Launch it after candidates finish writing; a judge spawned early reads partial outputs and reports them as dropouts. It runs in parallel with your own reading in Phase D.

## Phase D: Pick a base

Read every candidate end to end before picking; skimming surfaces only the most familiar-looking surface. Score criterion by criterion against the rubric, not holistic feel. Compare with the cross-judge: agreement confirms, disagreement means bias or an ambiguous rubric, so read both rationales.

Pick the base a future maintainer can extend most easily without breaking invariants. When tied, prefer the cleaner boundary or smaller surface ([laziness-protocol](../principles.md#laziness-protocol)). Record pick and reason in a short synthesis note beside the artifact, including the judge's verdict.

## Phase E: Graft

Walk each loser once for what is worth porting; usually one or two things per candidate. Fold grafts in by hand under one mental model, never pasted mechanically ([redesign-from-first-principles](../principles.md#redesign-from-first-principles)). Record what was grafted from which candidate and what was rejected and why; the rejections are the highest-signal part of the record.

N candidates converging on one shape is strong agreement: note it and ship the consensus shape. Wild divergence means Phase A was under-specified; reframe and re-run rather than averaging.

## Phase F: Verify

The synthesized artifact faces the same bar as any other output ([prove-it-works](../principles.md#prove-it-works)). A problem verification surfaces that the arena missed means either Phase A was wrong (re-frame) or a candidate caught it and you missed the graft (return to Phase E). Do not paper over.

**Output:** one synthesized artifact plus a synthesis note naming base, grafts with sources, rejections, dropouts, verification result.
