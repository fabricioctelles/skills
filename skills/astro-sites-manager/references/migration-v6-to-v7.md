# Migration Guide: Astro v6 → v7

> Official reference: https://docs.astro.build/en/guides/upgrade-to/v7/

---

## 1. Pre-Migration Checklist

- [ ] **Backup** — commit all changes, create a branch: `git checkout -b feat/astro-v7-upgrade`
- [ ] **Node.js ≥ 22** — required (v22.5.0+ for `node:sqlite` if replacing `@astrojs/db`)
  ```bash
  node -v  # must be >= 22
  ```
- [ ] **Audit dependencies** — check for packages that depend on Vite internals or the Go compiler
  ```bash
  npx astro info
  ```
- [ ] **Review remark/rehype plugins** — if you have any, plan for Sätteri migration or `@astrojs/markdown-remark` fallback
- [ ] **Check for `src/fetch.ts`** — if this file exists for non-routing purposes, plan a rename
- [ ] **Check for `@astrojs/db`** usage — plan a replacement (Drizzle, node:sqlite, Turso, Neon)

---

## 2. Upgrade Commands

```bash
# npm
npx @astrojs/upgrade

# pnpm
pnpm dlx @astrojs/upgrade

# yarn
yarn dlx @astrojs/upgrade
```

This upgrades Astro and all official integrations together. For manual control:

```bash
npm install astro@latest
npm install @astrojs/react@latest @astrojs/mdx@latest  # repeat for each integration
```

---

## 3. Breaking Changes

### 3.1 Vite 8

