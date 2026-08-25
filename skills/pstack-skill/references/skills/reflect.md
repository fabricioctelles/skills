# Reflect

Mine the finished conversation for durable learnings and route them into edits of this skill or its references. Invoke after a complex task landed cleanly, after dead ends resolved into a working path that generalizes, after the human corrected approach mid-task, or when a non-trivial workflow emerged uncaptured. Skip trivial, off-topic, or already-covered sessions; one-offs are not learnings.

1. **Digest the session.** Reconstruct what happened from your own context: the goal, the paths tried, dead ends, corrections received, the working recipe. Where your platform keeps transcripts, fan parallel reviewer subagents over them; otherwise work from the in-context digest.
2. **Review through three lenses** (subagents when available): **judgment** (which decisions were wrong, slow, or right for reasons worth encoding), **tooling** (missing checks, scripts, gates that would have caught failures earlier), **divergent** (what nobody thought to try; which playbook step exists only because of a failure this session disproved).
3. **Synthesize.** Merge into Accepted / Rejected / Backlog. Accepted items name the exact file and section to edit and the replacement text's intent. Reject with reasons.
4. **Structural enforcement check.** Any Accepted item better enforced by a lint rule, script, metadata flag, or runtime check moves to Backlog ([encode-lessons-in-structure](../principles.md#encode-lessons-in-structure)).
5. **Apply with approval.** Present the full list; wait for explicit approval before editing. Trivial edits apply directly; substantive ones follow the authoring-a-skill playbook. Backlog items go to whatever tracker the project uses.
6. **Summarize:** edits applied with one line each, new files created, backlog filed, dropped findings with reasons.
