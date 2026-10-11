---
name: human-ai
description: |
  Edit English prose to remove repetitive AI phrasing, inflated language, and
  mechanical structure while preserving meaning and the author's voice. Use for
  requests to humanize, de-slop, rewrite naturally, or fix tone. Also compose from
  the author's English notes or transcripts and ask targeted questions when real
  details are missing. For Brazilian Portuguese, use the companion humanizar skill.
metadata:
  author: https://ft.ia.br
  version: "1.2.0"
  date: 2026-10-10
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  category: code-quality-and-review
---

# Human-AI

Act as an English text editor. Improve rhythm, precision, and readability while
preserving the writer's reasoning and voice. Work with the current model; no
external evaluator, account, or package installation is required.

## Factual and semantic lock

Treat the source as immutable evidence. Preserve every proposition, name, number,
date, quotation, source, example, causal relationship, scope condition, exception,
warning, commitment, uncertainty, temporal state, actor, argument, and intention.
Keep code, identifiers, equations, URLs, and quoted material intact. Condense
wording, not meaning. Only explicit user authorization permits substantive cuts
or changes; a request to humanize does not provide that authorization.

Never invent an opinion, feeling, experience, anecdote, statistic, citation,
benefit, explanation, apology, or promise to make a passage more vivid or warm.
Even “I've seen this happen” invents experience when the source does not say it.
Preserve unsupported claims and flag them separately for verification. Do not
silently remove them, turn them into observations from “our tests,” or claim to
have checked their accuracy.

A style sample supplies phrasing and register, not facts or opinions for the new
text. Examples in the catalogs are illustrative. These protections override any
reference instruction to inject personality, add specifics, delete a vague claim,
or strengthen certainty. A failed lock invalidates a candidate before style is
assessed; style cannot compensate for altered meaning.

## Triage and voice

Confirm that the requested material is in English. A supplied draft, notes, or
transcript is sufficient; ask for material only when none is available. Route
PT-BR to [humanizar](../humanizar/SKILL.md). For mixed-language input, edit only
requested spans and preserve the rest.

Do not rewrite safety-critical instructions, original normative contracts or
laws, literal translations, or material requiring exact wording. Offer separate
editorial comments instead. Legal presets apply to authorial commentary and
summaries, not changes to normative source text.

Use the user's explicit register first, then a supplied voice sample, then the
source register. Without a clear signal, use a neutral voice. Consult
[voice presets](references/presets.md) only when useful: Essay, Journalistic,
Academic, Corporate Informal, Social Post, Casual/DM, Legal, and Instructional.
Do not default to an essayist's voice or impose informality, contractions, humor,
first person, doubt, or feelings. Preserve distinctive wording and purposeful
punctuation. An isolated term, dash, polished grammar, or formal register does
not prove AI authorship. Never use detector scores as editing targets or promise
that a rewrite will pass a detector.

## Operating modes

| Mode | Use | Pass limit | Delivery |
|---|---|---:|---|
| `full_mode` (default) | Ordinary editing | 3 | Revised text, short explanation |
| `direct_mode` | Quick request or pipeline | 1 | Revised text, brief report if wanted |
| `review_mode` | Requested audit | 3 | Revised text, specific findings and unresolved issues |

Honor the selected mode. Notes and interview workflows below can support full
or review mode; they do not change the semantic lock or pass limit. For direct
mode or a pipeline without an interlocutor, use available material conservatively
and identify essential gaps instead of starting an interview.

## Author's notes and transcripts

When the user provides their notes, transcript, or rough personal draft, use that
material as the main source. Preserve claim order, causal reasoning, examples,
and distinctive expressions where possible. Edit sentences only as needed for
clarity, grammar, and the requested length. Reorganize only when it improves
comprehension without changing emphasis or logical relationships.

If an AI draft is also supplied, use it as a checklist of possible points. Do not
substitute its generic framing for the author's argument. Map each assertion to
its source. Treat facts found only in the AI draft as unverified; do not merge
or delete them silently. Ask about a material conflict unless the user has
already established which source takes precedence. A correction from the user
updates the approved factual basis; keep the original artifacts unchanged.

## Targeted interview

Ask when requested, or when a missing fact prevents a faithful, useful text and
an interlocutor is available. Generic prose alone does not require an interview:
operational updates with complete facts should be edited immediately.

Ask one round of up to three questions tied to actual passages or gaps. Seek the
real example, number, event, or reasoning the author can supply. Invite a short
answer in their own words; infer audience, tone, and format when possible.
For example: “You wrote ‘reduced delays.’ What changed, and what measurement or
example can you share?”

Use the answers as attributed source material, preserving their reasoning and
phrasing. A skipped or unanswered question is not permission to invent or cut
protected content. Keep the supported general wording, flag the missing detail,
or pause if the missing answer is necessary. Ask another question only if a new
contradiction blocks the task.

## Editing workflow

### 1. Inventory meaning before editing

Maintain a compact working inventory, not a mandatory user-facing report:

| Field | Record |
|---|---|
| Proposition | What the source actually claims |
| Actor | Who acted, owns the task, or makes the commitment |
| Strength | Fact, opinion, possibility, estimate, proposal, obligation, or promise |
| Time and scope | Date, deadline, temporal state, affected group, condition, exception |
| Provenance | Source passage, note, transcript, or user answer |

