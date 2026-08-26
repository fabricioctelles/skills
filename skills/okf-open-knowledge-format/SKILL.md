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
  version: "2.0"
  date: 2026-08-25
  repository: https://github.com/fabricioctelles/skills
  license: Apache-2.0
  category: library-and-api-reference
  upstream: https://github.com/GoogleCloudPlatform/open-knowledge-format
---

# Open Knowledge Format (OKF)

OKF is a vendor-neutral, open spec (v0.2, released by Google Cloud) for representing knowledge as a directory of markdown files with YAML frontmatter. No SDK required — if you can `cat` a file, you can read OKF.

It formalizes the "LLM Wiki" pattern ([Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)) into an interoperable format: wikis written by different producers can be consumed by different agents without translation.

**v0.2 adds:** provenance tracking (`sources`), trust signals (`generated`, `verified`), lifecycle management (`status`, `stale_after`), and **Attested Computations** — a new concept type for sanctioned, verifiable calculations.

For the full spec, see:
- [references/spec-v02.md](references/spec-v02.md) — Current version (v0.2)
- [references/spec-v01.md](references/spec-v01.md) — Legacy version (v0.1)

### Design Principles

1. **Minimally opinionated** — Only `type` is required. The spec defines interoperability surface, not content model.
2. **Producer/consumer independence** — Who writes and who reads are decoupled. Human-authored bundles feed agents; LLM-generated bundles are browsed by humans.
3. **Format, not platform** — No cloud, SDK, or vendor dependency. Value comes from how many parties speak it.
4. **Trust is first-class** — v0.2 makes provenance, verification, and freshness queryable from frontmatter.

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Bundle** | A directory tree of `.md` files. The unit of distribution (git repo, tarball, or subdirectory). |
| **Concept** | One markdown file = one unit of knowledge (table, metric, playbook, API, etc.) |
| **Concept ID** | File path within the bundle, minus `.md` suffix. Example: `tables/users.md` → ID `tables/users` |
| **Frontmatter** | YAML block between `---` delimiters at file top. |
| **Body** | Everything after the frontmatter. Standard markdown. |
| **Link** | Standard markdown link expressing a relationship between concepts. |
| **Source** | A material a concept derives from, recorded in the `sources` frontmatter field. |
| **Provenance** | The set of sources a concept derives from. |
| **Actor** | Identity string: `<producer>/<version>` for agents, `human:<id>` for people, `process:<id>` for automation. |
| **Trust tier** | Level derived from `verified`: unverified, machine-confirmed, or human-reviewed. |
| **Attested Computation** | A concept (`type: Attested Computation`) carrying a sanctioned way to compute a value. |

---

## Quick Reference — Frontmatter Fields

### Core Fields (all concepts)

| Field | Required? | Description |
|-------|-----------|-------------|
| `type` | **YES** | Kind of concept (free-form string, e.g. `BigQuery Table`, `Metric`, `Playbook`, `Attested Computation`) |
| `title` | Recommended | Human-readable display name |
| `description` | Recommended | One-sentence summary |
| `resource` | Recommended | URI identifying the underlying asset (omit for abstract concepts) |
| `tags` | Optional | YAML list for cross-cutting categorization |

### Trust & Lifecycle Fields (v0.2)

| Field | Description |
|-------|-------------|
| `generated` | `{ by: <actor>, at: <ISO8601> }` — Who/what created this content and when |
| `verified` | List of `{ by: <actor>, at: <ISO8601> }` — Who confirmed correctness |
| `status` | `draft` \| `stable` \| `deprecated` — Default: `stable` |
| `stale_after` | ISO 8601 datetime — Content is stale on/after this instant |

### Provenance Fields (v0.2)

| Field | Description |
|-------|-------------|
| `sources` | List of source entries (see below) |
| `usage_window` | `{ from, to }` — Time range for `usage_count` signals |

Each `sources` entry:
- `resource` (REQUIRED): URL, bundle-relative path, or scope descriptor
- `id`: Stable key for footnote attribution
- `title`: Human-readable label
- `author`: Actor who produced the source
- `usage_count`: How often exercised (liveness signal)
- `last_modified`: When the source last changed

