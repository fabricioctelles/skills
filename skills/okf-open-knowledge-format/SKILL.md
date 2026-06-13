---
name: okf-open-knowledge-format
description: >
  Create, validate, and enrich Open Knowledge Format (OKF) bundles — the open
  spec for representing organizational knowledge as markdown files with YAML
  frontmatter. Use when the user mentions 'OKF', 'Open Knowledge Format',
  'knowledge bundle', 'OKF bundle', 'create a knowledge base for agents',
  'validate OKF', 'convert to OKF', 'enrich knowledge docs', 'agent-readable
  knowledge', 'LLM wiki', 'knowledge catalog', or wants to structure knowledge
  as markdown files for AI agent consumption. Also use when the user has a
  directory of markdown files and wants to make them interoperable or conformant
  with the OKF standard. Even for simple requests like 'make this folder OKF
  conformant' — the skill has critical structural rules the agent needs.
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-06-13
  repository: https://github.com/fabricioctelles/skills
  license: Apache-2.0
---

# Open Knowledge Format (OKF)

OKF is a vendor-neutral, open spec (v0.1, June 2026, Google Cloud) for representing knowledge as a directory of markdown files with YAML frontmatter. No SDK required — if you can `cat` a file, you can read OKF.

For the full spec, see [references/spec-v01.md](references/spec-v01.md).

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

When asked to validate, check the 3 conformance rules. Report:

```
✅ PASS: 12/12 concept files have valid frontmatter with type field
✅ PASS: index.md follows list structure (no frontmatter)
✅ PASS: log.md uses ISO 8601 date headings, newest first

⚠️  WARNING: 3 files missing 'description' field (recommended)
⚠️  WARNING: 2 broken cross-links (permitted but worth noting)
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
