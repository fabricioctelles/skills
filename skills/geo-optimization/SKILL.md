---
name: geo-optimization
description: This skill should be used when the user wants to improve content visibility in AI-generated responses (ChatGPT, Perplexity, Google AI Overview, Grok, Claude, Gemini), needs a GEO/AEO strategy, wants to measure citation rate, align terminology for LLMs, audit existing pages for AI discoverability, or create optimized pages such as roundups and FAQs.
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
---

# GEO Optimization (Generative Engine Optimization)

## Quick Actions Menu

Present the following options at the start of the interaction to guide the work:

1. **Full GEO Audit**: Analyze the current page, deliver a score and a prioritized roadmap.
2. **Roundup Page Builder**: Create a comparison page optimized for LLMs.
3. **Terminology Optimizer**: Generate new titles, metas, and headings aligned with LLM searches.
4. **FAQ + Schema Generator**: Create a complete FAQ set with schema markup.
5. **Community Signal Booster**: Structure a strategy to generate reviews on Product Hunt and Reddit.
6. **Citation Rate Test Kit**: Create 50 ready-made prompts for visibility measurement.
7. **FULL PACKAGE**: Execute all of the above as a complete optimization package using Multi Agents.

Default to option 1 (Full GEO Audit) when no specific action is requested.

## GEO Workflow

Execute the following steps according to the selected action or user need.

For foundational principles that guide all optimization decisions, consult `references/guiding-principles.md`.

### 1. Measurement and Tracking (Initial Diagnosis)

Always begin by evaluating the current state of AI visibility.

- Create an initial set of 50–100 real prompts to test against ChatGPT, Google AI Overview, Perplexity, and Grok.
- Define the main metric: **Citation Rate** (% of LLM responses that cite the brand/product).

### 2. Terminology Alignment

- Map how people actually query LLMs — do not rely solely on Google keyword patterns.
- Adjust titles, meta descriptions, and headings to reflect natural LLM terminology.
- Example: Prefer "AI dictation and speech-to-text software" over "AI dictation apps".

### 3. Page Format and Structure

Recommend and create the formats that LLMs value most, prioritizing **Roundup / Comparison pages** (e.g., "The best [category] in 2026").

Include in each optimized page:
- Title aligned with LLM terminology.
- 8–12 products with authentic community reviews.
- Comparison table.
- Complete FAQPage schema.
- "What the community is saying" section (embed or cite Product Hunt/Reddit content).

### 4. Hard-to-Fake Signals and Community

- Encourage real reviews and discussions on Product Hunt, Reddit, and Quora.
- Embed or cite community content directly on the page to strengthen trust signals.

### 5. Technical and Structured Data

Verify and implement the required technical elements:
- Add JSON-LD + FAQPage schema.
- Add Product schema where applicable.
- Confirm `robots.txt` allows AI crawlers (do not block Perplexity, ChatGPT, etc.).

### 6. Continuous Monitoring and Iteration

- Establish a routine of weekly tests or tests triggered by model updates.
- Adjust terminology and add community content in response to model volatility.

## Quality Checklist

Before delivering any output, verify:

- [ ] Citation Rate baseline is defined or a test kit has been created.
- [ ] Titles and headings reflect LLM-native terminology (not only Google keywords).
- [ ] Page structure includes comparison table and FAQPage schema.
- [ ] Community signals (Product Hunt, Reddit) are referenced or embedded.
- [ ] `robots.txt` does not block major AI crawlers.
- [ ] JSON-LD schemas are present and valid.
- [ ] Monitoring cadence is defined (weekly or post-model-update).
- [ ] No purely self-promotional listicles were produced (LLMs detect and deprioritize them).
- [ ] Bot-blocking risks have been flagged (e.g., Perplexity has temporarily blocked some platforms).
