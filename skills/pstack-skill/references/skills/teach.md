# Teach

Explain a body of work plainly so a person actually understands it: what it is, how it works, why it is built that way, at their pace. The goal is their understanding, not changing anything.

1. Decide the few things worth walking away with, chosen from why they are asking (about to change it, reviewing it, debugging it, new to it) and what they already know, both read from the conversation. Put depth where their question is.
2. Let `how` and `why` do the investigation; do not redo it by hand. Read enough code to get oriented, then run both (either alone suffices for small changes). Keep `why` narrow by default; put the narrowing in the ask itself so skipped categories get recorded per its contract.
3. Start with a plain definition naming the thing, then tie it to the case in front of you, then how it works, deeper reasons, edge cases. Smallest complete answer first, a sentence or two; add layers when asked. Never a wall of text. Explain mechanisms, do not just name parts. No framing labels ("the key insight", "TL;DR").
4. Keep it a conversation: offer to go deeper or move on, follow their lead. No quizzes, no pacing theater, no "here is the tricky part". Just say it.
5. Show, don't only tell. Open the diff, code, or debugger when fastest. Draw when a picture lands faster than words. Three or more moving parts: draw a series where each diagram redraws the last and adds exactly one part, so the reader watches the system assemble. Mermaid for flows where labels carry meaning; marker-style images for spatial ideas. The build-up rule holds for generated images too. A visual earns its place by teaching, not decorating.

Write every response through [unslop](unslop.md), plain spoken English, tight not terse: cut filler and hedging, keep the part that makes it click. One name per concept throughout. Normal sentence case, periods over commas, clauses split when they pile up.

**Reply:** the explanation itself, never a report about having explained something.
