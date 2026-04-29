---
name: ralph-loop-kiro-specs
description: >-
  Automated iterative agent runner for spec-based development in Kiro. Wraps kiro-cli in a
  self-correcting bash loop that picks up tasks from a Kiro spec, implements them one at a time,
  verifies against exit criteria, and accumulates corrections and codebase patterns across iterations.
  Use this skill when the user mentions "ralph loop", "ralph", "spec loop", "iterative spec runner",
  "run my spec tasks automatically", "kiro spec automation", "self-correcting agent loop",
  "implement spec tasks in a loop", "run kiro-cli in a loop", "automated task implementation",
  or wants to drive a Kiro spec to completion through repeated agent iterations. Also use when the
  user wants to set up, configure, troubleshoot, or understand the Ralph Loop workflow — including
  progress tracking, corrections, codebase patterns, timing logs, and the summary dashboard.
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-04-28
  license: Apache-2.0
  original_project: https://github.com/mreferre/ralph-loop-kiro-specs
  original_author: mreferre
---

# Ralph Loop for Kiro Specs

An automated, iterative agent runner that drives spec-based development in [Kiro](https://kiro.dev). It wraps `kiro-cli` in a bash loop, feeding it a carefully engineered prompt that turns Kiro into a disciplined, self-correcting implementation agent — one that picks up tasks from a spec, implements them, verifies its own work, and learns from its mistakes across iterations.

> **Attribution:** Based on [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) by [mreferre](https://github.com/mreferre), licensed under Apache License 2.0.

## When to Use

- Automate implementation of Kiro spec tasks through repeated agent iterations
- Drive a spec from start to finish without manual prompt-by-prompt interaction
- Set up the Ralph Loop in a new project
- Troubleshoot a stuck or failed Ralph Loop run
- Understand how progress tracking, corrections, and codebase patterns work
- Generate or interpret the summary dashboard after completion

## Prerequisites

| Requirement | Details |
|---|---|
| Kiro CLI | `kiro-cli` must be installed and on `PATH` ([kiro.dev/cli](https://kiro.dev/cli/)) |
| Kiro IDE | [kiro.dev](https://kiro.dev/) installed |
| Bash | Standard bash shell |
| Kiro Specs | A project with specs under `.kiro/specs/<specs_name>/` containing at least `requirements.md`, `design.md`, and `tasks.md` |

## How It Works

Ralph runs a loop where each iteration sends a prompt to `kiro-cli`. The prompt instructs the agent to follow a strict six-phase cycle:

### The Six Phases

1. **Load Context** — Read steering files (`product.md`, `structure.md`, `tech.md`) and the target spec (`requirements.md`, `design.md`, `tasks.md`, `progress.md`). Take stock of available tools.
2. **Pick ONE Task** — Find the lowest-numbered incomplete top-level task. Record start time. Never pick more than one task per iteration.
3. **Understand Before Implementing** — Read relevant source files, study existing patterns, re-read the Corrections and Codebase Patterns sections from `progress.md`, and apply every relevant correction proactively.
4. **Implement** — Implement the task and all subtasks in order. Run typechecks and tests. If something fails: fix it, write a correction immediately if a future iteration could hit the same problem, and move on. After 5 failed attempts, mark the task `[F]` and log an unresolved blocker.
5. **Verify Exit Criteria** — Re-read exit criteria from `requirements.md` and design constraints from `design.md`. Confirm each is satisfied before marking complete.
6. **Update Tracking** — Mark the task `[X]` in `tasks.md`, append a progress entry to `progress.md`, add new codebase patterns, do a final correction sweep, and record timing to `specs_time.md`.

### The Self-Correction System

The Corrections section at the top of `progress.md` is a flat lookup table of mistakes and their fixes. Every iteration reads it before doing any work and must never repeat a listed mistake. Corrections are written immediately when errors happen — not at the end of the task.

Format:
```
- ❌ `python manage.py migrate` → ✅ `python3 manage.py migrate` (system has no `python` alias)
- ❌ Running tests with `npm test` → ✅ `npm run test:unit` (project uses separate test scripts)
- ❌ UNRESOLVED: [description of issue that couldn't be fixed after 5 attempts]
```

### Codebase Patterns

Ralph accumulates conventions discovered during implementation — file naming, import patterns, error handling, testing commands, etc. Only patterns actually encountered are recorded, not speculative ones.

### Completion and Summary Dashboard

When all tasks are marked `[X]`, Ralph generates a self-contained `summary.html` in the spec directory with:
- **Top pane**: spec name, status indicator (green/red), total elapsed time, task count, date range
- **Left pane**: collapsible task tree with hover tooltips showing progress details
- **Right pane**: timing table with per-task start/end times and durations

## Project Structure

The user's project should look like this before running Ralph:

```
your-project/
├── ralph-loop-kiro-specs-prompt.md    # The Ralph agent prompt template
├── ralph-loop-kiro-specs-script.sh    # The loop runner script
└── .kiro/
    ├── steering/
    │   ├── product.md                 # What the product is
    │   ├── structure.md               # Project structure conventions
    │   └── tech.md                    # Tech stack and tooling
    └── specs/
        └── <specs_name>/
            ├── requirements.md        # Requirements and exit criteria
            ├── design.md              # Architecture and design decisions
            ├── tasks.md               # Task checklist
            ├── progress.md            # Auto-created: corrections, patterns, progress log
            ├── specs_time.md          # Auto-created: per-task timing
            └── summary.html           # Auto-generated on completion: visual dashboard
```

## Setup Instructions

To set up Ralph Loop in a project:

1. Copy the script and prompt template to the project root:
   - `ralph-loop-kiro-specs-script.sh` — the loop runner (bundled in this skill under `scripts/`)
   - `ralph-loop-kiro-specs-prompt.md` — the agent prompt template (bundled under `references/`)
2. Make the script executable: `chmod +x ralph-loop-kiro-specs-script.sh`
3. Ensure the project has Kiro specs set up under `.kiro/specs/<specs_name>/` with at least `requirements.md`, `design.md`, and `tasks.md`
4. Ensure steering files exist under `.kiro/steering/` (`product.md`, `structure.md`, `tech.md`) — these significantly improve output quality

## Usage

```bash
./ralph-loop-kiro-specs-script.sh <max_iterations> <specs_name>
```

| Argument | Description |
|---|---|
| `max_iterations` | Maximum number of loop iterations (positive integer). Each iteration implements one task. Set to at least the number of tasks plus a buffer for retries. |
| `specs_name` | Name of the spec directory under `.kiro/specs/`. Must already exist with the required files. |

### Example

```bash
# Run up to 15 iterations on the "auth-feature" spec
./ralph-loop-kiro-specs-script.sh 15 auth-feature
```

### Iteration Modes

The script asks at startup whether to run automatically or manually:

- **Automatic** — Tasks run back-to-back without pausing. Good for well-defined specs.
- **Manual** — Pauses after each iteration for review. Good for new or unfamiliar specs.

## Troubleshooting

### Ralph gets stuck on a task (marked `[F]`)

Fix the issue manually, update `tasks.md` to unmark the task, and re-run. The corrections from the failed attempt will still be in `progress.md` for the next iteration to learn from.

### Max iterations reached without completion

Increase `max_iterations` and re-run. Ralph will pick up where it left off since it reads `tasks.md` to find the next incomplete task.

### Agent implements more than one task per iteration

This violates the core constraint. Check that you're using the unmodified prompt template. The prompt has a critical constraint section at the top that enforces one-task-per-iteration.

### Steering files are missing

Ralph works without them but produces better results with context. Create `.kiro/steering/product.md`, `structure.md`, and `tech.md` with descriptions of your product, project structure, and tech stack.

## Quality Checklist

Before running Ralph Loop, verify:

- [ ] `kiro-cli` is installed and available on `PATH`
- [ ] Spec directory exists under `.kiro/specs/<specs_name>/`
- [ ] `requirements.md` has numbered requirements with exit criteria
- [ ] `design.md` has architecture and design decisions
- [ ] `tasks.md` has a numbered task checklist with subtasks
- [ ] Steering files exist under `.kiro/steering/` (recommended)
- [ ] `max_iterations` is set to at least the number of tasks + buffer
- [ ] The prompt template (`ralph-loop-kiro-specs-prompt.md`) is in the project root
- [ ] The script (`ralph-loop-kiro-specs-script.sh`) is executable

## Bundled Resources

| Resource | Path | Description |
|---|---|---|
| Runner script | `scripts/ralph-loop-kiro-specs-script.sh` | The bash loop that drives iterations. Copy to project root. |
| Prompt template | `references/ralph-loop-kiro-specs-prompt.md` | The agent prompt template. Copy to project root. |

Read the prompt template when you need to understand the detailed phase instructions, correction format, codebase pattern categories, or the summary dashboard specification.

## License

This skill is based on [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) by [mreferre](https://github.com/mreferre), licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

```
Copyright [mreferre]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
