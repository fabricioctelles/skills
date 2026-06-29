# Starlight & Common Patterns

## 1. Starlight Documentation Sites

### Setup

```bash
npm create astro@latest -- --template starlight
```

Or add to an existing Astro project:

```bash
npx astro add starlight
```

### Configuration

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://docs.example.com',
  integrations: [
    starlight({
      title: 'My Docs',
      defaultLocale: 'en',
      locales: {
        en: { label: 'English' },
        pt: { label: 'Português', lang: 'pt-BR' },
      },
      sidebar: [
        { label: 'Home', link: '/' },
        {
          label: 'Guides',
          items: [
            { slug: 'guides/getting-started' },
            { slug: 'guides/configuration' },
          ],
        },
        {
          label: 'Reference',
          autogenerate: { directory: 'reference' },
        },
      ],
      customCss: ['./src/styles/custom.css'],
    }),
  ],
});
```

### Sidebar Gotchas

**`link` and `items` are mutually exclusive.** A sidebar item is ONE of:

- `link` — a single URL (requires `label`)
- `slug` — reference to internal page (uses page title as label)
- `items` — array of child links/groups (requires `label`)
- `autogenerate` — auto-generates from a directory

```ts
// ❌ WRONG — cannot mix link with items
{ label: 'Guides', link: '/guides/', items: [...] }

// ✅ CORRECT — group with items
{ label: 'Guides', items: [{ slug: 'guides/intro' }] }

// ✅ CORRECT — single link
{ label: 'Guides', link: '/guides/' }
```

**Autogenerate limitations:**
- Only generates from files in `src/content/docs/<directory>/`
- Sorted alphabetically by filename (use numeric prefixes like `01-intro.md` to control order)
- Cannot filter files — all `.md`/`.mdx` in the directory are included
- Subfolders become nested groups automatically

### Built-in Components: Card vs LinkCard

| Component | Purpose | Required Props | Has `href`? | Accepts children? |
|-----------|---------|---------------|-------------|-------------------|
| `Card` | Display content in a styled box | `title` | ❌ NO | ✅ Yes |
| `LinkCard` | Prominent clickable link | `title`, `href` | ✅ YES | ❌ No |

```mdx
import { Card, LinkCard, CardGrid } from '@astrojs/starlight/components';

{/* Card — displays content, NOT a link */}
<Card title="Feature A" icon="star">
  Description of feature A goes here.
</Card>

{/* LinkCard — entire card is a clickable link */}
<LinkCard
  title="Getting Started"
  href="/guides/getting-started/"
  description="Learn how to set up your project."
/>

{/* Group in a grid */}
<CardGrid stagger>
  <Card title="Fast" icon="rocket">Built for speed.</Card>
  <Card title="Simple" icon="pencil">Easy to use.</Card>
</CardGrid>
```

### Component Overrides

Override any built-in Starlight UI component:

```js
// astro.config.mjs
starlight({
  components: {
    // Replace the SocialIcons component
    SocialIcons: './src/components/MyLinks.astro',
    // Replace the Header
    Header: './src/components/CustomHeader.astro',
  },
});
```

Reuse the built-in component inside your override:

```astro
---
// src/components/CustomHeader.astro
import Default from '@astrojs/starlight/components/Header.astro';
---
<Default><slot /></Default>
<div class="announcement-bar">New release available!</div>
```

Full list of overridable components: see [Overrides Reference](https://starlight.astro.build/reference/overrides/).

### Theming

Starlight uses a semantic color system via CSS custom properties. The naming is **counter-intuitive**:

| Variable | Meaning |
|----------|---------|
| `--sl-color-white` | **Foreground** (text) color |
| `--sl-color-black` | **Background** color |
| `--sl-color-gray-1` to `--sl-color-gray-6` | Gray scale (1 = lightest in dark mode) |
| `--sl-color-accent-low` | Accent background |
| `--sl-color-accent` | Accent mid (links, highlights) |
| `--sl-color-accent-high` | Accent foreground |

**You MUST define both `:root` (dark) and `:root[data-theme='light']` (light):**

```css
/* src/styles/custom.css */

/* Dark mode (default) */
:root {
  --sl-color-white: #ffffff;
  --sl-color-black: #181818;
  --sl-color-gray-1: #eee;
  --sl-color-gray-2: #c2c2c2;
  --sl-color-gray-3: #8b8b8b;
  --sl-color-gray-4: #585858;
  --sl-color-gray-5: #383838;
  --sl-color-gray-6: #272727;
  --sl-color-accent-low: #1a1047;
  --sl-color-accent: #8b5cf6;
  --sl-color-accent-high: #c4b5fd;
}

/* Light mode — invert the logic */
:root[data-theme='light'] {
  --sl-color-white: #181818;
  --sl-color-black: #ffffff;
  --sl-color-gray-1: #272727;
  --sl-color-gray-2: #383838;
  --sl-color-gray-3: #585858;
  --sl-color-gray-4: #8b8b8b;
  --sl-color-gray-5: #c2c2c2;
  --sl-color-gray-6: #eee;
  --sl-color-accent-low: #c4b5fd;
  --sl-color-accent: #6d28d9;
  --sl-color-accent-high: #1a1047;
}
```

**CSS Layer:** Starlight uses `@layer starlight` internally. Unlayered custom CSS automatically overrides it. For explicit layer control:

```css
@layer my-reset, starlight, my-overrides;