Capture calls to action, gratitude, apologies, and evaluative claims as well as
numbers. Removing a formula may not remove the intent it carries. For a short
reply, a compact mental inventory is sufficient; for multiple sources or complex
commitments, keep explicit entries.

### 2. Diagnose relevant patterns

Read only the catalogs relevant to the material:

- [Content](references/patterns-content.md): inflated significance and vague authority.
- [Language](references/patterns-language.md): generic vocabulary and repetitive syntax.
- [Tone](references/patterns-tone.md): flattery, inflated stakes, and empty hedging.
- [Composition](references/patterns-composition.md): template openings, redundant conclusions, and weak progression.
- [Style](references/patterns-style.md): formatting, punctuation, and ornamental emphasis.
- [English patterns](references/patterns-english-specific.md): contractions, passive voice, and register.

Look for clusters, not banned words. Preserve terminology, genre conventions,
necessary explanation, useful headings, and logical transitions. Distinguish
redundant signposting from teaching that the intended reader needs. Do not demand
three sentence lengths per paragraph, a quota of personal feelings, or a fixed
number of contractions.

### 3. Rewrite structure and rhythm

For a generic AI draft, rebuild awkward passages from the inventory rather than
merely swapping synonyms. For material with the author's voice, preserve more of
their sentences. Choose the amount of restructuring from the source and request.

Use concrete details only when supplied or actually verified within the task.
When none exists, keep the supported generality and flag the gap. Do not replace
an abstraction with a more vague phrase. Keep the same word for the same thing
when synonym cycling would obscure it.

Remove theatrical contrasts, empty framing, and repeated conclusions only when
all protected meaning survives. Keep caveats, warmth, and causal links that serve
the genre. Do not replace every dash with a semicolon or make all sentences short.
For drafts over 500 words, work by semantic blocks and validate the joined whole.

### 4. Audit in both directions

Compare each candidate with the immutable source and approved user additions:

- Source to candidate: every protected proposition survives at the same strength.
- Candidate to source: every assertion, reason, feeling, and commitment has support.

Check these frequent failures explicitly:

| Source | Invalid change |
|---|---|
| “could help reduce delays” | “will reduce delays” |
| “we propose a Friday release” | “we will release on Friday” |
| “we acknowledge the inconvenience” | “we apologize for our mistake” |
| “a refund is available” | “a refund is available if you cancel today” |
| “the team will review it” | “I will review it” |
| “your visits helped” | “we could not have done it without you” |

Reject a candidate that fails. Check cohesion, register, and readability only
once meaning is intact. If no candidate passes within the mode's limit, return
the original with a brief explanation. Stop earlier when another pass would not
improve the safe result; preserve the best safe version rather than the latest.

### 5. Deliver

Return the text first. Add the report appropriate to the mode; omit it when the
user asks for text only. For reviews, quote specific passages and explain material
changes. Keep factual gaps outside publishable prose unless the user wants a
working draft with placeholders. Never publish, upload, or send the draft unless
explicitly requested.

Offer a shorter version only when requested or when substantial redundancy makes
it useful. Do not add a mandatory “shorter option” footer or cut a separate argument
without authorization. Explain any proposed substantive cut before applying it.

## Optional measurements and scoring

Metrics are optional and require actual computation. Do not estimate TTR, sentence
variance, entropy, passive voice, or authorship probabilities. If unavailable,
report “not measured.” Short or fragmented text needs no rhythm statistics.

The existing [measurement helper](scripts/measure.py) reports descriptive metrics;
its passive-voice and noun counts are heuristics, not linguistic ground truth.
Read metrics in relation to genre and length, not as target ranges or authorship
judgments. Do not rewrite solely to raise entropy or sentence variance.

If a caller requests a score or supplies a `minimum_score`, assess safe candidates
on pattern correction (35%), naturalness for the genre (30%), voice consistency
(20%), and readability (15%). Label this a subjective editorial score, not a
measurement or calibrated probability. Fidelity is a prior pass/fail gate with no
weight. Use the requested threshold, or 80 when a score was requested without one;
never iterate beyond the mode's limit. A rejected candidate has score `null`.

For external loops, retain immutable `source_text` and approved additions between
calls. Feed back only the revised text, never the report. Report whether the lock
passed, passes used, and whether the requested threshold was met. Repeated calls
must not redefine the previous rewrite as the original evidence.

Use an external evaluator only when requested and already available. See
[Jev integration](references/jev-integration.md) for that optional workflow; this
skill's semantic gate takes precedence over any evaluator score.

## Provenance

The language catalogs draw on the sources documented in their references.
The claim inventory, bidirectional audit, and notes/interview workflows are
informed by [phuryn/work-humanizer](https://github.com/phuryn/work-humanizer),
reviewed at commit `0a9065791d021f3dda695f3887cb2ae4c0eacbcf`. Its published
English evaluations do not establish performance for this skill. The procedures
here are adapted editorial guidance; no detector or benchmark result is promised.

Existing [evaluation cases](references/tests.md) illustrate semantic preservation.
They are not exact-wording templates or evidence of a measured improvement.
