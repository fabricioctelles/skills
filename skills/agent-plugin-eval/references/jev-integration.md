# Jev Integration for Agent Plugin Eval

## Overview

This skill integrates with [TypeSafe Jev](https://github.com/AugmentHCI/typesafe-jev) for subjective quality evaluation of agent plugins. Jev provides calibrated probability judgments (Score) and categorical classifications (Noul) that augment the deterministic checks in `inspect_plugin.py`.

## When to Use Jev

| Evaluation Type | Use Jev? | Rationale |
|-----------------|----------|-----------|
| **Axes 1-3 Conformance** | No | Deterministic checks (JSON validity, schema presence, field existence) |
| **Axis 4 Product Quality** | **Yes (Score)** | Subjective assessment of UX, documentation clarity, error handling |
| **Axis 2 Quality Criteria** | **Yes (Score)** | Schema design elegance, naming consistency, API coherence |
| **Gate Classification** | **Yes (Noul)** | Categorical pass/fail on structure, coherence, validity |
| **Secret Detection** | **Yes (Noul)** | Pattern-based suspicion (confirmed requires external scanner) |
| **Quality Checklist** | **Yes (Noul)** | Present/missing classification for files |

## Discovery Protocol

Before invoking Jev, check availability:

```python
from typesafe import jev_available

if jev_available():
    from typesafe import Score, Noul
    # Use Jev for subjective criteria
else:
    # Fall back to heuristic scoring
```

## Question Categories

### Score Questions (0.0-1.0 probability)

Used for quality dimensions where gradations matter:

| ID | Axis.Criterion | Evaluates |
|----|----------------|-----------|
| `ux_coherence` | 4.6 | Tool interaction coherence |
| `documentation_clarity` | 4.8 | Docs completeness and clarity |
| `error_handling_quality` | 4.9 | Error message quality |
| `input_validation_robustness` | 2.15 | Validation thoroughness |
| `schema_design_quality` | 2.16 | Schema design quality |
| `naming_consistency` | 2.17 | Naming conventions |
| `api_design_elegance` | 2.18 | API simplicity and elegance |

### Noul Questions (categorical labels)

Used for binary or few-class decisions:

| Category | Questions | Labels |
|----------|-----------|--------|
| **Gates (G1-G4)** | 4 | conformant/valid/coherent vs malformed/invalid/incoherent |
| **Secrets** | 4 | suspected / not_suspected |
| **Quality Checklist** | 7 | present / missing |
| **Component Validity** | 4 | valid / invalid / missing |

## Integration Points

### 1. Score Integration (Axis 2 & 4)

```python
def evaluate_quality_with_jev(context: dict) -> dict:
    """Evaluate subjective quality criteria using Jev Score."""
    if not jev_available():
        return heuristic_quality_score(context)

    from typesafe import Score

    scores = {}
    questions = load_jev_questions()["questions"]["score"]

    for q in questions:
        ctx = extract_context(context, q["context_required"])
        result = Score(q["question"], context=ctx)
        scores[q["id"]] = {
            "probability": result.probability,
            "axis": q["axis"],
            "criterion": q["criterion"]
        }

    return aggregate_axis_scores(scores)
```

### 2. Gate Classification (Noul)

```python
def classify_gates_with_jev(context: dict) -> dict:
    """Classify conformance gates using Jev Noul."""
    if not jev_available():
        return deterministic_gate_check(context)

    from typesafe import Noul

    gates = {}
    questions = [q for q in load_jev_questions()["questions"]["noul"]
                 if "gate" in q]

    for q in questions:
        ctx = extract_context(context, q["context_required"])
        result = Noul(q["question"], labels=q["labels"], context=ctx)
        gates[q["gate"]] = {
            "label": result.label,
            "passed": result.label == q["labels"][0]  # First label is positive
        }

    return gates
```

### 3. Secret Detection (Noul)

```python
def detect_secrets_with_jev(context: dict) -> dict:
    """Flag potential secrets for human review using Jev Noul."""
    if not jev_available():
        return regex_secret_scan(context)

    from typesafe import Noul

    findings = {}
    questions = [q for q in load_jev_questions()["questions"]["noul"]
                 if q.get("category") == "secrets"]

    for q in questions:
        ctx = extract_context(context, q["context_required"])
        result = Noul(q["question"], labels=q["labels"], context=ctx)
        findings[q["id"]] = {
            "suspected": result.label == "suspected",
            "confidence": result.probability
        }

    # Flag for human review if any suspected
    return {
        "findings": findings,
        "requires_review": any(f["suspected"] for f in findings.values())
    }
```

## Score Aggregation

Jev Score returns probabilities [0.0, 1.0]. Map to rubric scores:

```python
def aggregate_axis_scores(scores: dict, max_per_axis: int = 25) -> dict:
    """Aggregate Jev scores to rubric scale."""
    axis_scores = {}

    for axis_num in [2, 4]:
        axis_items = [s for s in scores.values() if s["axis"] == axis_num]
        if axis_items:
            avg_prob = sum(s["probability"] for s in axis_items) / len(axis_items)
            axis_scores[f"axis_{axis_num}"] = round(avg_prob * max_per_axis, 1)

    return axis_scores
```

## Fallback Behavior

When Jev is unavailable, the skill falls back to:

1. **Quality scoring**: Heuristic checks (file existence, size, pattern matching)
2. **Gate classification**: Deterministic JSON/schema validation
3. **Secret detection**: Regex pattern matching (high false positive rate)

The fallback is functional but less nuanced than Jev evaluation.

## Context Preparation

Each question specifies required context. Extract from plugin repository:

```python
CONTEXT_EXTRACTORS = {
    "plugin_manifest": lambda repo: read_file(repo, "plugin.json"),
    "tool_definitions": lambda repo: extract_tools(repo),
    "readme": lambda repo: read_file(repo, "README.md"),
    "skill_files": lambda repo: glob_read(repo, "**/SKILL.md"),
    "source_files_sample": lambda repo: sample_source(repo, max_files=10),
    "file_listing": lambda repo: list_files(repo),
    # ... etc
}
```

## Output Format

Jev-enhanced evaluation adds a `jev` section to the report:

```json
{
  "score": 78,
  "axes": { ... },
  "gates": { ... },
  "jev": {
    "available": true,
    "quality_scores": {
      "ux_coherence": 0.72,
      "documentation_clarity": 0.85,
      ...
    },
    "gate_classifications": {
      "G1": {"label": "conformant", "passed": true},
      ...
    },
    "secret_findings": {
      "requires_review": false,
      "findings": { ... }
    }
  }
}
```

