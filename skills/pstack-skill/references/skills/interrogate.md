# Interrogate

Adversarial multi-model review of a change or design. One reviewer per available model, same prompt and rubric for all; the signal comes from diversity, not personas. Agreement across models is high-confidence; lone-model findings are worth reading but weighted lower. The deliverable is a synthesized verdict, never auto-applied changes.

## Steps

1. **Scope.** Specific files or diff if pointed at one; otherwise the full changeset against the base branch (`git diff main...HEAD`).
2. **State the intent.** One clear paragraph on what this change is trying to accomplish, derived from the message, commit messages, PR description, and code. Reviewers challenge whether the work achieves the intent well, not whether the intent is right. If intent is unclear, ask before proceeding.
3. **Spawn reviewers.** All in one message, read-only, different model families when available (extend or shrink labels A/B/C/D to the count). Same filled template to every reviewer: stated intent, the diff or files, this review rubric: correctness bugs, security holes, data loss, concurrency races, error-handling gaps, API misuse, performance cliffs, test gaps; plus this code-quality lens: dead abstractions, speculative generality, narrating comments, layers without compression, misleading names, hidden mutable state.
4. **Synthesize.** Parse all findings; consensus is 2+ models raising it independently; deduplicate paraphrases noting which models raised each; note explicit disagreements between models.
5. **Lead judgment.** You are a pragmatic senior lead, not a neutral aggregator. You hold context reviewers lack: goal, constraints, timeline, tradeoffs already considered. Use it aggressively. Categorize every finding:
   - **Act on.** Real correctness, security, or maintainability issues given actual goals. Would block a real PR.
   - **Consider.** Legitimate but cost/benefit unclear right now.
   - **Noted.** Valid yet not actionable here: premature, low-impact, context-dependent.
   - **Dismissed.** Wrong, nitpicky, missing context. One-line why.

## Output format

### Intent
> The stated intent paragraph.

### Reviewers
- Reviewer A: `<model>`, N findings (one bullet per reviewer)

### Act On / Consider / Noted / Dismissed
Findings grouped by bucket, each with which models raised it and a one-line rationale. Dismissed shows your filters so the user can override them.

### Agreement Map
Where models agreed and diverged, and what the pattern tells us.
