---
name: website-spec
description: >-
  Self-contained offline version of The Website Specification — runs without
  network access, ideal for air-gapped environments, maximum-privacy workflows,
  and internal projects. Audit, validate, and fix websites against 128 topics
  covering HTML foundations, SEO, accessibility (WCAG), security headers,
  well-known URIs, agent readiness (llms.txt, MCP, A2A), performance (Core Web
  Vitals), privacy, resilience, and i18n. Each topic is tagged
  required/recommended/optional/avoid with implementation guidance and
  verification steps. Use when the user asks "audit my site", "what should my
  website have", "is X required", "check accessibility", "security headers
  review", "agent readiness", "front-end checklist", "what's missing", "best
  practices for websites", or any site-quality question backed by WHATWG, W3C,
  IETF, and WCAG standards. Check https://specification.website/ for the online
  and updated version.
version: "1.0"
licence: CC-BY-4.0
source: https://github.com/jdevalk/specification.website
author: Joost de Valk and contributors
---

# The Website Specification

A platform-agnostic specification of the technical features every decent website
should have — from `<title>` to `/.well-known/security.txt`, from WCAG contrast
to `llms.txt`. Written for humans and agents.

## When to use this skill

- The user asks "what should my site have", "is X required", "audit this URL",
  "what does the spec say about Y", or anything similar.
- You're reviewing a site and want to cite primary standards rather than vendor
  blog posts.
- You need a checklist for a platform-agnostic audit.
- The user asks about agent readiness, accessibility, security headers,
  performance, SEO, or i18n best practices.

## Statuses — the contract

Every topic has a `status` field in its frontmatter:

| Status | Meaning |
|--------|---------|
| **required** | The platform contract breaks without it. Lead with these when recommending fixes. |
| **recommended** | A modern site should do it. |
| **optional** | Depends on context. |
| **avoid** | Outdated or harmful. Flag it if a site does one of these. |

The bar for `required` is "the platform breaks", not "we strongly suggest".
Never silently upgrade `recommended` to `required`.

## Categories

All topics are in `references/` organized by category:

| Category | Topics | Path | Description |
|----------|--------|------|-------------|
| Foundations | 14 | `references/foundations/` | HTML, head, and document basics every page needs |
| SEO | 13 | `references/seo/` | robots.txt, sitemaps, canonicals, structured data |
| Accessibility | 20 | `references/accessibility/` | WCAG-aligned rules for all abilities |
| Security | 12 | `references/security/` | Headers, transport, and policies |
| Well-Known URIs | 9 | `references/well-known/` | Standard paths under `/.well-known/` |
| Agent Readiness | 18 | `references/agent-readiness/` | Making sites legible to AI agents and crawlers |
| Performance | 19 | `references/performance/` | Core Web Vitals, caching, images, fonts |
| Privacy | 6 | `references/privacy/` | Consent, signals, respecting visitor choice |
| Resilience | 5 | `references/resilience/` | Error pages, offline, redirects |
| Internationalisation | 12 | `references/i18n/` | Language, locale, direction, translated content |

## Workflows

### Full site audit

**Trigger:** "audit my site", "check this URL", "what's missing"

**Procedure:**

1. Identify the target URL(s) and scope (full audit or specific categories).
2. For each applicable topic, verify the site against the "Verification" section
   in the reference file. Use browser tools, curl, view-source, or DevTools as
   described.
3. Record each topic as ✅ PASS, ❌ FAIL, or ⚠️ PARTIAL.
4. Produce the **Audit Report** (see output format below).
5. Save the report to `website-spec-audit.md` in the project root (or a path the
   user specifies).

**Execution order:**
- First pass: all `status: required` topics (blocking issues).
- Second pass: all `status: recommended` topics (quality gaps).
- Optional pass: `status: optional` topics relevant to the site's context.
- Flag any `status: avoid` patterns found.

### Output format — Audit Report

