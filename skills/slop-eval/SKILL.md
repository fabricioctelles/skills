---
name: slop-eval
description: >
  Objectively evaluate a UI/web design against the pols.dev anti-slop design
  law: detect catalogued slop tells with cited evidence, score 8 weighted
  axes (color, type, components, layout, motion, execution, signature,
  cohesion), and emit a Slop Report with a 0–100 Slop Index and grade. Use
  when the user asks to "evaluate design slop", "slop report", "is this
  design AI slop", "audit this landing page design", "de-slop review", or
  wants an objective score of how generic/machine-made a design looks. To
  fix text (not design), use human-ai or humanizar skills instead.
metadata:
  author: https://ft.ia.br
  version: "1.0.0"
  date: 2026-07-16
  repository: https://github.com/fabricioctelles/skills
  license: Apache-2.0
  category: code-quality-and-review
---

# Slop Eval

Evaluate a design the way `skill-evaluation` evaluates a skill: every finding
cites concrete evidence, every axis gets a 0–100 score, arithmetic runs
through a script, and the output is a structured report — never a vibe check.

The tell catalog lives in `references/tells.md`; read it before sweeping.
The positive rubric (signature formula, cohesion checks, slop→premium pairs)
lives in `references/premium-markers.md`; read it before scoring Axes 7–8.

## Source

