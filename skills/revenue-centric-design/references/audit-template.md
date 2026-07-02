# Audit Output Template

Deliver every audit run (landing page, pricing page, onboarding flow, cancellation flow,
features page) in this shape. A row may only enter the table once it passes the completion
criterion — named mechanism + cited principle + attached evidence.

## Header

> **Target:** <URL or flow name> · **Date:** <date>
> **ICP:** <buying criteria — trigger, pain, prior attempt, proof needed; not demographics>
> **Awareness level:** <Schwartz stage of the arriving traffic>
> **Verdict:** <one sentence — the single biggest revenue leak found>

If ICP or awareness level can't be stated, that **is** finding #1 — the debug order starts
there (ICP → awareness → proof → visual), never at the visual layer.

## Findings

Ordered by expected revenue impact, not by position on the page.

| # | Finding | Mechanism | Principle (reference file) | The move | Evidence |
|---|---------|-----------|----------------------------|----------|----------|
| 1 | Hero opens with the product category, not the visitor's pain | 5-second test | "Pass the 5-second test — lead with the problem" (conversion-and-landing-pages) | Rewrite the first line to the pain: "Your team loses 6 hours a week hunting for information" | Descriptive vs transformation-led LPs: 0.5% vs 3% across 30 Brazilian SaaS ([source](https://x.com/richardrx/status/2045154631974539650)) |

When a finding involves numbers (A/B sample size, churn→LTV, CAC per closed deal), paste the
actual `scripts/revenue_math.py` output into the Evidence cell — never an estimate.

## Close

- **Do first:** the top 1–3 moves, each with one line on why it outranks the rest.
- **Don't:** any tempting change the SKILL.md gotchas rule out (fabricated scarcity, LP rules
  applied to content pages, review manipulation, underpowered tests…).
- Append the prescribed moves to the project's `rcd-log.md` (format in SKILL.md) so the next
  engagement starts from what was already tried.
