---
name: premium-proposal-builder
description: Creates and structures premium proposals, slide decks, and scrollable sites optimized for purchase decisions. Generates effective prompts for Lovable, Gamma, Pitch, Relume, and similar tools. Helps choose the right format (website vs deck), structure high-impact sections, and generate clear, reader-focused content. Use when the user wants to create a business proposal, improve a pitch, generate prompts for design tools, or adapt structure for different industries (agencies, SaaS, enterprise).
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-02-20
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  focus: B2B Sales, agencies, consulting, SaaS, marketing, enterprise
---

# Premium Proposal Builder

This skill helps plan, structure, and generate high-perceived-value proposals that actually close bigger deals.

## Essential Principles

1. **Choose the format before the aesthetics** - Scrollable website or slide deck changes everything
2. **Clarity > pretty design** - Buyers want certainty, not impressions
3. **Follow the buyer's mental model** - Not the order you think looks nice
4. **Useful interactivity only** - Expanders, price toggles; never decorative
5. **Zero late surprises** - Crystal-clear scope and pricing prevent 80% of objections

## Decision Flow: Which Format?

### Scrollable Website when:
- Multiple decision-makers review asynchronously
- Will be forwarded internally
- Complex scope with variations
- Long cycle (cross-functional)

**Base prompt:**
```
Create a private scrollable proposal site.
Each section should make sense on its own (non-linear).
Professional design: 2-3 font families, generous spacing.
Use discreet anchors / side navigation.
Include relevant media in large blocks.
```

### Slide Deck when:
- Live presentation or scheduled meeting
- Linear narrative is important
- Small, aligned audience
- Limited time (15-30 min)

**Base prompt:**
```
Presentation deck optimized for verbal narration.
One central idea per slide.
Low text density, plenty of visual space.
Subtle transitions, consistent layouts.
Prepare short and direct presenter notes.
```

## Adaptation by Client Type

### Creative Agencies / Brand & Media

**Format:** Scrollable website + strong visual bias  
**Focus:** Emotional trust + aesthetic alignment

**Structure:**
1. Strong visual opening (brand mood)
2. Context / understood challenge
3. Creative direction / rationale
4. Contextualized relevant work
5. Scope + next steps

**Adapted prompt:**
```
Visual-forward branding/marketing proposal.
Hero visual aligned with brand identity.
Large media blocks, minimal and intentional text.
Calm, premium, and sophisticated feel.
```

### SaaS / Technology

**Format:** Structured website or website + complementary deck  
**Focus:** Clarity, predictability, perceived risk reduction

**Structure:**
- Executive Summary
- Current problem (framing)
- Measurable objectives (3-5)
- Approach/methodology
- Detailed scope (included/excluded)
- Visual timeline
- Transparent pricing
- Brief proof points

**Adapted prompt:**
```
Clear-technical proposal for SaaS/tech.
Use diagrams, tables, and flows when they help.
Explicitly define assumptions, constraints, what's NOT included.
Avoid decorative elements.
```

### Enterprise / Regulated Sectors

**Format:** Scrollable website (sections per stakeholder)  
**Focus:** Zero surprises, maximum professionalism, internally shareable

**Structure:**
- Executive Summary (1 page)
- Detailed scope + assumptions
- Pricing breakdown
- Timeline by phases
- Compliance/SLAs/legal aspects
- Required approvals

**Adapted prompt:**
```
Enterprise-grade proposal, conservative, highly shareable.
Prioritize predictability, clarity, risk reduction.
Dedicated sections: legal, finance, procurement.
Neutral and professional language.
```

## Standard Structure (9 Essential Sections)

| Section | Purpose | Base Prompt |
|---------|---------|-------------|
| **Cover/Overview** | Summary in 2-3 sentences | `Cover + neutral overview. What, for whom, why now.` |
| **Context** | Show understanding of the client | `Client's internal language. Current constraints and trade-offs.` |
| **Objectives** | 3-5 observable goals | `Each objective independent, measurable, clear.` |
| **Approach** | Process in phases + visual | Describe process. Use diagrams if needed. |
| **Scope** (critical) | Included, excluded, grouped | `Accordions/expandable. Make flexibility explicit.` |
| **Timeline** | Visual phases/milestones | `Timeline by phases. Deliverables for each stage.` |
| **Proof/Work** | Relevant examples | `3-5 cases. Brief result + metric when possible.` |
| **Pricing** | Clear and no surprises | Website: toggles/comparison. Deck: summary + appendix. |
| **Next Steps** | Actionable and obvious | `Clear CTA. Approval or scheduling button.` |

## Premium Design Tips

Regardless of format:
- Consistent and generous spacing
- Maximum 2-3 main colors + neutrals
- Restricted typography (1 display + 1-2 body)
- Rigorous alignment
- Relevant media (not decorative)
- Useful interactivity: expanders, toggles, internal links, discreet notes

## Recommended Workflow

1. **Understand client** > Choose format and industry
2. **Map content** > Brief, scope, pricing available?
3. **Structure sections** > Use template above, adapt by type
4. **Generate prompts** > For Lovable, Gamma, Pitch (according to format)
5. **Review before publishing** > Check: clarity, zero surprises, obvious CTAs

## Next Step

Ask the user:
- What type of client / industry?
- Live presentation or asynchronous delivery?
- Base content available (brief, scope, pricing)?
- Which tool do you want to use (Lovable, Gamma, Pitch, etc)?

Use these answers to choose format, adapt structure, and generate specific prompts.
