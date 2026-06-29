---
name: astro-sites-manager
description: >
  Comprehensive skill for building, migrating, and maintaining Astro v7
  projects. Covers best practices from the official AGENTS.md, the v6→v7
  migration path, validation of breaking/deprecated patterns, AI-enhanced dev
  server usage (background mode, JSON logging), advanced routing with
  src/fetch.ts, route caching, Sätteri Markdown, and the Rust compiler. Use
  when the user mentions 'Astro', '.astro files', 'astro dev', 'astro build',
  'islands architecture', 'content collections', 'SSG', 'SSR adapter',
  'upgrade to Astro 7', 'migrate Astro', 'Astro v7', 'Astro v6', 'Sätteri',
  'route caching', 'Astro.cache', 'astro dev --background', 'src/fetch.ts',
  'advanced routing', 'Hono + Astro', 'Rolldown', 'Vite 8', 'queued
  rendering', 'CDN cache provider', 'Astro AI', or asks about static site
  generation with Astro.
metadata:
  author: ft.ia.br
  version: "1.0.0"
  date: 2026-06-22
  repository: https://github.com/fabriciotelles/skills
  license: Apache-2.0
  category: ci-cd-and-deployment
---

# Astro Framework — v7

## MCP Documentation Access

This skill works alongside the **Astro Docs MCP server**. Before answering Astro questions, check if the `astro-docs` MCP tool is available and query it for the latest documentation. The MCP server provides real-time access to docs.astro.build and is the single source of truth for current APIs.

```
MCP Server: astro-docs
Tool: search_astro_docs
```

If the MCP server is unavailable, fall back to the reference material in this skill and https://docs.astro.build.

---

## Best Practices

### Component Design
- One `.astro` component per file. Keep components small and focused.
- Use frontmatter (`---`) for data fetching and logic; template below for markup only.
- Prefer Astro components over framework components unless client interactivity is needed.
- Use `client:*` directives sparingly — each adds JavaScript to the bundle.
- Directive hierarchy: `client:idle` > `client:visible` > `client:load` (prefer lazy).

### Routing & Pages
- Use file-based routing in `src/pages/`. Dynamic routes: `[slug].astro`, `[...path].astro`.
- Always export `getStaticPaths()` for prerendered dynamic routes.
- For SSR pages: `export const prerender = false` at the top.
- Use `src/fetch.ts` (v7) only when you need control beyond middleware — don't use it for simple auth.

### Content Collections
- Define schemas in `content.config.ts` with Zod — never trust untyped content.
- Use `getCollection()` for lists, `getEntry()` for single items.
- Prefer `glob()` loader for local files, custom loaders for CMS data.

### Performance
- Default to static (`prerender = true`). Use SSR only for personalized/dynamic content.
- Use `<Image />` from `astro:assets` — never raw `<img>` for local images.
- Prefer Sätteri (default v7) over unified for Markdown — it's significantly faster.
- Use Server Islands (`server:defer`) for mixing static shells with dynamic fragments.

### Styling
- Scoped `<style>` in `.astro` files is default and preferred.
- Use `is:global` only when truly needed (third-party component styling).
- Tailwind: install with `astro add tailwind`, don't configure manually.

### TypeScript
- Run `astro sync` after changing content schemas or env variables.
- Run `astro check` before committing — catches template type errors other tools miss.
- Use `astro:env/server` and `astro:env/client` for typed env variables (never `process.env` directly).

### Development Workflow
- Use `astro dev` for HMR. Never use `python -m http.server` or other static servers.
- Use `astro add` for official integrations — don't manually edit config for them.
- Use `astro build && astro preview` to test production behavior locally.
- In AI agent workflows: use `astro dev --background` and validate via `/_astro/status`.

---

## CLI Commands

```bash
npx astro dev              # Dev server (foreground)
npx astro dev --background # Dev server (detached, for AI agents)
npx astro dev --json       # Dev server with JSON structured logs
npx astro build            # Production build
npx astro preview          # Serve production build locally
npx astro check            # Type checking and diagnostics
npx astro sync             # Generate TypeScript types
npx astro add <integration># Install and configure integration
```

### Background Dev Server (AI Agents)

When working as an AI agent, use background mode:

```bash
# Start (blocks until ready, then detaches)
astro dev --background
# → Dev server running at http://localhost:4321 (pid 12345)

# Check status
astro dev status

# Read logs
astro dev logs

# Stop
astro dev stop

# Health check endpoint (JSON)
curl http://localhost:4321/_astro/status
# → {"ok": true}
```

