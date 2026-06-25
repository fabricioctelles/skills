# Verification Rubric

Use this when converting the user's definition of done into typed criteria.

## Taxonomy

`programmatic`
: A command or deterministic check returns pass/fail. Use this whenever
possible. Examples: tests, build, lint, schema validation, snapshot comparison,
or an extraction script that checks required headings.

`judge`
: A model scores a rubric and returns a structured verdict. Use this for
semantic quality that cannot be cheaply checked by code. The rubric must be
specific enough that a different model can apply it consistently.

`human`
: A person must sign off. Use this for taste, business judgment, private
knowledge, legal risk, or decisions where the user is the true authority.

## Required Fields

- Every criterion needs `id` and `type`.
- `programmatic` needs `check` as an argv array and `expect`.
- `judge` needs `rubric`.
- `human` needs `prompt`.

## Strong Criteria

- Check one thing at a time.
- Say what failure means.
- Prefer deterministic checks before model judgment.
- Make judge rubrics observable against artifacts the judge receives.
- Avoid relying on the host model to grade its own work.

## Anti-Patterns

- All criteria are judge or human criteria when tests or schema checks exist.
- "No errors thrown" as the only success criterion.
- Criteria that require hidden context not sent to the judge.
- Rubrics like "high quality" or "comprehensive" without dimensions.
- Programmatic checks written as shell strings instead of argv arrays.

## Structured Judge Contract

Judges should return a fenced JSON object:

```json
{
  "verdict": "pass",
  "blocking_issues": [],
  "confidence": 0.86,
  "notes": "The artifact satisfies the rubric."
}
```

Valid verdicts are `pass` and `revise`. If output cannot be parsed, the runner
will treat it as `revise` with a warning.

