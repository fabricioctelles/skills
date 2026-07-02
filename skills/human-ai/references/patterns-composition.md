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
