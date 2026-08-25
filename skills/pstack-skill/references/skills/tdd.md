# TDD bug fix

When fixing a bug with a clear cheap test path, make the broken behavior executable before touching production code: one focused regression test that fails before the fix and passes after. Do not force a test through broad harness setup, brittle mocks, slow e2e infrastructure, production-only state, or unrelated fixture churn; use the closest useful verification instead.

1. Understand the bug: intended behavior, current behavior, affected path, smallest observable reproduction.
2. Choose the narrowest executable check already used for that codepath (unit, component, integration, regression). No practical path: do not invent one just to satisfy the ritual.
3. Write the failing test first, encoding intended behavior rather than mirroring current implementation.
4. Run it before fixing. It must fail for the intended reason; otherwise correct the test or repro first.
5. Make the smallest production change satisfying intended behavior while preserving nearby contracts.
6. Rerun the regression test; it passes now.
7. Run nearby validation: adjacent tests, type checks, lint, scenario checks for broader-risk changes.

## When a failing test is impractical

Never silently skip the regression step: state why a failing test is not worth the cost, then pick the closest executable check (targeted script, manual repro command, browser automation, snapshot comparison, log assertion).

Prefer no new test over a bad test: one that mostly tests mocks, encodes implementation details, depends on timing or global state, or needs expensive infrastructure per fix.

## Guardrails

- Do not change tests merely to match a wrong implementation.
- Do not weaken assertions unless expected behavior genuinely changed, with a clear reason.
- Flaky bug: make the test deterministic where possible; document the signal locked down.
- Broader class of failures exposed: land the focused regression path first, consider sibling coverage after.

**Report:** failing-before evidence verbatim, passing-after run, nearby validation. If failing-before could not be shown, say why and name the closest check used.
