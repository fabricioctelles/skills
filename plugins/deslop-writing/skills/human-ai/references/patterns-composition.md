# Composition Patterns - AI Tropes in English

Structural patterns betraying AI-generated text at the level of **composition** - how the text is assembled, not what it says. Includes tropes cataloged by [tropes.fyi](https://tropes.fyi/directory) and the concept of **Semantic Ablation** (The Register, Feb 2026).

---

## Composition Tropes

### 1. Fractal Summaries

**Problem:** AI announces what it will say, says it, then summarizes what it said - in each section, subsection, and paragraph. Text becomes infinite recursion of meta-commentary.

**Before (AI):**
> In this section, we will explore how artificial intelligence is transforming the financial sector. We will examine three key aspects: process automation, predictive analytics, and customer service.
>
> [...3 paragraphs...]
>
> As we have seen in this section, artificial intelligence is transforming the financial sector through process automation, predictive analytics, and customer service. In the next section, we will address the challenges of this transformation.

**After (human):**
> Itau cut 40% of its back-office team in two years. Wasn't layoffs - it was automation eating the edges. A credit process that took a week now runs in four hours. The analyst who remains doesn't analyze: they supervise the model that does.

**Cut on sight:**
- "In this section, we will..."
- "As we saw previously..."
- "Next, we will discuss..."
- "As mentioned in the previous section..."
- "To summarize what we've discussed..."

**Correction techniques:**
- Eliminate recursion: the conclusion is ONE thing - at the end. Subsections don't need mini-conclusions
- Convert meta-commentary to direct statement: "As we saw, AI transforms the sector" -> "AI transforms the sector in three ways"
- If text has 3+ subsections with mini-conclusions, merge into a single block with continuous flow

---

### 2. Dead Metaphor on Repeat

**Problem:** AI finds a metaphor at the beginning and repeats ad nauseam as if it were the spine of the text. "Ecosystem" appears 30 times. "Journey" appears in every paragraph. The metaphor loses all power - becomes noise.

**Before (AI):**
> The startup ecosystem is maturing. In this ecosystem, the players need to adapt. The ecosystem demands new competencies. To survive in this ecosystem, entrepreneurs must build solid networks. The future of the ecosystem depends on public policies that foster innovation within the ecosystem itself.

**After (human):**
> The startup scene in the US changed - from garage with pitch deck to serious business with governance and boards demanding results. Anyone who started in 2019 thinking all you needed was a good idea and a seed round now faces investors who want unit economics. The party ended; the real work started.

**Rule:** Never repeat the same figurative word more than twice in a text. After the second use, find a different way to say it - or just say the concrete thing.

---

### 3. The "Many People" Ghost

**Problem:** AI attributes claims to unnamed masses: "many people believe", "researchers have found", "companies are increasingly", "there's a growing consensus". No specific person is cited. No specific research is named. It's the literary equivalent of "people are saying."

**Before (AI):**
> Many experts believe that AI will transform education. Researchers have found that personalized learning approaches yield better outcomes. Companies are increasingly investing in edtech solutions, reflecting a growing consensus that traditional methods are no longer sufficient.

**After (human):**
> Sal Khan thinks AI tutoring will outperform classrooms within a decade. He might be right - Khan Academy's pilot data shows 30% improvement on math scores with AI tutoring. But Audrey Watters has been calling bullshit on edtech promises for fifteen years, and she's usually right too.

**Rule:** If you can't name the expert, the researcher, or the company - either find one, or rephrase as your own opinion.

---

### 4. The Five-Paragraph Essay

**Problem:** AI defaults to intro-3points-conclusion structure regardless of content or context. Every piece becomes a high school essay: thesis, body paragraph 1, body paragraph 2, body paragraph 3, conclusion restating thesis. This is the structural equivalent of "In this essay, I will argue..."

**Before (AI structure):**
```
Introduction: State thesis
Point 1: First argument with support
Point 2: Second argument with support  
Point 3: Third argument with support
Conclusion: Restate thesis in different words
```

**After (human structure options):**
```
Open with a story -> derive the principle -> complicate it -> leave an open question
Start with the conclusion -> explain why it's surprising -> show the evidence
Describe the problem in detail -> show three failed solutions -> reveal what worked
```

**Rule:** Structure should emerge from content, not be imposed from template. Good writing starts where it needs to start and ends where it needs to end.

---

### 5. Semantic Ablation (The Register, 2026)

**Problem:** After multiple AI refinement passes, text loses specificity, personality, and edge. Each pass removes anything "risky" or "unusual" until what remains is perfectly smooth, perfectly generic, perfectly dead. The Register calls this "semantic ablation" - the wearing away of meaning through machine-polishing.

**Symptoms:**
- All specific examples replaced with generic ones
- All strong opinions softened to "balanced" perspectives
- All technical jargon replaced with layperson equivalents (losing precision)
- All humor or personality flattened to neutral tone
- Numbers rounded or removed ("about 3 million" becomes "many")

**Before (ablated):**
> Many companies are adopting new approaches to software development. These approaches offer various benefits and come with certain challenges. Teams should carefully evaluate their options.

**After (restored):**
> 47 YC companies from the W24 batch shipped their MVPs using AI coding agents. Not "AI-assisted" - full agent mode. Half of them have zero engineers on staff. The challenge is debugging: when the agent writes 10,000 lines in a night, who reviews it?

**Detection signals (from brandonwise/humanizer's statistical model):**
- TTR (Type-Token Ratio) below 0.45 - vocabulary is being recycled
- Burstiness below 5 - all sentences the same length (robotic rhythm)
- Shannon entropy significantly lower than human baseline for the genre
- Concrete noun density below 40% - everything is abstract

**Restoration technique:** Add back specificity at every opportunity: names, numbers, dates, anecdotes, qualifications. If the original had them, restore. If it didn't, flag that the text needs concreteness.

---

### 6. The Balanced Bookend

**Problem:** AI opens and closes with suspiciously symmetrical statements. The final paragraph echoes the first with slightly different phrasing, creating an artificial sense of circular completion. Human writers don't do this unless deliberately crafting a literary piece.

**Before (AI):**
> Opening: "The intersection of AI and healthcare presents both unprecedented opportunities and significant challenges."
> [...]  
> Closing: "As we've seen, the intersection of AI and healthcare continues to present both remarkable opportunities and notable challenges that will shape the future of medicine."

**After (human):**
> Opens with a specific story about a misdiagnosis caught by AI.
> [...]
> Ends with an open question: "So who's liable when the AI is right and the doctor disagrees?"

**Rule:** Endings should advance the thought, not echo it. If your conclusion says the same thing as your introduction, one of them is redundant.



---

### 7. Connective-Preserving Edits (Never Bare-Delete)

**Problem:** When aggressive AI-pattern removal strips transitions and connectives, it produces choppy, disconnected prose (asyndeton). This is itself a tell of automated cleanup - and a common failure mode of humanizer passes. The logical relations between sentences still exist; removing the markers just makes them implicit and harder to follow.

**Before (the AI text):**
> Additionally, the platform improved load times significantly. Furthermore, users reported higher satisfaction. Moreover, retention metrics increased by 15%.

**Wrong fix (bare deletion - creates choppy asyndeton):**
> The platform improved load times. Users reported higher satisfaction. Retention metrics increased by 15%.

**Right fix (connective preserved or restructured):**
> The platform improved load times, and users noticed - satisfaction scores went up. Retention followed: 15% improvement over the previous quarter.

**The rule: Edit, don't excise.** Whenever you remove a sentence-initial transition or a clause that carried the link to the previous sentence, restore the link by one of:

1. **Substitute a natural connective:** "In addition," → "We also found that..." / "Meanwhile," / "On top of that,"
2. **Echo a key noun from the previous sentence** (old-to-new flow): "...was associated with better outcomes. Better outcomes, in turn, correlated with..."
3. **Restructure into one sentence:** Merge the two sentences with an explicit conjunction or semicolon

**Division of labor:** The "Logical Discourse Markers to Preserve" section below lists markers you should NOT remove. This section governs what to do when an edit WOULD otherwise leave a gap - replace or restructure, never just cut.

---

### 8. Logical Discourse Markers to Preserve

**Problem:** Some humanizer approaches treat ALL transitions as AI tells and strip them indiscriminately. This is wrong. Certain discourse markers are hallmarks of good human writing - they make the logical structure explicit. Removing them damages the text.

**Preserve these (do NOT flag as AI patterns):**

| Category | Markers | Function |
|----------|---------|----------|
| **Contrast** | However, In contrast, Conversely, On the other hand, Nevertheless, Nonetheless, Although, Whereas, Yet | Signal that the next sentence contradicts or qualifies the previous |
| **Result/Consequence** | Thus, Hence, Therefore, Consequently, Accordingly, As a result | Signal that the next sentence follows logically from the previous |
| **Concession** | Although, Albeit, Even though, Granted, While (concessive) | Acknowledge a point before presenting counter-argument |
| **Reason/Grounds** | Because, Since, As, Given that | Explain why the previous claim holds |
| **Addition** | In addition, Also, We also found that | Add supporting evidence (but NOT mechanical "Furthermore/Moreover/Additionally" clusters) |
| **Sequence** | First, Second, Then, Next, Finally | Mark progression through steps or arguments |

**Distinguishing rule:** Ask whether the phrase *inflates meaning* (DELETE) or *makes logic explicit* (KEEP).

| DELETE (inflates) | KEEP (logical) |
|-------------------|----------------|
| "underscores the pivotal importance of..." | "Based on these results, we examined..." |
| "this highlights the crucial role that..." | "However, this effect disappeared when..." |
| "represents a significant advancement in..." | "Thus, the initial hypothesis was not supported." |

**The "sweet spot":** Well-written human text chains discourse markers densely and naturally while using ZERO inflated AI vocabulary. Aim for that profile: trim the slop vocabulary, but preserve the logical connectives that make arguments easy to follow.

**Vary connectives by logical relation - but only to avoid near repetition.** When rewriting, first identify what relation the sentence actually needs (result? contrast? addition?), then choose a marker that fits. If you just used "However," don't use it again in the next paragraph - pick "In contrast," or "On the other hand," instead. But never sprinkle uncommon connectives (albeit, thereby, whereby) just to "sound human" - that's decoration, not logic.

---

### 9. Paragraph Cohesion Check

**Problem:** Sentence-level edits accumulate into paragraph-level damage. Topic sentences get blunted, the chain from one sentence to the next breaks, and the contrast/continuity markers that tie paragraphs together disappear. Well-written human text is tightly chained; edited AI slop is disconnected.

**What well-written human text does:**

1. **Within a paragraph:** Each sentence picks up a key word from the previous one (old-to-new flow)
   > "...the exposure was associated with a higher score. The score used here consists of five components. To measure these components, we..."
   
   The repeated key term ("score") chains the sentences so the reader never gets dropped.

2. **Between paragraphs:** The opening sentence names what the paragraph covers and, where logic requires it, carries an explicit marker:
   - "However, this pattern did not hold for all groups."
   - "In addition to the main effect, we observed..."
   - "Taken together, the results suggest..."

**Cohesion checklist (apply after editing each paragraph):**

| # | Check | ✓/✗ |
|---|-------|-----|
| 1 | Does the first sentence state what the paragraph claims or covers? | |
| 2 | From sentence 2 onward, is each sentence linked to the previous by either a connective OR an echoed key word? | |
| 3 | If a link was broken by an edit, has it been restored (per Connective-Preserving Edits above)? | |
| 4 | Across paragraphs: are contrast/continuity openers (However, In contrast, Taken together) present where the argument needs them? | |

**If any check fails:** Add a connective, echo a key noun, or restructure. Choppy, disconnected prose is NOT acceptable humanized output.
