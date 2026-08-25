# Setup: model roles

pstack routes work by role. The skill speaks only role slugs; your environment binds each role to a concrete model through a config file. Resolution order: (1) `.agents/pstack-models.md` in the project, then `~/.agents/pstack-models.md`; (2) inline fallbacks below. On a single-model setup every role resolves to that model and panels degrade to sequential independent passes on fresh context — never skip or weaken a gate because of it.

## The roles

| Slug | Capability contract | Used for |
|---|---|---|
| `worker` | Fast, cheap, reliable instruction-following; mechanical work needing no judgment | Trivial edits, refactoring moves, codebase explorers, swarm workers |
| `builder` | Strongest instruction-following at high complexity, long context | Precisely specified implementation: named data shape, scope, success criteria already settled by the parent |
| `judge` | Deepest reasoning plus calibrated epistemics and clear prose | Prose, synthesis, explanation, lead reviews, cross-judging |
| `peer` | Strong reasoner from a **different family** than `judge`; when only one family exists, a fresh-context pass instead | Panel diversity, second opinions, red-team lanes |

The `peer` constraint is family diversity, not depth: agreement across families is high signal, agreement within one family is not. A slug never encodes a vendor.

## Binding syntax

One line per role. The value is whatever string your harness needs to spawn that model; a `prefix:` names an alternative CLI/harness. Comments carry the contract for future readers.

```
# pstack role bindings. One line per role. Delete a line to fall back to defaults.
worker:  grok-4-fast
builder: codex:gpt-5.6-high      # spawns via Codex CLI
judge:   claude:opus-5-thinking
peer:    gemini:3.1-pro          # family must differ from judge
```

## Setup flow (explicit, interactive)

Run this when the user asks to configure pstack models, or when a spawn fails because a binding points at nothing runnable. Setup is the one place pstack talks to the human about configuration; **runtime never does**: with no config file and no detection, every role falls back and work proceeds.

1. **Detect first.** Enumerate the models this session can actually spawn (your platform's model list, CLI sign-ins such as `codex` / `gemini` / `grok`, or prior successful spawns). Never write a binding you have not confirmed runnable.
2. **Propose bindings.** Fill the four roles from detection: `builder` gets your strongest instruction-follower, `judge` your deepest reasoner, `peer` the strongest model from a different family than `judge`, `worker` the fastest cheap model. Show the table.
3. **Ask before writing.** One structured question with concrete options, never free text first: accept as proposed / edit specific roles (offer detected models per role) / paste slugs for anything undetected. If detection found nothing usable, ask the user to paste what they have. Single-model setup: skip the questions, state the collapse plainly, write nothing unless the user wants the file anyway.
4. **Validate.** Every real slug in the file must be in the confirmed-runnable set. A bad binding silently breaks every delegation downstream, so stop and re-ask instead of writing a guess. Harness prefixes (`codex:`, `claude:`) validate against the named tool's own model list.
5. **Write and confirm.** Overwrite the whole file so re-runs stay idempotent. Tell the user which file was written and that new sessions pick it up.

## Runtime resolution

When a playbook says "spawn a subagent using the builder role": read the config files in order, take the first hit, and spawn through whatever harness the prefix names (no prefix = this session's native subagent mechanism). No hit anywhere: use the best model available to you now and keep going. If a spawn errors because the bound model is unresolvable, fall back once to the inline default, note it in the reply, and suggest a setup pass at the end of the task.
