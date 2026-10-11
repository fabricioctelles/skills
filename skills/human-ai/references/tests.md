# Evaluation cases

Existing sample set for evaluating future changes in `full_mode`. Expected wording
is illustrative, not an exact-match requirement. Compare each result to the
source for every protected proposition before assessing style. Style gains cannot
compensate for additions, omissions, changed certainty, or invented experience.

| # | Type | Source | Safe rewrite example |
|---|---|---|---|
| T1 | Corporate email | “I am writing to inform you that the report will be forwarded in due course” | “The report will be forwarded in due course.” |
| T2 | Academic paragraph | “Various authors discuss the question of language in broad terms” | “Various authors discuss language in broad terms.” |
| T3 | Authorial legal commentary | “It is well-established that strict liability applies in the context of consumer relations” | “It is well established that strict liability applies to consumer relations.” |
| T4 | Blog template | “In this article, we will explore 5 essential strategies to optimize your workflow” | “This article explores five essential strategies to optimize your workflow.” |
| T5 | AI hedging | “As a language model, I cannot state with certainty, but it appears that perhaps the system may be functioning” | “The system may be functioning, but that cannot yet be stated with certainty.” |
| T6 | Generic explainer | “Alice has 3 apples and Bob has 5. How many do they have together?” | “Alice has 3 apples and Bob has 5. How many apples do they have together?” |

T1 must retain the future state and unspecified timing. T2 must not invent authors
or citations. T3 must not add a jurisdiction, statute, or legal exception. T4 must
retain the count, purpose, and evaluation rather than introduce a personal story.
T5 may remove the assistant wrapper but must retain uncertainty and add no test
result. T6 must preserve names, quantities, and the arithmetic task; its simplicity
is not a reason to replace the example.

For a requested evaluation, reject unsafe candidates regardless of naturalness.
No behavioral benchmark was run merely by maintaining these examples.
