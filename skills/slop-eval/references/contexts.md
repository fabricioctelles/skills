# Design Contexts

Different design types have different expectations. A countdown timer on an
e-commerce sale page is legitimate; on a SaaS landing page it's a pressure
tactic. This file defines context-specific priorities and tolerances.

Set the `context` parameter to one of: `landing`, `saas`, `editorial`,
`ecommerce`, or `auto` (default — infer from the design).

## How to use this file

1. **Identify the context** before sweeping. If `auto`, look for signals:
   - Pricing cards, feature grids, integrations → `saas`
   - Product cards, cart, checkout → `ecommerce`
   - Articles, bylines, reading time → `editorial`
   - Hero + CTA + social proof only → `landing`

2. **Apply priority weights** — tells in the Priority section are more
   damaging to score perception in this context.

3. **Apply tolerances** — tells in the Tolerance section may be excluded
   with lighter justification (still document, but `// CONTEXT:` is valid).

4. **Note context-specific tells** — some patterns are only tells in
   certain contexts.

---

## Landing Page / Marketing

The classic conversion page: hero, value prop, social proof, CTA. Every
element must earn its place.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| L1 | Default hero stack | The hero IS the page — a generic hero sinks everything |
| L2 | Split hero | Same — the skeleton is immediately recognizable |
| S1 | Signature artifact (missing) | A landing page with no focal object is a template |
| C1 | Blue→purple gradient | The "AI landing page" signature; instant credibility loss |
| K9 | Default CTA button pair | The action is the point; generic buttons kill conversion |
| L4 | Pre-footer CTA slab | The closer matters; a template closer is a missed opportunity |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K2 | Pill / eyebrow badge | Common convention, low harm if the rest is strong |
| K14 | Countdown timer | Legitimate if tied to a real deadline (launch, sale end) |
| L9 | Email-pill + button form | Standard capture pattern; the form itself isn't the problem |
| K10 | Testimonial card | The format is expected; focus on whether content is real |

### Context-specific guidance

- **Fold ownership (L16) is critical** — the first viewport IS the pitch.
  A landing page hero that doesn't own the fold is a structural failure.
- **Signature artifact (S1) must be above the fold** — burying it below
  wastes the most valuable real estate.
- **Real specificity (S7) is table stakes** — fake logos, placeholder
  testimonials, lorem-adjacent copy are instant credibility killers.

---

## SaaS Product / Dashboard

Product pages, feature tours, pricing, and the product UI itself. Clarity
and execution matter more than flair.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| X1 | Nothing actually centered | Dashboards live or die on alignment |
| X3 | Ragged comparison columns | Pricing comparison is often the decision point |
| K6 | Kitchen-sink card | Overloaded UI signals poor product thinking |
| K22 | Metadata pills everywhere | Dashboard-kit aesthetic = no brand |
| L3 | Three-tier pricing preset | The pricing page IS the product pitch |
| L15 | SaaS meta-skeleton | Stripe/Linear/Vercel clone is the most common SaaS slop |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K1 | Icon-pack icons | System UI icons are expected in product UI |
| K13 | Hairline borders | Legitimate UI pattern for card separation |
| T4 | Mono as house voice | Acceptable for code, data, timestamps in product UI |
| K7 | App window mock | Legitimate if showing real product UI, not filler |

### Context-specific guidance

- **Execution axis (6) carries more weight** — a SaaS page can survive
  generic layout if the execution is flawless. Broken alignment, contrast
  failures, and dead controls are fatal.
- **K7 (fake window) flips in context** — a detailed, populated, real
  product UI is a signature, not a tell. The tell is an empty mock with
  traffic lights and placeholder kanban.
- **L15 (SaaS skeleton) compounds** — if the page follows the Stripe
  sequence AND each section is a known template, apply both the skeleton
  tell and the individual section tells.

---

## Editorial / Magazine