```markdown
# Website Spec Audit — {URL}
Date: {YYYY-MM-DD}
Scope: {full | categories audited}

## Summary
- Required: {n}/{total} passing
- Recommended: {n}/{total} passing
- Score: {passing required + recommended} / {total applicable} ({percentage}%)

## Findings

### {Category}
| Topic | Status | Result | Notes |
|-------|--------|--------|-------|
| {title} | required | ✅ | — |
| {title} | required | ❌ | {what's wrong + fix from "How to implement"} |
| {title} | recommended | ⚠️ | {partial implementation detail} |

## Priority fixes (required, failing)
1. {topic} — {one-line fix action from the reference}
2. ...

## Recommended improvements
1. {topic} — {one-line improvement}
2. ...
```

### Re-audit and comparison

**Trigger:** "check again", "did it improve", "re-audit", second run on same URL

**Procedure:**

1. Locate the previous `website-spec-audit.md` for the same URL.
2. Run the audit again using the same scope.
3. Produce a **Comparison Report** appended to or replacing the audit file:

```markdown
## Comparison — {previous date} → {current date}

| Topic | Previous | Current | Delta |
|-------|----------|---------|-------|
| {title} | ❌ | ✅ | 🟢 Fixed |
| {title} | ⚠️ | ✅ | 🟢 Improved |
| {title} | ✅ | ❌ | 🔴 Regression |

### Progress
- Fixed: {n} topics
- Regressed: {n} topics
- Remaining failures: {n} required, {n} recommended
- Score: {old%} → {new%} ({+/-}pp)
```

### Category-specific audit

**Trigger:** "check accessibility", "security headers review", "agent readiness"

Same procedure as full audit but scoped to one category folder. Use the same
output format filtered to that category.

### Lookup a specific topic

**Trigger:** "is X required", "what does the spec say about Y"

1. Find the matching file in `references/`.
2. Return the status, the "What it is" and "Why it matters" sections.
3. Quote the `sources` array from frontmatter as the authoritative reference.

### Generate implementation checklist

**Trigger:** "give me a checklist", "what do I need to implement"

1. List all `required` topics as a Markdown task list (`- [ ]`).
2. Group by category.
3. Optionally include `recommended` topics as a separate section.
4. Save to `website-spec-checklist.md` for the user to track progress.

## Topic file structure

Each `.md` file in `references/` follows this structure:

```yaml
---
title: "Topic title"
category: category-slug
status: required|recommended|optional|avoid
url: (original canonical URL)
updated: "ISO date"
sources:
  - title: "Source name"
    url: "source URL"
    publisher: "Publisher"
---
```

Followed by the full specification content with sections: What it is, Why it
matters, How to implement, Common mistakes, and Verification.

## References index

### Foundations (14)
- [references/foundations/doctype.md](references/foundations/doctype.md) — The HTML doctype
- [references/foundations/html-lang.md](references/foundations/html-lang.md) — The lang attribute on `<html>`
- [references/foundations/meta-charset.md](references/foundations/meta-charset.md) — `<meta charset>`
- [references/foundations/meta-viewport.md](references/foundations/meta-viewport.md) — `<meta name="viewport">`
- [references/foundations/title.md](references/foundations/title.md) — The `<title>` element
- [references/foundations/meta-description.md](references/foundations/meta-description.md) — `<meta name="description">`
- [references/foundations/canonical-url.md](references/foundations/canonical-url.md) — Canonical URL
- [references/foundations/favicons.md](references/foundations/favicons.md) — Favicons and app icons
- [references/foundations/theme-color.md](references/foundations/theme-color.md) — `<meta name="theme-color">`
- [references/foundations/color-scheme.md](references/foundations/color-scheme.md) — `<meta name="color-scheme">`
- [references/foundations/open-graph.md](references/foundations/open-graph.md) — Open Graph protocol
- [references/foundations/feed-discovery.md](references/foundations/feed-discovery.md) — Feed discovery with `rel="alternate"`
- [references/foundations/feed-hygiene.md](references/foundations/feed-hygiene.md) — Feed content hygiene
- [references/foundations/popover-api.md](references/foundations/popover-api.md) — Popover API

