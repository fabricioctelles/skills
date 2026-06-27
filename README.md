🇧🇷 [Versao em Portugues do Brasil](README-PT-BR.md)

[![skills.sh](https://skills.sh/b/fabricioctelles/skills)](https://skills.sh/fabricioctelles/skills)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?logo=cloudflare&logoColor=white)
![Astro](https://img.shields.io/badge/Astro-BC52EE?logo=astro&logoColor=white)
![Coolify](https://img.shields.io/badge/Coolify-6B16ED?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQTEwIDEwIDAgMCAwIDIgMTJhMTAgMTAgMCAwIDAgMTAgMTAgMTAgMTAgMCAwIDAgMTAtMTBBMTAgMTAgMCAwIDAgMTIgMnoiLz48L3N2Zz4=&logoColor=white)
![Google Analytics](https://img.shields.io/badge/Google%20Analytics-E37400?logo=googleanalytics&logoColor=white)
![Google Search Console](https://img.shields.io/badge/Search%20Console-458CF5?logo=google&logoColor=white)
![Substack](https://img.shields.io/badge/Substack-FF6719?logo=substack&logoColor=white)
![SEO](https://img.shields.io/badge/SEO%20%2F%20GEO-4285F4?logo=google&logoColor=white)
![AI Agents](https://img.shields.io/badge/AI%20Agents-8B5CF6?logo=openai&logoColor=white)
![LGPD](https://img.shields.io/badge/LGPD%20%2F%20Privacy-059669?logo=shieldsdotio&logoColor=white)
![Security](https://img.shields.io/badge/Security-DC2626?logo=owasp&logoColor=white)

# 🧠 Agent Skills by ft.ia.br

A collection of [Agent Skills](https://agentskills.io) for AI agents (Kiro, Cursor, Windsurf, Claude Code, and others). Each skill is a reusable module that teaches the agent to perform complex tasks with context, structure, and best practices.

Agent Skills are a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. Each skill is a folder with a `SKILL.md` file containing metadata and instructions that agents load on demand via progressive disclosure. Learn more at [agentskills.io](https://agentskills.io/what-are-skills.md).

## Available Skills

### 🔍 GEO Optimization (Generative Engine Optimization) · `code-quality-and-review`
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

### 📰 Substack Expert · `library-and-api-reference`
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

### ☁️ Pier Cloud API · `library-and-api-reference`
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

### 🎨 Ultimate Design System Master · `code-scaffolding-and-templates`
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

### 🗂️ Front-End Checklist _(moved)_

> **This skill has been retired.** The original project now offers 385 self-contained skills (one per rule) covering HTML, CSS, JavaScript, Performance, Accessibility, SEO, Security, Images, Testing, Privacy, and Internationalization — far more complete than what we maintained here.
>
> 👉 **Install directly from:** https://github.com/thedaviddias/Front-End-Checklist/tree/main/skills
>
> ```bash
> npx skills add frontendchecklist/skills
> ```

---

### 🚀 Coolify Operator · `ci-cd-and-deployment`
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

### 📄 Resume ATS Beater + LinkedIn Optimizer · `code-scaffolding-and-templates`
Rewrites resumes for ATS compatibility and audits LinkedIn profiles for professional positioning. Covers CV optimization for Brazilian ATS platforms (Gupy, Vagas.com, PandaPé, Sólides) and LinkedIn audit with heuristic scoring, SSI analysis, fix prompts, and LLM rewrite mega-prompts. Works for any specialized profession — not dev-only.

**When to use:** optimize resume for ATS, audit LinkedIn profile (headline, about, experiences, SSI), adapt CV to target role/industry, generate fix prompts per finding, align CV and LinkedIn in unified mode, improve bullets with measurable outcomes. Integrates with `humanizar` skill for narrative sections.

**Improvements in v2.0 (Jun 2026):**
- Added `modo_linkedin` (full profile audit with scoring) and `modo_unificado` (CV + LinkedIn with consistency check)
- LinkedIn audit: headline format enforcement (Position | Areas | Tools·), about structure, experience bullets, language, skills, featured, SSI
- Punitive scoring system: 100 - (critical×15 + warning×6 + info×2)
- SSI analysis with 4 pillars, classification by tier, and actionable tips
- Fix prompts per finding (standalone prompts for any LLM)
- Mega-prompt for full profile rewrite by LLM
- 18 career presets across tech, data, marketing, finance, engineering, legal, sales, HR, product
- Integration with `humanizar` skill (scoped to About/Summary sections)
- 3 new reference files: `auditoria-linkedin.md`, `ssi.md`, `presets-formatos.md`

📄 [View full documentation](skills/resume-ats-beater/SKILL.md)

---

### 🤖 Agent Ready — Cloudflare Scanner · `product-verification`
Audits any website for AI agent readiness using the Cloudflare [isitagentready.com](https://isitagentready.com) scanner. Scans 18 checks across 5 categories (Discoverability, Content, Bot Access Control, API/Auth/MCP Discovery, Commerce), assigns a level (0–5), and generates copy-paste fix prompts for every failing check. Includes 20 implementation sub-skills covering robots.txt, sitemap, Markdown for Agents, Content Signals, MCP Server Card, A2A Agent Card, Agent Skills Index, OAuth, WebMCP, and more.

**When to use:** scan a site for agent readiness, check agent-ready score, fix failing checks, implement MCP Server Card, add Content Signals, publish Agent Skills index, set up Markdown for Agents, batch scan multiple domains, improve AI agent discoverability.

📄 [View full documentation](skills/agent-ready-cloudflare/README.md)

---

### ✅ DESIGN.md Validator · `product-verification`
Validates DESIGN.md files against the official [Google design.md specification](https://github.com/google-labs-code/design.md) using the `@google/design.md` CLI linter. Works with local files and remote URLs. Always uses `npx` to run the latest published version — never stale.

**When to use:** lint a DESIGN.md for spec compliance, check WCAG contrast ratios, find broken token references, diff two design system versions, export tokens to Tailwind v3/v4 or W3C DTCG format, audit frontmatter schema.

📄 [View full documentation](skills/design-md-validator/SKILL.md)

---

### 🔁 Ralph Loop for Kiro Specs · `code-scaffolding-and-templates`
Automated iterative agent runner for spec-based development in [Kiro](https://kiro.dev). Wraps `kiro-cli` in a self-correcting bash loop that picks up tasks from a Kiro spec, implements them one at a time, verifies against exit criteria, and accumulates corrections and codebase patterns across iterations. Based on [ralph-loop-kiro-specs](https://github.com/mreferre/ralph-loop-kiro-specs) by [mreferre](https://github.com/mreferre).

**When to use:** automate Kiro spec task implementation, run kiro-cli in a loop, drive a spec to completion through repeated agent iterations, set up or troubleshoot the Ralph Loop workflow, understand progress tracking, corrections, codebase patterns, and the summary dashboard.

📄 [View full documentation](skills/ralph-loop-kiro-specs/SKILL.md)

---

### 🏗️ Loop Architect — Agent Loop Design Coach · `code-scaffolding-and-templates`
Design well-structured agent loops with best-practice coaching and cross-model review gates before you run them. Interviews you, critiques your design against built-in rubrics, wires in reviewers/judges, and emits portable artifacts (`loop.yaml`, `RUN_IN_SESSION.md`, `run-loop.py`). Integrates natively with Kiro CLI's `/goal` and subagent review loops. Based on [Looper](https://github.com/ksimback/looper) by [Kevin Simback](https://github.com/ksimback).

**When to use:** design an agent loop, set up a self-review or LLM-as-judge loop, build a multi-model council, create review-gated iterative workflows, or scaffold a `/goal`-driven process with typed verification and termination guards.

📄 [View full documentation](skills/loop-architect/SKILL.md)

---

### ✍️ Humanizar — AI Text Humanizer for Brazilian Portuguese · `code-quality-and-review`
Rewrites Brazilian Portuguese text to sound human, natural, and undetectable by AI detection tools. Removes AI slop patterns, restores semantic entropy, and injects voice and personality. Born from the English `humanizer` skill but evolved into something far more complete — with 55+ patterns specific to PT-BR that no other source has cataloged.

**Origin story:** I started from the English [humanizer](https://github.com/blader/humanizer) skill by [@blader](https://github.com/blader) (based on Wikipedia's "Signs of AI writing"), researched what makes AI text detectable specifically in Brazilian Portuguese, discovered there was *zero* consolidated material on PT-BR AI patterns, cataloged 55+ patterns from scratch (including 10 exclusive to Brazilian Portuguese like gerundismo, officialese, and ENEM-style hedging), incorporated the [tropes.fyi](https://tropes.fyi) directory and the concept of [semantic ablation](https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/) (The Register, 2026), and built a skill that doesn't just remove bad patterns — it restores the entropy that AI strips away.

**Why it's better for PT-BR than the original:**
- 55+ patterns vs 25 (including 10 that only exist in Brazilian Portuguese)
- Semantic entropy restoration with explicit alerts (not just removal)
- 6 voice presets calibrated for Brazilian contexts (crônica, journalistic, academic, corporate, social media, WhatsApp)
- Examples are culturally Brazilian, not translations from English
- Preserves naturalized foreign words (feedback, deploy, churn) — fighting linguistic purism is itself a humanization signal
- Uses the Brazilian *crônica* literary tradition as the gold standard for natural writing

**When to use:** humanize PT-BR text, remove AI slop, rewrite with voice, fix generic/bureaucratic tone, review text from another agent, "tirar cara de IA", "dar vida ao texto".

**Improvements in v1.2 (Jun 2026):**
- Added automatic document type detection with fallback (Step 0.5) — auto-selects the best voice preset
- Added post-rewrite scoring with 5 weighted dimensions (Step 5.5) — quantifiable quality gate
- Added iterative loop with strategy fallback — retries with different approaches when score < 60
- Loop protocol compatible with external orchestrator skills (ralph-wiggum, goal)
- Inspired by [humanize-it](https://github.com/smallnest/goal-workflow/blob/master/skills/humanize-it/SKILL.md) by [@smallnest](https://github.com/smallnest)

📄 [View full documentation](skills/humanizar/SKILL.md)

---

### 🔐 auth.md — Agent Authentication Protocol · `library-and-api-reference`
Generates, validates, and explains [auth.md](https://auth-md.com) files — the open protocol that lets AI agents register for services on behalf of users without signup forms. Supports the Agent Verified flow (ID-JAG identity assertions via trusted providers like OpenAI, Anthropic, Cursor) and the User Claimed flow (OTP-based registration with anonymous start or email required entrypoints). Extends RFC 9728 (Protected Resource Metadata) with CIMD support.

**When to use:** make your app agent-ready by publishing an `auth.md`, generate Protected Resource Metadata and Authorization Server metadata with `agent_auth` block, validate an existing `auth.md` against the protocol spec, implement agent registration endpoints (`/agent/auth`, `/agent/auth/claim`, `/agent/auth/revoke`), understand how the auth.md protocol works, configure ID-JAG verification and trust lists, set up OTP claim ceremonies.

📄 [View full documentation](skills/auth-md/SKILL.md) | 🌐 [auth-md.com](https://auth-md.com)

---

### 📦 OKF — Open Knowledge Format · `library-and-api-reference`
Create, validate, and enrich [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) bundles — the open spec (v0.1, announced June 12, 2026 by Sam McVeety & Amir Hormati at Google Cloud) that formalizes the "LLM Wiki" pattern into a portable, interoperable format for organizational knowledge. Markdown files with YAML frontmatter, consumable by any AI agent without SDK. Includes bash validator, conversion guides (Notion, Obsidian, CSV), and integration with Google Cloud Knowledge Catalog via kcmd CLI/MCP.

**When to use:** create OKF bundles, validate conformance, enrich concepts with schema/citations/cross-links, convert existing knowledge (Notion exports, Obsidian vaults, spreadsheets) to OKF, structure a knowledge base for AI agent consumption, generate index.md and log.md files, push bundles to Knowledge Catalog via kcmd.

📄 [View full documentation](skills/okf-open-knowledge-format/SKILL.md) | 🌐 [okf.md](https://okf.md)

---

### 🌐 Website Spec _(moved)_

> **This skill has been retired.** The original project now offers a more complete skill with 140+ topics, live updates via MCP server, delta re-audits, and MDN pairing — far beyond what we maintained here.
>
> 👉 **Use the official skill:** https://specification.website/.well-known/agent-skills/specification-website/SKILL.md
>
> MCP endpoint: `https://mcp.specification.website/mcp`

---

### 🔒 LGPD Check
> **Migrated** → This skill moved to [github.com/lgpd-app/skills](https://github.com/lgpd-app/skills)

Audits websites for compliance with Brazil's LGPD (Lei 13.709/2018).

---

---

### 📊 Skill Evaluation · `code-quality-and-review`
Evaluate any agent skill against 12 best-practice criteria from Anthropic and agentskills.io. Produces a structured markdown scorecard with per-criterion scores (0–100), weighted overall grade (A/B/C/D/F), category classification, bonus patterns assessment, and prioritized improvement actions.

**When to use:** evaluate a skill, rate skill quality, audit SKILL.md, compare two skills, skill scorecard, review best practices compliance, or check if a skill is production-ready.

**12 scored criteria:** Don't state the obvious · Gotchas · Progressive disclosure · Avoids railroading · Setup flow · Description for trigger · Memory · Scripts · Hooks · Conciseness · Coherent scope · Grounded in expertise

**4 bonus patterns (measured, not scored):** Validation loops · Output templates · Procedures over declarations · Defaults over menus

**How it differs from [agentskills.io evals](https://agentskills.io/skill-creation/evaluating-skills) and [skill-creator benchmark](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills):**

| | This skill | agentskills.io evals | skill-creator benchmark |
|---|---|---|---|
| Evaluates | Skill **structure** quality | Skill **output** quality | Output + regression + obsolescence |
| Method | Static inspection | Run test cases + grade | A/B blind comparison + multi-agent |
| When | Is it well-built? | Does it work? | Did it regress? Still needed? |
| Output | Scorecard + grade A-F | pass_rate, tokens, time | benchmark.json + comparator verdict |
| Platform | Any agent | Any agent | Claude Code only (plugin) |
| Cost | Zero (read-only) | Tokens (2x runs) | Tokens (2x runs + judge) |

Use in sequence: **skill-evaluation** (design review) → **evals** (functional validation) → **benchmark** (ongoing monitoring).

📄 [View full documentation](skills/skill-evaluation/SKILL.md)

---

### 🛡️ Security Specialist · `runbooks`
Full-stack application security agent — performs SAST (static code analysis), DAST (dynamic testing against running apps), threat modeling, vulnerability triage, remediation, and penetration testing. Combines source code review with live testing against local dev servers or production targets for complete evidence correlation.

**When to use:** security scan a repository, review a PR for security issues, build a threat model, triage vulnerability findings, fix a security bug, pentest a web application, validate a security fix, track findings to GitHub/Jira/Linear, generate a security report.

**Key features:**
- **Input-driven SOP**: path only → SAST + dev DAST; path + URL → SAST + dev + prod; URL only → DAST
- **12 steering workflows**: full-scan, diff-review, pentest, hunting, threat-model, attack-paths, discovery, triage, remediation, tracking, validation, reporting
- **6-phase pipeline** (full-scan): Recon → Hunt → Validate → Report → Schema → Verify — with parallel agents and adversarial validation
- **9 attack classes**: Injection, Access Control, Resource/File, Cryptography, Business Logic, Feature Abuse, Chained Attacks, Wildcard, Obvious Things
- **12-angle hunting methodology**: sad path, boundaries, component assumptions, wrong ordering, concurrency, parser disagreements, round-trip fidelity, config control, privilege tracing, leaked context, parameter overrides, unverified claims
- **Adversarial validation**: separate agents try to DISPROVE findings (5 gates: exploitation, impact, baseline, mitigation, parser/runtime)
- **Structured JSON output**: findings.json validated against JSON schema with trace (entrypoint→propagation→sink), conditions, execution, confidence
- **Schema validator**: zero-dependency Node.js script (`validate-findings.cjs`) for CI integration
- **Multi-run additive coverage**: each run targets gaps from prior runs; single run finds ~50% of total vulnerabilities
- **5 utility scripts**: SQLite scan DB, file ranker, report finalizer, pentest automation, schema validator
- **Pentest tool cascade**: nmap → python-nmap → socket scan; nikto → wapiti3 → header checks; gobuster → dirsearch → urllib brute
- **Three-layer correlation**: source finding → dev exploit → prod confirmation
- **Dynamic baseline calibration**: compares patterns against industry-standard comparable applications

**Architecture:**
```
security-specialist/
├── SKILL.md              (router + core principles + anti-patterns)
├── steering/             (12 workflow docs including hunting methodology)
├── scripts/              (5 tools: Python + Node.js validator)
└── references/           (5 spec docs: finding format, report format, severity policy, artifacts, report-schema.json)
```

**Improvements in v2.0 (Jun 2026):**
- Added 6-phase audit pipeline with parallel agents (inspired by Cloudflare security-audit-skill)
- Added `steering/hunting.md` with 9 attack classes and 12-angle hunting methodology
- Added adversarial validation (Phase 3) and independent verification (Phase 6)
- Added `references/report-schema.json` for structured findings with trace, conditions, execution, confidence
- Added `scripts/validate-findings.cjs` zero-dependency JSON schema validator
- Added multi-run additive coverage strategy
- Added 10 anti-patterns to avoid in security audits
- Added dynamic baseline calibration to severity policy
- Enhanced finding format: simple (SQLite) + structured (JSON pipeline) dual format

📄 [View full documentation](skills/security-specialist/SKILL.md)

---

### 🚀 Astro Sites Manager · `ci-cd-and-deployment`
Comprehensive skill for building, migrating, and maintaining Astro v7 projects. Covers the full lifecycle: best practices, v6→v7 migration with structured plan, validation of breaking/deprecated patterns, AI-enhanced dev server (background mode, JSON logging), advanced routing with src/fetch.ts, route caching, Sätteri Markdown, Rust compiler, Starlight docs, Pagefind search, SEO, testing, and deployment to 8+ platforms including Coolify.

**When to use:** build Astro sites, upgrade to v7, deploy on Coolify/Vercel/Netlify/Cloudflare, validate breaking changes, configure Starlight docs, set up Pagefind search, use background dev server as AI agent, configure route caching.

**Key features:**
- MCP Astro Docs integration (real-time docs access)
- 10 reference files covering migration, validation, testing, deployment, Starlight, and more
- Coolify-specific deployment guide with 17-project battle-tested patterns
- Feature detection: v7 features activate only when available (safe on v6)

📄 [View full documentation](skills/astro-sites-manager/SKILL.md)

---

> **Skills revised in March 2026** following the Anthropic standard for Agent Skills structure and quality.
> Source: [Improving Skill Creator: Test, Measure and Refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

## Installation

You can install these skills using any compatible installer or manually. Below are the most popular options.

### Via [Skills.sh](https://skills.sh/docs)

```bash
npx skills add https://github.com/fabricioctelles/skills
```

Or install a specific skill:

```bash
npx skills add https://github.com/fabricioctelles/skills -s geo-optimization
npx skills add https://github.com/fabricioctelles/skills -s substack-expert
npx skills add https://github.com/fabricioctelles/skills -s pier-cloud
npx skills add https://github.com/fabricioctelles/skills -s ultimate-design-system-master
npx skills add https://github.com/fabricioctelles/skills -s resume-ats-beater
npx skills add https://github.com/fabricioctelles/skills -s coolify-operator
npx skills add https://github.com/fabricioctelles/skills -s agent-ready-cloudflare
npx skills add https://github.com/fabricioctelles/skills -s ralph-loop-kiro-specs
npx skills add https://github.com/fabricioctelles/skills -s loop-architect
npx skills add https://github.com/fabricioctelles/skills -s humanizar
npx skills add https://github.com/fabricioctelles/skills -s auth-md
npx skills add https://github.com/fabricioctelles/skills -s astro-sites-manager
npx skills add https://github.com/fabricioctelles/skills -s security-specialist
```

### Via [Agent Skills CLI](https://www.agentskills.in/docs)

```bash
npm install -g agent-skills-cli
```

Then install the skills:

```bash
skills add https://github.com/fabricioctelles/skills
```

Or use without global install:

```bash
npx agent-skills-cli install https://github.com/fabricioctelles/skills
```

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/fabricioctelles/skills.git
```

2. Copy the desired skill folder to your agent's skills directory:
```bash
# Example for Cursor
cp -r skills/geo-optimization .cursor/skills/
cp -r skills/substack-expert .cursor/skills/
cp -r skills/pier-cloud .cursor/skills/
cp -r skills/ultimate-design-system-master .cursor/skills/
cp -r skills/resume-ats-beater .cursor/skills/
cp -r skills/coolify-operator .cursor/skills/
cp -r skills/agent-ready-cloudflare .cursor/skills/
cp -r skills/ralph-loop-kiro-specs .cursor/skills/
cp -r skills/loop-architect .cursor/skills/
cp -r skills/humanizar .cursor/skills/
cp -r skills/auth-md .cursor/skills/
cp -r skills/astro-sites-manager .cursor/skills/

# Example for Claude Code
cp -r skills/geo-optimization .claude/skills/
cp -r skills/substack-expert .claude/skills/
cp -r skills/pier-cloud .claude/skills/
cp -r skills/ultimate-design-system-master .claude/skills/
cp -r skills/resume-ats-beater .claude/skills/
cp -r skills/coolify-operator .claude/skills/
cp -r skills/agent-ready-cloudflare .claude/skills/
cp -r skills/ralph-loop-kiro-specs .claude/skills/
cp -r skills/loop-architect .claude/skills/
cp -r skills/humanizar .claude/skills/
cp -r skills/auth-md .claude/skills/
cp -r skills/astro-sites-manager .claude/skills/

# Example for Kiro
cp -r skills/geo-optimization .kiro/skills/
cp -r skills/substack-expert .kiro/skills/
cp -r skills/pier-cloud .kiro/skills/
cp -r skills/ultimate-design-system-master .kiro/skills/
cp -r skills/resume-ats-beater .kiro/skills/
cp -r skills/coolify-operator .kiro/skills/
cp -r skills/agent-ready-cloudflare .kiro/skills/
cp -r skills/ralph-loop-kiro-specs .kiro/skills/
cp -r skills/loop-architect .kiro/skills/
cp -r skills/humanizar .kiro/skills/
cp -r skills/auth-md .kiro/skills/
cp -r skills/astro-sites-manager .kiro/skills/
```

The Agent Skills format is universal and works with any compatible agent. See the [official specification](https://agentskills.io/specification.md) for details.

## Repository Structure

```
skills/
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
├── loop-architect/
│   ├── SKILL.md           # loop design coach (adapted from Looper by ksimback)
│   ├── scripts/           # compiler and model detection
│   ├── templates/         # portable Python runner
│   ├── references/        # rubrics (goal, verification, council, control)
│   ├── schemas/           # loop.yaml JSON schema
│   └── examples/          # ai-workflow-mapping example
├── humanizar/
│   ├── SKILL.md
│   └── references/        # 55+ AI patterns specific to Brazilian Portuguese (6 files)
├── auth-md/
│   ├── SKILL.md
│   └── references/        # protocol template, validation rules, metadata schema, example, implementation guide
│   ├── SKILL.md
│   └── references/        # 6 compliance check modules (privacy policy, cookies, data minimization, transfers, rights, scripts)
```

## Author

Created by [ft.ia.br](https://ft.ia.br)

## References

- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic's skill category framework (9 types)
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — Writing guidance from the Agent Skills spec
- [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills) — Eval-driven iteration with test cases and benchmarks

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