### Attested Computation Fields (v0.2)

For concepts with `type: Attested Computation`:

| Field | Description |
|-------|-------------|
| `runtime` | REQUIRED. How to run it: `bigquery`, `postgres`, `dbt`, `python`, `Looker` |
| `parameters` | List of `{ name, type, required }` — Typed holes the agent fills |
| `computation` | Path to computation file (if not inline in body) |
| `executor` | `{ resource, receipt: [...] }` — How to run and what evidence to capture |
| `attester` | `{ resource }` — Deterministic code that verifies the receipt |

### Reserved Filenames

| File | Purpose | Has frontmatter? |
|------|---------|-----------------|
| `index.md` | Directory listing for progressive disclosure | NO* |
| `log.md` | Change history, newest first | NO |

*Exception: bundle-root `index.md` MAY have frontmatter with `okf_version: "0.2"`.

### Conventional Body Headings

| Heading | When to use |
|---------|-------------|
| `# Schema` | Data assets — describe columns/fields |
| `# Examples` | Show concrete usage (code blocks, queries) |
| `# Computation` | Attested Computation — the sanctioned code/query |

---

## Actor Convention

Fields that record identity (`generated.by`, `verified[].by`, `sources[].author`) use:

- `<producer>/<version>` for agents: `reference_agent/gemini-2.5-pro`
- `human:<id>` for people: `human:ahormati`
- `process:<id>` for automation: `process:finance-nightly`

Trust tiers are derived from the `human:` prefix — human-verified > machine-confirmed > unverified.

---

## Trust Tiers

Consumers derive trust from the `verified` field:

| Condition | Trust Tier |
|-----------|------------|
| No `verified` key | **Unverified** |
| `verified` by non-`human:` actors only | **Machine-confirmed** |
| `verified` by a `human:<id>` actor | **Human-reviewed** |

Trust tiers are advisory signals, not access control.

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
---

# Monthly Recurring Revenue (MRR)

