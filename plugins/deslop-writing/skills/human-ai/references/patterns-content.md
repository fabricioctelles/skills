# Content Patterns

Patterns where AI inflates importance, fabricates authority, or closes texts with predictable formulas. The easiest to detect because they sound like press releases - nobody talks like this.

---

### 1. Undue emphasis on significance, legacy, and trends

**Trigger words/phrases:** represents a milestone, is a testament to, plays a crucial/vital/pivotal role, underscores the importance of, reflects a broader trend, symbolizing the, contributing to the, paving the way for, shaping the future of, ever-evolving landscape, inflection point, indelible mark, deeply rooted, redefines the paradigm

**Problem:** AI transforms any mundane fact into a revolution. A CRUD app becomes "a milestone in digital transformation". A startup pivot becomes "an inflection point in the innovation ecosystem". No human writes like this about normal things.

**Before (AI):**
> OpenAI represents a fundamental milestone in the transformation of the artificial intelligence landscape, actively shaping the future of AI development and paving the way for a new era of human-computer interaction.

**After (human):**
> OpenAI started by releasing GPT-3 as an API. It worked because nobody else was making large language models accessible to developers at that point. Now they have a consumer product with 100 million users.

**Detection signals:**
- Absolute superlatives without quantification ("greatest", "best", "unprecedented", "first-ever")
- Grandiose transformation verbs ("redefine", "shape", "pave the way")
- Text describing anything as an "inflection point" without saying what changes afterward

**Correction techniques:**
- Convert superlatives to **concrete data**: "largest fintech" -> "80 million customers"
- Replace grandiose verbs with **specific action verbs**: "pave the way" -> "hired 3 engineers for"
- "Journalist test" - if a reporter would read the sentence and ask "how so?", the term is empty

---

### 2. Forced emphasis on notability and media coverage

**Trigger words/phrases:** widely recognized, covered by major outlets, featured in leading publications, active social media presence, according to industry experts, benchmark in the market

**Problem:** AI lists outlets and awards as proof of importance without saying what was said or why it matters. Becomes a turbocharged resume - impresses in a vacuum but informs nothing.

**Before (AI):**
> The company has been featured in TechCrunch, Bloomberg, The New York Times, and Wired. Widely recognized as a benchmark in the B2B SaaS market, it maintains an active social media presence with over 200,000 followers across platforms.

**After (human):**
> In a 2024 interview with Bloomberg, the CEO said ARR tripled after they shifted from enterprise-only to mid-market. The pivot took six months and cost them their two largest contracts.

**Detection signals:**
- Listing publications without citing specific articles (date, title, link)
- "Active social media presence" without metrics (followers, engagement rate)
- Mention of awards or rankings without verifiable source

**Correction techniques:**
- If real source exists -> cite with date and link: "Per TechCrunch, March 12, 2025 (link)"
- If no source exists -> cut the notability claim entirely
- "Verifiability test" - if the reader can't check in 30 seconds, it's puffery

---

### 3. Superficial analysis with present participles

**Trigger words/phrases:** underscoring the importance of, demonstrating the commitment to, reflecting the trend toward, contributing to the strengthening of, evidencing the potential of, driving innovation, fostering growth, solidifying its position as

**Problem:** AI glues participle phrases to the end of sentences to simulate analysis, but it isn't analyzing. It's syntactic filler - padding without information. Like that intern who writes 3 pages to say "it worked".

**Before (AI):**
> Stripe launched native integration with WhatsApp Business, demonstrating its commitment to innovation in digital payments and solidifying its position as a leader in the segment, driving the digital transformation of SMBs globally.

**After (human):**
> Stripe launched WhatsApp Business integration. Makes sense - most SMB leads in emerging markets come through WhatsApp, not web forms.

**Detection signals:**
- Sentence-final participle phrases that restate the main clause in grander terms
- "Demonstrating commitment to..." (always empty)
- Three or more participle clauses chained with commas

**Correction techniques:**
- Delete the participle clause and check if meaning is lost. Usually it isn't.
- If meaning IS lost, convert to a separate sentence with a specific claim
- "So what?" test - if the participle clause doesn't answer "so what?", cut it

---

### 4. Hollow future projections

**Trigger words/phrases:** poised to, set to transform, is expected to revolutionize, has the potential to reshape, promises to redefine, will likely emerge as, positioned to become

**Problem:** AI loves predicting transformative futures without evidence. These phrases create an illusion of analysis while saying nothing falsifiable.

**Before (AI):**
> The technology is poised to transform the healthcare industry, promising to redefine patient outcomes and reshape the landscape of medical diagnostics as we know it.

**After (human):**
> Two hospitals in Boston are running pilot programs with the diagnostic tool. Early numbers show 12% fewer false negatives on lung scans. Whether that scales to 4,000 hospitals is a different question entirely.

**Detection signals:**
- Future tense without specific timeline
- "Poised to" / "set to" without citing who said so or what evidence supports it
- Combination of future projection + superlative ("will revolutionize")

**Correction techniques:**
- Replace with current evidence: what exists NOW that suggests the future claim?
- If no evidence exists, either cut the claim or caveat it: "If X happens, then Y"
- Anchor to specific numbers, dates, or named sources
