# Ralph Agent Instructions

> Based on [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) by [mreferre](https://github.com/mreferre).
> Licensed under Apache License 2.0.

## ⛔ CRITICAL CONSTRAINT — READ THIS FIRST

You must implement exactly ONE top-level task per invocation. This is non-negotiable.

- ONE top-level task means: a single root-level item (e.g., `1.`, `2.`, `3.`) and all of its subtasks (e.g., `2.1`, `2.2`, `2.3`).
- After completing that one top-level task and its subtasks, you MUST STOP implementing. Do not continue to the next top-level task. Instead, proceed to Phase 5 (Verify Exit Criteria) and Phase 6 (Update Tracking) for the task you just completed.
- Do not implement, touch, or mark any other top-level task — even if it seems small, related, or easy.
- If you catch yourself thinking "I can also knock out task N while I'm here" — STOP implementing. That is exactly the behavior this rule prohibits. Move on to verification and tracking for your one task.
- Violating this constraint invalidates the entire run.

## Phase 1: Load Context

Read the following files to understand the project. Skip any that don't exist.

1. `README.md` — read the project README for high-level context about the project's purpose, setup, and conventions
2. `docs/` folder — if it exists, scan for any additional documentation, ADRs, or context relevant to the spec
3. `.kiro/steering/product.md` — what the product is
4. `.kiro/steering/structure.md` — project structure conventions
5. `.kiro/steering/tech.md` — tech stack and tooling
6. `.kiro/specs/SPECS_NAME/requirements.md` — requirements and exit criteria
7. `.kiro/specs/SPECS_NAME/design.md` — architecture and design decisions
8. `.kiro/specs/SPECS_NAME/tasks.md` — the task list to implement
9. `.kiro/specs/SPECS_NAME/progress.md` — **read the top sections (Corrections and Codebase Patterns) FIRST and internalize them before doing anything else**, then review past progress entries

## Tool Awareness

After loading context, take stock of what tools are available to you in this environment (e.g., MCP servers, CLI utilities, linters, formatters, test runners, build tools). You are not required to use any of them — but knowing what's available may inform better decisions during implementation and verification. Use your judgment: if a tool would genuinely help with the current task, use it. If not, don't force it.

## Phase 2: Pick ONE Task

Capture the task start time by running these two shell commands and saving their output:
```bash
date '+%Y-%m-%d %H:%M:%S'
date +%s
```
The first gives you the human-readable start timestamp for the time log. The second gives you the epoch seconds — you will need both later in Phase 6 to compute elapsed time accurately.

1. Find the lowest-numbered **top-level** task in `tasks.md` that is NOT marked with `[X]`. A top-level task is one at the root indentation level (e.g., `- [ ] 1.`, `- [ ] 2.`). Subtasks nested under a top-level task (e.g., `1.1`, `1.2`) are NOT independent tasks — they are part of their parent and will be implemented together with it.
2. Read the requirement(s) and exit criteria referenced by that task in `requirements.md`
3. Read the relevant design details in `design.md`
4. Do NOT pick more than one top-level task. You implement exactly one top-level task (including all of its subtasks) per invocation. You must NOT mark any other top-level task as complete — only the one you pick here.

## Phase 3: Understand Before Implementing

Before writing any code:

1. Read the existing source files that are relevant to the task
2. Understand the current patterns, naming conventions, and structure already in use
3. **Re-read the Corrections section** at the top of `progress.md` with your chosen task in mind. Every entry there is a mistake a previous iteration already made and fixed. Do not repeat them. Apply every relevant correction proactively to the task you are about to implement.
4. Re-read the Codebase Patterns section in `progress.md` with your chosen task in mind — follow any patterns relevant to this task

## Phase 4: Implement

1. Implement the task and all its subtasks in their specified order
2. Follow the project's existing conventions and patterns
3. After implementation, run typecheck and tests as applicable to the project
4. If a command fails or a test breaks:
   a. Fix the issue
   b. **Immediately ask yourself: "Could a future iteration hit this same problem?"** If yes, add it to the Corrections section at the top of `progress.md` RIGHT NOW, before continuing. Do not wait until the end.
   c. If you cannot resolve a failure after 5 attempts, add it to the Corrections section as an unresolved blocker, mark the task as failed in `tasks.md` (e.g., `[F]`), and move on to Phase 6 to record what happened. Do NOT mark the task with `[X]`.
5. **STOP CHECK:** You have now finished implementing your one top-level task. Do NOT proceed to implement any other top-level task. Go directly to Phase 5.

## Phase 5: Verify Exit Criteria

Before marking the task complete:

1. Re-read the exit criteria from `requirements.md` for this task and confirm each one is satisfied.
2. Re-read the relevant design details from `design.md` and confirm the implementation conforms to the specified architecture, patterns, and constraints.
3. If any exit criteria or design constraints are not met, go back and address them.

## Phase 6: Update Tracking

1. In `tasks.md`, mark ONLY the single task you just completed (and its direct subtasks) with `[X]`. **Do NOT mark any other tasks as complete.** When editing `tasks.md`, use a surgical edit (e.g., find-and-replace on the specific task line) rather than rewriting the entire file. If you rewrite the file, you MUST preserve the exact checkbox state (`[ ]` or `[X]`) of every task you did NOT work on. Double-check the file after editing to confirm no other tasks were accidentally marked.
2. Append a progress entry to `progress.md` (see format below)
3. If you discovered a reusable codebase pattern, add it to the Codebase Patterns section in `progress.md`
4. Final sweep: if you hit ANY error during this task that you haven't already added to Corrections, add it now. If you followed Phase 4 step 4b faithfully, this step should be a no-op.
5. Capture the task end time by running these two shell commands:
   ```bash
   date '+%Y-%m-%d %H:%M:%S'
   date +%s
   ```
   The first gives you the human-readable end timestamp. The second gives you the epoch seconds.
   Compute elapsed time by subtracting the start epoch (captured in Phase 2) from the end epoch:
   ```bash
   echo $(( END_EPOCH - START_EPOCH ))
   ```
   Convert the result to `Xm Ys` format (e.g., if the difference is 754 seconds → `12m 34s`).
   Append a row to `SPECS_NAME/specs_time.md` in this format:
   ```
   | [Task ID] | [Start time] | [End time] | [Elapsed time] |
   ```
   Use `YYYY-MM-DD HH:MM:SS` for timestamps and `Xm Ys` for elapsed time.

## Progress Entry Format

Append to the bottom of `progress.md`:

```
## [Date] - [Task ID]: [Brief description]
- What was implemented
- Files changed
- Tools used (list any non-default tools you chose to use and why, e.g., "Used MCP linter to validate schema — caught a missing required field")
- Patterns discovered (list here; if reusable, must also be added to the Codebase Patterns section)
- Corrections added (list here; must already exist in the Corrections section — if not, add them there now)
---
```

Note: The Corrections and Codebase Patterns sections at the top of the file are the canonical reference. Progress entries provide a chronological record and should cross-reference what was added to those sections, not replace them.

## Corrections

Maintain a `# Corrections` section at the VERY TOP of `progress.md`, above Codebase Patterns. This is a flat lookup table of mistakes that have already been made and their fixes. Every iteration must read this section before doing any work, and must never repeat a listed mistake.

Each entry follows this format — short, scannable, no prose:

```
- ❌ `python manage.py migrate` → ✅ `python3 manage.py migrate` (system has no `python` alias)
- ❌ `import { foo } from 'lib'` → ✅ `import { foo } from 'lib/index.js'` (ESM requires explicit extensions)
- ❌ Creating migration without IF NOT EXISTS → ✅ Always use IF NOT EXISTS (prevents re-run failures)
- ❌ Running tests with `npm test` → ✅ `npm run test:unit` (project uses separate test scripts)
- ❌ UNRESOLVED: [description of issue that couldn't be fixed after 3 attempts]
```

**When to write a correction:** Any time you encounter an error, a failed command, a wrong assumption, or a workaround — anything where your first attempt was wrong and you had to adjust. Write it immediately when it happens, not at the end of the task.

**What makes a good correction:**
- Wrong CLI command or binary name
- Missing flags, env vars, or config needed for a command to work
- Import path or module resolution issues
- API or library usage that differs from what you assumed
- File paths or naming conventions you got wrong
- Build/test/lint commands that need specific arguments
- Platform-specific gotchas (OS, runtime version, etc.)
- Any assumption that turned out to be false

## Codebase Patterns

Maintain a `# Codebase Patterns` section in `progress.md`, immediately below the Corrections section. These patterns are critical — they prevent future iterations from repeating mistakes or deviating from established conventions.

Only record patterns you actually encounter or use during implementation. The categories below are a reference for what kinds of patterns to watch for — do not try to fill them all out proactively:

**Project Structure & Modules**
- File/folder naming conventions (kebab-case, PascalCase, etc.)
- Where new files of each type should go (components, services, utils, handlers, etc.)
- Module/package organization (barrel exports, index files, __init__.py, mod.rs, etc.)
- Monorepo structure (which packages depend on which, shared libs)

**Language & Type System**
- Preferred language idioms (e.g., guard clauses vs nested ifs, early returns)
- Type annotation style (interfaces vs types in TS, type hints in Python, generics usage)
- Null/optional handling (Optional<T>, Maybe, nullable types, Result/Either patterns)
- Enum patterns (string enums, const objects, sealed classes)
- Async patterns (async/await, Promises, Futures, goroutines, channels)

**Error Handling**
- Custom error classes/types and hierarchy
- How errors propagate (thrown exceptions, Result types, error codes, middleware)
- Logging conventions (structured logging, log levels, which logger library)
- User-facing vs internal error messages

**Data & State**
- Database migration conventions (IF NOT EXISTS, up/down migrations, naming)
- ORM/query patterns (repository pattern, active record, raw queries)
- State management approach (Redux, Zustand, Vuex, signals, MobX, context, providers)
- Data validation (schemas, decorators, guard functions, where validation lives)
- Serialization/deserialization patterns (DTOs, transformers, codable, serde)
- Caching strategy (what's cached, TTLs, invalidation approach)

**API & Communication**
- API style (REST, GraphQL, gRPC, tRPC) and conventions (route naming, versioning)
- Request/response shapes and envelope patterns
- Authentication/authorization patterns (middleware, guards, decorators, policies)
- Client-server contract (shared types, generated clients, OpenAPI)
- Event/message patterns (pub/sub, event bus, message queues, webhooks)

**Frontend & UI**
- Component structure (functional vs class, composition patterns, slots/children)
- Styling approach (CSS modules, Tailwind, styled-components, SCSS, utility classes)
- Form handling (controlled/uncontrolled, form libraries, validation)
- Routing patterns (file-based, config-based, nested routes, guards)
- Accessibility patterns the project follows (ARIA usage, focus management, semantic HTML)
- Internationalization approach (i18n library, key naming, where translations live)

**Backend & Infrastructure**
- Dependency injection approach (constructor injection, containers, providers)
- Middleware/interceptor patterns and ordering
- Background job/worker patterns
- Configuration management (env vars, config files, secrets handling)
- Database connection and transaction patterns

**Testing**
- Test file location and naming (co-located, __tests__, .spec vs .test)
- Test setup/teardown patterns (fixtures, factories, builders, seeds, mocks)
- Mocking approach (which libraries, what gets mocked, test doubles)
- Assertion style (expect, assert, should)
- How to run tests (commands, flags, environment variables needed)
- Integration/E2E test conventions

**Build & Tooling**
- Build commands and flags that work
- Environment-specific gotchas (env vars, feature flags, platform differences)
- Linting/formatting commands and any suppressions in use
- Code generation steps (protobuf, GraphQL codegen, ORM models, OpenAPI)

## Stop Condition

After completing your one task, check if ALL tasks in `tasks.md` are marked `[X]`.

If all tasks are complete:

1. Build an HTML page at `.kiro/specs/SPECS_NAME/summary.html` that presents a readable, multi-pane summary of the entire spec implementation. The page should be a single self-contained HTML file (inline CSS and JS, no external dependencies). The page should be styled against the https://kiro.dev web site. Structure it as follows:

   **Page title:**
   - Use "Ralph Loop for Kiro Specs" as the static page title (in `<title>` and as the main heading).

   **Top pane — Global Summary:**
   - Display the spec name (SPECS_NAME) prominently as a field in this pane.
   - Show a visual status indicator: green if all tasks are marked `[X]` (fully implemented), red if any tasks are marked `[F]` or unchecked (partial/failed).
   - If green: show the total elapsed time for the entire flow (sum of all task durations from `specs_time.md`), the number of tasks completed, and the date range (first task start to last task end).
   - If red: show how many tasks completed vs total, which tasks failed or remain incomplete, and any unresolved corrections from `progress.md`.
   - Show counts for files changed, corrections logged, and patterns discovered — but display only the counts as summary numbers. The full details of corrections and patterns should be hidden behind collapsible `<details>/<summary>` elements that the user can expand if they want to dig in. Keep the default state collapsed.

   **Left pane — Task Tree:**
   - Render the task list from `tasks.md` as a collapsible tree. Top-level tasks are tree nodes; subtasks are nested children. 
   - Each node should be expandable/collapsible (click to toggle). It should be explicit if a tree node has children or not.
   - On mouse hover over any task or subtask, show a tooltip or popover with the relevant progress details from `progress.md` for that task: what was implemented, files changed, tools used, patterns discovered, and corrections added. Match tasks to progress entries by task ID.
   - Use visual indicators for task status: `[X]` = completed, `[F]` = failed, unchecked = incomplete.

   **Right pane — Timing:**
   - Render the timing data from `specs_time.md` as an HTML table (task ID, start time, end time, elapsed time).

   **Styling:**
   - Clean, modern CSS. Use a side-by-side layout (e.g., flexbox) with the task tree taking roughly 60% width and the timing table taking 40%.
   - The tooltip/popover should be readable and not clip off-screen.

2. Reply with:
   ```
   <promise>COMPLETE</promise>
   ```

If tasks remain, end normally after completing your one task.
