# Model Detection and Privacy Notes

Loop-architect detection is intentionally dumb and transparent. It stores
invocation metadata only, never credentials.

## Registry

Default registry path:

```text
~/.loop-architect/models.json
```

Registry entries should look like:

```json
{
  "kiro": {
    "cli": "kiro-cli",
    "invoke": ["kiro-cli", "chat", "--trust-all-tools", "-p"],
    "probe": ["kiro-cli", "--version"],
    "available": true,
    "authed": true,
    "local": false,
    "capabilities": {
      "headless": true,
      "goal": true,
      "subagent": true,
      "review_loop": true
    }
  },
  "claude": {
    "cli": "claude",
    "invoke": ["claude", "-p"],
    "probe": ["claude", "--version"],
    "available": true,
    "authed": true,
    "local": false,
    "capabilities": {
      "headless": true,
      "goal": true,
      "subagent": false,
      "review_loop": false
    }
  }
}
```

## Capabilities

`headless`
: The CLI accepts a prompt via stdin/argument and returns output via stdout
  without interactive prompts. Required for use as host or judge in the
  external Python runner.

`goal`
: The CLI supports a `/goal` command that runs an autonomous loop with
  self-verification. When present, RUN_IN_SESSION.md can emit a `/goal`
  one-liner as an alternative execution path.

`subagent`
: The CLI can spawn isolated sub-agents with their own context. When present,
  the council can use native subagent review loops instead of shelling out.

`review_loop`
: The CLI supports iterative review loops with trigger-based feedback (e.g.
  Kiro's `loop_to` with `NEEDS_CHANGES` trigger). Enables native cross-model
  review without the external runner.

## Kiro CLI Specifics

- Headless mode requires `--trust-all-tools` or the session halts waiting for
  tool approval.
- Full invoke pattern: `["kiro-cli", "chat", "--trust-all-tools", "-p"]`
- The `/goal --max N` command provides native loop execution with configurable
  iteration limits (default 5).
- Subagent review loops use a `trigger` string (e.g. `NEEDS_CHANGES`) and
  `max_iterations` cap.

## `authed` Semantics

`authed` means the basic probe command exited cleanly. It is a convenience
signal, not a guarantee that a future paid model call will succeed.

## Default Redactions

- `.env`
- `.env.*`
- `secrets/**`
- `**/*.key`

Add project-specific globs for customer data, private transcripts, or internal
design docs before sending anything to a non-local council member.

## Local Model UX

Surface `ollama` as the privacy-preserving option when present. It may be lower
quality than frontier hosted models, but it keeps council review in-house.
