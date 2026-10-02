# Style and Formatting Patterns

Patterns betraying AI-generated text through visual and structural form, not content. Detection tools use these markers as high-confidence signals.

---

### 1. Em-Dash Cascade

**Problem:** AI uses 15-25 em-dashes per medium text. Humans use 2-3, and generally prefer commas, periods, or parentheses for most functions AI assigns to em-dashes.

**Before (AI):**
> The project — which started in 2022 — brought impressive results — especially in the data area — and is now being expanded — even with limited budget — to other regions.

**After (human):**
> The project started in 2022 and brought solid results in data. It's now expanding to other regions, even with a tight budget.

**Detection signals:**
- More than 2 em-dashes per paragraph
- Em-dash where comma resolves
- Chaining of parenthetical asides with em-dashes (— X — Y — Z)
- Text where >10% of punctuation marks are em-dashes

**Correction techniques:**
- **Limit of 2 em-dashes per paragraph** - convert extras to commas, periods, or parentheses
- Differentiate use: em-dash for strong contrast, parentheses for side comment, comma for light aside
- "Editor test" - if a human editor would have cut the em-dash, cut it

---

### 2. Excessive Bold

**Problem:** AI applies bold to every keyword as if the text were a slide deck. Running text with bold on every important noun reads like a product catalog, not human writing.

**Before (AI):**
> The **platform** offers **native integration** with leading **CRMs**, ensuring **scalability** and **security** for **sales** and **marketing** teams.

**After (human):**
> The platform integrates with the major CRMs. Works well for sales and marketing teams that need to scale without losing access control.

**Detection signals:**
- Bold on more than 1-2 terms per paragraph
- Bold on common nouns (platform, team, result) without editorial reason
- Bold used as substitute for good sentence structure
- Text where >5% of words are bolded

**Correction techniques:**
- **Limit of 1-2 bolds per section** - never per paragraph
- Use bold only for **intentional contrast**: "The problem isn't the tool - it's the **process**"
- If bold is compensating for lack of clarity, **restructure the sentence** instead
- "Print test" - if text looks like it was formatted for a reader with ADHD, bold is excessive

---

### 3. List-ification (Bullet Point Abuse)

**Problem:** AI converts prose into bullet points at every opportunity. Three sentences of flowing text become a bulleted list with "Key takeaways:" above it. Human writing uses lists sparingly - for actual enumerations, not for every paragraph.

**Before (AI):**
> Here are the key benefits:
> - **Increased efficiency** - Teams work 40% faster
> - **Improved collaboration** - Cross-functional alignment
> - **Better outcomes** - Measurable ROI improvements
> - **Scalability** - Grows with your organization

**After (human):**
> Teams work faster with it - about 40% based on our internal tracking. The real win is cross-functional alignment though: people who never talked to each other before are now in the same workflow.

**Detection signals:**
- Bulleted lists that could be flowing prose
- "Key takeaways:" / "Key points:" / "Here's what you need to know:" above lists
- Parallel structure in every bullet (same length, same construction)
- Lists with 5+ items where 3 would suffice

**Correction techniques:**
- If items are truly discrete enumerable things (steps, features, names), keep as list
- If items are connected thoughts, convert to prose paragraphs
- Break bullet symmetry: vary length, mix sentence fragments with full sentences
- "Would I say this aloud as a list?" test - if you'd narrate it, it's prose

---

### 4. Header Proliferation

**Problem:** AI creates a `##` header for every 2-3 paragraphs in any text longer than 400 words. Human prose flows continuously - headers appear when genuinely changing topic, not every 150 words.

**Before (AI):**
> ## Introduction
> The problem is clear.
> ## Background  
> Here's context.
> ## Current Situation
> Things have changed.
> ## Analysis
> Let's examine this.
> ## Conclusion
> In summary...

**After (human):**
> The problem is clear - and it's been getting worse since 2023. [continues flowing for 800 words with maybe one section break where the topic genuinely shifts]

**Detection signals:**
- Headers every 100-200 words in what should be continuous prose
- Generic headers: "Introduction", "Background", "Analysis", "Conclusion"
- Headers that just restate what the next paragraph says
- Document with 8+ headers for 1000 words

---

### 5. Emoji Inflation

**Problem:** AI (especially ChatGPT) injects emoji into every bullet point, section header, or list item. Human writers use emoji occasionally and contextually, not systematically.

**Before (AI):**
> 🚀 Key Features
> ✅ Automated deployment
> 💡 Smart suggestions
> 🔒 Enterprise security
> ⚡ Lightning-fast performance

**After (human):**
> The main features: automated deployment, smart suggestions, enterprise-grade security, and good performance. (It handles 10k requests/second on our benchmark.)

**Detection signals:**
- Emoji on every list item
- Emoji in headers
- More than 2 emoji per 500 words in professional text
- Systematic emoji (same emoji category repeated: all checkmarks, all rockets)

**Correction techniques:**
- Professional context: remove all emoji unless the format genuinely calls for them (social posts, chat)
- Social context: keep 1-2 per post, used for emphasis or tone, not decoration
- Never use emoji as bullet point markers in serious writing