@layer my-overrides {
  :root {
    --sl-content-width: 50rem;
  }
}
```

### Versioned Docs with starlight-utils multiSidebar

```bash
npm install @lorenzo_lewis/starlight-utils
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightUtils from '@lorenzo_lewis/starlight-utils';

export default defineConfig({
  integrations: [
    starlight({
      title: 'My Docs',
      plugins: [
        starlightUtils({
          multiSidebar: {
            switcherStyle: 'dropdown',
          },
        }),
      ],
      sidebar: [
        // Each top-level group becomes a separate sidebar
        {
          label: 'v2',
          items: [{ autogenerate: { directory: 'v2' } }],
        },
        {
          label: 'v1',
          items: [{ autogenerate: { directory: 'v1' } }],
        },
      ],
    }),
  ],
});
```

---

## 2. Search (Pagefind)

### Install and Build

Pagefind indexes static HTML after build. Starlight includes Pagefind by default. For non-Starlight Astro sites:

```bash
npm install -D pagefind
```

Add to your build script in `package.json`:

```json
{
  "scripts": {
    "build": "astro build && npx pagefind --site dist"
  }
}
```

### Indexing Controls

```html
<!-- Only index content inside this element -->
<main data-pagefind-body>
  <h1>Indexed heading</h1>
  <p>This paragraph is searchable.</p>

  <!-- Exclude specific elements -->
  <nav data-pagefind-ignore>
    <p>This won't appear in search results.</p>
  </nav>

  <!-- Boost heading weight in results -->
  <h2 data-pagefind-weight="2">Important Section</h2>
</main>
```

| Attribute | Effect |
|-----------|--------|
| `data-pagefind-body` | Only index inside this element (page-level) |
| `data-pagefind-ignore` | Exclude element from indexing |
| `data-pagefind-ignore="all"` | Exclude element and all descendants |
| `data-pagefind-weight="N"` | Boost ranking (default: 1, higher = more relevant) |
| `data-pagefind-meta="key:value"` | Add metadata to search results |

### UI Component Integration

```astro
---
// src/pages/search.astro
---
<html>
<head>
  <link href="/pagefind/pagefind-ui.css" rel="stylesheet" />
</head>
<body>
  <div id="search"></div>
  <script>
    import '/pagefind/pagefind-ui.js';
    new PagefindUI({ element: '#search', showSubResults: true });
  </script>
</body>
</html>
```

### Pagefind vs Fuse.js Decision Table

| Criteria | Pagefind | Fuse.js |
|----------|----------|---------|
| Index size | Pre-built, loads fragments on demand | Entire index in memory |
| Best for | Static sites with 50+ pages | Small datasets (<100 items), dynamic data |
| Setup | Build step required | No build step, works at runtime |
| Fuzzy matching | Limited (typo tolerance) | Excellent (configurable threshold) |
| Performance | O(1) per query chunk (WASM) | Degrades with data size |
| Works offline | ✅ Yes | ✅ Yes |
| SSR compatible | ❌ No (needs static HTML) | ✅ Yes |
| Custom data | Indexes HTML only | Indexes any JSON array |
| Bundle size | ~50KB (WASM) + on-demand chunks | ~25KB + full index |

**Rule of thumb:** Use Pagefind for documentation/blog search. Use Fuse.js for in-page filtering (command palettes, dropdown search, dynamic lists).

---

## 3. SEO

> **Full reference:** see [SEO Full Stack](seo-full-stack.md) — covers `@jdevalk/astro-seo-graph`, JSON-LD graph, IndexNow, auto-generated OG images, agent discovery, performance SEO, and build-time validation.

Below is just the minimal setup for Starlight (which already includes automatic sitemap):

### Starlight SEO Basics

Starlight generates a sitemap automatically — just set `site` in your config. For RSS and custom meta tags in non-Starlight sites, see the full reference file.

```js
// astro.config.mjs — minimum for Starlight SEO
export default defineConfig({
  site: 'https://docs.example.com', // Required for sitemap and canonical
  integrations: [starlight({ title: 'My Docs' })],
});
```

---

## 4. i18n Patterns

### Configuration

```js
// astro.config.mjs
export default defineConfig({
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'pt-br', 'es'],
    routing: {
      prefixDefaultLocale: false, // /about (en), /pt-br/about, /es/about
    },
    fallback: {
      'pt-br': 'en',
      es: 'en',
    },
  },
});
```

For Starlight, i18n is configured inside the integration:

```js
starlight({
  defaultLocale: 'root',
  locales: {
    root: { label: 'English', lang: 'en' },
    'pt-br': { label: 'Português', lang: 'pt-BR' },
  },
});
```

### Content Collections per Locale

```
src/content/docs/
├── index.md           ← English (root locale)
├── guides/
│   └── intro.md
└── pt-br/
    ├── index.md       ← Portuguese
    └── guides/
        └── intro.md
