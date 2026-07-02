# Language and Grammar Patterns (English)

Patterns that betray AI-generated text at the level of word choice, grammatical constructions, and sentence structure. Based on Wikipedia's Signs of AI Writing + tropes.fyi + blader/humanizer's 29-pattern set + brandonwise/humanizer's statistical model.

---

### 1. AI Vocabulary (The Slop Dictionary)

**Tier 1 - Zero Tolerance (cut on sight):**

| Word/Phrase | Why it's a tell | Human alternative |
|---|---|---|
| delve | No one says this in conversation | explore, dig into, look at |
| tapestry | Always used as "rich tapestry of..." | (cut entirely - always filler) |
| landscape (figurative) | "The AI landscape" | the AI space, AI right now |
| testament to | "It's a testament to..." | shows that, proves |
| serves as a reminder | Always preamble to nothing | (cut - just state the thing) |
| it's worth noting | Meta-commentary, not content | (cut - the note IS the content) |
| it bears mentioning | Same as above | (cut) |
| the ever-evolving landscape | Double slop | (cut entirely) |
| navigate (complexities) | "Navigate the challenges of" | deal with, handle, figure out |
| spearhead | "Spearheading the initiative" | lead, run, start |
| multifaceted | "This multifaceted problem" | complex, messy, complicated |
| pivotal | "A pivotal moment" | important, key, big |
| paramount | "Of paramount importance" | essential, critical |
| underscores | "This underscores the need" | shows, highlights |
| underpin | "Principles that underpin" | behind, supporting |
| in the realm of | "In the realm of AI" | in AI |
| shed light on | "Shedding light on this issue" | explain, clarify, show |
| this highlights | Meta-commentary | (cut - the highlight IS the sentence) |

**Tier 2 - High Suspicion (replace when clustered, OK once per 1000 words):**

`crucial, vital, comprehensive, robust, leverage, foster, facilitate, embark, harnessing, utilize, endeavor, moreover, furthermore, additionally, subsequently, nonetheless, overarching, intricate, nuanced, holistic, synergy, paradigm, catalyst, orchestrate, seamless, ecosystem (abstract), journey (figurative), unlock (figurative), empower, elevate`

**Tier 3 - Context-Dependent (flag if >2 per 500 words):**

`significant, enhance, innovative, dynamic, diverse, inclusive, sustainable, transformative, streamline, optimize, cutting-edge, state-of-the-art, game-changer, disruptive, scalable, impactful, actionable, meaningful, compelling, groundbreaking`

**Detection rule:**
- 1 Tier-1 word = flag the sentence
- 3+ Tier-2 words in one paragraph = flag the paragraph
- 5+ Tier-3 words in one page = flag the text
- Any combination of 2+ Tier-1 words in 500 words = near-certain AI

---

### 2. Copula Avoidance

**Trigger patterns:** constitutes, represents, serves as, functions as, operates as, positions itself as, stands as, emerges as, figures as

**Problem:** AI avoids "is" and "has" as if they were forbidden words. Replaces them with elaborate constructions no human would use in natural writing.

**Before (AI):**
> Stripe constitutes the leading payments infrastructure for the internet. The platform serves as a comprehensive solution for businesses and positions itself as the de facto standard for online transactions.

**After (human):**
> Stripe is the biggest payments company online. Their API is what most startups use to take money.

**Rule:** If "is" or "has" would work, use it. Save elaborate verbs for when you need precise meaning, not sophistication theater.

---

### 3. Negative Parallelisms

**Trigger patterns:** not merely X, but Y; it's not just about X, it's about Y; more than X, it's Y; goes far beyond X; transcends the simple X; not simply X, it's fundamentally Y

**Problem:** Formulaic construction that artificially inflates importance. Creates a false dichotomy where the writer pretends to reject something then embraces something bigger - but both parts say the same thing.

**Before (AI):**
> Product management is not merely about writing user stories. It goes far beyond simply shipping features - it's fundamentally about solving real problems. The PM transcends the role of ticket writer; they are, above all, a translator between business and technology.

**After (human):**
> Good PMs solve problems. Bad PMs write tickets. The difference isn't philosophical - it's practical. Look at someone's backlog and you'll know in 5 minutes.

---

### 4. Tricolon Abuse (Rule of Three)

**Trigger patterns:** clarity, concision, and coherence; innovation, technology, and transformation; plan, execute, and measure; any rhythmic triad with "and" before the third item; three adjectives in sequence; three abstract nouns grouped

**Problem:** AI groups ideas in threes because tricolon is rhetorically satisfying - but when it appears in every paragraph, it becomes a tic. Human text groups in 2, in 4, in 1. Rarely in 3 repeatedly.

**Before (AI):**
> The platform delivers speed, reliability, and scalability. Teams need clarity, collaboration, and consistency. Our approach combines innovation, expertise, and dedication.

**After (human):**
> It's fast. Reliable enough that we stopped worrying about downtime. And it scales - we went from 10k to 400k requests/day without changing anything.

**Detection rule:** If a text has 3+ tricolons per page, it's almost certainly AI-generated. Humans occasionally use rule-of-three for rhetorical effect. AI uses it as a structural crutch.

---

### 5. Weasel Qualifiers

**Trigger patterns:** it could be argued that, one might suggest, there are those who believe, it has been said that, some would argue, many experts believe, it is generally accepted

**Problem:** AI uses qualifiers to avoid committing to claims. The result reads like a Wikipedia article written by someone afraid of being corrected. Humans either commit to a claim or cite a specific source.

**Before (AI):**
> It could be argued that large language models represent a significant advancement. Many experts believe this technology has the potential to transform various industries, though some would argue the risks are considerable.

**After (human):**
> LLMs are a big deal. They'll change how most knowledge work gets done - I genuinely believe that. But Hinton is right that we don't understand alignment well enough to be comfortable.

---

### 6. Nominalization Disease

**Trigger patterns:** the implementation of, the utilization of, the facilitation of, the optimization of, the enhancement of, the establishment of, provides a demonstration of, performs an analysis of

**Problem:** AI converts verbs into nouns, making sentences longer, vaguer, and harder to parse. "We analyzed" becomes "we performed an analysis of". This is the passive-aggressive cousin of passive voice.

**Before (AI):**
> The implementation of the new system resulted in the enhancement of performance metrics and the facilitation of improved collaboration across teams.

**After (human):**
> We implemented the new system. Performance improved. Teams started collaborating more.

**Rule:** If a noun ending in -tion/-ment/-ance has a simpler verb form, use the verb.
