---
name: okf-open-knowledge-format
description: >
  Create, validate, and enrich Open Knowledge Format (OKF) bundles — the open
  spec for representing organizational knowledge as markdown files with YAML
  frontmatter. Use when the user mentions 'OKF', 'Open Knowledge Format',
  'knowledge bundle', 'OKF bundle', 'create a knowledge base for agents',
  'validate OKF', 'convert to OKF', 'enrich knowledge docs', 'agent-readable
  knowledge', 'LLM wiki', 'knowledge catalog', 'kcmd', or wants to structure
  knowledge as markdown files for AI agent consumption. Also use when the user
  has a directory of markdown files and wants to make them interoperable or
  conformant with the OKF standard. Even for simple requests like 'make this
  folder OKF conformant' — the skill has critical structural rules the agent
  needs.
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-06-17
  repository: https://github.com/fabricioctelles/skills
  license: Apache-2.0
  category: library-and-api-reference
---

# Open Knowledge Format (OKF)

OKF is a vendor-neutral, open spec (v0.1, announced June 12, 2026 by Sam McVeety & Amir Hormati at Google Cloud) for representing knowledge as a directory of markdown files with YAML frontmatter. No SDK required — if you can `cat` a file, you can read OKF.

It formalizes the "LLM Wiki" pattern ([Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) into an interoperable format: wikis written by different producers can be consumed by different agents without translation.

For the full spec, see [references/spec-v01.md](references/spec-v01.md).

### Design Principles

1. **Minimally opinionated** — Only `type` is required. The spec defines interoperability surface, not content model.
2. **Producer/consumer independence** — Who writes and who reads are decoupled. Human-authored bundles feed agents; LLM-generated bundles are browsed by humans.
3. **Format, not platform** — No cloud, SDK, or vendor dependency. Value comes from how many parties speak it.

---

## Key Terminology

- **Bundle** — A directory tree of `.md` files. The unit of distribution (git repo, tarball, or subdirectory).
- **Concept** — One markdown file = one unit of knowledge (table, metric, playbook, API, etc.)
- **Concept ID** — File path within the bundle, minus `.md` suffix. Example: `tables/users.md` → ID `tables/users`
- **Frontmatter** — YAML block between `---` delimiters at file top.
- **Body** — Everything after the frontmatter. Standard markdown.
- **Link** — Standard markdown link expressing a relationship between concepts.
- **Citation** — Link to an external source backing a claim in the body.

---

## Quick Reference — Frontmatter Fields

| Field | Required? | Description |
|-------|-----------|-------------|
| `type` | **YES** | Kind of concept (free-form string, e.g. `BigQuery Table`, `Metric`, `Playbook`, `API Endpoint`) |
| `title` | Recommended | Human-readable display name |
| `description` | Recommended | One-sentence summary |
| `resource` | Recommended | URI identifying the underlying asset (omit for abstract concepts) |
| `tags` | Optional | YAML list for cross-cutting categorization |
| `timestamp` | Optional | ISO 8601 datetime of last meaningful change |

Additional producer-defined keys are allowed. Never reject unknown fields.

## Reserved Filenames

| File | Purpose | Has frontmatter? |
|------|---------|-----------------|
| `index.md` | Directory listing for progressive disclosure | NO* |
| `log.md` | Change history, newest first | NO |

*Exception: bundle-root `index.md` MAY have frontmatter with `okf_version: "0.1"` to declare spec version.

## Conventional Body Headings

| Heading | When to use |
|---------|-------------|
| `# Schema` | Data assets — describe columns/fields |
| `# Examples` | Show concrete usage (code blocks, queries) |
| `# Citations` | List external sources backing claims (numbered) |

---

## Create a Bundle

When the user wants to create an OKF bundle from scratch:

### 1. Determine scope and structure

Ask: What knowledge are we capturing? (tables, metrics, APIs, playbooks, etc.)
Organize into a directory tree that makes sense for the domain.

### 2. Create concept documents

Each concept = one `.md` file. Minimal conformant example:

```markdown
---
type: Metric
title: Monthly Recurring Revenue
description: Sum of all active subscription revenue normalized to monthly.
tags: [revenue, saas]
timestamp: 2026-06-13T10:00:00Z
---

# Monthly Recurring Revenue (MRR)

## Definition

Sum of all active subscriptions normalized to a monthly amount.
Excludes one-time fees and overages.

## Formula

`MRR = Σ(active_subscription_monthly_value)`

## Related

- [Churn Rate](./churn.md) uses MRR as denominator
- [ARR](./arr.md) = MRR × 12
```

For more examples across domains, see [references/examples.md](references/examples.md).

### 3. Cross-link concepts

Use standard markdown links. Two forms:

- **Absolute** (bundle-relative, starts with `/`): `[customers](/tables/customers.md)` — **preferred** (stable when files move)
- **Relative**: `[churn](./churn.md)`

Links assert relationships. The kind of relationship is conveyed by surrounding prose, not by the link syntax. Broken links are explicitly permitted — they represent knowledge not yet written.

### 4. Generate index.md

Place in any directory for progressive disclosure. No frontmatter. Format:

```markdown
# Metrics

- [MRR](./mrr.md) - Monthly recurring revenue
- [Churn](./churn.md) - Monthly churn rate
- [NPS](./nps.md) - Net Promoter Score
```

Entries should include the description from the linked concept's frontmatter.

### 5. Generate log.md (optional)

Chronological change history, newest first, ISO 8601 date headings:

```markdown
# Update Log

## 2026-06-13
- **Creation**: Added MRR, Churn, and NPS metrics.
- **Creation**: Established directory structure.

## 2026-06-10
- **Initialization**: Bundle created.
```

The bold leading word (`**Update**`, `**Creation**`, `**Deprecation**`) is convention, not requirement.

### 6. Declare version (optional)

Bundle-root `index.md` may include frontmatter declaring the spec version:

```markdown
---
okf_version: "0.1"
---

# My Knowledge Bundle

- [Tables](./tables/) - Database tables
- [Metrics](./metrics/) - Business KPIs
```

This is the only place frontmatter is permitted in an `index.md`.

### 7. Distribution

A bundle can be distributed as:
- A **git repository** (recommended — history, attribution, diffs)
- A tarball or zip archive
- A subdirectory within a larger repository

### 8. Verify conformance

Three rules — all must pass:
1. Every non-reserved `.md` file has parseable YAML frontmatter
2. Every frontmatter has a non-empty `type` field
3. Reserved files (`index.md`, `log.md`) follow their defined structure when present

---

## Validate a Bundle

### Preferred: okflint (when available)

[okflint](https://github.com/mattdav/okflint) is a dedicated Python linter for OKF bundles with 18 rules across 3 tiers (OKF core, profile, hygiene). If installed, always prefer it over the built-in bash script.

**Agent behavior:** Before validating, check if okflint is installed (`command -v okflint`). If NOT installed, ask the user:

> "okflint (linter dedicado para OKF com 18 regras, profiles via manifesto e suporte a wikilinks) não está instalado. Quer que eu instale? Opções:
> 1. `uv tool install okflint` (recomendado, isolado)
> 2. `pip install okflint`
> 3. Seguir sem ele (validação básica com o script bash embutido)"

If the user agrees to install:

```bash
# Option 1: uv (recommended — installs isolated, no venv needed)
uv tool install okflint

# Option 2: pip (installs in current environment)
pip install okflint

# Verify installation
okflint --version
```

After installation (or if already available):

```bash
# Full validation with manifest (if okf-base.yaml exists)
if [ -f okf-base.yaml ]; then
  okflint validate --manifest okf-base.yaml ./bundle/
else
  # Core OKF validation only (no manifest needed)
  okflint validate ./bundle/
fi
```

**okflint advantages over the built-in script:**
- Manifest-driven profiles (enforce custom required fields, status vocabularies, per-type constraints)
- Wikilink resolution against full Obsidian vault
- JSON output (`--json`) for CI pipeline parsing
- Detects broken markdown links and ambiguous wikilinks
- Exit codes: `0` = pass, `1` = conformance failure, `2` = bad manifest

### Fallback: built-in bash script

When okflint is not installed, use [scripts/validate.sh](scripts/validate.sh) which checks the 3 core conformance rules.

When asked to validate, check the 3 conformance rules. Report:

```
✅ PASS: 12/12 concept files have valid frontmatter with type field
✅ PASS: index.md follows list structure (no frontmatter)
✅ PASS: log.md uses ISO 8601 date headings, newest first

⚠  WARNING: 3 files missing 'description' field (recommended)
⚠  WARNING: 2 broken cross-links (permitted but worth noting)
```

For a script-based check, see [scripts/validate.sh](scripts/validate.sh).

### Errors (conformance failures)

- `E1`: File `{path}` has no YAML frontmatter
- `E2`: File `{path}` has frontmatter but no `type` field (or empty)
- `E3`: Reserved file `{path}` has unexpected structure

### Warnings (non-blocking, spec allows these)

- `W1`: Missing recommended field `title` or `description`
- `W2`: Broken cross-link `{link}` in `{file}`
- `W3`: No `timestamp` field
- `W4`: No `index.md` in directory `{dir}`
- `W5`: `log.md` dates not in ISO 8601 format

Consumers MUST NOT reject a bundle because of: missing optional fields, unknown type values, unknown frontmatter keys, broken links, or missing index files.

---

## Enrich Concepts

When the user has existing OKF concepts that need enrichment:

### Add schema section

For data assets, add `# Schema` with a columns table:

```markdown
# Schema

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | STRING | Unique identifier |
| `customer_id` | STRING | FK to [customers](/tables/customers.md) |
```

### Add examples section

For APIs, queries, or tools, add `# Examples` with fenced code blocks showing usage.

### Add citations

When claims reference external sources, add `# Citations` at the bottom, numbered:

```markdown
# Citations

[1] [Official docs](https://example.com/docs)
[2] [Internal runbook](https://wiki.internal/quality)
```

Citations may be absolute URLs, bundle-relative paths, or paths into a `references/` subdirectory.

### Add cross-links

Weave links into natural prose. Don't create a standalone "links" section — express relationships in context where they're meaningful.

### Fill recommended fields

If `title`, `description`, `tags`, or `timestamp` are missing, add them. Derive values from body content when possible.

### Enrichment workflow reference

The official enrichment agent follows this pattern — apply the same logic manually:
1. Start with metadata-only docs (just frontmatter + minimal body)
2. Add schema/structure from source system
3. Add citations from authoritative documentation
4. Weave cross-links based on discovered relationships (FKs, shared tags, join paths)
5. Generate `index.md` files for progressive disclosure

---

## Convert Sources to OKF

For detailed conversion guides, see [references/conversion.md](references/conversion.md).

### Quick rules

**Notion export:** Properties → frontmatter. Remove UUID suffixes from filenames. Convert Notion links → relative markdown links.

**Obsidian vault:** Convert `[[wikilinks]]` → `[title](./file.md)`. Ensure `type` field exists. Move inline `#tags` to frontmatter.

**CSV/spreadsheet:** Each row = one concept. Map columns to frontmatter fields. First column = filename.

---

## Guardrails

1. **NEVER invent data.** If you don't know the correct `type`, ask. If you don't have schema info, leave it out. No fabricated URLs or column names.
2. **Preserve unknown fields.** OKF explicitly allows extension. Don't delete fields you don't recognize.
3. **Don't impose taxonomy.** Type values are free-form strings. Suggest descriptive values but never reject a bundle for having unexpected types.
4. **Broken links are OK.** The spec explicitly permits them — they represent not-yet-written knowledge.
5. **Minimal by default.** Generate only `type` (required) + recommended fields that are warranted. Don't pad with empty values.
6. **Ask before assuming.** If the domain is unclear, ask what types and structure make sense.

---

## Serve via Google Cloud Knowledge Catalog

Google Cloud's Knowledge Catalog **natively ingests OKF bundles** and serves them to agents. This is the enterprise path — optional but powerful.

### kcmd CLI (Metadata as Code)

`kcmd` is a bidirectional sync tool between OKF-like local metadata and Knowledge Catalog. Think "git for metadata."

```bash
# Initialize from BigQuery dataset
kcmd init --bigquery-dataset <project>.<dataset>

# Pull current state from catalog
kcmd pull

# Push local changes
kcmd push --dry-run
kcmd push
```

Also ships as an **MCP server** for agent integration:

```json
{
  "mcpServers": {
    "kc-mac": {
      "command": "kcmd",
      "args": ["mcp", "--path", "/path/to/root"]
    }
  }
}
```

MCP tools: `pull`, `push`, `list-entries`, `lookup-entry`, `modify-entry`.

### Reference Enrichment Agent

The official enrichment agent (Python, ADK, Gemini) auto-generates OKF bundles from BigQuery metadata. Two-pass architecture:

1. **BQ pass** — one OKF doc per table/view from metadata
2. **Web pass** — LLM crawls seed URLs and for each page decides to:
   - **(a) Enrich** existing concepts with citations/schemas
   - **(b) Mint** a new `references/<slug>` doc
   - **(c) Skip** irrelevant content

Controls: `--web-seed-file`, `--web-max-pages`, `--web-allowed-host`, `--no-web`.

**When to mention this to users:** If they're enriching BigQuery datasets, point them to the [reference agent](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf). If they want enterprise catalog integration, point to [kcmd](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode) and the [ingest demo](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo).

---

## Output Format

When creating a bundle, present results as:

1. **Directory tree** showing the full structure
2. **Each file's content** in fenced code blocks
3. **Conformance check** confirming the bundle passes the 3 rules

```
saas-metrics/
├── index.md
├── log.md
├── mrr.md
├── churn.md
└── nps.md
```

Then show each file, then confirm: "Bundle is OKF v0.1 conformant ✅"
