# TypeSafe Jev Integration

Documentation on how the `human-ai` skill detects and uses Jev for calibrated evaluation.

## What is Jev

Jev is TypeSafe AI's flagship model — the first **System One Model**. Unlike LLMs that generate text, Jev returns typed decisions with calibrated probabilities.

**Characteristics:**
- Does not generate text — only classifies, scores, and decides
- Calibrated probabilities (when it says 70%, it's actually 70%)
- Latency: 70-500ms for dozens of parallel questions
- Cost: $0.042/M input tokens, output is free
- ~50-100x cheaper than GPT-4 evaluation

## Why Use Jev in Evaluation Steps

| Aspect | LLM Evaluation | Jev Evaluation |
|--------|----------------|----------------|
| Consistency | Varies between calls | Deterministic |
| Calibration | P(70%) ≠ 70% actual | P(70%) = 70% actual |
| Cost | ~$0.01-0.05/evaluation | ~$0.0001-0.0002/evaluation |
| Latency | 1-5s | 70-500ms |
| Output | Text (requires parsing) | Native structured |

**Jev is ideal for diagnosis, verification, and scoring. The LLM continues doing the rewriting.**

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
  → Use that tool for evaluation
  → Skip to execution
```

#### Step 2: Check OpenRouter

```
If the harness uses OpenRouter as provider:
  → Check if `typesafe/jev-latest` is in the catalog
  → If yes, request that model for evaluation calls
```

#### Step 3: Check Auxiliary Slots

```
In Hermes Agent:
  → Check if `approval` slot is configured with Jev
  → If yes, use that slot for evaluation

In Devin:
  → Check if subagent profile exists with model: jev-latest
  → If yes, delegate evaluation to that subagent

In OpenAI Codex:
  → Check if auxiliary model slot is configured with Jev
  → If yes, route evaluation calls to that slot

In Cursor:
  → Check if alternative model is available via OpenRouter
  → If yes, request typesafe/jev-latest for evaluation
```

#### Step 4: LLM Fallback

```
If no Jev option available:
  → Execute inline evaluation using current LLM
  → Use the same criteria, but via prompt engineering
```

---

## Instructions by Harness

### Claude Code / Kiro CLI

```markdown
## Jev Discovery

1. Check MCP: run `mcp list` or consult .claude/mcp.json
2. If `jev-eval` MCP server configured → use tool `jev_evaluate`
3. If not → inline evaluation via Claude
```

### Cursor

```markdown
## Jev Discovery

1. Check if OpenRouter is configured as provider
2. If yes, request model `typesafe/jev-latest` for evaluation
3. If not → inline evaluation via current model
```

### GitHub Copilot

```markdown
## Jev Discovery

1. Check available tools and extensions
2. If MCP server with Jev available → use that tool
3. If not → inline evaluation via Copilot model
```

### Devin

```markdown
## Jev Discovery

1. Check custom subagent profiles in agents/
2. If profile exists with `model: typesafe/jev-latest`:
   → Delegate evaluation: "evaluate using subagent jev-eval"
3. If not → inline evaluation
```

### Hermes Agent

```markdown
## Jev Discovery

1. Check config.yaml → auxiliary.approval
2. If configured with `model: typesafe/jev-latest`:
   → Evaluation will use approval slot automatically
3. If not → inline evaluation via main model
```

### OpenAI Codex / ChatGPT

```markdown
## Jev Discovery

1. Check if auxiliary model slots are configured
2. Check if OpenRouter integration is available
3. If not → inline evaluation via GPT
```

### Cline / Aider / Continue

```markdown
## Jev Discovery

1. Check MCP servers configured
2. Check if provider supports Jev model
3. Fallback → inline evaluation
```

### Windsurf

```markdown
## Jev Discovery

1. Check Cascade's available models and tools
2. If Jev available via custom integration → use it
3. If not → inline evaluation via Cascade
```

---

## Jev Question Format

When Jev is available, use the `scripts/jev_questions.json` file containing:

### Diagnosis (51 Noul questions)

Each AI pattern mapped to binary question (P(yes) between 0-1):

| Category | Count | Example |
|----------|-------|---------|
| Composition | 9 | "Does the text announce what it will say, say it, then summarize?" |
| Tone | 14 | "Does the text use generic praise like 'Great question!'?" |
| Language | 9 | "Does the text overuse pompous AI vocabulary?" |
| Content | 5 | "Does the text turn mundane facts into revolution?" |
| Style | 7 | "Does the text use em-dash excessively as asides?" |
| English-Specific | 5 | "In informal context, does the text avoid ALL contractions?" |
| False Positive | 2 | "Does the text contain strong human authorship markers?" |

### Verification (4 Noul questions)

| Check | Critical | Question |
|-------|----------|----------|
| FACTUAL LOCK | ✓ | "Was any fact altered, added, or removed?" |
| Argument | ✓ | "Was author's argument and position preserved?" |
| Modality | ✓ | "Was modality preserved?" |
| Voice | | "Was opinion or first person improperly added?" |

### Evaluation (5 Score questions)

| Dimension | Weight | Levels |
|-----------|--------|--------|
| Pattern removal | 30% | 5 levels (0-20 to 81-100) |
| Naturalness | 25% | 5 levels |
| Factual completeness | 20% | 5 levels |
| Voice consistency | 15% | 5 levels |
| Readability | 10% | 5 levels |

---

## Jev Request/Response Structure

### Request

```json
{
  "state": {
    "source_text": "The original text...",
    "rewritten_text": "The candidate..."
  },
  "model": "jev-latest",
  "questions": {
    "composition_fractal_summaries": {
      "type": "noul",
      "instructions": "Does the text announce what it will say, say it, then summarize?",
      "labels": {
        "yes": "Contains fractal summaries",
        "no": "Direct flow"
      }
    },
    "score_naturalness": {
      "type": "score",
      "instructions": "Does the rewritten_text sound natural?",
      "levels": ["Very artificial (0-20)", "...", "Very natural (81-100)"]
    }
  }
}
```

### Response

```json
{
  "answers": {
    "composition_fractal_summaries": {
      "type": "noul",
      "noul": 0.23
    },
    "score_naturalness": {
      "type": "score",
      "score": 3.2,
      "probabilities": {"0": 0.02, "1": 0.05, "2": 0.15, "3": 0.48, "4": 0.30},
      "confidence": 0.78
    }
  },
  "usage": {"input_tokens": 1523, "output_tokens": 0}
}
```

---

## Result Interpretation

### Noul (Diagnosis/Verification)

- **P(yes) ≥ 0.5**: Pattern detected / Violation detected
- **P(yes) < 0.5**: Pattern absent / Verification passed

### Score (Evaluation)

- **Final score** = Σ(dimension × weight)
- **Converged**: score ≥ threshold (default: 80)

### Decisions

| Result | Action |
|--------|--------|
| FACTUAL LOCK violated | Discard candidate, return source_text |
| Argument altered | Discard candidate |
| Score < threshold | Iterate or return best_result |
| Score ≥ threshold | Converged, return candidate |

---

## Integration Files

| File | Description |
|------|-------------|
| `scripts/jev_questions.json` | 56 typed questions (Noul + Score) |
| `scripts/measure.py` | Statistical metrics (TTR, burstiness, entropy) |
| `references/jev-integration.md` | This document |

The `jev_questions.json` file contains all questions in the format expected by the Jev API. Harnesses with Jev access (via MCP, OpenRouter, or slots) can use this file directly to construct requests.

---

## References

- [TypeSafe AI Docs](https://docs.typesafe.ai)
- [Jev API Reference](https://docs.typesafe.ai/api)
- [OpenRouter - Jev](https://openrouter.ai/typesafe/jev-latest)
- `scripts/jev_questions.json` - Typed questions
- `scripts/measure.py` - Statistical measurement script
