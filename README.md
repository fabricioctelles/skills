🇧🇷 [Versao em Portugues do Brasil](README-PT-BR.md)

# 🧠 Agent Skills by ft.ia.br

A collection of [Agent Skills](https://agentskills.io) for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusable module that teaches the agent to perform complex tasks with context, structure, and best practices.

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Each skill is a folder with a `SKILL.md` file containing metadata and instructions that agents load on demand via progressive disclosure. Learn more at [agentskills.io](https://agentskills.io/what-are-skills.md).

## Available Skills

### 🏆 Premium Proposal Builder
Creates and structures premium proposals, slide decks, and scrollable sites optimized for purchase decisions. Generates effective prompts for Lovable, Gamma, Pitch, Relume, and similar tools.

**When to use:** create a business proposal, improve a pitch, generate prompts for design tools, adapt structure for different industries (agencies, SaaS, enterprise).

📄 [View full documentation](skills/premium-proposal-builder/SKILL.md)

---

### 🔍 GEO Optimization (Generative Engine Optimization)
Optimizes digital content and marketing strategies for Generative Engines (LLMs, AI agents) to maximize citations in AI responses.

**When to use:** improve visibility in AI responses (ChatGPT, Perplexity, Google AI Overview), measure citation rate, align terminology for LLMs, audit pages for AI, create optimized roundups and FAQs.

📄 [View full documentation](skills/geo-optimization/SKILL.md)

---

### 📰 Substack Expert
Substack platform expert. Guides post formatting, SEO optimization (titles, slugs, meta descriptions), native engagement strategies (Notes, Chat), and conversion to paid subscriptions.

**When to use:** format and optimize Substack posts, improve newsletter SEO (titles, slugs, meta descriptions), grow audience with Notes and recommendations, convert free readers to paid subscribers, customize homepage and welcome emails.

📄 [View full documentation](skills/substack-expert/SKILL.md)

---

### ☁️ Pier Cloud API
Complete guide to consuming the [Pier Cloud](https://piercloud.com/en/) (Lighthouse) API with authentication, context management, workspaces, and data views.
*Note: The documentation for this skill is in Portuguese, but it can be used in any language.*

**When to use:** authenticate with Pier Cloud, list available contexts (AWS, etc), manage workspaces, access cost analysis views, run FinOps scripts.

📄 [View full documentation](skills/pier-cloud/SKILL.md)

---

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

# Example for Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/

# Example for Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
```

The Agent Skills format is universal and works with any compatible agent. See the [official specification](https://agentskills.io/specification.md) for details.

## Repository Structure

```
skills/
├── premium-proposal-builder/
│   └── SKILL.md
├── geo-optimization/
│   └── SKILL.md
├── substack-expert/
│   └── SKILL.md
└── pier-cloud/
    └── SKILL.md
```

Each skill contains a `SKILL.md` file with the configuration frontmatter and all the documentation the agent needs to execute. This follows the open [Agent Skills specification](https://agentskills.io/specification.md).

## Author

Created by [ft.ia.br](https://ft.ia.br)

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
