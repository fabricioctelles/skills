# No comments

Strip comments from the diff before review. Spawn one read-only reviewer subagent (the comment killer) over the scope, audit its report skeptically, then fix accepted findings yourself.

The reviewer's rubric, passed verbatim:

- Flag every comment that narrates what the code does, restates the next line, or exists for the author's benefit while writing ("// increment counter", "// Phase 1: add cards"). These die. The assertion, log string, or test name is the only doc most code needs: write `assert(ok, 'persisted across restart')`, not a comment plus code.
- Flag verify/test scripts that narrate their phases.
- Keep only comments carrying a non-obvious *why* the code cannot show: a constraint from outside the repo, a warning about a non-obvious trap, a link to a governing issue. A keep survives only with proof it is about something we cannot change.
- Flag suppression comments (`eslint-disable`, `@ts-ignore`, `nolint`) for audit: correctness or safety suppressions stay actionable kills.
- Never edit application logic; read-only review, findings only.

## Steps

1. Scope: the caller's files or diff, else the working diff against the base branch.
2. Spawn the reviewer subagent with the rubric above. Do not restate its rules in the prompt beyond the scope.
3. Audit the report. Reject misapplied flags: intentional keeps with real proof stay; reshape-on-our-code-surprise flags stay actionable. If a kill is ambiguous, do not delete; if an ambiguous keep survives scrutiny twice, delete it.
4. Implement accepted deletions plus the smallest root-cause fix each finding points at ([fix-root-causes](../principles.md#fix-root-causes)); never bolt on symptom guards.
5. Constraint comments ("do not remove", "talk to X before changing") about things genuinely outside our control: leave them, offer the cheapest lint, runtime check, or CI rule that would enforce the constraint structurally instead ([encode-lessons-in-structure](../principles.md#encode-lessons-in-structure)). Approved encoding replaces the comment.
6. Report: deletion count, restored comments, fixes, encodings applied or offered, constraints left open.

Authoring agents defend their comments; that is why the reviewer runs first and fresh.
