# How

Answer "how does X work?" with a clear architectural explanation at senior-onboarding level: enough for a working mental model, not annotated source. Also owns placement questions ("where should this live", "which package owns this", "is this the right layer").

Two modes:

1. **Explain** (default). Explore and explain.
2. **Critique.** Explain first, then independent architectural critics attack the explanation before you hand anything back.

## Explain

1. **Understand the question and assess complexity.** Subsystem, feature flow, or runtime trace? State your best-guess interpretation if ambiguous; let the user redirect. Simple (one module, narrow question): skip explorers, do it in one pass. Complex (multi-file subsystem, cross-cutting): spawn parallel explorers first.
2. **Explore (complex only).** Decompose into 2-4 angles, each a distinct slice so explorers don't duplicate work (data model / request path / config-and-metrics is a classic split). Spawn all in one message as read-only subagents. Each explorer: start broad (glob directories, grep key type names), follow the thread from entry point through callers, callees, data flow; read the actual code; stop when it can describe input-to-output without hand-waving; note surprises and newcomer traps. Return structured findings; overlap is fine, you reconcile.
3. **Synthesize.** Reconcile overlapping findings, resolve contradictions, weave one unified picture.
4. **Present.** Light edits only; the explanation is the product.

### Output format

Adapt to the question; not every section is needed every time.

- **Overview.** 1-2 paragraphs. What it is, what it does, why it exists.
- **Key concepts.** The types, services, or abstractions needed to understand the rest, briefly defined.
- **How it works.** What triggers it, step by step, where data goes, decision points. Prose, not pseudocode. Reference real files and functions so the reader can go look.
- **Where things live.** A brief map of the relevant files. Only what someone needs to start working here.
- **Gotchas.** Non-obvious traps, historical context for weirdness, sharp edges.

## Critique

Run the full explain flow first; you cannot critique what you have not understood.

Then spawn independent critic subagents (different model families when available) in one message, each read-only. Give each: the explanation, the relevant file paths, and this rubric: find coupling that should not exist, layers that earn nothing, ownership confusion, missing boundaries, error-handling gaps, concurrency hazards, and places where the design fights the domain. No style nits.

Lead judgment like the interrogate procedure: categorize findings Act on / Consider / Noted / Dismissed, each with a one-line reason. Present the explanation first, the critique verdict below it. Someone who wants only understanding should be able to stop reading after the explanation.
