# Control Rubric

Use this when setting gates, iteration caps, budgets, and stop conditions.

## Required Guards

- `loop_control.max_iterations`
- `gates.*.max_revisions`
- `loop_control.no_progress.max_stalled_iterations`
- At least one wall-clock, token, or USD budget cap when external models run.
  The generated Python runner enforces wall-clock caps directly; token and USD
  caps are advisory unless the chosen model CLI exposes accounting that the
  loop operator wires in separately.
- A stop condition that describes success.
- A stop condition that describes no-progress or repeated failure.

## Good Gate Design

- Plan gate runs before delivery work.
- Delivery gate runs after each delivery artifact.
- Programmatic checks run before judge calls when possible.
- Human checkpoints sit at high-leverage points, usually after plan approval or
  before external egress.
- Resume happens at gate boundaries unless the user explicitly needs finer
  granularity.

## Execution Boundary

- Name where the loop is allowed to modify files: current workspace, branch,
  worktree, throwaway directory, or an external orchestrator workspace.
- Identify actions with side effects: pushes, PR comments, Slack messages,
  deploys, file deletes, database writes, or vendor sends.
- Decide whether side-effecting actions require approval, idempotency notes, or
  duplicate-action checks.
- If the loop may run on a schedule or in parallel, call out the need for an
  external orchestrator with concurrency controls.

## Failure Behavior

- Stop immediately when a hard cap is reached.
- Write the latest state to `loop-workspace/state.json`.
- Append each meaningful step, decision, check result, and blocker to
  `loop-workspace/run-log.md`.
- Preserve review notes even when the gate fails.
- Stop or ask the human when the same blocker repeats for the configured
  no-progress window.
- Do not let the host keep revising forever.

## Anti-Patterns

- No maximum iteration count.
- A judge gate with no judge.
- A budget cap in prose but not in `loop_control`.
- No no-progress detector.
- A loop that can send duplicate external notifications or repeat destructive
  actions after restart.
- Scheduled or multi-agent work with no durable orchestrator or concurrency
  story.
- Human signoff required but no checkpoint.
- Stop conditions that require subjective self-satisfaction.
