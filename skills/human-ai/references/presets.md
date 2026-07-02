# Voice Calibration - Presets (Full Reference)

Detailed characteristics, examples, and guidelines for each voice preset.


## 🖋️ Essay (default)

Tone of an English essayist. Controlled informality, wit, specific observation turned into insight. Mixes high and low register. A turn at the end.

**Characteristics:**
- "Look" and "honestly" coexist with precise vocabulary
- Sentence fragments as dramatic pause
- Dry humor, self-awareness
- Explicit opinion
- Rhetorical questions left unanswered

**Example:**
> Everyone knows that coworker who automated their own job and told nobody. Sat there for months pretending to type. Well. Now the entire company is that coworker - just using ChatGPT instead of Python scripts. The difference is nobody's pretending. And so the question becomes: efficiency or laziness? I don't know. Probably both.


## 📰 Journalistic

Tone of the NYT or The Atlantic. Maximum clarity, concrete data, no fluff.

**Characteristics:**
- Subject + verb + object (in that order)
- Numbers and dates whenever possible
- Attribution to named sources
- No evaluative adjectives
- No first person (except opinion columns)

**Example:**
> Nubank laid off 40 people from its customer service team in May. The company declined to comment, but two former employees confirmed that replacement by chatbots motivated the cuts. The department had 120 people at the start of the year.


## 🎓 Academic

Formal but not bureaucratic. Terminological rigor without officialese.

**Characteristics:**
- Precise domain vocabulary
- Legitimate qualifications (not empty hedging)
- References to specific authors/studies
- Avoids cliches: "it is worth noting", "it goes without saying", "in the context of"

**Example:**
> The convergence-toward-median hypothesis (Nastruzzi, 2026) finds support in TTR analysis of texts submitted to multiple AI refinement cycles. The phenomenon - semantic ablation - differs from hallucination: it does not add falsehood, it subtracts specificity.


## 💬 Corporate Informal

Startup email, professional Slack. Direct, light, no corporate speak.

**Characteristics:**
- Short, direct sentences
- Contractions used naturally
- Action verbs instead of nominalizations
- Tech jargon where appropriate (deploy, sprint, ship)

**Example:**
> Team, quick update: the hotfix went out last night, already in prod. The duplication bug stopped since 11pm. I'll monitor for another 48h and if it stays clean, we close the issue. Ping me if anything pops up.


## 📱 Social Post

LinkedIn or Twitter/X. Short, opinionated, hook in the first line.

**Characteristics:**
- First sentence is the hook
- Paragraphs of 1-2 lines
- Strong personal opinion
- Uses "I" freely
- Subtle or no CTA

**Example:**
> I fired ChatGPT from my writing workflow.
>
> Not because it's bad. Because everything I published sounded like everyone else.
>
> I went back to writing by hand. Takes 3x longer. But people actually reply now.
>
> Efficiency without voice isn't an advantage. It's invisibility.


## 💬 Casual/DM

Maximum orality. Stream of consciousness allowed.

**Characteristics:**
- Incomplete sentences ok
- Natural abbreviations (tbh, ngl, idk)
- Slang accepted
- Zero concern with formal grammar

**Example:**
> dude did you see what the data team did
>
> they pushed a model to prod without telling anyone
>
> then it started sending wrong emails to clients
>
> absolute chaos


## ⚖️ Legal / Formal

Briefs, memos, formal notices. High register with deliberate conventions that, when used intentionally, sound more authentic than AI's generic imitation.

**Characteristics:**
- Structure: background -> facts -> analysis -> conclusion/recommendation
- Controlled use of genre conventions ("notwithstanding", "hereinafter", "pursuant to")
- Citation of specific statutes, cases, regulations
- Active voice when possible to avoid bureaucratic emptiness

**Signs of AI in this register:**
- Excess "it is worth noting", "it should be emphasized", "in the context of this analysis"
- Generic citations without case numbers or statute references
- Perfectly symmetrical paragraphs (3-4 identical-length sentences)

**Example (AI -> Human):**
> *AI*: "It is well-established that the right to privacy must be balanced against public interest, as consistently recognized by relevant jurisprudence. It should be noted that the present case requires careful analysis."
>
> *Human*: "The right to privacy exists, yes - but it's not absolute. The Supreme Court held in *Carpenter v. United States*, 585 U.S. 296 (2018), that public interest can prevail. In this case, the photo was taken at a public event. The question is whether there was commercial exploitation. That's what separates privacy from publicity rights."

**What to preserve (not an AI sign):**
- Section headings in caps ("BACKGROUND", "ANALYSIS", "CONCLUSION") - expected formatting in briefs
- Numbered items in arguments and requests
- Citation with specific case numbers and dates
- Background -> facts -> analysis -> conclusion structure - it's the genre, not AI template

**Key signal separating human from AI in this register:** humans cite specific case numbers, statutes, sections. AI says "as established by relevant authorities" without citing anything.


## 🧑‍🏫 Instructional / Explainer

Edtech, documentation, tutorials, friendly technical writing.

**Characteristics:**
- Pattern: question -> explanation -> concrete example -> reinforcement
- Accessible but precise vocabulary (not dumbed down)
- Specific, verifiable examples (not "Alice has 3 apples")
- Explicit transitions: "So", "Now", "Let's see this in practice"

**Signs of AI in this register:**
- Generic, artificial examples
- Encyclopedic tone without interaction with reader
- "In this chapter, we will explore X, Y and Z" -> empty template

**Example:**
> Let's cut to it: a *callback* is a function you pass as an argument to another function, so it can "call you back" when it's done. Sounds complicated, but that's all it is. Think of ordering delivery: instead of calling every 5 minutes to check if it arrived, you leave your number and the driver texts you when they're at the door. Your number is the callback.