### SEO (13)
- [references/seo/robots-txt.md](references/seo/robots-txt.md) — robots.txt
- [references/seo/xml-sitemaps.md](references/seo/xml-sitemaps.md) — XML sitemaps
- [references/seo/sitemap-index.md](references/seo/sitemap-index.md) — Sitemap index files
- [references/seo/image-sitemaps.md](references/seo/image-sitemaps.md) — Image and video sitemap extensions
- [references/seo/url-structure.md](references/seo/url-structure.md) — URL structure
- [references/seo/redirects.md](references/seo/redirects.md) — Redirects (301/302/308)
- [references/seo/soft-404.md](references/seo/soft-404.md) — Soft 404s
- [references/seo/meta-robots.md](references/seo/meta-robots.md) — Meta robots and X-Robots-Tag
- [references/seo/heading-hierarchy.md](references/seo/heading-hierarchy.md) — Heading hierarchy
- [references/seo/internal-linking.md](references/seo/internal-linking.md) — Internal linking
- [references/seo/structured-data.md](references/seo/structured-data.md) — Structured data (JSON-LD)
- [references/seo/breadcrumbs.md](references/seo/breadcrumbs.md) — Breadcrumbs
- [references/seo/indexnow.md](references/seo/indexnow.md) — IndexNow

### Accessibility (20)
- [references/accessibility/color-contrast.md](references/accessibility/color-contrast.md) — Colour contrast
- [references/accessibility/image-alt-text.md](references/accessibility/image-alt-text.md) — Image alt text
- [references/accessibility/form-labels.md](references/accessibility/form-labels.md) — Form labels
- [references/accessibility/keyboard-navigation.md](references/accessibility/keyboard-navigation.md) — Keyboard navigation
- [references/accessibility/focus-indicators.md](references/accessibility/focus-indicators.md) — Visible focus indicators
- [references/accessibility/skip-links.md](references/accessibility/skip-links.md) — Skip links
- [references/accessibility/semantic-html.md](references/accessibility/semantic-html.md) — Semantic HTML and landmarks
- [references/accessibility/aria-usage.md](references/accessibility/aria-usage.md) — ARIA — first rule of ARIA
- [references/accessibility/link-text.md](references/accessibility/link-text.md) — Descriptive link text
- [references/accessibility/empty-links-buttons.md](references/accessibility/empty-links-buttons.md) — Empty links and buttons
- [references/accessibility/form-errors.md](references/accessibility/form-errors.md) — Accessible form errors
- [references/accessibility/document-language.md](references/accessibility/document-language.md) — Document and parts language
- [references/accessibility/reduced-motion.md](references/accessibility/reduced-motion.md) — Reduced motion
- [references/accessibility/accessibility-overlays.md](references/accessibility/accessibility-overlays.md) — Accessibility overlays
- [references/accessibility/captions-and-transcripts.md](references/accessibility/captions-and-transcripts.md) — Captions and transcripts
- [references/accessibility/data-tables.md](references/accessibility/data-tables.md) — Accessible data tables
- [references/accessibility/touch-target-size.md](references/accessibility/touch-target-size.md) — Touch target size
- [references/accessibility/hidden-until-found.md](references/accessibility/hidden-until-found.md) — Hidden until found
- [references/accessibility/native-interactive-elements.md](references/accessibility/native-interactive-elements.md) — Native interactive elements
- [references/accessibility/css-state-selectors.md](references/accessibility/css-state-selectors.md) — CSS state and relational selectors

### Security (12)
- [references/security/https-tls.md](references/security/https-tls.md) — HTTPS and TLS
- [references/security/hsts.md](references/security/hsts.md) — HSTS (Strict-Transport-Security)
- [references/security/content-security-policy.md](references/security/content-security-policy.md) — Content Security Policy (CSP)
- [references/security/security-txt.md](references/security/security-txt.md) — /.well-known/security.txt
- [references/security/x-content-type-options.md](references/security/x-content-type-options.md) — X-Content-Type-Options: nosniff
- [references/security/frame-ancestors.md](references/security/frame-ancestors.md) — Clickjacking protection
- [references/security/referrer-policy.md](references/security/referrer-policy.md) — Referrer-Policy
- [references/security/permissions-policy.md](references/security/permissions-policy.md) — Permissions-Policy
- [references/security/subresource-integrity.md](references/security/subresource-integrity.md) — Subresource Integrity (SRI)
- [references/security/cookie-attributes.md](references/security/cookie-attributes.md) — Cookie attributes
- [references/security/caa-records.md](references/security/caa-records.md) — DNS CAA records
- [references/security/dnssec.md](references/security/dnssec.md) — DNSSEC

