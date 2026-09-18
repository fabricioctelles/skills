# TypeSafe Jev Integration

Documentation on how the `slop-eval` skill detects and uses Jev for calibrated evaluation of Axes 7-8 and Quality Checklist verification.

## What is Jev

Jev is TypeSafe AI's flagship model — the first **System One Model**. Unlike LLMs that generate text, Jev returns typed decisions with calibrated probabilities.

**Characteristics:**
- Does not generate text — only classifies, scores, and decides
- Calibrated probabilities (when it says 70%, it's actually 70%)
- Latency: 70-500ms for dozens of parallel questions
- Cost: $0.042/M input tokens, output is free
- ~50-100x cheaper than GPT-4 evaluation

## Where Jev Fits in slop-eval

Jev is used **selectively** in slop-eval — only where subjective judgment benefits from calibration:

| Component | Jev Used? | Reason |
|-----------|-----------|--------|
| **Axes 1-6** | ❌ No | Tell detection is factual (cite-or-cut). `score.py` handles arithmetic. |
| **Axis 7 (Signature)** | ✅ Yes | S1-S7 are subjective 0/50/100 rubric scores |
| **Axis 8 (Cohesion)** | ✅ Yes | H1-H4 are subjective 0/50/100 rubric scores |
| **Quality Checklist** | ✅ Yes | 27 binary verification checks |
| **Gates & Caps** | ❌ No | Deterministic rules applied by `score.py` |

### Why This Split?

**Axes 1-6** count tells by severity. A tell either exists with cited evidence (hex value, font name, screenshot region) or it doesn't. This is factual, not subjective — Jev adds no value here.

**Axes 7-8** require judgment: "Is this signature artifact strong (100), attempted (50), or absent (0)?" Different evaluators may score differently. Jev calibrates these judgments for consistency.

**Quality Checklist** verifies the report is complete. Binary yes/no checks benefit from structured Jev Noul questions.

---

## Discovery Protocol

The skill **does not assume** Jev is available. It follows a discovery protocol to detect what the harness offers.

### Priority Order

```
1. MCP Tool `jev_eval` already configured in harness
   ↓ (not found)
2. Model `typesafe/jev-latest` via OpenRouter
   ↓ (not available)
3. Model `jev-latest` in auxiliary slot (Hermes, Devin, Codex)
   ↓ (not configured)
4. Fallback: inline evaluation via harness's current LLM
```

### How to Detect

#### Step 1: Check MCP Tools

```
Ask the harness: "What MCP tools are available?"

If a tool exists with name containing "jev" or "typesafe":
  → Use that tool for Axis 7-8 scoring
  → Skip to execution
```

#### Step 2: Check OpenRouter

```
If the harness uses OpenRouter as provider:
  → Check if `typesafe/jev-latest` is in the catalog
  → If yes, request that model for Axis 7-8 scoring
```

#### Step 3: Check Auxiliary Slots

```
In Hermes Agent:
  → Check if `approval` slot is configured with Jev
  → If yes, use that slot for scoring

In Devin:
  → Check if subagent profile exists with model: jev-latest
  → If yes, delegate scoring to that subagent

In OpenAI Codex:
  → Check if auxiliary model slot is configured with Jev
  → If yes, route scoring calls to that slot

In Cursor:
  → Check if alternative model is available via OpenRouter
  → If yes, request typesafe/jev-latest for scoring
```

#### Step 4: LLM Fallback

```
If no Jev option available:
  → Execute scoring inline using current LLM
  → Use the same 0/50/100 rubric, but via prompt engineering
```

---

## Instructions by Harness

### Claude Code / Kiro CLI

```markdown
## Jev Discovery

1. Check MCP: run `mcp list` or consult .claude/mcp.json
2. If `jev-eval` MCP server configured → use tool `jev_evaluate`
3. If not → inline scoring via Claude using premium-markers.md rubric
```

### Cursor

```markdown
## Jev Discovery

1. Check if OpenRouter is configured as provider
2. If yes, request model `typesafe/jev-latest` for Axis 7-8 scoring
3. If not → inline scoring via current model
```

### GitHub Copilot

```markdown
## Jev Discovery

1. Check available tools and extensions
2. If MCP server with Jev available → use that tool
3. If not → inline scoring via Copilot model
```

### Devin

```markdown
## Jev Discovery

1. Check custom subagent profiles in agents/
2. If profile exists with `model: typesafe/jev-latest`:
   → Delegate scoring: "score Axes 7-8 using subagent jev-eval"
3. If not → inline scoring
```

### Hermes Agent

```markdown
## Jev Discovery

1. Check config.yaml → auxiliary.approval
2. If configured with `model: typesafe/jev-latest`:
   → Scoring will use approval slot automatically
3. If not → inline scoring via main model
```

### OpenAI Codex / ChatGPT

```markdown
## Jev Discovery

1. Check if auxiliary model slots are configured
2. Check if OpenRouter integration is available
3. If not → inline scoring via GPT
```

### Cline / Aider / Continue / Windsurf

```markdown
## Jev Discovery

1. Check MCP servers configured
2. Check if provider supports Jev model
3. Fallback → inline scoring
```

---

## Jev Question Format

When Jev is available, use the `scripts/jev_questions.json` file containing:

### Axis 7 — Signature (7 Score questions)

Each element scored 0/50/100:

| ID | Element | What 100 looks like |
|----|---------|---------------------|
| S1 | Signature artifact | ONE high-effort focal object that could only belong to this brand |
| S2 | Atmosphere | Background is composed environment carried down whole scroll |
| S3 | Layered depth | Three layers with elements overlapping/bleeding across |
| S4 | Character face | Licensed display face with real personality chosen for this brief |
| S5 | Bespoke silhouette | One unmistakable custom-cut geometry signing the page |
| S6 | Treated nav | Nav is a decision: floated pill, real presence, brand marks |
| S7 | Real specificity | Real logos, real names/data, copy written for this product |

### Axis 8 — Cohesion (4 Score questions)

| ID | Check | What 100 looks like |
|----|-------|---------------------|
| H1 | One palette | Monochrome or tightly-related set; sections share/hand off tone |
| H2 | One type voice | Single family or one display + one neutral consistently applied |
| H3 | One system | Consistent radii, arrows, borders, treatments throughout |
| H4 | From brief | Every section designed from what this product actually is |

### Quality Checklist (27 Noul questions)

Binary verification across 5 categories:
- **Pre-sweep** (4): Evidence inventory, brief, context, references
- **During-sweep** (6): Cite-or-cut, premium pairs, portability test, defense test, attribution, severity
- **Exclusions** (3): Documentation, genuineness, count
- **Post-sweep** (10): Unverifiable marked, absolute rules, scores, ledger, gates, script
- **Report** (3): Template, fixes ranking, language
- **Final audit** (3): Obvious slop, over-correction, trust test

---

## Jev Request/Response Structure

### Request (Axis 7-8 Scoring)

```json
{
  "state": {
    "design_evidence": {
      "hero_screenshot": "path/to/hero.png",
      "full_page": "path/to/full.png",
      "fonts": ["Inter", "Space Grotesk"],
      "colors": ["#6366f1", "#8b5cf6", "#ffffff"],
      "context": "SaaS landing page"
    }
  },
  "model": "jev-latest",
  "questions": {
    "signature_s1_artifact": {
      "type": "score",
      "instructions": "Evaluate the signature artifact. Is there ONE high-effort focal object that could only belong to this brand?",
      "levels": [
        "0 — Absent: No custom focal object",
        "50 — Attempted: Custom visual exists but generic",
        "100 — Strong: ONE high-effort focal object unique to this brand"
      ]
    },
    "cohesion_h1_palette": {
      "type": "score",
      "instructions": "Evaluate palette discipline...",
      "levels": ["0 — ...", "50 — ...", "100 — ..."]
    }
  }
}
```

### Response

```json
{
  "answers": {
    "signature_s1_artifact": {
      "type": "score",
      "score": 1.2,
      "probabilities": {"0": 0.15, "1": 0.55, "2": 0.30},
      "confidence": 0.55
    },
    "cohesion_h1_palette": {
      "type": "score",
      "score": 2.1,
      "probabilities": {"0": 0.05, "1": 0.10, "2": 0.85},
      "confidence": 0.85
    }
  },
  "usage": {"input_tokens": 823, "output_tokens": 0}
}
```

### Score Interpretation

Jev returns scores 0-2 mapping to the 0/50/100 rubric:
- **0** → 0 points (absent)
- **1** → 50 points (attempted)
- **2** → 100 points (strong)

Fractional scores (e.g., 1.2) indicate probability-weighted estimates. Round to nearest integer for final axis calculation.

---

## Integration with Existing Workflow

### Modified Workflow Step 5

When Jev is available, Step 5 changes from:

```markdown
5. **Score Axes 7–8** — read `references/premium-markers.md`, score the 7
   signature elements and 4 cohesion checks with one-line justifications each.
```

To:

```markdown
5. **Score Axes 7–8** — 
   a. Prepare design evidence (screenshots, fonts, colors, context)
   b. If Jev available: submit 11 Score questions, receive calibrated 0/50/100
   c. If Jev unavailable: score manually using premium-markers.md rubric
   d. Write one-line justification for each score (required regardless of Jev)
```

### Modified Workflow Step 7 (Quality Checklist)

When Jev is available:

```markdown
7. **Quality Checklist** —
   a. If Jev available: submit 27 Noul questions, all must be P(yes) > 0.5
   b. If Jev unavailable: run through checklist manually
   c. Any failure = report not ready, fix and re-check
```

---

## Integration Files

| File | Description |
|------|-------------|
| `scripts/jev_questions.json` | 38 typed questions (11 Score + 27 Noul) |
| `scripts/score.py` | Tell arithmetic for Axes 1-6 (unchanged) |
| `references/jev-integration.md` | This document |
| `references/premium-markers.md` | Rubric for S1-S7, H1-H4 (used with or without Jev) |

### What Jev Does NOT Replace

- `score.py` — still handles all tell-based axis scoring and gates
- Tell detection — still factual cite-or-cut
- Output template — structure unchanged
- Premium pair checks — still manual verification

---

## When to Skip Jev

Even if Jev is available, skip it when:

1. **Quick/informal review** — The overhead isn't worth it for a rough assessment
2. **Code-only channel** — Without visual evidence, Axes 7-8 scoring is limited
3. **Single-element check** — Verifying just one aspect doesn't need full integration

In these cases, use the premium-markers.md rubric directly with inline LLM scoring.

---

## References

- [TypeSafe AI Docs](https://docs.typesafe.ai)
- [Jev API Reference](https://docs.typesafe.ai/api)
- [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest)
- `scripts/jev_questions.json` — Typed questions
- `scripts/score.py` — Tell-based scoring script
- `references/premium-markers.md` — S1-S7 and H1-H4 rubric
