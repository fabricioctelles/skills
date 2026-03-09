---
name: ultimate-design-system-master
description: Create comprehensive design systems, brand identities, and UI component libraries. Use when the user says "create design system", "build brand identity", "design UI components", "generate design tokens", "create figma specs", "review my design", "analyze design trends", "audit accessibility", "convert design to code", or "create presentation deck". Covers 10 specialized roles from system architecture to executive presentations.
metadata:
  author: ft.ia.br
  version: "2.2"
  date: 2026-03-08
  license: Apache 2.0
---

# Ultimate Design System Master

## Workflow

1. **Gather briefing** — Apply the 18-question questionnaire in `references/briefing-questionnaire.md`. Retain all answers in conversation context.
2. **Present menu** — Display the 10 generators below. Accept single or multiple selections.
3. **Execute** — Load the selected `references/prompt-*.md` file as the sole source. Apply briefing data. Generate output.
4. **Loop** — After each delivery, present the menu again until the user selects "Exit".

## Menu

| # | Generator | Role-play | Reference |
|---|-----------|-----------|-----------|
| 1 | Design System Architect | Apple Principal Designer → HIG-level system | [prompt-01](references/prompt-01-design-system-architect.md) |
| 2 | Brand Identity Creator | Pentagram Creative Director → strategy + rationale | [prompt-02](references/prompt-02-brand-identity-creator.md) |
| 3 | UI/UX Pattern Master | Apple Senior UI Designer → 8 detailed screens | [prompt-03](references/prompt-03-ui-ux-pattern-master.md) |
| 4 | Marketing Asset Factory | Top agency Creative Director → 47+ assets | [prompt-04](references/prompt-04-marketing-asset-factory.md) |
| 5 | Figma Auto-Layout Expert | Figma Design Ops Specialist → technical specs | [prompt-05](references/prompt-05-figma-auto-layout-expert.md) |
| 6 | Design Critique Partner | Apple Design Director → Nielsen critique + alternatives | [prompt-06](references/prompt-06-design-critique-partner.md) |
| 7 | Design Trend Synthesizer | frog Design Researcher → 2026 trends + roadmap | [prompt-07](references/prompt-07-design-trend-synthesizer.md) |
| 8 | Accessibility Auditor | Apple Accessibility Specialist → WCAG 2.2 AA audit | [prompt-08](references/prompt-08-accessibility-auditor.md) |
| 9 | Design-to-Code Translator | Vercel Design Engineer → production-ready code | [prompt-09](references/prompt-09-design-to-code-translator.md) |
| 10 | Presentation Designer | Apple Presentation Designer → executive narrative | [prompt-10](references/prompt-10-presentation-designer.md) |
| 11 | Exit | | |

## Rules

- Maintain full consistency with briefing data across all outputs.
- Load only the selected prompt file — do not mix prompts.
- Use clear, professional, immediately usable formatting.
- Present the menu again after each delivery.

## Quality Checklist

- [ ] All 18 briefing questions answered before generating output.
- [ ] Only the selected prompt file was loaded.
- [ ] Output is consistent with the briefing (brand name, colors, tone, platform, tech stack).
- [ ] Formatting is production-ready (no placeholders left unfilled).
- [ ] Menu presented again after delivery.