Content-first designs: articles, blogs, publications, portfolios. Typography
and reading experience dominate.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| T1 | Google-shelf signature face | Editorial identity lives in type |
| T2 | Recognizable slop pairing | Type pairing IS the voice |
| T3 | Didone-as-luxury reflex | The "premium editorial" autopilot |
| L7 | Big serif statement block | The philosophy-beat cliché |
| W2 | Wall of copy | Editorial should know better |
| L10 | Image card with overlay caption | The magazine-grid autopilot |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| C7 | Cream/beige editorial default | Legitimate editorial palette choice if consistent |
| L5 | Kicker + serif-H2 section head | Expected editorial convention |
| K21 | Hairline rules as decoration | Traditional editorial element |
| T6 | Letterspaced serif wordmark | May be the actual brand identity |

### Context-specific guidance

- **Typography axis (2) carries 3x effective weight** — in editorial, type
  IS the design. A generic typeface choice sinks the whole piece.
- **C7 (cream background) is context-dependent** — warm cream as a
  deliberate paper-texture choice is premium; cream as "I need a background
  that isn't white" is slop. Check if it's carried with intent (grain,
  texture, tonal variation) or just a flat fill.
- **Reading experience tells** — check line length (45–75 chars), line
  height (1.4–1.6 for body), and paragraph spacing. These aren't in the
  catalog but affect the editorial context strongly.

---

## E-commerce / Retail

Product listings, category pages, cart, checkout. Conversion mechanics and
trust signals dominate.

### Priority tells (most damaging here)

| ID | Tell | Why it matters more |
|----|------|---------------------|
| X3 | Ragged comparison columns | Product comparison must be scannable |
| X5 | Unreadable contrast | Price and CTA must be instantly legible |
| K23 | Faked or missing logos | Trust signals are everything in commerce |
| W3 | Fake metrics | Invented social proof destroys trust |
| M8 | Dead controls | Add-to-cart that doesn't work = lost sale |
| L3 | Three-tier pricing preset | Subscription/plan selection UX matters |

### Tolerance (lighter justification OK)

| ID | Tell | Why tolerance applies |
|----|------|----------------------|
| K14 | Countdown timer | Legitimate for real sales, flash deals, inventory |
| K22 | Metadata pills | Product tags, categories, badges are expected |
| K17 | Floating tag on image | Price tags, sale badges on product images are standard |
| L12 | Numbered steps | Checkout progress indicators are expected |

### Context-specific guidance

- **Trust signals are non-negotiable** — K23 (fake logos) and W3 (fake
  metrics) are effectively critical in e-commerce context. Payment badges,
  security seals, and customer logos must be real.
- **K14 (countdown) splits by reality** — a countdown to a real sale end
  is legitimate UX; an evergreen fake countdown is manipulative slop.
  Document which it is.
- **Execution axis (6) is conversion-critical** — every pixel of friction
  in checkout costs money. Alignment issues, contrast failures, and
  confusing states are business failures, not just design failures.

---

## Multi-context pages

Some pages span contexts (e.g., a SaaS landing page with editorial blog
section, an e-commerce site with magazine-style lookbooks). Handle by:

1. **Identify the primary context** — what is the page's main job?
2. **Section-level context switching** — apply different tolerances to
   different sections where appropriate.
3. **Document in the report** — note when a section was evaluated under a
   different context than the page default.

Example:
```markdown
> Context: `saas` (primary), `editorial` for Blog section

## Section Ledger
| Section | Context | Verdict | ... |
|---------|---------|---------|-----|
| Hero | saas | SUSPICIOUS | ... |
| Features | saas | CLEAN | ... |
| Blog | editorial | INFLATED | ... |
```

---

## Context detection heuristics

When `context: auto`, use these signals:

| Signal | Likely context |
|--------|---------------|
| Pricing cards with tiers | `saas` |
| "Start free trial", "Book demo" CTAs | `saas` |
| Product grid with prices | `ecommerce` |
| Cart icon, "Add to cart" | `ecommerce` |
| Byline, reading time, article body | `editorial` |
| Category/tag taxonomy | `editorial` |
| Single hero + CTA + testimonials only | `landing` |
| No product UI shown | `landing` |

If signals conflict, ask the user or default to `landing` (the most
common evaluation target).
