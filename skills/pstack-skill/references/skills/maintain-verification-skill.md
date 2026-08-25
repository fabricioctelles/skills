# Maintain a verification skill

A feature map rots the moment the app changes. Upkeep loop for a project-local verification skill with a feature map. Unit of rigor: the feature, not every sentence.

Pick one outcome and say which: **clean** (full source and live coverage, nothing worth shipping, no PR), **changed** (one PR of proven corrections), or **blocked** (say exactly what blocked).

Edit scope: only the verification skill's own directory. Never edit product code during a run; behavior the map describes but the app no longer does is doc drift (fix map) or product regression (report, do not paper over in docs).

1. **Locate the target:** the project-local skill whose body has launch/drive sections and a feature map. Ambiguous candidates: ask. None: point at [create-verification-skill](create-verification-skill.md) instead of inventing one.
2. **Index hygiene:** read the map README and siblings; fix missing, extra, duplicate, dead entries.
3. **Source wave:** one read-only subagent per feature file, concurrent. Each explains how the feature works from source, flags likely drift with citations, returns one live-verification recipe. Children never drive the app nor edit files.
4. **Reconcile:** merge overlapping recipes into as few app states as practical; spot-check cited drift; sweep recent churn for unmapped user-facing surfaces (concrete source path required before calling one missing).
5. **Live pass:** required even when source looks clean. Coordinator owns all driving per the skill's launch model. Exercise every feature once. Invariants throughout: doctor before first drive and after any surprising failure; captured evidence survives every cleanup, checked at its named location; nothing a drive started outlives its usefulness. Unreachable features are `verified-unreachable` only with the concrete prerequisite named; a missing prerequisite in the map is drift.
6. **Triage:** wrong description = doc drift, fix. Harness cannot drive working behavior = harness gap, fix and re-prove live. App actually broken = product gap, record for the user, keep out of this PR.
7. **Ship or stop:** changed ships one PR of re-read proven corrections; clean or blocked report honestly without a PR.

Keep concise run notes in scratch; do not commit them.
