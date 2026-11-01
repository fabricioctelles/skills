### Multi-phase or multi-PR plan

**You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence.** For work that spans phases or stacked PRs. The plan is the deliverable. Do not implement.

1. When the change is one or two files with an obvious approach, skip the plan. Say so and stop.
2. Settle open questions by prototype before you write. For a question about layout, timing, behavior, or whether an API works, run `playbooks/prototype.md`. Keep the branch, the SHA, and the screenshots for Appendix A. Ask the operator only about a product or preference call that no run can settle. Give options (the **never-block-on-the-human** principle skill).
3. Explore com subagentes do papel `worker`, conforme [setup-pstack](../references/skills/setup-pstack.md) e o princípio **guard-the-context-window**. Sem subagentes, faça passes sequenciais independentes. Each returns file pointers, conventions, test commands, and entry points. No inlined dumps.
4. Copy the skeleton below into the plan file and fill every placeholder. Unless the operator names a path, write the file under the agent store's `docs/`. Keep every heading and every sub-block in the order shown. One section per PR. One PR is one change with its own evidence (the **sequence-verifiable-units** principle skill). Name the execution playbook in **How to read this**. Pick `playbooks/autopilot-full.md` when the run may merge. Pick `playbooks/autopilot-stack.md` when the operator lands the PRs. A standing program takes `playbooks/orchestrate.md`.
5. Write under `/technical-writing` in full, then `/unslop`. The body is one Diátaxis mode, how-to. Appendices hold explanation and reference. Two rules apply verbatim. "i dont want any abstract metaphors" and "write like hemingway". Each heading states the task or the finding. No long dashes. No mid-sentence colons.
6. Run `node skills/pstack-skill/scripts/check-plan.mjs <plan.md>` and fix every line it prints (the **encode-lessons-in-structure** principle skill). It enforces the skeleton's shape, the verification rule in every verification block, and the punctuation rules.
7. Hand back. Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go, under the execution playbook the plan names.

**Verification.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked (the **prove-it-works** principle skill). That sentence is the verification rule. Every verification block opens with it. The live block is mandatory. Ten lanes on `worker` at the PR head drive the real surface through its control skill, per the **swarm** skill. Each lane is one box with a concrete scenario, the screenshot it saves, and its pass predicate. The perf block names the metric, the probe, the trunk baseline measured first, and the rule with the number that fails. A PR that changes an interaction is review-gated. The operator reviews it in chat with screenshots and a video before merge. A PR that changes no interaction writes `**Review gate.** None. <PR id> is not review-gated.` and no boxes under it.

**Control skill.** Escolha o driver pela superfície. Browser, Electron e interfaces web usam a automação de navegador disponível. CLIs e TUIs usam o terminal ou o driver do projeto. Mobile nativo usa o simulador disponível. Um PR que toca duas superfícies tem lanes em ambas. Sem driver disponível, registre o risco no Appendix C e como cada lane executará o teste real.

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `<pstack-skill>/playbooks/<execution playbook>.md`. Resolve `<pstack-skill>` to the maintained skill folder before execution. <Who merges, and which PR ids are the operator's items that stop at merge-ready.>

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] On the operator's go, record a persistent objective (`/goal` only when the harness provides it) with this exact text. "<The plan path, the PR ids in order, the verification rule, who merges, and the done condition.>"
- [ ] Resolve the maintained skill folder as `<pstack-skill>`. Read these at program start and every tick. Do not assume the project vendors this skill on trunk.
  - [ ] `<pstack-skill>/playbooks/<execution playbook>.md`
  - [ ] `<pstack-skill>/references/skills/swarm.md`
  - [ ] `<pstack-skill>/playbooks/opening-a-pr.md`
  - [ ] `<pstack-skill>/references/skills/<each other bundled procedure>.md`
- [ ] Read the project's own verification procedure from current trunk with `git show origin/main:<project verification path>`. When the driver is installed outside the project, read its maintained skill file instead.
- [ ] Arm the 30-minute audit tick with the harness's event or background wake mechanism. Without one, record the next checkpoint and check it at each turn. Never invent a running watcher.
- [ ] Use this tick prompt, verbatim. "Re-read the maintained execution playbook and the recorded objective. Audit the operation against both and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then post a status message to the operator in chat, whether or not anything changed, with the queue table of PR, owner, state, and head SHA, the verdicts since the last tick, what merged, open operator gates, and blockers."
- [ ] On the operator's hold or stand-down, send every owner a zero-writes order at once.

### Spawn owners

- [ ] Spawn one owner per PR with the full lifecycle the execution playbook names.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Open the PR ready with the forge CLI, such as `gh pr create`. Verify its live state. Stacked PRs need no Graphite.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Strip slop from the diff before each commit and run `references/skills/no-comments.md` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that base during fixes. Rebase again at merge prep, on a conflict, on CI broken by trunk, or when a known concurrent change to the same files lands.

### Verdict and merge, for every PR

- [ ] A full swarm runs once at the code-ready head. Repeat it for new behavior, a redesign, or a large new diff. Rebase, conflict resolution, or a small fix gets one verifier at the new head. Wording-only changes need no new verifier. Run the swarm per `references/skills/swarm.md`. Include the gates, live, perf, and independent audit lanes. Audit the merge-ready receipts before the verdict.
- [ ] Judge each finding by the execution playbook's blocking rule. A clean verdict has no blocking finding. A failure already present on the base is a follow-up unless the PR copies or newly reaches it. A new head needs a fresh verdict except where the patch-id rule preserves the result.
- [ ] <The merge or handoff rule from the execution playbook, with the patch-id rule from `playbooks/shipping.md`.>

### Boot recipe, for every live lane

Each live lane runs in an isolated worktree or checkout at the PR head. Use the available driver named by the plan.

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report.

## <Task as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `worker` at the PR head, per the boot recipe.

- [ ] Lane 1. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. <What is measured.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails.>

**Review gate.** The operator reviews before merge.

- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change on a lane VM. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] <The owner merges within the grant, or hands the verified PR to the operator without merging.>

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get `references/skills/how.md` and `references/skills/interrogate.md`. The trail per `references/skills/show-me-your-work.md`.>
````

**Reply:** the plan path, the PR ids with their dependencies and the review-gated set, what the prototypes proved and what stays unproven, and the check script's output.
