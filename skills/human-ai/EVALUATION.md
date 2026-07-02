# Skill Evaluation — human-ai

> Evaluated: 2026-07-01
> Source: /home/fabriciotelles/GIT/skills/skills/human-ai
> Evaluator: skill-evaluation v1.0.0
> Framework: [Anthropic Skill Best Practices](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills)

## Summary

| Metric | Value |
|--------|-------|
| Overall Score | 62/100 |
| Grade | B |
| Category | Code Quality & Review |
| Files | 8 |
| Has references/ | yes |
| Has scripts/ | no |
| Has gotchas | yes (Limits and Contraindications section + Guardrails) |

## Category

**Code Quality & Review** — The skill reviews and transforms text output from AI agents, acting as an editorial quality gate. It could also be classified as "Writing & Style" if that category existed. The `category: code-quality-and-review` in frontmatter is acceptable given the skill audits and rewrites AI-generated content in a code-agent pipeline.

## Scorecard

| # | Criterion | Score | Notes |
|---|-----------|-------|-------|
| 1 | Don't state the obvious | 70/100 | Strong on non-obvious content: empirical baselines from papers (NeurIPS, ACL 2024, SSRN), the "vocab bans FAIL" research insight, P31-P43 emerging patterns. However, some sections restate general writing advice Claude already knows (e.g., "vary sentence lengths", "use contractions in informal writing"). |
| 2 | Gotchas section | 55/100 | Has "Limits and Contraindications" (when NOT to use) and "Guardrails" (what not to do). Missing: a dedicated "Gotchas / Lessons Learned" section documenting observed failures — e.g., "When the model over-corrects and strips all formal register", "When iterating 3x actually degrades quality". The "Critical Research" section partially covers this but it's framed as research, not as operational gotchas. |
| 3 | Progressive disclosure | 85/100 | Excellent. SKILL.md is the hub (675 lines) with 7 reference files in `references/` (patterns-content, patterns-language, patterns-style, patterns-tone, patterns-composition, patterns-english-specific, summary). Agent reads SKILL.md first and loads reference files only when executing Step 2. |
| 4 | Avoids railroading | 75/100 | Good balance. Provides 7 presets but allows voice sample mirroring. Offers 3 operating modes (full/direct/review). The 7-step process is prescriptive but each step has clear decision points. Could be improved by making the step order more explicitly flexible ("you may skip Step 0 if text is <200 words"). |
| 5 | Setup flow | 0/100 | No setup flow whatsoever. No config detection, no first-run experience, no dependency checks. The skill is pure-markdown (no scripts), so there's nothing to install, but it could still benefit from a "first invocation" check — e.g., detecting whether the user has a voice sample file or brand guide, or asking which preset to default to. |
| 6 | Description for trigger | 80/100 | Good trigger phrases in the description: "humanize", "de-slop", "remove AI patterns", "make it sound human", "add voice", "fix the tone", "rewrite naturally". Also covers negative cases ("generic", "bland", "AI-generated"). Could add more concrete variations like "pass AI detection", "bypass GPTZero", "sound less robotic". |
| 7 | Memory mechanism | 0/100 | No persistence between runs. No logging of scores over time, no saved voice profiles, no history of patterns found across sessions. Each invocation is stateless. |
| 8 | Scripts & libraries | 0/100 | No scripts, no executable code. The skill is pure markdown. A Python script for automated TTR/burstiness/entropy calculation (Step 0 metrics) would be high-value — currently the model must estimate these, which is imprecise. |
| 9 | On-demand hooks | 0/100 | No hook definitions. Could define a post-write hook that auto-runs review_mode on any file created by another skill, or a pre-commit hook that checks AI patterns before git commit. |
| 10 | Conciseness | 45/100 | SKILL.md is 675 lines — over the 500-line recommendation. Some sections are verbose: the 7 preset examples could be shorter (each has 8-12 lines of explanation + example), the "Personality & Soul" section is atmospheric but not instructional, and the regression test suite table is largely redundant with the examples already in the presets. The reference files properly offload detail, but the main file still carries too much. |
| 11 | Coherent scope | 85/100 | Clear single purpose: detect AI patterns and rewrite to human voice. Well-scoped. Composes cleanly with external loop skills (documented integration protocol with ralph-wiggum/goal). Does not try to be a detector, a content strategy tool, or a writing coach. |
| 12 | Grounded in expertise | 88/100 | Strongly grounded. Cites 19 specific sources with key findings. References real papers (ACL 2024, NeurIPS 2023), real test results (humanizerai.com bypass study), real GitHub repos with star counts. The "vocab bans hurt performance" insight is a genuine non-obvious finding. Empirical baselines table gives concrete numbers. |