**Key behaviors:**
- Lockfile prevents duplicate instances — starting again returns existing instance
- All commands are idempotent (stop when not running = silent success)
- Auto-detected when running inside an AI agent (no flag needed)
- Opt out: `ASTRO_DEV_BACKGROUND=0 astro dev`

---

## Project Structure

```
src/
├── pages/          # File-based routing (.astro, .md, .mdx)
├── layouts/        # Reusable page layouts
├── components/     # Astro & framework components
├── content/        # Content collections (type-safe)
├── middleware.ts   # Request middleware
├── fetch.ts        # Advanced routing (v7, optional)
├── styles/         # Global CSS
├── assets/         # Optimized assets (images, fonts)
├── actions/        # Server actions
└── env.d.ts        # Environment type declarations
astro.config.mjs    # Main configuration
content.config.ts   # Content collection schemas
tsconfig.json       # TypeScript config
```

---

## Configuration (v7)

```typescript
import { defineConfig, memoryCache, logHandlers } from 'astro/config';

export default defineConfig({
  // Output mode
  output: 'static', // or configure per-page with server adapter

  // Route caching (stable in v7)
  cache: {
    provider: memoryCache(),
  },
  routeRules: {
    '/blog/[...path]': { maxAge: 300, swr: 60 },
  },

  // Logger (stable in v7)
  logger: logHandlers.json(), // or .console(), or .compose(...)

  // Markdown (Sätteri is default in v7)
  markdown: {
    // No config needed for defaults (GFM, smartypants, heading IDs)
    // For extra features:
    // processor: satteri({ features: { directive: true, math: true } })
  },

  // Advanced routing file (default: src/fetch.ts)
  // fetchFile: null, // disable if src/fetch.ts is used for other purposes

  // Whitespace (v7 default: 'jsx')
  compressHTML: 'jsx', // or true (v6 behavior), or false (preserve all)
});
```

---

## Islands Architecture (client:* directives)

```astro
<!-- Load immediately (interactive above the fold) -->
<Counter client:load />

<!-- Load when browser is idle (non-critical interactivity) -->
<Newsletter client:idle />

<!-- Load when scrolled into viewport (below the fold) -->
<Comments client:visible />

<!-- Load on media query match (mobile-only widget) -->
<MobileMenu client:media="(max-width: 768px)" />

<!-- Client-only, skip SSR entirely (browser APIs needed) -->
<MapWidget client:only="react" />

<!-- Server Island: static shell, fetched at request time (v6+) -->
<UserGreeting server:defer />
```

**Decision guide:** No directive (default) = zero JS, static HTML. Add directive only when user interaction is required.

---

## Image Optimization

```astro
---
import { Image } from 'astro:assets';
import heroImage from '../assets/hero.jpg';
---
<!-- Local image (optimized, lazy-loaded, responsive) -->
<Image src={heroImage} alt="Hero" width={1200} />

<!-- Remote image (must allowlist domain in config) -->
<Image src="https://cdn.example.com/photo.jpg" alt="Photo" width={800} height={600} />
```

Config for remote images:
```typescript
// astro.config.mjs
image: {
  domains: ['cdn.example.com'],
  remotePatterns: [{ protocol: 'https', hostname: '**.cloudinary.com' }],
}
```

---

## Detailed References

- [Install MCP Server](references/install-mcp.md) — Setup Astro Docs MCP for any AI tool (Kiro, Claude, Cursor, VS Code, etc.)
- [Migration Guide v6→v7](references/migration-v6-to-v7.md) — Step-by-step upgrade plan with breaking changes checklist
- [Validation Checklist](references/validation-checklist.md) — Verify installation, detect breaking/deprecated patterns
- [AI Dev Server](references/ai-dev-server.md) — Background mode, JSON logging, agent detection
- [Astro v7 Features](references/v7-features.md) — Rust compiler, Sätteri, Advanced Routing, Route Caching, CDN providers
- [Astro v6 Features](references/v6-features.md) — Content Collections v2, Actions, Sessions, Server Islands, env module
- [Testing](references/testing.md) — Vitest components, Playwright E2E, link checking, CI pipeline
- [SEO Full Stack](references/seo-full-stack.md) — JSON-LD graph, agent discovery, IndexNow, OG images, build-time validation, performance
- [Starlight & Patterns](references/starlight-and-patterns.md) — Docs sites, Pagefind search, i18n, pagination, RSS
- [Deployment](references/deployment.md) — Cloudflare, Vercel, Netlify, Firebase, GitHub Pages, Docker/Coolify, Azure
- [Coolify Deploy](references/coolify-deploy.md) — Self-hosted deploy on Coolify (Dockerfile, API, gotchas, recommended stack)
