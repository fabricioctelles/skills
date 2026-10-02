# English-Specific Patterns

Patterns unique to AI-generated English text that don't have direct equivalents in other languages. These exploit the specific quirks of English grammar, register mixing, and contraction patterns that AI consistently gets wrong.

---

### 1. Contraction Avoidance

**Problem:** AI-generated English dramatically underuses contractions compared to human writing. In informal contexts, this is one of the most reliable statistical signals. GPTZero and Originality.ai both flag texts with unusually low contraction rates.

**Human contraction rates by register:**
| Register | Contraction rate |
|---|---|
| Casual speech/DM | 95%+ ("don't", "won't", "it's", "we're", "they'll") |
| Blog/newsletter | 80-90% |
| Professional email | 60-80% |
| Journalism | 40-70% (varies by outlet) |
| Academic | 10-30% (deliberately formal) |
| Legal | 5-15% (genre convention) |

**AI typical rate:** 30-50% across ALL registers (doesn't adapt)

**Before (AI - blog register):**
> It is important to note that the system does not function as expected. We cannot determine the root cause at this time. There is no indication that this will be resolved soon.

**After (human - blog register):**
> It's not working the way it should. We can't figure out why yet. There's no sign it'll be fixed soon.

**Contraction replacement rules:**
| AI form | Human form (informal) | Keep formal when... |
|---|---|---|
| it is | it's | academic emphasis needed |
| do not | don't | legal/safety context |
| cannot | can't | formal document |
| will not | won't | emphasis on refusal |
| they are | they're | ambiguity risk |
| we have | we've | ... |
| should not | shouldn't | ... |
| would not | wouldn't | ... |
| there is | there's | ... |
| that is | that's | ... |

**Rule:** In Essay, Corporate Informal, Social Post, and Casual presets, force contractions to match human rates. In Academic and Legal presets, low contractions are correct.

---

### 2. Register Uniformity

**Problem:** Humans naturally mix registers within a single text - formal vocabulary next to colloquial phrasing, technical terms next to slang, high register next to low. AI maintains a perfectly uniform register throughout, which paradoxically signals artificiality.

**Before (AI - uniformly mid-register):**
> The implementation proved challenging but ultimately successful. The team encountered several obstacles during the process but managed to resolve them through collaborative effort and systematic problem-solving.

**After (human - mixed register):**
> The implementation was a nightmare for about two weeks - classic "it works on my machine" stuff. Then Sarah figured out the race condition and we shipped it. Sometimes the fix is embarrassingly simple.

**Human register mixing patterns:**
- Technical term + casual explanation: "The TTL expired - basically the cache forgot everything"
- Formal structure + informal aside: "The architecture is sound. (The naming conventions, less so.)"
- Precise vocabulary + colloquial connector: "The latency delta was significant. Look, 340ms vs 40ms isn't subtle."

**Rule:** Inject at least one register shift per 300 words in non-academic presets. A formal paragraph should have one casual moment. A casual text should have one precise term.

---

### 3. Passive Voice Overuse

**Problem:** AI defaults to passive voice far more than humans, especially when the agent (who did the thing) is uncertain or the AI is hedging. Human English strongly prefers active voice in most contexts.

**Before (AI):**
> The decision was made to restructure the team. It was determined that performance had been negatively impacted. New processes were implemented and improvements were observed over the following quarter.

**After (human):**
> The VP restructured the team. Performance had tanked - everyone knew it. They implemented new processes and saw improvement by Q3.

**Acceptable passive uses (don't convert these):**
- When the agent is genuinely unknown: "The server was compromised overnight"
- When the object is more important: "Three people were injured in the crash"
- Scientific convention: "The sample was heated to 300°C"
- Deliberate de-emphasis of actor: "Mistakes were made" (though this is also a cliche)

**Detection signal:** More than 30% of clauses in passive voice = AI signal. Measure by counting "was/were + past participle" constructions.

---

### 4. Transition Word Abuse

**Problem:** AI uses explicit transition words between nearly every sentence. Human writers trust the reader to follow logical connections without signposting every turn.

**AI transition word frequency:** every 2-3 sentences
**Human transition word frequency:** every 5-8 sentences (varies by genre)

**The worst offenders (cut 80% of these):**
| Word | AI frequency | Human frequency | Action |
|---|---|---|---|
| Furthermore | Every paragraph | Rare in non-academic | Cut or replace with "And" |
| Moreover | Every paragraph | Rare | Cut |
| Additionally | Every paragraph | Rare | Cut |
| However | Every 3 sentences | Every 6-8 sentences | Keep some, cut most |
| Consequently | Frequent | Rare in non-academic | "So" or cut |
| Subsequently | Frequent | Rare | "Then" or cut |
| Nevertheless | Frequent | Occasional | Keep sparingly |
| In contrast | Frequent | Occasional | "But" or restructure |

**Rule:** Trust the reader. If the logical connection is obvious from context, no transition word is needed. Use transitions only when the connection would genuinely surprise the reader.

---

### 5. "The" Proliferation in Abstractions

**Problem:** AI over-uses "the" before abstract nouns, creating a false specificity. "Innovation" becomes "the innovation". "Technology" becomes "the technology". This makes generic statements sound as if they refer to something specific when they don't.

**Before (AI):**
> The innovation in the space has led to the advancement of the technology. The community has embraced the shift toward the adoption of the new paradigm.

**After (human):**
> Innovation in this space accelerated after GPT-4 launched. Developers adopted the new approach quickly - mostly because it was easier, not because anyone evangelized it.

**Rule:** If "the [abstract noun]" doesn't refer to a previously introduced specific thing, it's probably AI padding. Cut "the" or replace with a specific referent.

---

### 6. Absence of Sentence Fragments

**Problem:** Human English, especially in informal and semi-formal writing, uses sentence fragments freely for rhythm and emphasis. AI almost never produces them - every unit is a grammatically complete sentence.

**AI (all complete sentences):**
> The product launched last week. It received positive reviews. The team is now focused on iteration. They plan to ship a major update by March.

**Human (with natural fragments):**
> The product launched last week. Positive reviews all around. Now the team's heads-down on iteration. Major update by March. Maybe.

**Fragment types humans use:**
- Answers: "Absolutely not."
- Emphasis: "Every. Single. Time."
- Afterthoughts: "Not ideal."
- Rhythm breaks: "So there's that."
- Dramatic pause: "Three million lines of code. Overnight."

**Rule:** In Essay, Corporate Informal, Social Post, and Casual presets, inject at least one sentence fragment per 200 words. In Academic and Legal presets, fragments are inappropriate.

---

### 7. Perfect Paragraph Length Uniformity

**Problem:** AI generates paragraphs of remarkably similar length (typically 3-5 sentences, 80-120 words each). Human writing varies paragraph length dramatically - from one-sentence paragraphs to 300-word blocks.

**AI pattern:** 4 sentences, 4 sentences, 4 sentences, 4 sentences
**Human pattern:** 1 sentence, 6 sentences, 2 sentences, 8 sentences, 1 sentence

**Detection signal (from brandonwise/humanizer):** Coefficient of variation in paragraph length below 0.3 = AI signal. Human English averages ~0.6 CoV in paragraph length.

**Rule:** Vary paragraph length intentionally. Use one-sentence paragraphs for impact. Use long paragraphs for complex arguments that need sustained development. The variation IS the voice.
