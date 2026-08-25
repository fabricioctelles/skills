# Why

Investigate motivation and intent behind code: why built this way, what constraints shaped it, what alternatives were rejected. Companion to `how`, which answers what the code does; this answers what forces led to its shape.

## Posture

Evidence before narrative. Collect first, then see what story the pieces support. Never pick a story and recruit evidence to fit it.

- **Cite everything.** Every claim about intent references a commit hash, PR number, ticket ID, doc URL, chat permalink, or code comment. Uncited means inference, labeled as such.
- **Hedge on purpose.** Indirect evidence gets "appears to", "likely", "suggests". Confidence-matching phrasing is part of the product; do not strip hedges to sound authoritative.
- **Surface contradictions.** Two sources disagree: show both.
- **Name the gaps.** An honest "we could not find out" beats a confident guess. Null results are findings about how the decision was made.
- **Never infer intent from code shape.** Code tells you what it does, rarely why it exists.

## Steps

1. **Anchor in code.** File paths, line ranges, key symbols, last commits touching the target (`git blame -L`, `git log --follow -p`), PR numbers from merge subjects, PR bodies via `gh`. Cheap inline; every investigator gets this seed context.
2. **Sweep every evidence category in parallel**, one investigator per category, all spawned in one message:
   - **Source control** (always available): PR descriptions, review threads, inline comments, test names encoding motivating edge cases. Most trustworthy; ties to the diff that shipped.
   - **Issue tracker** (Linear/Jira/GitHub Issues): customer forcing functions, compliance deadlines, initiative framing.
   - **Long-form docs** (Notion/Confluence/docs/ADRs): problem statements, alternatives-considered sections, postmortems.
   - **Team chat** (Slack/Discord): real-time deliberation that never reached a doc, incident channels, author activity around the ship date.
   - **Infra observability** (metrics/logs/APM): monitor thresholds matching code constants, spikes right before a merge, dashboards born as postmortem actions.
   - **Error tracking** (Sentry and peers): exceptions bracketing the ship date that motivated defensive code.
   - **Product analytics warehouse**: usage trajectories around the ship date, flag exposure data, pre-ship distributions explaining threshold constants.

   Use whichever of these sources actually exist in this environment (MCPs, CLIs, repos); record skipped categories as gaps. Skip only with written justification naming the category provably irrelevant. "Probably nothing there" is not justification. A null result costs one subagent; a missed design doc costs a wrong answer.
3. **Synthesize.** One pass over all findings including nulls. Spot-check citations before presenting.

## Output format

Keep the confidence separation intact.

- **The question.** Restated in one line.
- **The code in question.** Paths, symbols. One or two lines.
- **What we found (direct evidence).** Cited claims, present tense, quoted or paraphrased.
- **What we can reasonably infer.** Hedged claims, each with its inference chain spelled out.
- **Competing hypotheses.** When evidence fits several stories: each with evidence for and against. Skip when there is a clear answer.
- **What we don't know.** Specific gaps and searches that came up empty.
- **Sources consulted.** One line per category searched, found or empty or skipped-with-reason, so the reader judges breadth at a glance.

If the why precedes changing this code, convert lineage into a Preserve / Change / Avoid / Risk constraint set for planning.
