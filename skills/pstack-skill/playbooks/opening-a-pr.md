### Opening a PR

Invoked at the end of every other playbook.

Work from a git worktree off trunk, and keep unrelated work out of it. Rebase into small, landable commits. Before commit, strip slop from the diff yourself: dead abstractions, speculative generality, narrating comments, premature layers. Run [no-comments](../references/skills/no-comments.md) before review. Write the title, body, and commit messages per [technical-writing](../references/skills/technical-writing.md), then apply [unslop](../references/skills/unslop.md).

Title: `type(scope): subject`, naming a real symbol when one carries the change. Body: a one-minute briefing under 40 lines with these `##` headings in order, dropping empty ones: `## Why` (open with the user's goal), `## What changed`, `## Scope`, `## Tradeoffs` (only rejected alternatives a reviewer would otherwise ask about), `## Blast Radius`, `## Verification`. Link long logs and tables instead of pasting them.

Stack follow-ups by base branch. Open PRs ready for review, never as a draft: through the run's PR tool with drafts off, or the forge's own CLI, such as `gh pr create` without `--draft` or `glab mr create` without `--draft`. Opening a PR does not start a babysit. Post the URL and keep building. A subagent that opens a PR returns the URL to its coordinator and starts a babysit only when its brief assigns one.
