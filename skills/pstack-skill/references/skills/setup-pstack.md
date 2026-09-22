# Setup: model roles and reasoning budget

pstack routes work by role. The skill speaks only role slugs; your environment binds each role to a concrete model through a config file. Resolution order: (1) `.agents/pstack-models.md` in the project, then `~/.agents/pstack-models.md`; (2) inline fallbacks below. On a single-model setup every role resolves to that model and panels degrade to sequential independent passes on fresh context — never skip or weaken a gate because of it.

## The roles

| Slug | Capability contract | Used for |
|---|---|---|
| `worker` | Fast, cheap, reliable instruction-following; mechanical work needing no judgment | Trivial edits, refactoring moves, codebase explorers, swarm workers |
| `builder` | Strongest instruction-following at high complexity, long context | Precisely specified implementation: named data shape, scope, success criteria already settled by the parent (feature, refactoring, bug fix, perf, hillclimb) |
| `judge` | Deepest reasoning plus calibrated epistemics and clear prose | Prose, synthesis, explanation, lead reviews, cross-judging |
| `peer` | Strong reasoner from a **different family** than `judge`; when only one family exists, a fresh-context pass instead | Panel diversity, second opinions, red-team lanes |

The `peer` constraint is family diversity, not depth: agreement across families is high signal, agreement within one family is not. A slug never encodes a vendor.

Upstream Cursor pstack maps five code-delegate playbooks (feature, refactoring, bug fix, perf, hillclimb) onto one fast code model. This portable skill does the same by routing all five through `builder` — bind `builder` once; do not hardcode Cursor-only slugs into playbooks.

## Binding syntax

One line per role. The value is whatever string your harness needs to spawn that model; a `prefix:` names an alternative CLI/harness. Comments carry the contract for future readers. An optional `# budget:` line records the reasoning budget chosen in setup (see below).

```
# pstack role bindings. One line per role. Delete a line to fall back to defaults.
# budget: unlimited (max)
worker:  grok-4-fast
builder: codex:gpt-5.6-high      # spawns via Codex CLI
judge:   claude:opus-5-thinking
peer:    gemini:3.1-pro          # family must differ from judge
```

### Optional Cursor-context defaults

If you run inside Cursor and want upstream's current code-delegate defaults, you may bind `builder` to a Cursor agent model id such as `grok-4.6-fast-xhigh` (and keep `judge` on a deeper reasoning slug). That is optional and Cursor-context only — never required for Claude Code, Codex, opencode, Kiro, or other non-Cursor agents. Prefer role contracts over vendor slugs in shared/public catalog copies.

## Setup flow (explicit, interactive)

Run this when the user asks to configure pstack models, set a pstack budget, or when a spawn fails because a binding points at nothing runnable. Setup is the one place pstack talks to the human about configuration; **runtime never does**: with no config file and no detection, every role falls back and work proceeds.

1. **Detect first.** Enumerate the models this session can actually spawn (your platform's model list, CLI sign-ins such as `codex` / `gemini` / `grok`, or prior successful spawns). Never write a binding you have not confirmed runnable.
2. **Load current state.** If a config file already exists, read its `# budget` line and role values as the current choices. Otherwise start from the role contracts and any inline examples above.
3. **Budget, map, and confirm.**

   **(a) Ask for a budget.** Prefer one structured question over free text. Offer these four options with these exact labels, and name the current budget when the file records one.

   - `unlimited — keep max`
   - `large — xhigh reasoning`
   - `medium — high reasoning`
   - `small — medium reasoning`

   **(b) Apply it when bindings carry effort tokens.** Build the working table from the role defaults (and on a re-run keep any role the user already changed by family, prefix, or alias). `unlimited` leaves every effort as in that table. `large`, `medium`, and `small` rewrite the effort token of every real slug that has one to `xhigh`, `high`, or `medium`. The effort token is the last token, or the one before a trailing `fast`, on the ladder `max` > `xhigh` > `high` > `medium` > `low`. If the result is not in the detected set, use the same family's detected slug with the highest effort at or below the target, else mark the role as needing a choice. Bindings with no effort token (plain `grok-4-fast`, `codex:gpt-5.6-high`, single-model collapses) are left unchanged aside from recording the budget line. Aliases such as `inherit-parent` / `auto` (parent chat model), when the harness supports them, do not change.

   **(c) Propose bindings and confirm.** Fill the four roles from detection: `builder` gets your strongest instruction-follower, `judge` your deepest reasoner, `peer` the strongest model from a different family than `judge`, `worker` the fastest cheap model. Show the table with budget applied. Ask whether to accept as proposed / edit specific roles (offer detected models per role) / paste slugs for anything undetected. Single-model setup: skip the role questions, state the collapse plainly, still record the budget if the user picked one, write nothing else unless the user wants the file anyway.
4. **Validate.** Every real slug in the file must be in the confirmed-runnable set. A bad binding silently breaks every delegation downstream, so stop and re-ask instead of writing a guess. Harness prefixes (`codex:`, `claude:`) validate against the named tool's own model list.
5. **Write and confirm.** Overwrite the whole file so re-runs stay idempotent. Include `# budget: <label> (<target>)` when a budget was chosen. Tell the user which file was written and that new sessions pick it up.

## Runtime resolution

When a playbook says "spawn a subagent using the builder role": read the config files in order, take the first hit, and spawn through whatever harness the prefix names (no prefix = this session's native subagent mechanism). No hit anywhere: use the best model available to you now and keep going. If a spawn errors because the bound model is unresolvable, fall back once to the inline default, note it in the reply, and suggest a setup pass at the end of the task.
