# Council Rubric

Use this when selecting reviewers and judges.

## Roles

`reviewer`
: Gives notes only. It may improve quality, but it cannot declare a gate clean.

`judge`
: Gives a structured verdict. It can be used as a gate `verdict_source`.

## Selection Guidance

- Prefer a different model family from the host for blind-spot coverage.
- Prefer local models such as `ollama` when privacy matters more than judgment
  quality.
- Prefer a judge for gates that must block progress.
- Prefer a reviewer for brainstorming, adversarial notes, or tone critique
  where a deterministic pass/fail would be fake precision.
- Keep council scope small: `plan`, `delivery`, or specific paths.

## Gate Rule

`verdict_policy: revise_until_clean` requires `verdict_source` to be either a
judge member or `human`. A reviewer-only gate can use `fixed_passes`, but it
cannot honestly claim clean.

## Judge Rubric Tips

- Name the artifact being judged.
- Name the exact criteria IDs.
- Ask for blocking issues, not general commentary.
- Require the fenced JSON verdict first or last.
- Keep the judge prompt short enough that the artifact, not the instruction
  wrapper, dominates the context.

## Privacy Notes

Cross-vendor review can send project context to another CLI and vendor account.
Always name the destination, scope what it receives, apply redaction globs, and
require consent before the first send.

