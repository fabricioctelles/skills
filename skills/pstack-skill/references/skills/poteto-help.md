# Poteto help

Guides users through pstack setup, poteto-mode, and picking the skill, playbook, or principle for a task. Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from.

For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is not a help question. Read the poteto-mode entry, do the work under it, and mention once that the mode stays on.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with poteto-mode
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

## Pick a skill

The default answer is poteto-mode, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | poteto-mode |
| Check that the agent understood their goal and the problem before it starts | in-your-own-words |
| Aim a task higher before starting: more expert, more outcome-focused, not overspecified | sharpen |
| Know how code works now, or where new code should live | how |
| Know why code is shaped this way, or where a number came from | why |
| Understand a change or subsystem, explained plainly | teach |
| Catch up on their own recent work on a topic | recall |
| Catch up on what changed in this chat since their last message, in plain words and small visuals, with every item waiting on them listed and decidable from the reply alone | ketchup |
| Know what a small diff could break outside itself | blast-radius |
| Settle types and module shape before code that crosses a function boundary | architect |
| Get several attempts at one brief, merged into the best one | arena |
| Run parallel checks over slices, or race workers | swarm |
| Have different models review a diff and try to break it | interrogate |
| Fix a bug test-first when a cheap local test exists | tdd |
| Apply TypeScript rules to `.ts` or `.tsx` work | typescript-best-practices |
| Strip comments before review, using a reviewer that didn't write them | no-comments |
| Clean AI tells out of prose | unslop |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | technical-writing |
| Hear the last reply again in plain words | bro |
| Give agents a scripted way to drive the app and prove behavior | create-verification-skill |
| Bring a verification skill and its feature map back in line with the app | maintain-verification-skill |
| Formally verify a race, invariant, or other property that tests rarely reach | create-formal-verification-skill |
| Vet a performance number before reporting or acting on it | benchmark-checklist |
| Run a large or cross-cutting change, or one to review after stepping away | figure-it-out |
| Keep a decision log during a run, and review it afterward | show-me-your-work |
| Pick a model for each role and a reasoning budget | setup-pstack |
| Turn their own working habits into a personal mode skill | automate-me |
| Turn what a finished task taught into skill edits | reflect |
| Stop agents from repeating the same mistakes in this repo | correct |
| Find their way around pstack | poteto-help |

Close calls:

- `how` explains what the code does. `why` explains the reasons. `teach` runs one or both and explains the result plainly.
- `arena` gives every worker the same brief and merges the best parts. `swarm` splits work into slices or a race and returns one report.
- `architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `interrogate` reviews the diff. `blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `recall` rebuilds context across recent chats. `ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

## Playbooks and principles

Playbooks are step lists inside poteto-mode, not skills, so they have no slash command. Inside poteto-mode, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "stack them, don't ship" runs Autopilot-stack.
- "run the eval playbook" runs Eval.

Principles are one-rule skills that poteto-mode reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output."

## Reply

Lead with the answer. Give at most one example prompt, then the link to that file. Keep it short unless the user asked for the whole map.
