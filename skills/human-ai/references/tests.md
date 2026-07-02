# Regression Test Suite (Full Reference)

Minimum sample set for validating future evolutions. Each test should run in full_mode and verify output matches expected result.

| # | Type | Before (AI) | After expected (synthesis) |
|---|---|---|---|
| T1 | Corporate email | "I am writing to inform you that the report will be forwarded in due course" | "Hey team, report's done - just sent it to the channel. Ping me with questions." |
| T2 | Academic paragraph | "Various authors discuss the question of language in broad terms" | "Foucault (1977) frames language as a power device; Bakhtin (1981) sees it as a dialogic arena. The disagreement isn't just terminological." |
| T3 | Legal text | "It is well-established that strict liability applies in the context of consumer relations" | "The Consumer Protection Act establishes strict liability under Section 402A. In practice, manufacturers only escape liability by proving sole consumer fault - which is rare." |
| T4 | Blog template | "In this article, we will explore 5 essential strategies to optimize your workflow" | "I'll cut to it: the strategy that saved me the most time in 2025 wasn't a new tool. It was stopping using new tools." |
| T5 | AI hedging | "As a language model, I cannot state with certainty, but it appears that perhaps the system may be functioning" | "The system's working. I just tested it and the endpoint responded in 340ms." |
| T6 | Generic explainer | "Alice has 3 apples and Bob has 5. How many do they have together?" | "Think about the last time you split a restaurant bill. That's the arithmetic that matters - not hypothetical apples." |

> **Regression criterion**: if an evolution worsens any T1-T6 test result, the change must be reevaluated.
