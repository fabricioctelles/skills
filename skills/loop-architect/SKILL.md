---
name: loop-architect
description: >
  Design well-structured agent loops with best-practice coaching and cross-model
  review gates before you run them. Use when the user wants to design, build, or
  set up an agent loop, iterative agent workflow, self-review loop, LLM-as-judge
  loop, multi-model council, reviewer/judge gate, or goal-driven looping process.
  Guides goal refinement, typed verification criteria, reviewer/judge selection,
  privacy boundaries, termination guards, and observability, then emits a
  RUN_IN_SESSION.md handoff prompt plus portable loop.yaml, loop.resolved.json,
  LOOP.md, and run-loop.py.
metadata:
  author: https://ft.ia.br
  version: "1.0"
  date: 2026-06-25
  repository: https://github.com/fabriciotelles/skills
  license: MIT
  original_project: https://github.com/ksimback/looper
  original_author: Kevin Simback (@ksimback)
  attribution: >
    Reinterpretation of Looper (MIT License) by Kevin Simback, adapted for
    Kiro CLI with native /goal, subagent, and review loop integration.
---

# Loop Architect

A loop design coach for Kiro CLI. Interviews you, critiques your design against
built-in best-practice rubrics, wires in cross-model reviewers or judges, shows
the loop as an ASCII flow preview, and writes portable artifacts you can run
immediately with `/goal` or later with the Python runner.

