---
name: humanizar
description: Write and edit Brazilian Portuguese prose with natural rhythm and the author's voice while preserving facts, meaning, and intent. Use for PT-BR requests to humanizar, tirar cara de IA, remover AI slop, reescrever com voz, simplify language, or write a post, email, article, or bio. For English text, use the bundled human-ai skill.
---

# Humanizar

Edit or draft Brazilian Portuguese text using the bundled PT-BR catalogs.
Return the text in PT-BR. Work with the current model without external services,
MCP tools, scripts, accounts, or package installation.

## Trava factual

Preserve names, numbers, dates, quotations, sources, examples, causal relationships,
uncertainty, commitments, argument, intent, code, and notation. Condense form, not
meaning. Never invent a statistic, personal experience, source, deadline, status,
or example to make a passage more concrete. Preserve unsupported claims and flag
them separately for verification instead of silently changing them.

The references contain illustrative examples. Do not transfer their facts into
the user's text. This factual lock takes priority over every catalog suggestion
to add detail, remove a claim, strengthen certainty, or inject an opinion.

Preserve natural regionalisms, contractions, and domain terms such as feedback,
deploy, churn, and onboarding. Correct grammar only when it serves the user's
request. A word, dash, or formal register alone does not prove AI authorship.
Never use detector scores as editing targets or promise a detector outcome.

## Modes and voice

- `modo_completo` (default): diagnosis, rewrite, and a short report; at most three passes.
- `modo_direto`: one pass with a brief report, or text only when requested.
- `modo_revisao`: detailed findings and rewrite; at most three passes.
- `modo_criacao`: draft from a supplied topic and factual material; at most two passes.

Honor the selected mode. Use the requested voice, then a supplied sample, then
the source register. Without a clear signal, use a neutral voice. Supported
registers include cronica, jornalistico, academico, corporativo, social post,
WhatsApp, juridico, didatico, portugues simplificado, assertivo, enxuto, and resumo.
Do not invent opinion or personal experience to imitate a sample.

## Workflow

1. For editing, confirm a PT-BR source exists; ask for it if missing. For creation,
   obtain the topic, audience, and available factual material. Route English to
   [human-ai](../human-ai/SKILL.md). In mixed-language text, edit only requested spans.
2. Select the voice and read the catalogs relevant to the task:
   - [Conteudo](references/padroes-conteudo.md): inflated claims and vague authority.
   - [Linguagem](references/padroes-linguagem.md): mechanical vocabulary and syntax.
   - [Tom](references/padroes-tom.md): hedging, flattery, and artificial emphasis.
   - [Composicao](references/padroes-composicao.md): templates and weak progression.
   - [Estilo](references/padroes-estilo.md): formatting and punctuation.
   - [PT-BR](references/padroes-exclusivos-pt-br.md): gerundismo, oficialês, and ENEM-style endings.
   - [Linguagem simples](references/padroes-portugues-simplificado.md): accessible wording when requested.
   - [Consumo rapido](references/padroes-consumo-rapido.md): assertivo, enxuto, and resumo when relevant.
3. Diagnose clusters of mechanical patterns. Keep intentional formality,
   regionalisms, purposeful repetition, logical transitions, and dialogue dashes.
4. Restructure rhythm and flow before swapping words. Preserve every proposition,
   scope condition, warning, and degree of certainty. For text over 500 words,
   work in semantic blocks and validate the joined result.
5. Compare each candidate with the immutable source. Reject factual or semantic
   changes. For creation, every factual assertion must come from supplied or
   actually verified material. If a fact is missing, use simpler wording, ask for
   the missing fact, or mark `[DADO OU EXEMPLO REAL NECESSARIO]`.
6. Deliver the best safe candidate within the mode's pass limit. If none is safe,
   return the source and explain why. Never keep iterating indefinitely.

## Delivery

Return the text first. Add only the report appropriate to the selected mode.
In `modo_criacao`, or when the user asks for text only, deliver just the text;
briefly identify a missing fact when needed. For review, cite actual passages and
explain each material change. Do not invent numerical scores or measurements.

Do not rewrite safety-critical instructions, original normative laws or contracts,
literal translations, or exact-match material. Offer separate comments instead.
Do not publish, upload, or send the user's text without an explicit request.
