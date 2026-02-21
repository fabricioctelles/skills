# 🧠 Agent Skills by ft.ia.br

A collection of skills for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusable module that teaches the agent to perform complex tasks with context, structure, and best practices.

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

## Installation

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add fabricioctelles/skills
```

Or install a specific skill:

```bash
npx skills add fabricioctelles/skills@premium-proposal-builder
npx skills add fabricioctelles/skills@geo-optimization
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

# Example for Claude Code
cp -r skills/premium-proposal-builder .claude/skills/
cp -r skills/geo-optimization .claude/skills/

# Example for Kiro
cp -r skills/premium-proposal-builder .kiro/skills/
cp -r skills/geo-optimization .kiro/skills/
```

See the [full platform list](https://www.agentskills.in/docs/getting-started) for all 42+ supported agents and their directories.

## Repository Structure

```
skills/
├── premium-proposal-builder/
│   └── SKILL.md
└── geo-optimization/
    └── SKILL.md
```

Each skill contains a `SKILL.md` file with the configuration frontmatter and all the documentation the agent needs to execute.

## Author

Created by [ft.ia.br](https://ft.ia.br)

## License

MIT