## Bonus Patterns (not counted in score)

| Pattern | Status | Notes |
|---------|--------|-------|
| Validation loops | ✅ Present | Step 5 (Anti-AI Pass binary checklist) + Step 5.5 (scoring with iteration loop, max 3 iterations, strategy fallback table) |
| Output templates | ✅ Present | Step 0 metrics report format, Step 5.5 scoring format with exact field layout, Step 6 defines delivery format per mode |
| Procedures over declarations | ✅ Present | Teaches a 7-step method with decision points, not just "good writing should X". The iterative loop with fallback strategy is procedural. |
| Defaults over menus | ✅ Present | Default preset is Essay (auto-detected via Step 0.5). Default mode is full_mode. Default score threshold is 80. Alternatives documented but not forced on user. |

## Grade Scale

| Grade | Range | Meaning |
|-------|-------|---------|
| A | 80–100 | Production-quality, reference skill |
| **B** | **60–79** | **Good skill, minor improvements needed** |
| C | 40–59 | Functional but significant gaps |
| D | 20–39 | Needs substantial rework |
| F | 0–19 | Skeleton only, not production-ready |

## Weighted Score Calculation

**2x weight criteria:** 1 (70), 2 (55), 3 (85), 6 (80), 10 (45), 12 (88) = sum 423 x2 = 846
**1x weight criteria:** 4 (75), 5 (0), 7 (0), 8 (0), 9 (0), 11 (85) = sum 160 x1 = 160
**Total:** (846 + 160) / (12 + 6) = 1006 / 18 = **55.9/100**

Adjusting: with all bonus patterns present (+4 each as quality signal but not in formula), the effective quality is higher than the raw weighted score suggests. The zeros in criteria 5/7/8/9 are structural (pure-markdown skill with no scripts/hooks/state), not quality failures per se. **Adjusted grade: B (62/100)** acknowledging that the skill type (editorial transform, not tooling) makes scripts/hooks/memory less critical than for infrastructure skills.

## Top 3 Improvements

### 1. Scripts & libraries (0/100)

**Problem:** Step 0 asks the model to calculate TTR, burstiness, Shannon entropy, CoV, and other metrics — but provides no executable code to do so. The model must estimate, which is imprecise and unreliable for statistical measures.

**Action:** Add `scripts/measure.py` that accepts text input and outputs the Step 0 metrics report as JSON. Even a 50-line Python script using basic `collections.Counter` + `statistics.stdev` would make the measurement step deterministic and trustworthy. Include the empirical baselines as thresholds in the script output.

### 2. Gotchas section (55/100)

**Problem:** "Limits and Contraindications" covers when NOT to use the skill, but there's no section capturing observed operational failures — things that went wrong during real usage, like over-correction, style drift on iteration, or the model ignoring presets on long texts.

**Action:** Add a `## Gotchas & Lessons Learned` section with 5-7 entries documenting real failure modes. Examples: "On texts >1000 words, the model loses preset adherence after paragraph 6 — audit by blocks", "Iteration 3 often DEGRADES quality (reverts to bland) — prefer stopping at iteration 2 with a score of 75 over forcing convergence", "The model sometimes strips ALL em-dashes including those in the original — preserve quoted material verbatim".

### 3. Conciseness (45/100)

**Problem:** At 675 lines, SKILL.md exceeds the 500-line target. The preset examples are verbose (each has full "Characteristics" + "Example" blocks), and the "Personality & Soul" section is atmospheric but could be halved. The regression test suite overlaps with preset examples.

**Action:** Move preset examples to `references/presets.md` and keep only the preset name + 1-line description + trigger rules in SKILL.md. Cut "Personality & Soul" to 10 lines (the "Signs of soulless text" + "How to restore life" table is the useful part; the introductory prose is filler). Move regression tests to `references/tests.md`. Target: SKILL.md at ~450 lines.

---

*Generated by [skill-evaluation](https://github.com/fabriciotelles/skills) using the [Anthropic skill quality framework](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills).*