- [The pols.dev anti-slop design law](https://pols.dev/slop.md) — the tell
  catalog, absolute rules, and signature formula are distilled from it.
- Method modeled on
  [skill-evaluation](https://github.com/fabricioctelles/skills/tree/main/skills/skill-evaluation)
  (cite-or-cut, weighted axes, scripted scoring, failure-mode diagnosis).

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `target` | What to evaluate: live URL, screenshot(s), code path, or Figma export | Ask user |
| `brief` | Brand brief or explicit user directions the design followed | None |
| `output` | Path to write the report | `./SLOP-REPORT.md` |

Write the report in the language the user is speaking; keep tell IDs and
names in English so they stay greppable against the catalog.

## Evidence channels

What you can verify depends on what you were given. Never score a check you
could not observe — mark it **Unverifiable** and exclude it (like N/A in
skill-evaluation).

| Channel | Can verify | Cannot verify |
|---------|-----------|---------------|
| Code (CSS/JSX/HTML) | Fonts, hex values, gradients, shadows, radii, `opacity:0` gating, icon imports, layout skeletons | Optical centering, rendered contrast, seams, whether controls respond |
| Screenshot(s) | Everything visual: palette, type, layout, alignment, centering, clipping, contrast, seams | Hover/scroll motion, dead controls, invisible-content trap, responsive behavior |
| Live URL (browse + screenshot) | All of the above plus interactions, motion, fold ownership | Only what you didn't exercise |

With code, grep before you stare: `fonts.googleapis|next/font`,
`lucide-react`, `linear-gradient`, `box-shadow`, `border-radius: *9999`,
`backdrop-filter`, `opacity: *0`, `initial={{ *opacity: *0`,
`overflow: *hidden`, `clip-path`, `position: *fixed`. Each hit is a lead,
not a verdict — confirm against the catalog entry before recording it.

## Evidence acquisition SOP

Route by what the `target` is; always end with an evidence inventory
(what was captured, what is Unverifiable) — it feeds the report header.

**Live URL** — the richest channel; prefer it whenever reachable.
Use whatever browser automation this session has (a browser MCP such as
Playwright or Chrome DevTools, or `npx playwright screenshot` as the
no-MCP fallback) and capture, saving every artifact to the scratchpad so
findings can cite `file + region`:

1. Load at desktop (1440×900) and mobile (390×844); wait for network idle.
2. Full-page screenshot of both viewports **immediately after load,
   before any scrolling** — sections sitting at `opacity:0` waiting for a
   scroll reveal show up blank here (M1 evidence).
3. Scroll pass top to bottom, then a second full-page capture; diff the
   two mentally for reveal-gated content, seams (C11, X13), and fold
   ownership (L16).
4. Interaction pass: hover the primary CTA, one card, one nav link
   (M2–M4); click every tab, accordion, toggle, and button (M8); Tab
   through the page and confirm a visible focus ring (X14).
5. Zoom crops at 2x of: anything near a clipped edge (X2), circled/tiled
   numbers and icons (X1), pricing columns side by side (X3), button
   labels (X5).
6. Pull the rendered sources for the code-channel greps: font names from
   the network panel or `<link>`/`@font-face`, computed hex values from
   the stylesheets.

No browser automation available → fetch the HTML/CSS (`curl`) and run the
code channel on it, ask the user for full-page desktop + mobile prints,
and mark every visual-only and interaction check Unverifiable until the
prints arrive. Never score a visual check from raw HTML.

**Screenshots** — Read each image. If only partial crops were provided,
ask for full-page desktop + mobile before sweeping (a hero-only print
cannot support L11, L15, or the cohesion axis). All interaction checks
(M1, M8, X14, hover tells) are Unverifiable.

**Code path** — run the greps, read every file they hit, plus the layout/
page components and global styles. If the project runs locally, start its
dev server and continue under the Live URL SOP — code plus a live render
is the only combination that can verify everything.

**Figma export** — treat as Screenshots for visual tells; additionally
fonts, hex values, and spacing are exact from the file. Motion and
interaction axes are Unverifiable (score `NA` for Axis 5 unless
prototypes were shared).

## Axes and weights

| # | Axis | Weight | Scored from |
|---|------|--------|-------------|
| 1 | Color & Light | 2x | Tells C1–C15 |
| 2 | Typography & Copy | 2x | Tells T1–T10, W1–W3 |
| 3 | Components & Ornament | 1x | Tells K1–K27 |
| 4 | Layout & Composition | 2x | Tells L1–L21 |
| 5 | Motion & Interaction | 1x | Tells M1–M8 |
| 6 | Execution & Craft | 2x | Tells X1–X14 |
| 7 | Signature & Uniqueness | 3x | 7-element formula (positive rubric) |
| 8 | Cohesion | 2x | 4 checks (positive rubric) |

Axis 7 carries the heaviest weight on purpose: the law's deepest rule is
that dodging the tell list is still slop — a page with zero tells and no
signature is unfinished work wearing restraint as an alibi.

## Scoring

**Axes 1–6 (tell-counted).** Count confirmed tells on the axis by severity,
then: `score = max(0, 100 − 30·critical − 15·major − 5·minor)`. Run
`scripts/score.py axis CRIT MAJOR MINOR` — don't do it by hand. One tell,
one count: a pattern repeated across sections is still one tell (note the
repetition in the evidence; repetition may upgrade minor → major where the
catalog says so).

**Axis 7 (Signature).** Score each of the 7 formula elements 0 (absent),
50 (attempted, weak), or 100 (strong) per the rubric in
`premium-markers.md`; the axis is their mean.

**Axis 8 (Cohesion).** Same 0/50/100 on the 4 cohesion checks; mean.

**Compounding rule.** Three or more *major* layout tells on one page cap
Axis 4 at 40 — a page assembled from known skeletons is slop no matter how
clean each block is.

**Gates** (pass as `--cap` to the overall run):
- **Signature gate:** Axis 7 < 40 caps the overall at 59 (grade C max). No
  amount of clean spacing rescues a page with no signature.
- **Absolute-rule gate:** any confirmed critical tell caps the overall at
  69 (no grade A with broken execution).

**Overall & Slop Index.**

```
overall    = sum(axis_score × weight) / sum(weight)   # capped by gates
Slop Index = 100 − overall
```

Run `scripts/score.py overall 1:80:2 2:65:2 ... [--cap 59] [--cap 69]`.
Unverifiable axes score `NA` and drop out of both sums. `--fail-below N`
exits non-zero for CI gating, e.g. gating a PR on its preview deploy:

```yaml
# .github/workflows/slop-gate.yml (step excerpt)
- name: Slop gate
  run: |
    # run slop-eval against $PREVIEW_URL, export each axis score, then:
    python3 skills/slop-eval/scripts/score.py overall \
      1:$A1:2 2:$A2:2 3:$A3:1 4:$A4:2 5:$A5:1 6:$A6:2 7:$A7:3 8:$A8:2 \
      --fail-below 40
```

## Grade scale

| Grade | Overall | Slop Index | Verdict |
|-------|---------|------------|---------|
| A | 80–100 | 0–20 | Premium — deliberate, signed, executed |
| B | 60–79 | 21–40 | Considered — mostly deliberate, some defaults |
| C | 40–59 | 41–60 | Generic — clean but templated or unsigned |
| D | 20–39 | 61–80 | Slop — assembled from presets |
| F | 0–19 | 81–100 | Pure slop |

## Absolute rules check

Six execution laws, each pass/fail/unverifiable, reported in their own
table. Any **fail** is a critical tell (counts on its axis AND triggers the
absolute-rule gate):

1. **Content visible by default** — nothing gated on an entrance animation
   (`opacity:0` + reveal) (M1)
2. **Clear the cut** — no text/control sliced by clip, notch, overflow, or
   fixed height (X2, X11)
3. **Parallel alignment** — comparable columns share baselines; buttons
   anchored (X3)
4. **Real centering** — everything meant to be centered is, mathematically
   and optically (X1)
5. **Legible contrast** — every text clears its background by a real value
   gap (X5)
6. **Controls work** — every interactive-looking control responds (M8)

## Workflow

1. **Gather evidence** — route the `target` through the Evidence
   acquisition SOP above. Done when the evidence inventory states what
   was captured and what is Unverifiable.
2. **Read `references/tells.md`** — the catalog you sweep against.
3. **Sweep axes 1–6** — walk the catalog group by group. **Cite-or-cut**:
   a tell is only recorded with concrete evidence (hex value, font name,
   `file:line`, or screenshot region); no evidence, no tell. Check each
   candidate against its premium-pair note — the crafted version of a
   pattern is not the tell. Done when every catalog group has been swept
   and every recorded tell carries a citation.
4. **Run the absolute rules check** — all six, pass/fail/unverifiable with
   evidence.
5. **Score Axes 7–8** — read `references/premium-markers.md`, score the 7
   signature elements and 4 cohesion checks with one-line justifications
   each. Done when all 11 items carry a score and a justification.
6. **Compute** — `score.py axis` per tell-counted axis, then
   `score.py overall` with weights and any triggered `--cap`. Never
   hand-compute.
7. **Write the report** — read `references/output-template.md` and emit
   exactly that structure to `output`, ending with the 3–5 prioritized
   fixes that would move the score most (biggest weighted deltas first;
   a missing signature usually outranks any single tell).

## Gotchas

- **The brief overrides the law.** If the user or brand explicitly directed
  a choice (a color, a layout, an effect), it is not a tell — the law
  itself says the user's word wins 100%. Ask for the brief when the design
  clearly follows one; note excluded tells in the report.
- **Context flips a tell.** Mono on real data is correct; a populated,
  real-feeling product window is a signature, not the fake-window tell; a
  tight micro-grid with texture is premium, a full-page graph paper is
  slop. Always check the premium pair before recording.
- **Don't reward the clean miss.** Zero tells with a weak signature is the
  most common failure of designs that *tried* to avoid slop. The signature
  gate exists for this — apply it without mercy.
- **Severity discipline.** Critical is reserved for *broken* (the six
  absolute rules). A blue-purple gradient is loud but not broken: major.
- **One-axis bleed.** Some tells could sit on two axes (cut-off glow is
  color and execution). The catalog assigns each tell to exactly one axis —
  count it only there.
- **Portfolio tells.** L19 (recycling your own house style) needs prior
  work from the same author to verify; without it, mark Unverifiable
  rather than guessing.

## Quality checklist

Final gate before delivering — each item re-checks a workflow step:

- [ ] every recorded tell has ID + severity + citation (step 3)
- [ ] every unverifiable check is marked, not silently passed (steps 1, 4)
- [ ] all 6 absolute rules reported (step 4)
- [ ] all 11 signature/cohesion items scored with justification (step 5)
- [ ] caps applied when gates triggered; math from `score.py` only (step 6)
- [ ] report matches the template, fixes ranked by weighted impact (step 7)