> Based on [Looper](https://github.com/ksimback/looper) by Kevin Simback, MIT License.
> Adapted for Kiro CLI by ft.ia.br.

## Why This Exists

Kiro CLI ships `/goal` (autonomous loop with self-verification) and subagents
(parallel pipelines with review loops). These **execute** a loop. Loop Architect
helps you **design** one worth executing — with a coached goal, typed
verification, a cross-model gate, and explicit termination guards.

| | `/goal` | Subagent pipeline | **Loop Architect** |
|---|---|---|---|
| Layer | execution | execution | **design (pre-flight)** |
| Coaches your goal | no | no | **yes** |
| Typed verification | no | no | **yes (programmatic / judge / human)** |
| Reviewer model | same model | configurable | **different model, by default** |
| Portable artifact | no | no | **loop.yaml + resolved spec** |
| Runs the loop | **yes** | **yes** | **yes, via handoff** |

## Workflow

1. Resolve the target path from the user. Default: `./loop-architect-output`. If
   the target contains an existing `loop.yaml`, treat as edit/resume.

2. Load the relevant rubric only when entering that stage:
   - Goal stage: `references/goal-rubric.md`
   - Verification stage: `references/verification-rubric.md`
   - Council stage: `references/council-rubric.md`
   - Control stage: `references/control-rubric.md`
   - Model detection: `references/model-detection.md`

3. Interview in seven stages: goal, verification, host model, council,
   gates/control, confirmation flow preview, emit/run option. In the control
   stage, cover execution boundary, isolation, no-progress signals, state, and
   run logging.

4. Critique each stage before accepting it. Prefer concrete alternatives over
   vague warnings. Push weak goals toward outcome, scope, context, and done
   state. Push weak verification toward programmatic checks first, then judge
   rubrics, then human signoff.

5. Keep reviewer and judge roles distinct. A reviewer writes notes. A judge
   returns a structured verdict. `revise_until_clean` must name a judge member
   or `human` as `verdict_source`.

6. Require multiple termination guards: `max_iterations`, a revision cap on
   each gate, a no-progress stop, and either a budget cap or an explicit human
   stop point.

7. Before any cross-vendor council member is selected, state what context will
   leave the user's machine, which CLI receives it, which redaction globs apply,
   and that both execution paths require first-send consent.

8. Show an ASCII flow preview and ask for confirmation before final emission.

9. Emit these files into the target:
   - `loop.yaml`
   - `loop.resolved.json`
   - `LOOP.md`
   - `RUN_IN_SESSION.md`
   - `run-loop.py`
   - `loop-workspace/`
   - `README.md`

10. After writing `loop.yaml`, compile it:
    ```bash
    python3 ~/.kiro/skills/loop-architect/scripts/looper.py compile \
      <target>/loop.yaml \
      --out <target>/loop.resolved.json \
      --render <target>/LOOP.md \
      --session-prompt <target>/RUN_IN_SESSION.md
    ```

11. Ask whether the user wants to run the loop now. If yes:
    - **Easy path**: Follow `RUN_IN_SESSION.md` directly, or suggest a `/goal`
      one-liner derived from the `definition_of_done`.
    - **Subagent path**: If the council uses a model with `review_loop`
      capability, offer to execute via a subagent pipeline with native review
      loops.
    - **External path**: Explain that `run-loop.py` is available for running
      later or outside the session.

## Execution Paths

### Path 1: `/goal` (simplest)

When the loop is straightforward and the host is the current Kiro session:

```
/goal --max 12 <definition_of_done from loop.yaml>
```

This uses Kiro's native self-verification loop. No cross-model review, but
fast and zero-config.

### Path 2: Subagent review pipeline (recommended)

When a cross-model reviewer is needed and the host has `subagent` capability:

```
Implement the loop following RUN_IN_SESSION.md. Use a subagent as reviewer
with trigger "NEEDS_CHANGES" and max 3 iterations per gate.
```

This leverages Kiro's native `loop_to` mechanism for the plan and delivery
gates.

### Path 3: External Python runner (advanced)

```bash
python3 ./loop-architect-output/run-loop.py
```

For scheduled runs, CI integration, or when you need strict budget enforcement.

## File Rules

- Write argv arrays, never shell command strings, for all model invocations.
- Do not write API keys, tokens, or credentials into any emitted file.
- Default redaction globs: `.env`, `.env.*`, `secrets/**`, `**/*.key`.
- Keep `loop.yaml` human-readable and commented.
- Keep `RUN_IN_SESSION.md` as the default/easy execution handoff.
- Copy `templates/run-loop.py` exactly unless the user asks to edit it.

## Helper Scripts

Detect model CLIs:
```bash
python3 ~/.kiro/skills/loop-architect/scripts/looper.py detect-models --write
```

Register a custom CLI:
```bash
python3 ~/.kiro/skills/loop-architect/scripts/looper.py register-model <id> \
  --invoke kiro-cli chat --trust-all-tools -p --authed
```

Compile and render:
```bash
python3 ~/.kiro/skills/loop-architect/scripts/looper.py compile <target>/loop.yaml \
  --out <target>/loop.resolved.json \
  --render <target>/LOOP.md \
  --session-prompt <target>/RUN_IN_SESSION.md
```

## Confirmation Flow Preview

```text
+--------------------------------+
| 1. Goal + context              |
|    read sources                |
+--------------------------------+
              |
              v
+--------------------------------+
| 2. Draft plan.md               |
|    state -> state.json         |
+--------------------------------+
              |
              v
+--------------------------------+
| 3. Plan gate                   |
|    verdict: reviewer-1         |
+--------------------------------+
  | needs work -> revise <= 3 -> step 2
  | pass
              v
+--------------------------------+
| 4. Write delivery-N.md         |
|    log -> run-log.md           |
+--------------------------------+
              |
              v
+--------------------------------+
| 5. Delivery gate               |
|    verdict: reviewer-1         |
+--------------------------------+
  | needs work -> revise <= 3 -> step 4
  | pass
              v
+--------------------------------+
| 6. Final output                |
|    all gates clean             |
+--------------------------------+

Stops: pass gates | max 12 iterations | no progress x2 | budget 30m, $5.0
```

## Emit Checklist

- The goal has a clear outcome, scope boundary, context sources, and done state.
- Verification criteria are typed as `programmatic`, `judge`, or `human`.
- At least one criterion is not purely vibe-based.
- Each `revise_until_clean` gate has a valid `verdict_source`.
- Every external invocation is an argv array with a timeout.
- Cross-vendor egress is scoped, redacted, and consent-gated.
- `loop_control` has iteration, revision, no-progress, and budget caps.
- Execution boundary and isolation are explicit.
- Observability names a `run-log.md` and `state.json` path.
- Compiled artifacts (`loop.resolved.json`, `LOOP.md`, `RUN_IN_SESSION.md`)
  pass validation before handoff.