```

### Fallback Strategy

Show default locale content with a banner when translation is missing:

```astro
---
// src/components/TranslationBanner.astro
import { getEntry } from 'astro:content';

const currentLocale = Astro.currentLocale ?? 'en';
const slug = Astro.params.slug;

// Check if translation exists
const localizedEntry = await getEntry('docs', `${currentLocale}/${slug}`);
const isFallback = !localizedEntry && currentLocale !== 'en';
---

{isFallback && (
  <aside class="translation-banner" role="alert">
    ⚠️ This page is not yet translated to {currentLocale}.
    Showing English version.
  </aside>
)}
```

In Starlight, fallback is automatic — missing translations show the `defaultLocale` content with a built-in notice.

### getRelativeLocaleUrl Helper

```astro
---
import { getRelativeLocaleUrl } from 'astro:i18n';

const locale = Astro.currentLocale ?? 'en';
---
<nav>
  <a href={getRelativeLocaleUrl(locale, 'about')}>About</a>
  <a href={getRelativeLocaleUrl(locale, 'guides/intro')}>Guide</a>
</nav>
```

---

## 5. Common Recipes

### Pagination

```astro
---
// src/pages/blog/[...page].astro
import { getCollection } from 'astro:content';
import type { GetStaticPaths } from 'astro';

const POSTS_PER_PAGE = 10;

export const getStaticPaths: GetStaticPaths = async ({ paginate }) => {
  const allPosts = await getCollection('blog');
  const sorted = allPosts.sort(
    (a, b) => b.data.publishDate.valueOf() - a.data.publishDate.valueOf()
  );
  return paginate(sorted, { pageSize: POSTS_PER_PAGE });
};

const { page } = Astro.props;
---
<h1>Blog — Page {page.currentPage}</h1>

<ul>
  {page.data.map((post) => (
    <li>
      <a href={`/blog/${post.id}/`}>{post.data.title}</a>
    </li>
  ))}
</ul>

<nav>
  {page.url.prev && <a href={page.url.prev}>← Previous</a>}
  <span>Page {page.currentPage} of {page.lastPage}</span>
  {page.url.next && <a href={page.url.next}>Next →</a>}
</nav>
```

### Tag/Category Archives

```astro
---
// src/pages/tags/[tag]/[...page].astro
import { getCollection } from 'astro:content';

export async function getStaticPaths({ paginate }) {
  const allPosts = await getCollection('blog');
  const allTags = [...new Set(allPosts.flatMap((post) => post.data.tags))];

  return allTags.flatMap((tag) => {
    const filtered = allPosts.filter((post) => post.data.tags.includes(tag));
    return paginate(filtered, {
      params: { tag },
      pageSize: 10,
    });
  });
}

const { page } = Astro.props;
const { tag } = Astro.params;
---
<h1>Posts tagged "{tag}"</h1>

<ul>
  {page.data.map((post) => (
    <li><a href={`/blog/${post.id}/`}>{post.data.title}</a></li>
  ))}
</ul>
```

Tag index page:

```astro
---
// src/pages/tags/index.astro
import { getCollection } from 'astro:content';

const allPosts = await getCollection('blog');
const tags = [...new Set(allPosts.flatMap((post) => post.data.tags))].sort();
---
<h1>All Tags</h1>
<ul>
  {tags.map((tag) => (
    <li><a href={`/tags/${tag}/1/`}>{tag}</a></li>
  ))}
</ul>
```

### Static Forms

**Formspree:**

```astro
<form action="https://formspree.io/f/{form_id}" method="POST">
  <label>
    Email
    <input type="email" name="email" required />
  </label>
  <label>
    Message
    <textarea name="message" required></textarea>
  </label>
  <button type="submit">Send</button>
</form>
```

**Netlify Forms:**

```astro
<form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact" />
  <p class="hidden"><input name="bot-field" /></p>
  <label>
    Email
    <input type="email" name="email" required />
  </label>
  <label>
    Message
    <textarea name="message" required></textarea>
  </label>
  <button type="submit">Send</button>
</form>
```

### Dark Mode Toggle

```astro
---
// src/components/ThemeToggle.astro
---
<button id="theme-toggle" aria-label="Toggle dark mode" type="button">
  <span class="sun">☀️</span>
  <span class="moon">🌙</span>
</button>

<script>
  const toggle = document.getElementById('theme-toggle')!;

  function getTheme(): 'light' | 'dark' {
    return (
      (localStorage.getItem('theme') as 'light' | 'dark') ??
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
    );
  }

  function setTheme(theme: 'light' | 'dark') {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem('theme', theme);
  }

  // Apply on load
  setTheme(getTheme());

  toggle.addEventListener('click', () => {
    setTheme(getTheme() === 'dark' ? 'light' : 'dark');
  });
</script>

<style>
  #theme-toggle {
    background: none;
    border: none;
    cursor: pointer;
    font-size: 1.25rem;
  }
  :root[data-theme='dark'] .sun { display: none; }
  :root[data-theme='light'] .moon { display: none; }
</style>
```

> **Note:** Starlight includes a built-in theme toggle. This pattern is for custom Astro sites.
