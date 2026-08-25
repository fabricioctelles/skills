# Recall

Before starting or resuming work, rebuild recent working context from your own history and the shared record; hand back a tight current-state brief. For "recall my work on X", "catch me up", "where did I leave off".

1. **Classify, then route.** One specific prior session to resume: the Session pickup playbook instead. Turning habits into a skill: automate-me. A user-supplied state capsule (paths, branch, change): use it and skip mining.
2. **Lock scope before searching.** Pin the window ("recent" defaults to 7 days), the topic if named, and the workspace. State scope back; never quietly turn "all" into "recent N".
3. **Fan out across your own history.** Parallel subagents over slices of your transcript store (or reconstruct from git history and prior PRs when no transcripts exist): order candidates by modification time, grep topic first, read only matching regions, skip the current chat plus obvious noise. Each returns one block per chat: topic, user goal, decisions, open threads, corrections received, artifacts (PRs, branches), each citing its source. Raw transcripts stay in the subagents.
4. **Sweep the shared record whenever the topic names a feature, file, or bug.** Default posture, not a judgment call: a named target carries history invisible in your own transcripts. Run the `why` investigators steered from "why was this built this way" to "what is the current state, what was tried and reverted, what do users still report". Null results are findings. Skip only for pure activity recall with no named target.
5. **Verify against live state.** Transcripts and tickets are history, not truth: check surfaced PRs, branches, and tickets with `git` and `gh` before briefing.
6. **Write the brief.**

## Output contract

- **Capsule.** At most 5 bullets: what this work is, where it stands overall.
- **Threads.** One line each, exactly one status tag: `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, `[planned, not started]`.
- **Problems.** At most 5 recurring ones, including symptoms still reported and any fix that shipped and got reverted.
- **Next move.** The single most useful next action, concrete.

Adjacent features stay out unless they block this one. When capsule and threads outgrow a screen, cut detail before cutting threads. Write through [unslop](unslop.md); cite chat findings by source and shared-record findings by PR number, ticket ID, or permalink.
