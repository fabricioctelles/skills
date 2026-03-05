---
name: premium-proposal-builder
description: Creates and structures premium proposals, slide decks, and scrollable sites optimized for purchase decisions. Generates effective prompts for Lovable, Gamma, Pitch, Relume, and similar tools. Helps choose the right format (website vs deck), structure high-impact sections, and generate clear, reader-focused content. Use when the user wants to create a business proposal, improve a pitch, generate prompts for design tools, or adapt structure for different industries (agencies, SaaS, enterprise).
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  focus: B2B Sales, agencies, consulting, SaaS, marketing, enterprise
---

# Premium Proposal Builder

## Essential Principles

1. **Choose the format before the aesthetics** - Scrollable website or slide deck changes everything
2. **Clarity over design** - Buyers want certainty, not impressions
3. **Follow the buyer's mental model** - Not the order that looks nice
4. **Useful interactivity only** - Expanders, price toggles; never decorative
5. **Zero late surprises** - Crystal-clear scope and pricing prevent 80% of objections

## Parameters

| Parameter | Options | Default |
|-----------|---------|---------|
| `client_type` | agency, saas, enterprise, other | other (apply standard structure) |
| `delivery_mode` | async, live | async (scrollable website) |
| `tool` | Lovable, Gamma, Pitch, Relume, other | Gamma |
| `content_available` | brief, scope, pricing (any combination) | none (gather from user first) |

## Workflow

1. **Gather context** - Collect `client_type`, `delivery_mode`, `tool`, and any available content (brief, scope, pricing). If none provided, ask for them before proceeding.
2. **Choose format** - Use `delivery_mode` and `client_type` to select scrollable website or slide deck. Consult `references/proposal-formats-and-templates.md` for decision criteria and base prompts.
3. **Adapt structure** - Apply the client-type profile and section order. Consult `references/proposal-formats-and-templates.md` for the 9-section standard structure and per-profile variants.
4. **Generate prompts** - Produce tool-specific prompts (Lovable, Gamma, Pitch, etc.) tailored to the chosen format and client profile.
5. **Review before delivering** - Apply the quality checklist below before presenting output.

## Quality Checklist

- [ ] Format matches delivery mode (async → website; live → deck)
- [ ] Each section serves the buyer's decision, not the seller's narrative
- [ ] Scope section explicitly states what is included and excluded
- [ ] Pricing has no hidden items or late surprises
- [ ] CTAs are clear and immediately actionable
- [ ] Design guidance: max 2-3 main colors, 1 display + 1-2 body typefaces, generous spacing
- [ ] Interactivity is functional (expanders, toggles), never decorative

## References

- Consult `references/proposal-formats-and-templates.md` for format selection criteria, client-type profiles with adapted prompts, and the standard 9-section structure table.