Sum of all active subscriptions normalized to a monthly amount.
```

Full v0.2 example with provenance and trust:

```markdown
---
type: Metric
title: Monthly Recurring Revenue
description: Sum of all active subscription revenue normalized to monthly.
tags: [revenue, saas, kpi]
status: stable
generated: { by: human:ftelles, at: 2026-08-25T10:00:00Z }
verified: { by: human:finance-lead, at: 2026-08-25T14:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: stripe-docs
    resource: https://stripe.com/docs/billing/subscriptions
    title: Stripe Subscription Billing
    author: team:stripe-docs
    last_modified: 2026-06-01T00:00:00Z
---

# Monthly Recurring Revenue (MRR)

## Definition

Sum of all active subscriptions normalized to a monthly amount.[^stripe-docs]
Excludes one-time fees and overages.

## Formula

`MRR = Σ(active_subscription_monthly_value)`

## Related

- [Churn Rate](./churn.md) uses MRR as denominator
- [ARR](./arr.md) = MRR × 12

[^stripe-docs]: Stripe Subscription Billing
```

For more examples across domains, see [references/examples.md](references/examples.md).

### 3. Cross-link concepts

Use standard markdown links. Two forms:

- **Absolute** (bundle-relative, starts with `/`): `[customers](/tables/customers.md)` — **preferred** (stable when files move)
- **Relative**: `[churn](./churn.md)`

Links assert relationships. The kind of relationship is conveyed by surrounding prose, not by the link syntax. Broken links are explicitly permitted — they represent knowledge not yet written.

### 4. Add provenance with footnotes (v0.2)

When claims reference external sources, use `sources` in frontmatter and footnotes in body:

```yaml
sources:
  - id: ga4-schema
    resource: https://developers.google.com/analytics/bigquery/export-schema
    title: GA4 BigQuery Export schema
```

```markdown
The `events_` table is sharded daily as `events_YYYYMMDD`.[^ga4-schema]

[^ga4-schema]: GA4 BigQuery Export schema
```

### 5. Generate index.md

Place in any directory for progressive disclosure. No frontmatter. Format:

```markdown
# Metrics

- [MRR](./mrr.md) - Monthly recurring revenue
- [Churn](./churn.md) - Monthly churn rate
- [NPS](./nps.md) - Net Promoter Score
```

Entries should include the description from the linked concept's frontmatter.

### 6. Generate log.md (optional)

Chronological change history, newest first, ISO 8601 date headings:

```markdown
# Update Log

## 2026-08-25
- **Creation**: Added MRR, Churn, and NPS metrics.
- **Creation**: Established directory structure.

## 2026-08-20
- **Initialization**: Bundle created.
```

### 7. Declare version (optional)

Bundle-root `index.md` may include frontmatter declaring the spec version:

```markdown
---
okf_version: "0.2"
---

# My Knowledge Bundle

- [Tables](./tables/) - Database tables
- [Metrics](./metrics/) - Business KPIs
```

### 8. Distribution

A bundle can be distributed as:
- A **git repository** (recommended — history, attribution, diffs)
- A tarball or zip archive
- A subdirectory within a larger repository

### 9. Verify conformance

Three rules — all must pass:
1. Every non-reserved `.md` file has parseable YAML frontmatter
2. Every frontmatter has a non-empty `type` field
3. Reserved files (`index.md`, `log.md`) follow their defined structure when present

---

## Create an Attested Computation (v0.2)

Attested Computations are concepts that carry not just what a value *means* but a sanctioned way to *compute* it. Use them when you need verifiable, reproducible calculations.

### When to use

- Financial metrics where compliance requires audit trails
- KPIs that must be computed consistently across reports
- Any calculation where "did the sanctioned thing run" matters

### Structure

```markdown
---
type: Attested Computation
title: Revenue for fiscal year
description: Recognized revenue for a fiscal year, per Finance's definition.
status: stable
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: references/skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: references/attesters/revenue.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-09-23T00:00:00Z
sources:
  - id: rev-policy
    resource: https://wiki.acme/finance/revenue-recognition
    title: Revenue recognition policy
---

# Computation

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = @year

The computation binds only the declared `parameters`, per the recognition
policy.[^rev-policy]

[^rev-policy]: Revenue recognition policy
```

### Key rules

1. **Agent fills parameters only** — The agent supplies *values* for declared `parameters`, never edits the computation itself
2. **Computation can be inline or external** — Use `# Computation` heading for inline, or `computation:` field for external file
3. **Executor produces receipt** — Evidence the attester inspects
4. **Attester is deterministic** — No LLM, just code that verifies the receipt

### Linking to computations

Other concepts link to Attested Computations:

```markdown
---
type: Metric
title: Revenue
---

# Definition

Recognized revenue for a fiscal year, computed by 
[the revenue computation](../computations/revenue.md).
```

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

When okflint is not installed, use [scripts/validate.sh](scripts/validate.sh) which checks the 3 core conformance rules plus v0.2 fields.

When asked to validate, check the 3 conformance rules. Report:

```
✅ PASS: 12/12 concept files have valid frontmatter with type field
✅ PASS: index.md follows list structure (no frontmatter)
✅ PASS: log.md uses ISO 8601 date headings, newest first

⚠  WARNING: 3 files missing 'description' field (recommended)
⚠  WARNING: 2 broken cross-links (permitted but worth noting)
ℹ  INFO: 5 files with trust fields (generated/verified)
ℹ  INFO: 2 Attested Computation concepts found
```

For a script-based check, see [scripts/validate.sh](scripts/validate.sh).

### Errors (conformance failures)

- `E1`: File `{path}` has no YAML frontmatter
- `E2`: File `{path}` has frontmatter but no `type` field (or empty)
- `E3`: Reserved file `{path}` has unexpected structure
- `E4`: Attested Computation missing required `runtime` field

### Warnings (non-blocking, spec allows these)

- `W1`: Missing recommended field `title` or `description`
- `W2`: Broken cross-link `{link}` in `{file}`
- `W3`: No `generated` field (v0.2 recommended)
- `W4`: No `index.md` in directory `{dir}`
- `W5`: `log.md` dates not in ISO 8601 format
- `W6`: `sources` entry missing `resource` field
- `W7`: `stale_after` date has passed — content is stale

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

### Add provenance (v0.2)

Add `sources` to frontmatter and footnotes to body for per-claim attribution:

```yaml
sources:
  - id: official-docs
    resource: https://example.com/docs
    title: Official Documentation
    author: team:product-docs
    last_modified: 2026-07-15T00:00:00Z
```

### Add trust signals (v0.2)

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-08-25T10:00:00Z }
verified: { by: human:domain-expert, at: 2026-08-25T14:00:00Z }
status: stable
stale_after: 2026-12-31T00:00:00Z
```

### Add cross-links

Weave links into natural prose. Don't create a standalone "links" section — express relationships in context where they're meaningful.

### Fill recommended fields

If `title`, `description`, `tags` are missing, add them. Derive values from body content when possible.

### Enrichment workflow reference

The official enrichment agent follows this pattern — apply the same logic manually:
1. Start with metadata-only docs (just frontmatter + minimal body)
2. Add schema/structure from source system
3. Add `sources` from authoritative documentation
4. Weave cross-links based on discovered relationships (FKs, shared tags, join paths)
5. Generate `index.md` files for progressive disclosure
6. Add `generated` and optionally `verified` for trust tracking

---

## Migrate v0.1 to v0.2

### Breaking changes to address

1. **`timestamp` → `generated.at`**
   ```yaml
   # v0.1
   timestamp: 2026-05-28T22:53:05Z
   
   # v0.2
   generated: { by: human:author, at: 2026-05-28T22:53:05Z }
   ```

2. **`# Citations` → `sources`**
   ```markdown
   # v0.1 body
   # Citations
   [1] https://example.com/docs
   
   # v0.2 frontmatter
   sources:
     - id: docs
       resource: https://example.com/docs
       title: Example Documentation
   ```

