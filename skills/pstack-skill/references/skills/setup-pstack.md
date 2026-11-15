# Setup: model roles and reasoning budget

pstack routes work by role. The skill speaks only role slugs; your environment binds each role to a concrete model through a config file. Resolution order: (1) `.agents/pstack-models.md` in the project, then `~/.agents/pstack-models.md`; (2) inline fallbacks below. On a single-model setup every role resolves to that model and panels degrade to sequential independent passes on fresh context — never skip or weaken a gate because of it.

## The roles

| Slug | Capability contract | Used for |
|---|---|---|
| `worker` | Fast, cheap, reliable instruction-following; mechanical work needing no judgment | Trivial edits, refactoring moves, codebase explorers, swarm workers |
| `builder` | Strongest instruction-following at high complexity, long context | Precisely specified implementation: named data shape, scope, success criteria already settled by the parent (feature, refactoring, bug fix, perf, hillclimb) |
| `judge` | Deepest reasoning plus calibrated epistemics and clear prose | Prose, synthesis, explanation, lead reviews, cross-judging |
| `peer` | Independent reasoner, preferably from a confirmed different family; otherwise a fresh-context pass | Panel diversity, second opinions, red-team lanes |

Prefer a peer from a demonstrably different model family when available. Treat model identifiers as opaque and do not infer family or provider from their spelling. If diversity is unavailable or unknown, use an independent fresh-context pass and report that diversity was not verified.

The five code-delegate playbooks use `builder`. Choose the strongest available instruction-follower for that role. The upstream defaults are not requirements for this portable skill.

## Binding syntax

Store one `role: value` line per role in `.agents/pstack-models.md` or `~/.agents/pstack-models.md`. Values are opaque identifiers accepted by the active harness. Any routing syntax must be supported by that harness and authorized in this session. An optional `# budget:` line records the user's preference. For example, the following placeholders illustrate the shape and are not runnable values:

```text
worker: <available-worker-model>
builder: <available-builder-model>
judge: <available-judge-model>
peer: <available-peer-model>
```

## Setup flow

Run setup only when requested or when resolving a failed binding. Runtime never requires setup.

1. Discover the models and delegation controls actually exposed and authorized in this session. A locally installed CLI or a known model name alone does not establish availability or permission. If discovery is unavailable, inherit the session model rather than guessing.
2. Read existing role bindings and budget. Preserve explicit user choices unless unavailable or the user changes them.
3. Select `builder` for instruction-following, `judge` for reasoning, `worker` for mechanical work, and `peer` for independent review. Prefer confirmed family diversity for `peer` when available. A single model can fill all roles.
4. If a reasoning budget is requested, record it and apply it only through documented controls and supported values exposed by the active harness. Never rewrite or parse model identifiers to infer effort, family, or provider. If no supported control exists, report that the preference could not be applied.
5. Validate bindings against confirmed capabilities. Explicitly configured identifiers that cannot be verified require a user choice during setup; do not silently invent one. Write the configuration only as authorized and report the result.

## Runtime resolution

Resolve each role from the project file first, then the user file. Use a binding only if the active harness supports it and the session permits the action. Otherwise inherit the session model and report the fallback. When delegation is unavailable or prohibited, perform independent passes sequentially in fresh context where possible. Never claim model diversity without evidence. An unavailable binding or effort setting must not block the task or weaken verification.

## Offer verification skills (optional)

After writing the bindings, offer once each, unless the project already has one:

- **Verification skill.** Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work?" On yes, run the **create-verification-skill** procedure.
- **Formal verification skill.** Check whether the project already has a project skill that runs a model checker, a proof, or another verifier against the code. If not, offer: "want a formal verification skill, so agents can prove a key property of your code holds in every case in scope, not only the cases tests reach?" On yes, run the **create-formal-verification-skill** procedure.

On no, move on without pushing.