Astro v7 upgrades to [Vite 8](https://vite.dev/blog/announcing-vite8). The main impact is on **custom Vite plugins** and projects using Vite internals directly.

Key Vite 8 changes:
- **esbuild → Rolldown** as the production bundler (Rolldown is a Rust-based Rollup replacement)
- Plugin API surface changes — check the [Vite 8 migration guide](https://vite.dev/guide/migration)

**What to do:**
- If you have custom Vite plugins in `astro.config.mjs`, verify they work with Vite 8
- If you use `esbuild`-specific options (e.g. `esbuild.target`, `esbuild.jsxFactory`), check if they still apply under Rolldown

```js
// Before: esbuild-specific config (may need review)
export default defineConfig({
  vite: {
    esbuild: {
      target: 'esnext',
      jsxFactory: 'h',
    },
  },
});

// After: verify compatibility — most configs carry over, but test your build
export default defineConfig({
  vite: {
    // Rolldown handles bundling; esbuild options may behave differently
    // Test `astro build` and check output
  },
});
```

> **Most Astro users need no changes.** This primarily affects integration authors and projects with custom Vite plugins.

---

### 3.2 Rust Compiler

The Rust-based compiler is now the **default and only compiler**, replacing the Go-based compiler. It is stricter about HTML syntax.

#### Unclosed tags now produce errors

```astro
<!-- Before: Go compiler silently accepted this -->
<p>Hello world

<!-- After: Rust compiler requires closing tags -->
<p>Hello world</p>
```

```astro
---
import Layout from '../layouts/Layout.astro';
---

<!-- Before: unclosed component tag accepted -->
<Layout>
  <p>Content here

<!-- After: all tags must be closed -->
<Layout>
  <p>Content here</p>
</Layout>
```

> **Void elements** (`<br>`, `<img>`, `<input>`, `<hr>`) do NOT need closing tags.

#### No HTML auto-correction

The Go compiler silently reordered invalid HTML (e.g. `<div>` inside `<p>`). The Rust compiler passes markup through as-is.

```astro
<!-- Before: compiler restructured this silently -->
<p>
  <div>Block inside paragraph</div>
</p>

<!-- After: browser handles it (will close <p> early, breaking layout) -->
<!-- Fix: use valid nesting -->
<div>
  <div>Block content here</div>
</div>
```

#### JSX whitespace handling

See [Section 3.5 compressHTML](#35-compresshtml-jsx-is-new-default) for the related whitespace changes.

#### CSS output differences (cosmetic, no action needed)

- Named colors may become hex: `rebeccapurple` → `#639`
- `url()` values may gain/lose quotes: `url(/path)` ↔ `url('/path')`

---

### 3.3 Reserved File Name: `src/fetch.ts`

`src/fetch.ts` (or `.js`) is now reserved for [advanced routing](https://docs.astro.build/en/guides/routing/#advanced-routing) configuration.

```js
// Before: you had src/fetch.ts for custom fetch logic
// src/fetch.ts — your custom utility
export function fetchData() { /* ... */ }

// After: Option A — rename your file
// src/fetcher.ts (or src/api-client.ts, etc.)
export function fetchData() { /* ... */ }
// Update all imports:
// import { fetchData } from '../fetch' → import { fetchData } from '../fetcher'
```

```js
// After: Option B — disable advanced routing in astro.config.mjs
import { defineConfig } from 'astro/config';

export default defineConfig({
  fetchFile: null, // disables advanced routing, keeps your src/fetch.ts
});
```

```js
// After: Option C — point fetchFile elsewhere
import { defineConfig } from 'astro/config';

export default defineConfig({
  fetchFile: './src/router.ts', // use a different file for advanced routing
});
```

---

### 3.4 New Default Markdown Processor: Sätteri

[Sätteri](https://satteri.bruits.org/) replaces the remark/rehype (unified) pipeline as the default Markdown processor. `@astrojs/markdown-remark` is no longer installed by default.

**If you DON'T use remark/rehype plugins:** no action needed. Sätteri applies GFM and SmartyPants like before.

**If you DO use remark/rehype plugins:**

```bash
# Install the unified pipeline package
npm install @astrojs/markdown-remark
```

```js
// Before: plugins configured directly (worked because unified was the default)
import { defineConfig } from 'astro/config';
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';

export default defineConfig({
  markdown: {
    remarkPlugins: [remarkToc],
    rehypePlugins: [rehypeSlug],
  },
});

// After: explicitly set unified() as processor + install @astrojs/markdown-remark
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';

export default defineConfig({
  markdown: {
    processor: unified({
      remarkPlugins: [remarkToc],
      rehypePlugins: [rehypeSlug],
    }),
  },
});
```

**Alternative:** Port your plugins to Sätteri MDAST/HAST plugins:

```js
// Using Sätteri with its native plugin model
import { defineConfig } from 'astro/config';
import { satteri } from '@astrojs/markdown-satteri';
import { myMdastPlugin } from './my-satteri-plugin.mjs';

export default defineConfig({
  markdown: {
    processor: satteri({
      mdastPlugins: [myMdastPlugin()],
      features: { directive: true },
    }),
  },
});
```

---

### 3.5 `compressHTML: 'jsx'` is New Default

Whitespace between inline elements is now stripped using JSX rules (like React), instead of HTML-aware compression.

```astro
<!-- Before (v6): renders as "hello world" (space preserved) -->
<span>hello</span>
<em>world</em>

<!-- After (v7): renders as "helloworld" (space removed) -->
<span>hello</span>
<em>world</em>
```

**Fix: add explicit space with `{' '}`:**

```astro
<!-- After: explicit space between inline elements -->
<span>hello</span>{' '}<em>world</em>
```

**Or revert to v6 behavior globally:**

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';

export default defineConfig({
  compressHTML: true, // v6 HTML-aware behavior
  // compressHTML: false  // preserve ALL whitespace
});
```

---

## 4. Deprecated

### `getContainerRenderer()` from package root

Importing `getContainerRenderer()` from the integration's package root is deprecated. Use the dedicated `/container-renderer` entrypoint.

```js
// Before
import { getContainerRenderer } from '@astrojs/react';

// After
import { getContainerRenderer } from '@astrojs/react/container-renderer';
```

Available for: `@astrojs/react`, `@astrojs/preact`, `@astrojs/solid-js`, `@astrojs/svelte`, `@astrojs/vue`, `@astrojs/mdx`.

---

## 5. Removed

### 5.1 `@astrojs/db`

The package is removed and no longer maintained. Replace with:

| Alternative | Use case |
|---|---|
| `node:sqlite` | Node.js adapter, local SQLite (Node ≥ 22.5.0) |
| [Drizzle ORM](https://orm.drizzle.team/) | Schema-based queries with any DB |
| [Turso](https://turso.tech/) | Edge SQLite (libSQL) |
| [Neon](https://neon.tech/) | Serverless Postgres |

```bash
# Remove
npm uninstall @astrojs/db
```

```js
// Before: @astrojs/db
import { db, sql } from 'astro:db';
const results = await db.select().from(Posts).all();

// After: Drizzle ORM example
import { drizzle } from 'drizzle-orm/node-postgres';
import { posts } from './schema';
const db = drizzle(process.env.DATABASE_URL);
const results = await db.select().from(posts);
```

Remove `db` from `astro.config.mjs` integrations array and delete `db/` config files.

---

### 5.2 `astro:transitions` Internals

The following exports are removed:

| Removed API | Replacement |
|---|---|
| `TRANSITION_BEFORE_PREPARATION` | `'astro:before-preparation'` |
| `TRANSITION_AFTER_PREPARATION` | `'astro:after-preparation'` |
| `TRANSITION_BEFORE_SWAP` | `'astro:before-swap'` |
| `TRANSITION_AFTER_SWAP` | `'astro:after-swap'` |
| `TRANSITION_PAGE_LOAD` | `'astro:page-load'` |
| `isTransitionBeforePreparationEvent()` | `event.type === 'astro:before-preparation'` |
| `isTransitionBeforeSwapEvent()` | `event.type === 'astro:before-swap'` |
| `createAnimationScope()` | Remove entirely |

```js
// Before
import {
  TRANSITION_AFTER_SWAP,
  isTransitionBeforePreparationEvent,
} from 'astro:transitions/client';

document.addEventListener(TRANSITION_AFTER_SWAP, (event) => {
  if (isTransitionBeforePreparationEvent(event)) { /* ... */ }
});

// After
document.addEventListener('astro:after-swap', (event) => {
  if (event.type === 'astro:before-preparation') { /* ... */ }
});
```

---

## 6. Experimental Flags to Remove (Now Stable)

Remove these from your `astro.config.mjs` `experimental` block:

| Flag | Status in v7 |
|---|---|
| `experimental.logger` | Stable — use top-level `logger` field |
| `experimental.queuedRendering` | Default behavior — just remove |
| `experimental.rustCompiler` | Default and only compiler — just remove |
| `experimental.advancedRouting` | Default — just remove (note: `src/fetch.ts` is now reserved) |
| `experimental.cache` | Stable — move to top-level `cache` field |
| `experimental.routeRules` | Stable — move to top-level `routeRules` field |

```js
// Before
import { defineConfig, logHandlers, memoryCache } from 'astro/config';

export default defineConfig({
  experimental: {
    logger: logHandlers.json({ pretty: true }),
    queuedRendering: { enabled: true },
    rustCompiler: true,
    advancedRouting: true,
    cache: { provider: memoryCache() },
    routeRules: {
      '/blog/[...path]': { maxAge: 300, swr: 60 },
    },
  },
});

// After
import { defineConfig, logHandlers, memoryCache } from 'astro/config';

export default defineConfig({
  logger: logHandlers.json({ pretty: true }),
  cache: { provider: memoryCache() },
  routeRules: {
    '/blog/[...path]': { maxAge: 300, swr: 60 },
  },
});
```

---

## 7. Post-Migration Validation

Run these steps after upgrading:

```bash
# 1. Install dependencies
npm install

# 2. Run the dev server — check for compiler errors
npm run dev

# 3. Run a full production build
npm run build

# 4. Preview the production build
npm run preview

# 5. Check for visual regressions (especially whitespace issues from compressHTML)
# Open key pages and inspect inline element spacing

# 6. Run tests if you have them
npm test

# 7. Check TypeScript
npx astro check
```

**What to look for:**
- ❌ Compiler errors about unclosed tags → add missing closing tags
- ❌ Layout shifts or broken nesting → fix invalid HTML (block elements inside `<p>`, etc.)
- ❌ Missing spaces between inline elements → add `{' '}` where needed
- ❌ Markdown rendering issues → install `@astrojs/markdown-remark` if using remark/rehype plugins
- ❌ Build errors mentioning `src/fetch.ts` → rename or set `fetchFile: null`
- ❌ Import errors for `@astrojs/db` → replace with alternative DB solution
- ❌ Import errors for `TRANSITION_*` constants → use event name strings directly

---

## Quick Reference: Search & Replace

| Find | Replace with |
|---|---|
| `from '@astrojs/react'` (for getContainerRenderer) | `from '@astrojs/react/container-renderer'` |
| `TRANSITION_BEFORE_PREPARATION` | `'astro:before-preparation'` |
| `TRANSITION_AFTER_PREPARATION` | `'astro:after-preparation'` |
| `TRANSITION_BEFORE_SWAP` | `'astro:before-swap'` |
| `TRANSITION_AFTER_SWAP` | `'astro:after-swap'` |
| `TRANSITION_PAGE_LOAD` | `'astro:page-load'` |
| `isTransitionBeforePreparationEvent(e)` | `e.type === 'astro:before-preparation'` |
| `isTransitionBeforeSwapEvent(e)` | `e.type === 'astro:before-swap'` |
| `createAnimationScope` | (remove entirely) |
| `experimental.rustCompiler` | (remove) |
| `experimental.queuedRendering` | (remove) |
| `experimental.advancedRouting` | (remove) |

---

## Ecosystem Compatibility (learned from real upgrades)

### Starlight 0.40+ Sidebar Schema Change

Starlight 0.40 (required for Astro v7) changed the sidebar schema. `autogenerate` can no longer be a direct property of a sidebar group — it must be inside `items`:

```javascript
// BEFORE (Starlight 0.38):
{ label: 'Reference', autogenerate: { directory: 'reference' } }

// AFTER (Starlight 0.40):
{ label: 'Reference', items: [{ autogenerate: { directory: 'reference' } }] }
```

### astro-mermaid — Incompatible with v7

`astro-mermaid` (all versions through 2.0.4) uses `isUnifiedProcessor()` which was removed in Astro v7. Replace with Mermaid CDN client-side script:

```javascript
// In Starlight head config or Layout.astro:
{
  tag: 'script',
  attrs: { type: 'module' },
  content: `
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
    mermaid.initialize({ startOnLoad: false });
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('pre > code.language-mermaid').forEach((el) => {
        const pre = el.parentElement;
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = el.textContent;
        pre.replaceWith(div);
      });
      mermaid.run();
    });
  `,
}
```

### Docker Alpine — Sätteri native binding missing

Sätteri only ships `linux-x64-gnu` (glibc). Alpine uses musl. Build stage MUST use `node:22-slim`:

```dockerfile
FROM node:22-slim AS build  # NOT alpine
```

### .npmrc required in Dockerfile

Astro v7 with Starlight plugins causes peer dependency conflicts. The `.npmrc` with `legacy-peer-deps=true` must be copied into Docker:

```dockerfile
COPY package*.json .npmrc ./
RUN npm ci
```

### @astrojs/node Must Be v11 for Astro v7

`@astrojs/node@10` builds fine but **crashes at runtime** with Astro v7:

```
TypeError: app.getAdapterLogger is not a function
    at createAppHandler (dist/server/entry.mjs)
```

The build succeeds, the image is created, the container starts — then immediately exits. Coolify shows `restarting:unknown` or `exited:unhealthy`.

**Fix:** Always upgrade `@astrojs/node` alongside Astro:
```bash
npm install astro@latest @astrojs/node@latest @astrojs/mdx@latest
```

**Required versions for v7:**
| Package | Minimum |
|---------|---------|
| `astro` | `^7.0.0` |
| `@astrojs/node` | `^11.0.0` |
| `@astrojs/mdx` | `^7.0.0` |
| `@astrojs/sitemap` | `^3.7.2` (unchanged) |

### pnpm 11.9+ — approve-builds Required in Docker

pnpm 11.9 blocks postinstall scripts by default. `esbuild` and `sharp` need native compilation after install. Without approval the Docker build fails:

```
[ERR_PNPM_IGNORED_BUILDS] Ignored build scripts: esbuild@0.28.1, sharp@0.34.5
```

**Fix:** Run `pnpm approve-builds` locally (generates `pnpm-workspace.yaml`), then copy it in Docker:

```dockerfile
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./
RUN pnpm install --frozen-lockfile
```
