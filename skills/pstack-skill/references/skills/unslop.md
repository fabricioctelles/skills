# Unslop

Edit text to remove AI patterns and add human voice. Applies to every prose surface: replies, docs, PR descriptions, commit messages, decision-log rows.

## Process

1. Scan for the patterns below.
2. Rewrite preserving meaning and intended tone.
3. Add soul.
4. Self-audit: "what makes this obviously AI generated?" Fix what remains.

## Adding soul

Removing patterns is half the job; sterile voiceless writing is just as obvious.

- **Have opinions.** React to facts instead of neutrally listing pros and cons.
- **Vary rhythm.** Short sentences, then longer ones that take their time.
- **Acknowledge complexity.** "Impressive but also kind of unsettling" beats "impressive".
- **Use "I" when it fits.**
- **Let some mess in.** Perfect structure looks machine-made.
- **Be specific.** Not "this is concerning" but the concrete thing that concerns you.

## Patterns

Content:
1. Puffery ("pivotal moment", "testament to", "evolving landscape"). State what happened.
2. Name-dropping outlets without context. Pick one, say what was said.
3. Superficial -ing phrases ("highlighting...", "ensuring..."). Delete or expand with real sources.
4. Promotional language ("nestled", "groundbreaking", "stunning"). Neutral description.
5. Vague attribution ("Experts believe"). Name the source or delete.
6. Formulaic challenges ("Despite challenges... continues to thrive"). Specific facts.

Language:
7. AI vocabulary (additionally, crucial, delve, foster, garner, interplay, intricate, landscape, pivotal, showcase, tapestry, testament, underscore, vibrant). Plain words.
8. Fancy "is" ("serves as", "stands as", "boasts"). Say "is" or "has".
9. "Not just X, but Y." State the point directly.
10. Forced rule-of-three groupings. Use the natural number.
11. Synonym cycling for one concept. Pick one term, repeat it.
12. False ranges ("from X to Y" with no meaningful scale). List topics directly.

Style:
13. Em dashes. Avoid entirely; periods or commas only.
14. Colons as mid-sentence connectors. Fine before a list; otherwise rewrite.
15. Boldface on every proper noun or acronym.
16. Inline-header lists where the bold label restates the line. Convert to prose.
17. Title case headings. Sentence case.
18. Decorative emojis in headings and bullets.
19. Curly quotes. Straight quotes.

Artifacts:
20. Chatbot phrases ("I hope this helps!", "Let me know if...", "Certainly!").
21. Cutoff disclaimers ("While specific details are limited...").
22. Sycophancy ("Great question! You're absolutely right!"). Respond directly.

Filler:
23. Filler phrases ("In order to" → "To"; "Due to the fact that" → "Because"; "It is important to note that" → deleted).
24. Stacked hedging ("could potentially possibly be argued that it might" → "may").
25. Generic conclusions ("The future looks bright."). Specific plans or facts.

Jargon:
26. Abstract metaphor nouns (substrate, wedge, vector, nexus, primitive as noun, harness as metaphor, bedrock, scaffolding as metaphor, modality, paradigm, gold-plating, ratchet as metaphor, endgame, north star, flywheel). Use the concrete word: substrate→base, wedge in→add, vector→way, ratchet→the mechanism's real name.

Plain speech:
27. Say what it does, not how it feels. Name the mechanism or the number. A sentence that could appear unchanged in another project's docs says nothing about this one; cut it.
28. Split dense sentences the reader must backtrack through. One idea per sentence.
29. Active voice. Catch "is/are/was/were + past participle" and name the actor. Passive only when the actor is unknown or beside the point.
30. Cut adverbs or use stronger verbs ("significantly improves" becomes the measured delta).
31. The plain word ("utilize"→use, "leverage"→use, "facilitate"→help, "numerous"→many).
