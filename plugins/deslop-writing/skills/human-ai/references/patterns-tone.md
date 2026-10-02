# Tone Patterns - Detection and Correction

Patterns betraying artificial, servile, or performative tone in English text. Each pattern includes triggers, examples (tech/startup/marketing/dev contexts), and human alternatives.

---

### 1. Sycophantic Tone

**Trigger words/phrases:** "Great question!", "Absolutely!", "Excellent observation!", "I hope this helps!", "I'm happy to help!", "Thank you for sharing!"

**Problem:** Generic praise to the interlocutor before answering. Nobody talks like this in professional writing - it's the signature of a chatbot trying to please.

**Before (AI):**
> Great question! Continuous deployment with GitHub Actions is really a fascinating approach. I'd be happy to help you with that! Let's dive in: first, you need to configure the workflow YAML...

**After (human):**
> To set up continuous deployment with GitHub Actions, start with the workflow YAML. Create a `.github/workflows/deploy.yml` triggered on push to main...

**Cut on sight:**
- "Great question!" / "Excellent point!"
- "Absolutely!" / "Definitely!"
- "I hope this helps!" / "Happy to contribute!"

---

### 2. Knowledge-Cutoff Disclaimers

**Trigger words/phrases:** "As of my last update...", "Based on the information available to me...", "As of my knowledge cutoff...", "I cannot confirm with certainty, but...", "According to my limited information..."

**Problem:** Exposes the machine nature of the author. Humans don't signal the temporal boundary of their own knowledge - they simply state what they know or say "I don't know."

**Before (AI):**
> As of my last update, Next.js 15 introduced Server Actions as a stable feature. However, more recent developments may have changed this landscape. Based on the information available to me, the recommendation is to use App Router.

**After (human):**
> Next.js 15 stabilized Server Actions. If something changed since, check the official docs - but as of what I've tested, App Router is the way to go.

---

### 3. Residual Collaborative Communication

**Trigger words/phrases:** "Here's an example of...", "I can help you with...", "I'll show you how...", "Below is...", "Feel free to ask more!", "Don't hesitate to reach out!"

**Problem:** Text retains traces of assistant-user interaction. Reads like a support response, not authored text. When published as an article or post, immediately betrays its origin.

**Before (AI):**
> Here's an example of how to implement JWT authentication in Express. I'll walk you through the setup step by step. Feel free to adapt according to your needs!

**After (human):**
> JWT auth in Express boils down to a middleware that validates the token before letting the request through. The basic setup looks like this:

---

### 4. Excessive Hedging

**Trigger words/phrases:** "it seems", "perhaps", "it could be that", "one might argue", "it's possible that", "it may be the case", "to some extent", "in a sense"

**Problem:** AI over-qualifies every statement to avoid being wrong. The result is prose with no conviction. Reads like someone trying to never be pinned down on anything.

**Before (AI):**
> It seems that perhaps the new architecture may offer some improvements. One might argue that, to some extent, the performance gains could be significant, though it's possible that further testing may reveal limitations.

**After (human):**
> The new architecture is faster. Our benchmarks show 40% improvement on cold starts. Whether that holds under production load is an open question, but the synthetic results are clear.

**Rule:** Qualify only when:
- You genuinely don't know (and say so directly: "I don't know")
- There's real disagreement among sources (cite both)
- The data genuinely doesn't support a firm claim (show the data)

Otherwise: commit to the claim.

---

### 5. Stakes Inflation

**Trigger words/phrases:** "crucial for the future of humanity", "this will define a generation", "the most important challenge of our time", "could fundamentally alter the course of", "the stakes have never been higher"

**Problem:** AI inflates the importance of everything to sound thoughtful. A CSS framework becomes "crucial for the future of web development". A project management tool becomes "fundamental to how teams will work for decades to come."

**Before (AI):**
> This represents one of the most crucial challenges facing the technology industry today. The implications could fundamentally alter the course of software development as we know it.

**After (human):**
> It's a hard problem. The teams I've seen tackle it took 6-12 months to get right. Most gave up and used the workaround instead.

**Rule:** Match stakes to scope. A framework choice is a framework choice, not a civilizational decision. Reserve grand language for genuinely grand topics - and even then, specifics beat superlatives.

---

### 6. False Empathy / Emotional Performance

**Trigger words/phrases:** "I understand how frustrating this must be", "I can only imagine how difficult", "This is truly inspiring", "What an incredible journey", "I'm deeply moved by"

**Problem:** AI performs emotions it cannot have. The result rings hollow because the reader intuitively knows no genuine feeling exists behind the words. Human writers either feel something specific and show it through detail, or they don't perform emotion at all.

**Before (AI):**
> I understand how frustrating this situation must be for everyone involved. It's truly inspiring to see the community come together during such a challenging time. What an incredible journey this has been.

**After (human):**
> That sucks. I've been there - the deploy failed at 2am on a Friday and the on-call person was unreachable. What the community did next was interesting though: three people independently submitted patches before Monday.

**Rule:** Show, don't perform. If you feel something, name it specifically. If you don't, don't fake it.