### Well-Known URIs (9)
- [references/well-known/well-known-overview.md](references/well-known/well-known-overview.md) — Well-known URIs overview
- [references/well-known/change-password.md](references/well-known/change-password.md) — /.well-known/change-password
- [references/well-known/openid-configuration.md](references/well-known/openid-configuration.md) — /.well-known/openid-configuration
- [references/well-known/api-catalog.md](references/well-known/api-catalog.md) — /.well-known/api-catalog
- [references/well-known/webfinger.md](references/well-known/webfinger.md) — /.well-known/webfinger
- [references/well-known/apple-app-site-association.md](references/well-known/apple-app-site-association.md) — apple-app-site-association
- [references/well-known/assetlinks-json.md](references/well-known/assetlinks-json.md) — assetlinks.json
- [references/well-known/nodeinfo.md](references/well-known/nodeinfo.md) — /.well-known/nodeinfo
- [references/well-known/traffic-advice.md](references/well-known/traffic-advice.md) — /.well-known/traffic-advice

### Agent Readiness (18)
- [references/agent-readiness/agent-readiness-overview.md](references/agent-readiness/agent-readiness-overview.md) — Agent readiness overview
- [references/agent-readiness/llms-txt.md](references/agent-readiness/llms-txt.md) — /llms.txt
- [references/agent-readiness/llms-full-txt.md](references/agent-readiness/llms-full-txt.md) — /llms-full.txt
- [references/agent-readiness/markdown-source-endpoints.md](references/agent-readiness/markdown-source-endpoints.md) — Per-page Markdown source endpoints
- [references/agent-readiness/robots-for-ai-crawlers.md](references/agent-readiness/robots-for-ai-crawlers.md) — robots.txt for AI crawlers
- [references/agent-readiness/content-signals.md](references/agent-readiness/content-signals.md) — Content Signals in robots.txt
- [references/agent-readiness/web-bot-auth.md](references/agent-readiness/web-bot-auth.md) — Web Bot Auth
- [references/agent-readiness/stable-urls.md](references/agent-readiness/stable-urls.md) — Stable URLs
- [references/agent-readiness/structured-data-for-agents.md](references/agent-readiness/structured-data-for-agents.md) — Structured data for agents
- [references/agent-readiness/machine-readable-formats.md](references/agent-readiness/machine-readable-formats.md) — Machine-readable formats
- [references/agent-readiness/link-headers.md](references/agent-readiness/link-headers.md) — HTTP Link headers for discovery
- [references/agent-readiness/mcp-and-tool-discovery.md](references/agent-readiness/mcp-and-tool-discovery.md) — MCP and tool discovery
- [references/agent-readiness/a2a-agent-cards.md](references/agent-readiness/a2a-agent-cards.md) — A2A agent cards
- [references/agent-readiness/agent-skills-discovery.md](references/agent-readiness/agent-skills-discovery.md) — Agent Skills discovery
- [references/agent-readiness/dns-aid.md](references/agent-readiness/dns-aid.md) — DNS for AI Discovery
- [references/agent-readiness/nlweb.md](references/agent-readiness/nlweb.md) — NLWeb
- [references/agent-readiness/webmcp.md](references/agent-readiness/webmcp.md) — WebMCP
- [references/agent-readiness/schemamap.md](references/agent-readiness/schemamap.md) — Schemamap

