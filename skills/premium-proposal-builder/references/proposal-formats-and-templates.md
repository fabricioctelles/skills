# Proposal Formats, Client Profiles, and Section Templates

## Format Selection Guide

### Scrollable Website

Use when:
- Multiple decision-makers review asynchronously
- The proposal will be forwarded internally
- Scope is complex with variations
- The sales cycle is long or cross-functional

**Base prompt:**
```
Create a private scrollable proposal site.
Each section should make sense on its own (non-linear).
Professional design: 2-3 font families, generous spacing.
Use discreet anchors / side navigation.
Include relevant media in large blocks.
```

### Slide Deck

Use when:
- Live presentation or scheduled meeting
- A linear narrative is important
- Audience is small and already aligned
- Time is limited (15-30 min)

**Base prompt:**
```
Presentation deck optimized for verbal narration.
One central idea per slide.
Low text density, plenty of visual space.
Subtle transitions, consistent layouts.
Prepare short and direct presenter notes.
```

---

## Client Type Profiles

### Creative Agencies / Brand & Media

**Format:** Scrollable website + strong visual bias
**Focus:** Emotional trust + aesthetic alignment

**Section order:**
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

---

### SaaS / Technology

**Format:** Structured website or website + complementary deck
**Focus:** Clarity, predictability, perceived risk reduction

**Section order:**
- Executive Summary
- Current problem (framing)
- Measurable objectives (3-5)
- Approach / methodology
- Detailed scope (included / excluded)
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

---

### Enterprise / Regulated Sectors

**Format:** Scrollable website (sections per stakeholder)
**Focus:** Zero surprises, maximum professionalism, internally shareable

**Section order:**
- Executive Summary (1 page)
- Detailed scope + assumptions
- Pricing breakdown
- Timeline by phases
- Compliance / SLAs / legal aspects
- Required approvals

**Adapted prompt:**
```
Enterprise-grade proposal, conservative, highly shareable.
Prioritize predictability, clarity, risk reduction.
Dedicated sections: legal, finance, procurement.
Neutral and professional language.
```

---

## Standard 9-Section Structure

| Section | Purpose | Base Prompt |
|---------|---------|-------------|
| **Cover / Overview** | Summary in 2-3 sentences | `Cover + neutral overview. What, for whom, why now.` |
| **Context** | Show understanding of the client | `Client's internal language. Current constraints and trade-offs.` |
| **Objectives** | 3-5 observable goals | `Each objective independent, measurable, clear.` |
| **Approach** | Process in phases + visual | `Describe process. Use diagrams if needed.` |
| **Scope** (critical) | Included, excluded, grouped | `Accordions/expandable. Make flexibility explicit.` |
| **Timeline** | Visual phases / milestones | `Timeline by phases. Deliverables for each stage.` |
| **Proof / Work** | Relevant examples | `3-5 cases. Brief result + metric when possible.` |
| **Pricing** | Clear and no surprises | Website: toggles/comparison. Deck: summary + appendix. |
| **Next Steps** | Actionable and obvious | `Clear CTA. Approval or scheduling button.` |
