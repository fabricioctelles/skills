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
- Description optimized to be more concise and actionable (Mar 8)

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

**Improvements in v2.2 (Mar 8, 2026):**
- Description rewritten with user-spoken trigger phrases for better skill activation
- License Apache 2.0 added to metadata
- Full compliance with Official Anthropic Guide for Agent Skills achieved

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

### 🚀 Coolify Operator
Master operator for Coolify — the self-hosted open-source deployment platform (alternative to Heroku/Vercel/Netlify). Manages applications, servers, databases and services via REST API and official CLI.

**When to use:** connect to Coolify instances, deploy/restart/stop applications, manage environment variables, list servers and databases, monitor deployment logs, manage multiple environments (dev/staging/prod), troubleshoot connection and auth issues.

**Improvements in v1.1 (Mar 8, 2026):**
- Description optimized for clarity and brevity (350→250 characters)
- License MIT added to metadata
- Quality Checklist with 10 verification points added
- Internal README.md removed for full compliance with Official Anthropic Guide
- Full compliance with Official Anthropic Guide for Agent Skills achieved

📄 [View full documentation](skills/coolify-operator/SKILL.md)

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

### 🤖 Agent Ready — Cloudflare Scanner
Audits any website for AI agent readiness using the Cloudflare [isitagentready.com](https://isitagentready.com) scanner. Scans 18 checks across 5 categories (Discoverability, Content, Bot Access Control, API/Auth/MCP Discovery, Commerce), assigns a level (0–5), and generates copy-paste fix prompts for every failing check. Includes 20 implementation sub-skills covering robots.txt, sitemap, Markdown for Agents, Content Signals, MCP Server Card, A2A Agent Card, Agent Skills Index, OAuth, WebMCP, and more.

**When to use:** scan a site for agent readiness, check agent-ready score, fix failing checks, implement MCP Server Card, add Content Signals, publish Agent Skills index, set up Markdown for Agents, batch scan multiple domains, improve AI agent discoverability.

📄 [View full documentation](skills/agent-ready-cloudflare/README.md)

---

### 🔁 Ralph Loop for Kiro Specs
Automated iterative agent runner for spec-based development in [Kiro](https://kiro.dev). Wraps `kiro-cli` in a self-correcting bash loop that picks up tasks from a Kiro spec, implements them one at a time, verifies against exit criteria, and accumulates corrections and codebase patterns across iterations. Based on [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) by [mreferre](https://github.com/mreferre).

**When to use:** automate Kiro spec task implementation, run kiro-cli in a loop, drive a spec to completion through repeated agent iterations, set up or troubleshoot the Ralph Loop workflow, understand progress tracking, corrections, codebase patterns, and the summary dashboard.

📄 [View full documentation](skills/ralph-loop-kiro-specs/SKILL.md)

---

### 🔐 auth.md — Agent Authentication Protocol
Generates, validates, and explains [auth.md](https://auth-md.com) files — the open protocol that lets AI agents register for services on behalf of users without signup forms. Supports the Agent Verified flow (ID-JAG identity assertions via trusted providers like OpenAI, Anthropic, Cursor) and the User Claimed flow (OTP-based registration with anonymous start or email required entrypoints). Extends RFC 9728 (Protected Resource Metadata) with CIMD support.

**When to use:** make your app agent-ready by publishing an `auth.md`, generate Protected Resource Metadata and Authorization Server metadata with `agent_auth` block, validate an existing `auth.md` against the protocol spec, implement agent registration endpoints (`/agent/auth`, `/agent/auth/claim`, `/agent/auth/revoke`), understand how the auth.md protocol works, configure ID-JAG verification and trust lists, set up OTP claim ceremonies.

📄 [View full documentation](skills/auth-md/SKILL.md) | 🌐 [auth-md.com](https://auth-md.com)

---

### 🌐 Website Spec (Offline Edition)
Self-contained offline version of [The Website Specification](https://specification.website/) by Joost de Valk. A platform-agnostic spec of what a good website does — 128 topics across 10 categories (Foundations, SEO, Accessibility, Security, Well-Known URIs, Agent Readiness, Performance, Privacy, Resilience, i18n), each tagged required/recommended/optional/avoid with implementation guidance and verification steps. Designed to run without network access in air-gapped environments, maximum-privacy workflows, and internal projects.

**When to use:** audit a website against web standards, check what is required for production, verify agent readiness, review security headers, run accessibility checks, generate implementation checklists, compare audit results between runs. All content is bundled locally — no external requests needed.

**Update (May 2026) — Full LGPD compliance:**
- Privacy section rewritten for 100% compatibility with Brazil's LGPD (Lei 13.709/2018)
- Covers ANPD's 2026 reorganization (Resolution 33), Brazil-EU mutual adequacy decision (Resolution 32/2026), mandatory SCCs (Resolution 19/2024), opt-in cookie consent model, 15-day DSAR deadline, 3-business-day breach notification, 10 legal bases, DPO/Encarregado requirements, children's data (ECA Digital), and AI/automated decisions (Art. 20)
- All 6 privacy reference files updated: privacy-policy, cookie-consent, data-minimization, global-privacy-control, analytics-privacy, third-party-scripts

📄 [View full documentation](skills/website-spec/SKILL.md) | 🌐 [specification.website](https://specification.website/) (online/updated version)

---

### 🔒 LGPD Check
Audits websites for compliance with Brazil's LGPD (Lei 13.709/2018). Validates privacy policy, cookie consent, data minimization, international transfers, data subject rights, third-party scripts, and analytics. Generates a compliance report with score and prioritized fixes. Fully written in Portuguese.

**When to use:** audit a website for LGPD compliance, validate privacy policy against Brazilian law, check cookie consent implementation, verify data subject rights channels, assess international data transfers, review third-party scripts for privacy risks, generate LGPD compliance score.

📄 [View full documentation](skills/lgpd-check/SKILL.md)

---

> **Skills revised in March 2026** following the Anthropic standard for Agent Skills structure and quality.
> Source: [Improving Skill Creator: Test, Measure and Refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

## Installation

You can install these skills using any compatible installer or manually. Below are the most popular options.

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add https://gitlab.com/fabriciotelles/skills
```

Or install a specific skill:

```bash
npx skills add https://gitlab.com/fabriciotelles/skills -s premium-proposal-builder
npx skills add https://gitlab.com/fabriciotelles/skills -s geo-optimization
npx skills add https://gitlab.com/fabriciotelles/skills -s substack-expert
npx skills add https://gitlab.com/fabriciotelles/skills -s pier-cloud
npx skills add https://gitlab.com/fabriciotelles/skills -s ultimate-design-system-master
npx skills add https://gitlab.com/fabriciotelles/skills -s front-end-checklist
npx skills add https://gitlab.com/fabriciotelles/skills -s resume-ats-beater
npx skills add https://gitlab.com/fabriciotelles/skills -s coolify-operator
npx skills add https://gitlab.com/fabriciotelles/skills -s agent-ready-cloudflare
npx skills add https://gitlab.com/fabriciotelles/skills -s ralph-loop-kiro-specs
npx skills add https://gitlab.com/fabriciotelles/skills -s auth-md
npx skills add https://gitlab.com/fabriciotelles/skills -s website-spec
npx skills add https://gitlab.com/fabriciotelles/skills -s lgpd-check
```

### Via [Agent Skills CLI](https://www.agentskills.in/docs)

```bash
npm install -g agent-skills-cli
```

Then install the skills:

```bash
skills add https://gitlab.com/fabriciotelles/skills
```

Or use without global install:

```bash
npx agent-skills-cli install https://gitlab.com/fabriciotelles/skills
```

### Manual Installation

1. Clone this repository:
```bash
git clone https://gitlab.com/fabriciotelles/skills.git
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
cp -r skills/coolify-operator .cursor/skills/
cp -r skills/agent-ready-cloudflare .cursor/skills/
cp -r skills/ralph-loop-kiro-specs .cursor/skills/
cp -r skills/auth-md .cursor/skills/
cp -r skills/website-spec .cursor/skills/
cp -r skills/lgpd-check .cursor/skills/

# Example for Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/front-end-checklist .claude/skills/
cp -r skills/resume-ats-beater .claude/skills/
cp -r skills/coolify-operator .claude/skills/
cp -r skills/agent-ready-cloudflare .claude/skills/
cp -r skills/ralph-loop-kiro-specs .claude/skills/
cp -r skills/auth-md .claude/skills/
cp -r skills/website-spec .claude/skills/
cp -r skills/lgpd-check .claude/skills/

# Example for Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/front-end-checklist .kiro/skills/
cp -r skills/resume-ats-beater .kiro/skills/
cp -r skills/coolify-operator .kiro/skills/
cp -r skills/agent-ready-cloudflare .kiro/skills/
cp -r skills/ralph-loop-kiro-specs .kiro/skills/
cp -r skills/auth-md .kiro/skills/
cp -r skills/website-spec .kiro/skills/
cp -r skills/lgpd-check .kiro/skills/
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
├── coolify-operator/
│   ├── SKILL.md
│   └── evals/             # 8 test scenarios
└── ultimate-design-system-master/
    ├── SKILL.md
    └── references/        # briefing questionnaire, 10 specialized prompt files
├── agent-ready-cloudflare/
│   ├── README.md          # human-readable documentation with examples
│   ├── SKILL.md           # main skill (API docs, operational flow, prompt templates)
│   └── */SKILL.md         # 20 implementation sub-skills (robots-txt, mcp-server-card, etc.)
├── ralph-loop-kiro-specs/
│   ├── SKILL.md
│   ├── scripts/           # bash loop runner script
│   └── references/        # Ralph agent prompt template
├── auth-md/
│   ├── SKILL.md
│   └── references/        # protocol template, validation rules, metadata schema, example, implementation guide
├── website-spec/
│   ├── SKILL.md
│   └── references/        # 128 spec topics in 10 category folders (offline bundle from specification.website)
├── lgpd-check/
│   ├── SKILL.md
│   └── references/        # 6 compliance check modules (privacy policy, cookies, data minimization, transfers, rights, scripts)
```

## Author

Created by [ft.ia.br](https://ft.ia.br)

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