### Performance (19)
- [references/performance/core-web-vitals.md](references/performance/core-web-vitals.md) — Core Web Vitals (LCP, INP, CLS)
- [references/performance/image-optimization.md](references/performance/image-optimization.md) — Image optimisation
- [references/performance/lazy-loading.md](references/performance/lazy-loading.md) — Lazy loading
- [references/performance/preload-prefetch-preconnect.md](references/performance/preload-prefetch-preconnect.md) — Preload, prefetch, preconnect
- [references/performance/cache-control.md](references/performance/cache-control.md) — Cache-Control headers
- [references/performance/no-vary-search.md](references/performance/no-vary-search.md) — No-Vary-Search
- [references/performance/compression.md](references/performance/compression.md) — Compression
- [references/performance/font-loading.md](references/performance/font-loading.md) — Web font loading
- [references/performance/critical-css.md](references/performance/critical-css.md) — Critical CSS
- [references/performance/script-loading.md](references/performance/script-loading.md) — Script loading
- [references/performance/http3.md](references/performance/http3.md) — HTTP/2 and HTTP/3
- [references/performance/speculation-rules.md](references/performance/speculation-rules.md) — Speculation Rules
- [references/performance/resource-hints.md](references/performance/resource-hints.md) — Resource hints overview
- [references/performance/view-transitions.md](references/performance/view-transitions.md) — View Transitions
- [references/performance/bfcache.md](references/performance/bfcache.md) — Back/forward cache
- [references/performance/visibility-aware-rendering.md](references/performance/visibility-aware-rendering.md) — Visibility-aware rendering
- [references/performance/css-containment.md](references/performance/css-containment.md) — CSS containment
- [references/performance/scroll-driven-animations.md](references/performance/scroll-driven-animations.md) — Scroll-driven animations
- [references/performance/scrollbar-gutter.md](references/performance/scrollbar-gutter.md) — Scrollbar gutter

### Privacy (6)
- [references/privacy/privacy-policy.md](references/privacy/privacy-policy.md) — Privacy policy
- [references/privacy/cookie-consent.md](references/privacy/cookie-consent.md) — Cookie consent
- [references/privacy/global-privacy-control.md](references/privacy/global-privacy-control.md) — Global Privacy Control (GPC)
- [references/privacy/third-party-scripts.md](references/privacy/third-party-scripts.md) — Third-party scripts and privacy
- [references/privacy/analytics-privacy.md](references/privacy/analytics-privacy.md) — Privacy-respecting analytics
- [references/privacy/data-minimization.md](references/privacy/data-minimization.md) — Data minimisation

### Resilience (5)
- [references/resilience/error-pages.md](references/resilience/error-pages.md) — Custom error pages (404, 500)
- [references/resilience/maintenance-pages.md](references/resilience/maintenance-pages.md) — Maintenance pages and 503
- [references/resilience/offline-support.md](references/resilience/offline-support.md) — Offline support and service workers
- [references/resilience/pwa-manifest.md](references/resilience/pwa-manifest.md) — Web app manifest
- [references/resilience/monitoring-uptime.md](references/resilience/monitoring-uptime.md) — Monitoring and uptime

### Internationalisation (12)
- [references/i18n/international-url-structure.md](references/i18n/international-url-structure.md) — International URL structure
- [references/i18n/hreflang.md](references/i18n/hreflang.md) — hreflang
- [references/i18n/localised-metadata.md](references/i18n/localised-metadata.md) — Localised page metadata
- [references/i18n/sitemap-hreflang.md](references/i18n/sitemap-hreflang.md) — hreflang in XML sitemaps
- [references/i18n/avoid-auto-geo-redirects.md](references/i18n/avoid-auto-geo-redirects.md) — Avoid automatic IP-based redirects
- [references/i18n/lang-attribute.md](references/i18n/lang-attribute.md) — lang attribute on inline content
- [references/i18n/language-switcher.md](references/i18n/language-switcher.md) — Language switcher
- [references/i18n/rtl-support.md](references/i18n/rtl-support.md) — RTL and bidirectional text
- [references/i18n/writing-modes.md](references/i18n/writing-modes.md) — Writing modes and CJK line breaking
- [references/i18n/locale-content.md](references/i18n/locale-content.md) — Locale-aware content
- [references/i18n/plural-rules.md](references/i18n/plural-rules.md) — Plural rules and grammatical number
- [references/i18n/idn-support.md](references/i18n/idn-support.md) — Internationalised Domain Names (IDN)
