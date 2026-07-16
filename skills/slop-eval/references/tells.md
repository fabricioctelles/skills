# The tell catalog

Distilled from [the pols.dev anti-slop design law](https://pols.dev/slop.md).
Each tell has an ID (grep the report with it), a severity, and what counts
as evidence. Severity: **crit** = broken (absolute-rule violation),
**major** = a recognized slop signature, **minor** = a default reached for
without intent.

A tell is recorded once per page, with its worst instance cited. Where a
"premium pair" note exists, the crafted version is NOT the tell — check it
before recording.

## C — Color & Light (Axis 1)

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| C1 | Blue→purple gradient | major | The single most recognizable slop move: soft blue-to-purple anywhere (backgrounds, buttons, borders, avatars). Any glowy two-adjacent-hue gradient counts. (Community name: the "AI purple problem".) |
| C2 | Purple default palette | minor | Purple as the unexamined brand hue; upgrade to C1 when gradiated with blue. |
| C3 | Pastel candy gradient background | major | Butter-yellow→peach→strawberry-milk (`#ffe6a8`→`#ffc0da` family), mint-to-lavender, sherbet washes filling a page/section. |
| C4 | Drifting aurora blobs | major | 2–4 big blurred radial blobs at ~0.5 opacity, often `mix-blend-mode: multiply` + `blur()`, melting into a pastel aurora behind content. Muted hexes don't rescue it. |
| C5 | Radial glow halo behind an object | major | Concentric bloom centered behind a hero object. Warm color doesn't rescue a symmetric halo — light comes from a direction or not at all. |
| C6 | Cool blue-charcoal dark default | major | The slate-indigo "serious dark product" base (~`#0c0e15`), bluer panels, lilac/periwinkle accent. Dark that nobody chose — the night-mode twin of C1, equally recognizable, equally default. |
| C7 | Cream/beige "editorial" default | minor | Warm cream/bone as the reflexive "tasteful premium" background — the new blue-purple. Major when it carries the whole brand across every surface. |
| C8 | Slop gray (UI-kit neutral) | minor | gray-100/200 family (`#f3f4f6`, `#eceef2`, `#e7ecf3`) as footer band, card fill, or page base — a wireframe left at its default. |
| C9 | Saturated accent sprayed everywhere | major | One vivid mid-saturation hue on the accent word, eyebrow dot, button fill, and labels at once. Premium accents are tonal (value-shifted, desaturated), not poster-bright. |
| C10 | Colliding colors / muddy wash | major | Two saturated unrelated hues fighting; an accent belonging to no system; a dim brown/grey-beige envelope under a fine component. |
| C11 | Hard color seams between sections | major | A gradient/glow that dies at a section boundary; the page should resolve one section's color into the next. (Deliberate breaks — a footer stepping onto its own floor — are fine.) |
| C12 | Background glow blob | minor | Soft radial accent bleeding from a corner/edge of a dark section for "atmosphere". See X12 for the clipped version. |
| C13 | Gradient-filled headline text | major | `background-clip: text` pouring magenta-purple-cyan (or blue-cyan) into display type. |
| C14 | Banded gradient | minor | A large color transition with visible stripes and no grain/dither. Premium pair: grainy gradients (noise dithered in) read as expensive. |
| C15 | Full-page grid / graph-paper background | major | Faint module grid (often radial-masked) laid under the whole page, even at low opacity. Premium pair: a tight, textured micro-grid behind one panel, or sparse blueprint marks (ruler ticks, crop marks). |

## T — Typography · W — Copy (Axis 2)

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| T1 | Google-shelf signature face | major | The identity carried by a free Google default. Rejected rotation — sans: Inter, Space Grotesk, Sora, Syne, Archivo, Onest, Darker Grotesque, Geologica, Hanken Grotesk, Spline Sans, Schibsted Grotesk, Gabarito, Figtree, Quicksand; serif: Fraunces, Cormorant, Bodoni/Didones, Playfair, Petrona, Hedvig Letters Serif, Brygada 1918, Young Serif; mono: JetBrains Mono, IBM Plex Mono, Spline Sans Mono, Fragment Mono. Inter as body is fine; Inter as the signature is the tell. |
| T2 | Recognizable slop pairing | major | Fraunces+Work Sans, Space Grotesk+Inter, Sora+JetBrains Mono, or any serif-display+clean-sans house pairing reused across brands. |
| T3 | Didone-as-luxury reflex | major | Bodoni/Didot/Playfair reached for because something "needs to feel expensive", usually letterspaced full caps. A Didone chosen on autopilot is slop. |
| T4 | Mono as the house voice | minor | Monospace on copyright lines, eyebrows, captions, labels everywhere to signal "technical". Mono is correct only for genuine data (timestamps, codes, prices, tables). |
| T5 | One label treatment everywhere | minor | The identical tracked-out-caps (or mono) costume on eyebrow, buttons, figure numbers, nav, and colophon at once. Different roles need different treatments. |
| T6 | Letterspaced serif wordmark | minor | Brand name in all-caps serif with wide tracking and nothing else — instant "luxury" logo. (SaaS twin: K12.) |
| T7 | Multi-line headline + dangling accent | major | Display line wrapping to 3–4 stacked rows; worse when the one colored/italic accent word lands stranded on the last line. Hold display to 1–2 composed lines, one coherent emphasis. |
| T8 | Cramped display type | major | Big numbers/words with negative tracking until glyphs nearly touch, separators buried ("0·fail"). Large type needs air. |
| T9 | The "tasteful" font swap | minor | Reaching for the known good alternative (Clash Display, General Sans, Big Shoulders, Newsreader, Instrument Serif, Bricolage) *because it's the reputed safe pick*. Picking type by reputation instead of by the brief is the tell. |
| T10 | Novelty rounded display + system body | major | Fat bubbly display faces (Baloo, Fredoka, Chewy, Lobster, Bagel Fat One) carrying headings, wordmark, and prices over a default system-ui body. |
| W1 | Em dashes as AI voice | minor | Em-dash-heavy copy — the classic AI writing tell. Hyphen, colon, or split the sentence. |
| W2 | Wall of copy | minor | Many stacked lines of filler text where hierarchy and visuals should carry meaning. Premium is terse. |
| W3 | Fake-but-impressive metrics | major | Invented social proof in copy: "velocity jumped 32%", fabricated customer names/titles ("VP Engineering, Northwind Labs"). |

## K — Components & Ornament (Axis 3)

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| K1 | Icon-pack icons everywhere | minor | Uniform thin-stroke line icons (lucide-react and kin) on every feature/section. Also covers "custom" redrawn versions of the same generic glyphs, and emojis standing in for icons. Premium pair: a bespoke set with an invented construction. |
| K2 | Pill / eyebrow badge | minor | The capsule above the hero headline (tiny icon + short text). Default hero decoration. |
| K3 | Glowy pill buttons | major | Fully-rounded gradient-filled buttons with a soft blurred glow beneath. |
| K4 | Oversized icon in a colored tile | major | Big icon centered in a filled rounded square/circle as hero visual or feature bullet. |
| K5 | Floating/bobbing cards | minor | Cards over a hero that bob or float in a loop — decorative motion with no purpose. |
| K6 | Kitchen-sink card | major | One card stacking icon-tile + category pill + tag pills + hairline divider + big price + glowy CTA. The clearest single signature. |
| K7 | Fake macOS / app window | major | CSS-drawn window with traffic-light dots and mock UI (kanban, avatars, status pills) as hero filler. Premium pair: a detailed, fully-populated, real product UI floated with depth — but only when a product UI actually exists. |
| K8 | Gradient pill with icon + text | major | Rounded box/pill with blue-purple fill holding an icon plus (often uppercase) label — the complete stack in one element. |
| K9 | Default CTA button pair | major | Gradient primary with trailing arrow + glow, next to an outlined ghost ("See how it works"), same medium radius. |
| K10 | Testimonial / quote card | major | Wide card, big quote-mark glyph, centered quote, avatar + name + title. Includes decorative oversized smart quotes around any line. |
| K11 | Gradient-circle initials avatar | minor | Two-letter initials on a gradient circle standing in for a photo. Major when the gradient is blue-purple. |
| K12 | Logo lockup (gradient tile + wordmark) | major | Icon in a small gradient squircle beside the name in a generic geometric font — the instant made-by-AI logo. |
| K13 | Hairline light border on every box | minor | 1px low-opacity outline (white-on-dark / light-grey-on-light) as default card styling. Premium pair: self-colored borders + tonal elevation (an edge you feel, not see). |
| K14 | Countdown timer | minor | DAYS/HRS/MIN/SEC boxes faking urgency whether or not anything ends. |
| K15 | Accent-bar card | minor | Dark box with one bright line down an edge to "add interest". Premium pair: the same idea with an invented silhouette (chamfer, notch, custom bracket). |
| K16 | Fake code-snippet window | major | Dark rounded panel, traffic lights, `quickstart.ts` tab, toy SDK call, purple-keyword/green-string palette in JetBrains Mono. |
| K17 | Floating tag pinned to an image | minor | Small info chip ("28°C & clear") stuck top-left on an image or gradient box. |
| K18 | Inner-glow box / pulsing live dot | minor | Bordered chip lit from inside; a status dot with an expanding glow ring. |
| K19 | Dot under the active nav item | minor | A lone dot as active state. Premium pair: weight/color shift on the type, or a genuine sliding tab indicator. |
| K20 | Eyebrow tick | minor | The ~30px hairline (often gradient-fading) drawn beside a kicker label to make it feel "designed". |
| K21 | Unrounded hairline rules as decoration | minor | Square-capped lines faking structure: dividers beside paragraphs, rails down lists. |
| K22 | Metadata as tinted pill chips, everywhere | minor | Every category/status/tag wrapped in a colored pill — component-kit dashboard, not a brand. |
| K23 | Faked or missing logos | major/minor | Faked: invented brand marks, fake customers, uniform icon-pack rows as filler (major). Missing: no social/integration marks where real ones would earn legitimacy (minor). Real marks, one size, one quiet treatment = premium. |
| K24 | Icon or logo in a box | minor | Any mark parked on a filled tile/chip/circle. Premium pair: the bare mark, sized and colored with intent. |
| K25 | Botched glass | major | Blur banding/pixelation over a flat backdrop, shadow/glow leaking below, a resting halo, or blur that pops on hover. A bad blur is worse than no blur. Premium pair: real liquid glass over a backdrop worth refracting (see premium-markers.md). |
| K26 | Grain over content | minor | A noise layer sitting on top of text, icons, or panels, muddying legibility. Grain belongs on the substrate; one deliberately masked display word is the allowed exception. |
| K27 | AI-brand convergence kit | minor | The unexamined AI-startup identity default: orbital/orbit-ring logo mark + corporate blue + generic geometric sans (often a name ending in -AI/-ly). Cite the mark and palette actually shown; the vibe alone is not evidence. |

## L — Layout & Composition (Axis 4)

Fonts are one axis; layout is the other — a recolored skeleton is still
slop. ≥3 majors here trigger the compounding cap (Axis 4 ≤ 40).

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| L1 | Default hero stack | major | Eyebrow → headline → subline → primary button + secondary link, centered down the middle. Slop layout even with fine type and color. |
| L2 | Split hero / hero + right panel | major | Left column (kicker, big headline, subline, two buttons, stat row) + right framed visual/product panel. The skeleton is the tell, not any piece. |
| L3 | Three-tier pricing preset | major | Free/Pro/Enterprise cards, pill over heading, "$X /mo", checkmark list, glowing "MOST POPULAR" middle card. |
| L4 | Pre-footer CTA slab | major | Full-width rounded gradient box: centered headline, "no credit card required" byline, one dark + one light button. |
| L5 | Kicker + serif-H2 section head | minor | Tiny uppercase accent kicker ("HOW IT WORKS") above a medium serif headline opening every section. Major when it opens 3+ sections. |
| L6 | Small-label-over-big-heading | minor | L5 generalized past serifs: mono/uppercase label over big heading as the template for starting any section. |
| L7 | Big serif statement block | minor | Kicker + one large serif sentence with a single italic accent word as the "philosophy" beat. |
| L8 | Inset enquire island as default closer | minor | The rounded floated panel (kicker + serif headline + lead + form) as the closing CTA, every time. |
| L9 | Email-pill + button form | minor | Long pill email input beside a pill button — the most repeated capture row there is. |
| L10 | Image card with overlay caption | minor | Portrait tile, bottom gradient scrim, uppercase meta label, serif name, link arrow. |
| L11 | Flat fill under everything after the hero | major | Atmospheric hero, then every section drops to one flat dark/cream field with boxes. The whole page needs atmosphere, not just the fold. |
| L12 | Numbered steps beside a vertical rail | minor | 01/02/03 items along a rule. Worse with square caps (also K21). |
| L13 | Filled + outlined button pair | major | Solid primary beside ghost secondary as the default action row, any color/radius. |
| L14 | Standard footer | minor | Wordmark + tagline, rule, four link columns under uppercase labels, rule, copyright with a cute sign-off. Correct, expected, no idea. |
| L15 | The SaaS meta-skeleton | major | The Stripe/Linear/Vercel clone: two-column hero → three icon-tile feature cards → tabbed switch → pricing cards → FAQ accordion → CTA slab → multi-column footer. Counts as one major AND each present block counts on its own — this is how the compounding cap fires. |
| L16 | Hero doesn't own the fold | major | Hero shorter than the viewport with the next section peeking in unaligned; the first frame is an accident, not a composition. |
| L17 | Content flung to far edges | minor | Two clusters jammed against opposite rims with a dead gulf between (default-asymmetric footers). Symmetry and a real grid unless asymmetry is composed. |
| L18 | Fixed background trailing the scroll | minor | One `position: fixed` sheet dragged behind every section (and the nav) — a static texture wearing a costume. |
| L19 | Recycling your own house style | major | The same five section shapes across briefs with a new palette — a theme reskinned, not a design. Needs portfolio context; else Unverifiable. |
| L20 | Botched oversized footer wordmark | major | Giant brand word pasted without composition: off-center, caps clipped, gradient fighting the background, default face with no treatment. Premium pair: anchored flush to the bottom edge, above the texture, deliberate case and spacing, bleeding intentionally. |
| L21 | Repeated section template | major | 3+ sections (or 3+ blocks in a row: identical cards with icon + heading + two lines) built on the same grid/card/column skeleton with only content, icon, or color swapped. The self-cloning is the tell, not any single block. (L15 is the page-level *sequence*; this is repetition *within* one page.) |

## M — Motion & Interaction (Axis 5)

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| M1 | Invisible-content trap | **crit** | Content starting at `opacity:0` / translated-away, revealed by JS or scroll timeline. Covers `animation-timeline: view()`, IntersectionObserver toggles, and `initial={{opacity:0}}`. If the reveal never fires, the section is GONE. Content is visible by default — absolute rule 1. |
| M2 | Hover boop | minor | Button lifts (translateY) or scales on hover. Buttons don't move; change state cleanly (fill/color shift, icon slide). |
| M3 | Underline-fill hover | minor | Underline that grows/wipes/travels in on links or ghost buttons. |
| M4 | Default card hover-lift | minor | Translate-up + all-around shadow bloom + accent glowing border on every card grid. |
| M5 | Sun-and-moon theme toggle | minor | The stock pill sliding a knob between sun and moon. |
| M6 | Botched fill animation | major | Caps flipping sharp↔rounded mid-transition (scaleY on a rounded shape), partial fill of the track, stuttering ease. Half-built motion screams slop. |
| M7 | Dead page | major | No authored motion at all: static nav, nothing responds to scroll or hover. "Boring/static" is a rejection on its own. Calm is allowed; dead is not. |
| M8 | Dead controls / fake interactivity | **crit** | Tabs, accordions, toggles, or buttons that look live and do nothing when clicked — or props dressed as controls. Absolute rule 6; verify with a real click. |

## X — Execution & Craft (Axis 6)

The "broken, not designed" family. X1, X2, X3, X5, X11 are the remaining
absolute rules.

| ID | Tell | Sev | Evidence to look for |
|----|------|-----|----------------------|
| X1 | Nothing actually centered | **crit** | Numbers floating high in circles, glyphs sitting low in tiles, labels off-axis in pills. SVG traps: `text-anchor: middle` without `dominant-baseline`, optical vs bounding-box center. Zoom in and verify. |
| X2 | Content sliced by an edge | **crit** | Caps shaved flat, controls missing top pixels, descenders vanishing into borders — from clip-path, notches, `overflow:hidden`, fixed heights. "Clear the cut": content must sit fully inside the visible region. |
| X3 | Ragged comparison columns | **crit** | Pricing/plan/feature columns where titles, prices, list starts, and above all buttons sit at different heights because copy length pushed rows around. Equal heights, bottom-anchored CTAs, shared baselines. |
| X4 | Text jammed against the edge | major | Copy kissing the viewport/container rim with no gutter. (Deliberate cropped watermarks excepted.) |
| X5 | Unreadable contrast | **crit** | Text too close in value to its background; worst on filled buttons. Every string clears its background by a real value gap. |
| X6 | Default all-around shadow | major | Soft symmetric shadow bloomed on every side of everything by reflex — the "float it on a fluffy cloud" signature. Premium pair: tight, low-offset, directional, tinted to the surface/element — or depth from tone with no shadow. |
| X7 | Fake shadow (second box) | major | A literal offset rectangle/duplicate element imitating a shadow to dodge a no-shadow rule — routing around the rule, worse than the shadow. |
| X8 | Botched shadow (hard-edged box) | major | A shadow reading as a solid rounded-rectangle silhouette behind the element. If you can trace the shadow's border, it's a box, not a shadow. |
| X9 | Bloom = blurred self-copy | major | Glow/shadow that is the element's own outline blurred and offset — a sticker with a halo, pooling to the sides, never blending. |
| X10 | Off-center strike line | major | Strike-through/redaction bar floating off the true optical center of the glyphs (measure against real x-height). |
| X11 | Clipped at a section overlap | **crit** | Content that should continue under an overlapping panel/sheet guillotined at the seam by the upper layer's edge or `overflow:hidden`. |
| X12 | Cut-off glow | major | A glow clipped by a section edge so it ends in a hard line — the accidental edge on a "premium" effect. |
| X13 | Hard image seams | major | Full-bleed image butting a flat section with a visible line. Premium fix: mask the image's own pixels with a long many-stop fade, tall section, continuous page color — never a color overlay, and never a scrim ending at the boundary. |
| X14 | Focus states stripped | major | `outline: none` (or `:focus` suppressed) on interactive elements with no visible replacement — keyboard navigation rendered invisible. Sibling of X5: legibility laws apply to keyboard users too. Verifiable in code or by tabbing through a live page. |
