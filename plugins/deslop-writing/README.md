# Deslop Writing

Remove AI writing patterns. Keep your meaning and voice.

Deslop Writing bundles two editorial workflows for ChatGPT and Codex:

- **human-ai** edits English prose.
- **humanizar** writes and edits Brazilian Portuguese prose.

Both workflows use the current model with bundled language-specific references.
No MCP server, API key, external evaluator, or package installation is required
to run the writing workflows.

## Try it

> Edit this email to sound natural. Keep all facts, deadlines, and commitments.

> Remove repetitive AI phrasing from this draft. Preserve my voice and return only the edited text.

> Humanize this Brazilian Portuguese article without changing its argument or quotations.

Fictional example:

**Before:** “We would like to take this opportunity to inform you that the report
will be delivered on Friday.”

**After:** “The report will be delivered on Friday.”

Edits preserve facts, uncertainty, quotations, and intent. This is an editing
workflow, not an authorship detector or a guarantee of passing one.

## Install from Git

```bash
codex plugin marketplace add fabricioctelles/skills --ref main
codex plugin add deslop-writing@ft.ia.br
```

Git access follows the repository's access permissions. Installation availability
depends on the client's plugin support. In ChatGPT desktop Work/Codex, browse
the ft.ia.br Skills marketplace in the Plugins Directory and install Deslop
Writing. Start a new chat/session after installation.

License: [Apache-2.0](LICENSE). See [NOTICE](NOTICE) for provenance.
