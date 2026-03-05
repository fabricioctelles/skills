🇧🇷 [Versao em Portugues do Brasil](README-PT-BR.md)

# 🧠 Agent Skills by ft.ia.br

A collection of [Agent Skills](https://agentskills.io) for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusable module that teaches the agent to perform complex tasks with context, structure, and best practices.

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Each skill is a folder with a `SKILL.md` file containing metadata and instructions that agents load on demand via progressive disclosure. Learn more at [agentskills.io](https://agentskills.io/what-are-skills.md).

## Available Skills

### 🏆 Premium Proposal Builder
Creates and structures premium proposals, slide decks, and scrollable sites optimized for purchase decisions. Generates effective prompts for Lovable, Gamma, Pitch, Relume, and similar tools.

**When to use:** create a business proposal, improve a pitch, generate prompts for design tools, adapt structure for different industries (agencies, SaaS, enterprise).

**Improvements in v1.1 (Mar 2026):**
- Added Parameters table with explicit defaults for client type, delivery mode, and tool
- Moved format profiles, client-type templates, and 9-section proposal structure to `references/proposal-formats-and-templates.md`
- Converted Premium Design Tips into an actionable Quality Checklist
- Fixed second-person language to imperative form throughout

📄 [View full documentation](skills/premium-proposal-builder/SKILL.md)

---

### 🔍 GEO Optimization (Generative Engine Optimization)
Optimizes digital content and marketing strategies for Generative Engines (LLMs, AI agents) to maximize citations in AI responses.

**When to use:** improve visibility in AI responses (ChatGPT, Perplexity, Google AI Overview), measure citation rate, align terminology for LLMs, audit pages for AI, create optimized roundups and FAQs.

**Improvements in v1.1 (Mar 2026):**
- Moved Guiding Principles and case study context to `references/guiding-principles.md`
- Fixed second-person language to imperative form throughout
- Added explicit default action (Full GEO Audit) when no specific request is made
- Converted Edge Cases section into a structured Quality Checklist with checkboxes

📄 [View full documentation](skills/geo-optimization/SKILL.md)

---

### 📰 Substack Expert
Substack platform expert. Guides post formatting, SEO optimization (titles, slugs, meta descriptions), native engagement strategies (Notes, Chat), and conversion to paid subscriptions.

**When to use:** format and optimize Substack posts, improve newsletter SEO (titles, slugs, meta descriptions), grow audience with Notes and recommendations, convert free readers to paid subscribers, customize homepage and welcome emails.

**Improvements in v1.1 (Mar 2026):**
- Removed duplicate Overview section and stray Portuguese artifact/orphaned code fence
- Moved formatting tips to `references/formatting-best-practices.md`
- Moved Input/Output Examples to `references/seo-output-example.md`
- Added Parameters table with defaults for topic, goal, and language
- Added explicit Clarify Scope step for ambiguous requests
- Added Quality Checklist with 8 pre-delivery verification points

📄 [View full documentation](skills/substack-expert/SKILL.md)

---

### ☁️ Pier Cloud API
Complete guide to consuming the [Pier Cloud](https://piercloud.com/en/) (Lighthouse) API with authentication, context management, workspaces, and data views.
*Note: The documentation for this skill is in Portuguese, but it can be used in any language.*

**When to use:** authenticate with Pier Cloud, list available contexts (AWS, etc), manage workspaces, access cost analysis views, run FinOps scripts.

**Improvements in v1.1 (Mar 2026):**
- Rewrote description to third-person trigger format
- Removed verbatim Overview section that duplicated the frontmatter description
- Fixed broken and incomplete Prerequisites section
- Converted second-person language to imperative form throughout
- Cleaned up workflow links to properly defer to `references/REFERENCE.md`
- Added Quality Checklist

📄 [View full documentation](skills/pier-cloud/SKILL.md)

---

### 🎨 Ultimate Design System Master
Generates Apple/Pentagram/frog/Vercel/Figma-level design deliverables using 10 specialized role-play prompts. Covers Design Systems, Brand Identity, UI/UX Patterns, Marketing Assets, Figma Specs, Design Critique, Trend Analysis, Accessibility Audit, Design-to-Code, and Executive Presentations.

**When to use:** create a design system, build brand identity, generate UI/UX patterns, produce marketing assets, write Figma specs, get design critique, analyze design trends, run accessibility audit, translate design to code, create presentation decks.

**Improvements in v2.1 (Mar 2026):**
- Rewrote description to third-person trigger format
- Moved 18-question Briefing Questionnaire to `references/briefing-questionnaire.md`
- Added Quality Checklist with 5 concrete verification conditions
- Removed intro sentence that duplicated frontmatter description

📄 [View full documentation](skills/ultimate-design-system-master/SKILL.md)

---

### 🗂️ Front-End Checklist
An exhaustive list of all elements you need to have or to test before launching your website or HTML page to production. Inspired by the [Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist).

**When to use:** review code before production, validate accessibility, SEO, performance, and enforce front-end best practices.

**Improvements in v1.1 (Mar 2026):**
- Rewrote description to third-person trigger format with concrete trigger phrases
- Added Parameters section with explicit defaults for checklist and scope
- Added Quality Checklist covering high-priority items, actionable fixes, and blocking vs. non-blocking separation
- Restructured workflow steps to imperative voice with full execution flow
- Added explicit References section documenting all 5 reference files

📄 [View full documentation](skills/front-end-checklist/SKILL.md)

---

### 📄 Resume ATS Beater
Rewrites resumes from scratch for ATS compatibility and recruiter impact, with a workflow tailored to ATS platforms in Brazil (Gupy, Vagas.com, PandaPé, Sólides).

**When to use:** optimize resume for ATS, adapt CV to a target role/industry, improve experience bullets with measurable outcomes, validate eliminatory requirements and semantic matching.

**Improvements in v1.2 (Mar 2026):**
- Merged overlapping diagnostic steps (Etapas 2+3) into a single unified step
- Moved diagnostic output templates to 3 new references files: `diagnostico-ats.md`, `diagnostico-avancado.md`, `template-saida.md`
- Added explicit default mode (`modo_completo`) when execution mode is not specified
- Added guardrail: block all workflow steps until `curriculo_atual` is provided
- Added skip instruction: `modo_reescrita` bypasses the diagnostic step entirely
- Added behavioral note for `plataforma_ats_alvo` when platform is known

📄 [View full documentation](skills/resume-ats-beater/SKILL.md)

---

> **Skills revised in March 2026** following the Anthropic standard for Agent Skills structure and quality.
> Source: [Improving Skill Creator: Test, Measure and Refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

## Installation

You can install these skills using any compatible installer or manually. Below are the most popular options.

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add fabricioctelles/skills
```

Or install a specific skill:

```bash
npx skills add fabricioctelles/skills@premium-proposal-builder
npx skills add fabricioctelles/skills@geo-optimization
npx skills add fabricioctelles/skills@substack-expert
npx skills add fabricioctelles/skills@pier-cloud
npx skills add fabricioctelles/skills@ultimate-design-system-master
npx skills add fabricioctelles/skills@front-end-checklist
npx skills add fabricioctelles/skills@resume-ats-beater
```

### Via [Agent Skills CLI](https://www.agentskills.in/docs)

```bash
npm install -g agent-skills-cli
```

Then install the skills:

```bash
skills add fabricioctelles/skills
```

Or use without global install:

```bash
npx agent-skills-cli install fabricioctelles/skills
```

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/fabricioctelles/skills.git
```

2. Copy the desired skill folder to your agent's skills directory:
```bash
# Example for Cursor
cp -r skills/premium-proposal-builder .cursor/skills/
cp -r skills/geo-optimization .cursor/skills/
cp -r skills/substack-expert .cursor/skills/
cp -r skills/pier-cloud .cursor/skills/
cp -r skills/ultimate-design-system-master .cursor/skills/
cp -r skills/front-end-checklist .cursor/skills/
cp -r skills/resume-ats-beater .cursor/skills/

# Example for Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/front-end-checklist .claude/skills/
cp -r skills/resume-ats-beater .claude/skills/

# Example for Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/front-end-checklist .kiro/skills/
cp -r skills/resume-ats-beater .kiro/skills/
```

The Agent Skills format is universal and works with any compatible agent. See the [official specification](https://agentskills.io/specification.md) for details.

## Repository Structure

```
skills/
├── premium-proposal-builder/
│   ├── SKILL.md
│   └── references/        # format profiles, client types, proposal templates
├── geo-optimization/
│   ├── SKILL.md
│   └── references/        # guiding principles and case studies
├── substack-expert/
│   ├── SKILL.md
│   └── references/        # formatting best practices, SEO output example
├── pier-cloud/
│   ├── SKILL.md
│   ├── scripts/           # Python scripts for API consumption
│   └── references/        # API reference, troubleshooting guide
├── front-end-checklist/
│   ├── SKILL.md
│   └── references/        # design, head, performance checklists
├── resume-ats-beater/
│   ├── SKILL.md
│   └── references/        # diagnostic templates, output structure
└── ultimate-design-system-master/
    ├── SKILL.md
    └── references/        # briefing questionnaire, 10 specialized prompt files
```

## Author

Created by [ft.ia.br](https://ft.ia.br)

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
