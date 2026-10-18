# pstack in Claude Code

Adapted from upstream `pstack/docs/harness/claude-code.md` (cursor/plugins, MIT). pstack-skill already speaks in roles instead of vendor slugs, but some steps and playbooks still carry Cursor names. In Claude Code, read this file once per session and map each Cursor name you meet with the tables below. `<pstack-skill>` means this skill's folder. If a Cursor field has no row, drop it and say so. Never pass a field or value the tool schema rejects.

The same shape works for any other harness: one mapping file per harness under `references/harness/`, loaded only when you run in that harness.

## Tools

| Cursor | Claude Code |
| --- | --- |
| `Task` | `Agent` |
| `AskQuestion` | `AskUserQuestion`. In `-p` mode it is absent, so ask in plain text. |
| Open a todolist | Use `TodoWrite` if the session offers it. Otherwise keep the list in your reply and update it at each phase. |
| Run another bundled procedure (a bold lowercase name, or `/name`) | `Read` `<pstack-skill>/references/skills/<name>.md` and follow it. |
| `Grep`, `Glob` | `Bash` with `rg` when the session has no `Grep` or `Glob`. |

## Subagent fields

| Cursor | Claude Code |
| --- | --- |
| `subagent_type: generalPurpose` | `subagent_type: "general-purpose"` |
| `readonly: true` | `subagent_type: "Explore"`. It keeps `Bash`, so the brief also says "do not edit files", and you check `git status` afterward. |
| `readonly: false` | `general-purpose`. It keeps the session's MCP servers. |
| `environment: "cloud"` | `isolation: "worktree"`. Name the branch or commit the worker checks out. |
| `environment: "local"` | Omit. |
| `cloud_base_branch: <b>` | Tell the worker to check out `<b>` first. |
| `run_in_background: true` | Omit. Subagents run in the background by default and notify you when they finish. |
| `resume` | Spawn a new agent and paste the earlier result into its brief. |
| `file_attachments` | List the paths in the brief. |

## Models

pstack-skill binds roles in `.agents/pstack-models.md` (see `references/skills/setup-pstack.md`). Claude Code does not load that file by itself, so read it at the start of the session.

| Binding value | Claude Code |
| --- | --- |
| `<model> <effort>`, such as `opus xhigh` | `model: "opus"` and `effort: "xhigh"`. `model` takes only the values the `Agent` tool schema lists. Drop `-fast`. |
| A `claude-<family>-<version>-<effort>[-fast]` slug | Map to the family name in the schema and keep the effort token. |
| A `grok-*`, `gpt-*`, `gemini-*`, or other non-Claude slug, or a `prefix:` naming another CLI | Omit `model` so the agent runs on the session model, and say so. |
| `auto` or `inherit-parent` | Omit `model`. |
| A role line that is missing | Use the default from `references/skills/setup-pstack.md`. |

## Paths

| Cursor | Claude Code |
| --- | --- |
| `.cursor/skills/`, `~/.cursor/skills/` | `.claude/skills/`, `~/.claude/skills/` |
| `.cursor/rules/*.mdc`, always-applied rules | `CLAUDE.md`, or `AGENTS.md` when no `CLAUDE.md` exists. Claude Code never reads `.mdc` files. |
| Transcripts in `~/.cursor/projects/<slug>/agent-transcripts/` | `~/.claude/projects/<slug>/<session>.jsonl`. The slug is the workspace path with each `/` and `.` changed to `-`, so `/Users/you/proj` is `-Users-you-proj`. The newest `.jsonl` directly in that folder is the current session. Its `<session>/subagents/` folder holds subagent transcripts. Read only this workspace's folder. |

## Cursor-only features

Claude Code has no Cursor Automations, Bugbot, Cursor cloud agents, or built-in PR tool. When a step needs one, put one line in your reply, `Skipped in Claude Code: <step>. <reason>.`, then go on to the next step. Do not stop, ask, or retry. When a later step needs what the skipped step made, such as a URL or a key, leave a placeholder and name it in the line.

| Cursor | Claude Code |
| --- | --- |
| Cursor Automations: routines, routine wakes, and webhooks | Skip with the line. |
| Bugbot | Bugbot comments on a GitHub PR are ordinary review threads, so triage them with the forge command that the step gives. Skip a step that starts, waits for, or configures Bugbot when the PR has no Bugbot check or comment. |
| Cursor cloud agents | `environment: "cloud"` maps to a worktree, as in Subagent fields. Skip a step that needs the cloud agent itself, such as its dashboard status or its own machine. |
| A built-in PR tool | Use the forge command that the step gives, such as `gh pr create`. That is not a skip, so write no line. |