### Migration script pattern

```bash
# For each .md file:
# 1. Extract timestamp, convert to generated
# 2. Parse # Citations, convert to sources
# 3. Add footnotes in body for citations

# Consumers MAY fall back to legacy fields when v0.2 fields absent
```

### Backward compatibility

v0.2 consumers SHOULD:
- Fall back to `timestamp` when `generated` is absent
- Parse legacy `# Citations` when `sources` is absent

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
7. **Respect trust hierarchy.** Only mark as `verified` by `human:` if actually human-reviewed. Don't fabricate verification.
8. **Computation integrity.** Never edit the computation in an Attested Computation concept — only fill parameters.

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

### Visualizer

The reference agent includes a `visualize` subcommand that renders any OKF bundle as a self-contained interactive HTML file:

```bash
python -m reference_agent visualize --bundle ./bundles/<name>
```

Features:
- Force-directed graph of concepts with colored nodes by type
- Detail panel with frontmatter and rendered markdown
- "Cited by" backlinks
- Search and type filtering

**When to mention this to users:** If they're enriching BigQuery datasets, point them to the [reference agent](https://github.com/GoogleCloudPlatform/open-knowledge-format). If they want enterprise catalog integration, point to kcmd.

---

## Output Format

When creating a bundle, present results as:

1. **Directory tree** showing the full structure
2. **Each file's content** in fenced code blocks
3. **Conformance check** confirming the bundle passes the 3 rules
4. **Trust summary** (v0.2) showing verified/unverified counts

```
saas-metrics/
├── index.md
├── log.md
├── metrics/
│   ├── index.md
│   ├── mrr.md
│   ├── churn.md
│   └── nps.md
└── computations/
    └── mrr-calculation.md
```

Then show each file, then confirm:

```
Bundle is OKF v0.2 conformant ✅
- 4 concept files
- 1 Attested Computation
- 3 human-verified, 1 unverified
- 0 stale concepts
```
