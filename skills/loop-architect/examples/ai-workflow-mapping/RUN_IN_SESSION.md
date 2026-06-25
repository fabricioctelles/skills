# Run `ai-workflow-mapping` In This Session

Use this prompt when the user wants to run the Looper-designed loop in the current LLM session.
This is the default/easy execution path. The Python runner is the advanced path for running later or outside the session.

## Operator Instructions

You are executing a Looper-designed loop in this current session.
Follow the resolved spec below, write handoff files into the workspace, and enforce the caps manually.
Do not use `run-loop.py` unless the user explicitly asks for the advanced external runner.

1. Create the workspace directory if it does not exist.
2. Read the context sources before drafting the plan.
3. Draft `plan.md` in the workspace.
4. Run the plan gate. Apply programmatic checks when available. For judge criteria, use the configured judge only after consent for any non-local egress; otherwise ask the user to approve a human/current-session substitute.
5. Revise until the gate passes or `max_revisions` is reached.
6. Produce `delivery-N.md` in the workspace.
7. Run the delivery gate after each delivery.
8. Stop when all delivery criteria pass, a cap is reached, or the user stops the loop.
9. Keep `state.json` current with status, iteration, last gate, consent, and blockers.
10. Append a compact entry to `run-log.md` after every context read, model call, check, gate verdict, revision, blocker, and stop decision.
11. Compare each blocker against the previous blocker. If the same blocker repeats for the configured no-progress window, stop or ask for the configured human checkpoint instead of revising again.
12. Treat token and USD budgets as operator limits in this session: if exact accounting is unavailable, stop and ask before continuing when the loop appears likely to exceed them.

## Files

- Source spec: `loop.yaml`
- Human summary: `LOOP.md`
- Resolved spec: `loop.resolved.json`
- Workspace: `./loop-workspace`
- State file: `state.json`
- Run log: `run-log.md`

## Goal

Produce an agent workflow map that converts the process notes into a stepwise design with tool calls, model responsibilities, and human checkpoints.

## Definition Of Done

A LOOP.md-style workflow map exists, every step has an owner, input, output, and checkpoint decision where needed, and there are no TBDs.

## Context Sources

- Read file `./inputs/process-notes.md`

## Verification Criteria

- `required-sections` programmatic: run `["python", "scripts/check-loop-doc.py", "loop-workspace/delivery-1.md"]` and expect `exit_zero`
- `covers-goal` judge rubric: Every part of the goal statement is addressed. Each workflow step has an owner, required input, output artifact, and human checkpoint where business judgment is needed. No step depends on information the loop never gathers. There are no unresolved TBDs.


## Council

- `reviewer-1` judge via `["claude", "-p"]` (non-local; timeout 600s)

## Gates

### plan_gate

- When: `after_plan`
- Policy: `revise_until_clean`
- Verdict source: `reviewer-1`
- Criteria: `covers-goal`
- Max revisions: `3`

### delivery_gate

- When: `after_each_delivery`
- Policy: `revise_until_clean`
- Verdict source: `reviewer-1`
- Criteria: `required-sections, covers-goal`
- Max revisions: `3`

## Loop Control

- Max iterations: `12`
- Budget: `{"tokens": 2000000, "usd": 5.0, "wall_clock_min": 30}`
- No-progress: `{"action": "stop", "max_stalled_iterations": 2, "signals": ["same blocking issue repeats", "delivery artifact has no material change", "verifier output is unchanged"]}`
- Human checkpoints: `none`
- Stop conditions:
  - all deliveries pass their gate clean
  - max_iterations reached
  - same blocker repeats for 2 iterations
  - any budget cap exceeded

## Execution Boundary

- Mode: `in_session`
- Isolation: `current_workspace`
- Side effects: `{"duplicate_action_check": true, "requires_approval": true}`

If the loop needs scheduled runs, child-agent lifecycle management, concurrency control, or restart-safe step retries, stop and tell the user this Looper spec should be handed to a durable orchestrator.

## Observability

- State file: `state.json`
- Run log: `run-log.md`
- Checkpoint granularity: `gate`

Use `state.json` for the latest resumable status and `run-log.md` for the append-only history of what happened.

## Privacy

- Before sending `plan, deliveries` to `reviewer-1`, confirm consent and apply redactions `.env, .env.*, secrets/**, **/*.key`.

## Start Now

If the user asked to run now, begin at step 1 under Operator Instructions and keep going until a stop condition is reached.
