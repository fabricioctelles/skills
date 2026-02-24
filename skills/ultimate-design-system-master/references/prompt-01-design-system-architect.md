PROMPT 1: The Design System Architect

You are a Principal Designer at Apple, responsible for the Human Interface Guidelines.

Create a comprehensive design system for [BRAND/PRODUCT NAME].

Brand attributes:
- Personality: [MINIMALIST/BOLD/PLAYFUL/PROFESSIONAL/LUXURY]
- Primary emotion: [TRUST/EXCITEMENT/CALM/URGENCY]
- Target audience: [DEMOGRAPHICS]

Deliverables following Apple HIG principles:

1. FOUNDATIONS
   ## Color system:
     - Primary palette (6 colors with hex, RGB, HSL, accessibility ratings)
     - Semantic colors (success, warning, error, info)
     - Dark mode equivalents with contrast ratios
     - Color usage rules (what each color means and when to use it)

   ## Typography:
     - Primary font family with 9 weights (Display, Headline, Title, Body, Callout, Subheadline, Footnote, Caption)
     - Type scale with exact sizes, line heights, letter spacing for desktop/tablet/mobile
     - Font pairing strategy
     - Accessibility: Minimum sizes for legibility

   ## Layout grid:
     - 12-column responsive grid (desktop: 1440px, tablet: 768px, mobile: 375px)
     - Gutter and margin specifications
     - Breakpoint definitions
     - Safe areas for notched devices

   ## Spacing system:
     - 8px base unit scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128)
     - Usage guidelines for each scale step

2. COMPONENTS (Design 30+ components with variants)
   ## Navigation: Header, Tab bar, Sidebar, Breadcrumbs
   ## Input: Buttons (6 variants), Text fields, Dropdowns, Toggles, Checkboxes, Radio buttons, Sliders
   ## Feedback: Alerts, Toasts, Modals, Progress indicators, Skeleton screens
   ## Data display: Cards, Tables, Lists, Stats, Charts
   ## Media: Image containers, Video players, Avatars

   For each component:
   - Anatomy breakdown (parts and their names)
   - All states (default, hover, active, disabled, loading, error)
   - Usage guidelines (when to use, when NOT to use)
   - Accessibility requirements (ARIA labels, keyboard navigation, focus states)
   - Code-ready specifications (padding, margins, border-radius, shadows)

3. PATTERNS
   ## Page templates: Landing page, Dashboard, Settings, Profile, Checkout
   ## User flows: Onboarding, Authentication, Search, Filtering, Empty states
   ## Feedback patterns: Success, Error, Loading, Empty

4. TOKENS
   ## Complete design token JSON structure for developer handoff

5. DOCUMENTATION
   ## Design principles (3 core principles with examples)
   ## Do's and Don'ts (10 examples with visual descriptions)
   ## Implementation guide for developers

Format as a design system documentation that could be published immediately.

