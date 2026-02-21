---
name: geo-optimization
description: Optimizes digital content and marketing strategies for Generative Engines (LLMs, AI agents) to maximize citations. Use when the user wants to improve visibility in AI responses (ChatGPT, Perplexity, Google AI Overview), needs a GEO/AEO strategy, wants to measure citation rate, align terminology for LLMs, audit current pages for AI, or create optimized pages (such as roundups and FAQs).
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-02-20
  repository: https://github.com/fabricioctelles/skills
---

# GEO Optimization (Generative Engine Optimization)

This skill provides strategies to make brands, products, and content consistently cited by LLMs (ChatGPT, Google AI Overview, Perplexity, Grok, Claude, Gemini). Based on insights extracted from X and the Product Hunt 2026 case study.

## Guiding Principles

- **AI Visibility is measurable**: Treat it like SEO, measure the citation % (Citation Rate).
- **Terminology drives retrieval**: Align the title with how users ask LLMs.
- **Authority beats volume**: One high-signal page is worth more than dozens of weak pages.
- **Authentic community is the new gold**: Real reviews and discussions (Product Hunt, Reddit) are the strongest signal.
- **Models are volatile**: Monitor continuously, as model updates change visibility.
- **Traditional SEO + Structured Data are still the foundation**: JSON-LD and schemas remain essential.

## Quick Actions Menu

When starting the interaction, offer these options to the user to guide the work:

1. **Full GEO Audit**: Analyze the current page, deliver a score and a prioritized roadmap.
2. **Roundup Page Builder**: Create a comparison page optimized for LLMs.
3. **Terminology Optimizer**: Generate new titles, metas, and headings aligned with LLM searches.
4. **FAQ + Schema Generator**: Create a complete set of FAQs with schema markup.
5. **Community Signal Booster**: Structure a strategy to generate reviews on Product Hunt and Reddit.
6. **Citation Rate Test Kit**: Create 50 ready-made prompts for visibility measurement.
7. **FULL PACKAGE**: All of the above in a complete optimization package - Execute using Multi Agents.

## GEO Workflow

Execute the following steps according to the user's needs:

### 1. Measurement and Tracking (Initial Diagnosis)

Always start by evaluating the current state of visibility.
- Offer to create an initial set of 50–100 real prompts to test against ChatGPT, Google AI Overview, Perplexity, and Grok.
- Define the main metric: **Citation Rate** (% of responses that cite the brand/product).

### 2. Terminology Alignment

- Map how people actually ask LLMs (don't focus only on Google keywords).
- Adjust titles, meta descriptions, and headings to reflect this natural terminology.
- *Example*: Change from "AI dictation apps" to "AI dictation and speech-to-text software".

### 3. Page Format and Structure Selection

Recommend and create the formats that LLMs value most, such as **Roundup / Comparison pages** (e.g., "The best [category] in 2026").

When creating the page, include:
- Title optimized with LLM terminology.
- 8–12 products with authentic community reviews.
- Comparison table.
- Complete FAQ Schema.
- "What the community is saying" section (embed Product Hunt/Reddit).

### 4. Hard-to-Fake Signals & Community

- Guide the user to encourage real reviews and discussions on Product Hunt, Reddit, Quora.
- Suggest embedding or citing community content directly on the page.

### 5. Technical & Structured Data

Verify and implement the mandatory technical requirements:
- Add JSON-LD + FAQPage schema.
- Add Product schema (if applicable).
- Confirm that `robots.txt` allows AI bots (don't block Perplexity, ChatGPT, etc.).

### 6. Continuous Monitoring and Iteration

- Establish a routine of weekly tests or after model updates.
- Adjust terminology and add more community content according to model volatility.

## Edge Cases & Warnings

- Avoid purely self-promotional listicles (LLMs detect and penalize them).
- Monitor bot blocks (e.g., Perplexity temporarily blocked Product Hunt).
- Focus on the user's actual search channels (ChatGPT generally has more volume than Perplexity).
