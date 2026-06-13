# Converting Sources to OKF

Guides for transforming existing knowledge into conformant OKF bundles.

---

## From Notion Export

Notion exports as markdown with properties in YAML-like format.

### Steps

1. **Export** from Notion as Markdown & CSV
2. **Clean filenames** — remove UUID suffixes (`Page Name abc123def.md` → `page-name.md`)
3. **Map properties to frontmatter:**

| Notion Property | OKF Field |
|-----------------|-----------|
| Type (select) | `type` (required) |
| Name | `title` |
| Tags (multi-select) | `tags` |
| Last Edited | `timestamp` |
| URL | `resource` |

4. **Convert links** — Notion uses `[Page Name](Page%20Name%20abc123def.md)`. Convert to clean relative paths: `[Page Name](./page-name.md)`
5. **Remove Notion artifacts** — empty toggle blocks, breadcrumb headers, cover image references
6. **Add missing `type` field** — if Notion had no "Type" property, ask the user what type to assign

### Edge cases

- Notion databases: each row becomes a concept. Database title becomes the directory name.
- Nested pages: respect the hierarchy. Child pages go in subdirectories.
- Inline databases: flatten into a list in the parent concept's body.
- Notion formulas/rollups: drop them — they don't translate to static markdown.

---

## From Obsidian Vault

Obsidian vaults are already close to OKF. Main differences: wikilinks and potentially missing `type` field.

### Steps

1. **Convert wikilinks to standard links:**
   - `[[Note Name]]` → `[Note Name](./note-name.md)`
   - `[[Note Name|Display Text]]` → `[Display Text](./note-name.md)`
   - `[[Note Name#Heading]]` → `[Note Name](./note-name.md#heading)`

2. **Ensure `type` field exists** in every frontmatter block. Common mappings:

| Obsidian pattern | Suggested OKF type |
|------------------|--------------------|
| Daily notes | `Log` |
| MOC / index note | Convert to `index.md` (reserved file) |
| Permanent notes | `Reference` |
| Literature notes | `Reference` |
| Project notes | `Playbook` or domain-specific |

3. **Convert tags:**
   - Inline `#tag` → move to frontmatter `tags: [tag]`
   - Nested `#parent/child` → flatten to `tags: [parent, child]` or keep as `parent/child`

4. **Handle embeds:**
   - `![[Note]]` — convert to a regular link or inline the content
   - `![[image.png]]` — keep as standard markdown image `![](./image.png)`

5. **Remove Obsidian-specific syntax:**
   - `%%comments%%` → remove
   - `> [!callout]` → convert to blockquote or heading
   - Dataview queries → remove (dynamic, not portable)

### What to keep as-is

- Standard markdown formatting (headings, lists, tables, code blocks)
- Existing YAML frontmatter (just add `type` if missing)
- Standard markdown links (already OKF-compatible)
- Mermaid diagrams (standard markdown fenced blocks)

---

## From CSV / Spreadsheet

Each row becomes one concept document.

### Steps

1. **Identify column mapping:**

| Column role | Maps to |
|-------------|---------|
| Primary identifier / name | Filename (slugified) |
| Category / kind | `type` field |
| Short description | `description` field |
| Tags / labels | `tags` field |
| URL / link | `resource` field |
| Last modified date | `timestamp` field |
| All other columns | Body content (as table or sections) |

2. **Generate one `.md` per row:**

```markdown
---
type: {category_column}
title: {name_column}
description: {description_column}
tags: [{tag1}, {tag2}]
timestamp: {date_column}T00:00:00Z
---

# {name_column}

| Field | Value |
|-------|-------|
| Column3 | {value} |
| Column4 | {value} |
```

3. **Generate index.md** from the full list:

```markdown
# {Sheet Name}

- [{row1_name}](./{row1_slug}.md) - {row1_description}
- [{row2_name}](./{row2_slug}.md) - {row2_description}
```

4. **Generate log.md** with creation entry:

```markdown
# Update Log

## {today_iso8601}
- **Creation**: Generated {N} concepts from spreadsheet import.
```

### Edge cases

- Empty cells: omit the field entirely (don't write empty strings)
- Multi-value cells (comma-separated): parse into YAML list for `tags`
- Very long text cells: put in body as a section, not in frontmatter
- Duplicate names: append a disambiguator (e.g., `widget-v1.md`, `widget-v2.md`)
