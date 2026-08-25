# Create a verification skill

Every serious project needs a scripted way to drive the real app and prove behavior: launch it, exercise a feature the way a user would, capture evidence. Generate that as a project-local skill (`verify-<app>/` with a SKILL.md) tailored to the repo. Write it for the next agent reading cold, mid-task, never having seen the app.

## 1. Interview the repo, not the user

Answer from the codebase; ask only what cannot be observed:

- **Surface:** what does a user touch (web UI, CLI/TUI, desktop, API, mobile)? Pick the primary; note the rest.
- **Run:** how does the app start locally? Prefer the repo's own documented dev command. Note ports, env vars, seed data, auth.
- **Drive:** how can an agent interact programmatically? Existing harnesses first (Playwright specs, expect scripts, PTY helpers, curl-able endpoints, debug port), else a generic recipe: browser/CDP for web and Electron, tmux/PTY for CLI/TUI, plain HTTP for services.
- **Observe:** what evidence can be captured: screenshots, terminal transcripts, response bodies, logs, exit codes, DB state.
- **Isolate:** can two instances run side by side? If not, say so in the generated skill; refusing to double-drive beats corrupting the user's session.

If the checkout does not build or start as-is, fix that or report precisely before generating.

## 2. Generate the skill

Write `verify-<app>/SKILL.md` with frontmatter (`name: verify-<app>`, description naming app, surface, and when to reach for it) plus sections grounded in what the interview found, no placeholders:

- **Launch:** exact start command and readiness signal (log line, port answering, prompt); teardown included.
- **Doctor:** one read-only check answering "is this instance worth driving": process up, right version, port owned by us, auth valid.
- **Drive:** harness recipe with real selectors/commands from this repo; stable handles (ARIA labels, data attributes, route paths) over coordinates.
- **Evidence:** what to capture and where; proof standards: real user path not internal setters, action plus resulting state, side effects verified, dry-runs observed rather than trusted by name.
- **Cleanup:** tear down only instances you started; evidence survives teardown at a named location.
- **Helpers:** any shipped script is executable with invocation shown in the body.

## 3. Seed the feature map

Create `verify-<app>/features/README.md` plus one file per top user-facing feature (start with 3-5). Each answers from the user's POV: what it is, how to reach it, how to drive it with the harness, what observable end state proves it works. The map is the maintained verification source.

## 4. Prove the generated skill before handing over

Run its own instructions once end to end: launch, doctor, drive ONE mapped feature, capture evidence, clean up, confirm evidence survived cleanup. Fix failures and clean residue after every failed iteration too. A generated skill never executed is a draft, not a deliverable.

## 5. Offer the maintenance loop

Point at [maintain-verification-skill](maintain-verification-skill.md) for keeping the map honest as the app changes.
