# SEO Full Stack for Astro

Complete reference for implementing technical SEO, structured data, agent discovery, and performance in Astro sites. Based on the `@jdevalk/astro-seo-graph` stack + complementary patterns.

> **Sources:** [Astro SEO: the definitive guide](https://joost.blog/astro-seo-complete-guide/) by Joost de Valk + official [astro-seo-graph](https://github.com/jdevalk/seo-graph/tree/main/packages/astro-seo-graph) documentation.

---

## 1. Installation

```bash
pnpm add @jdevalk/astro-seo-graph @jdevalk/seo-graph-core
```

`@jdevalk/seo-graph-core` is a transitive dep, but depending on it explicitly lets you pin the version and import piece builders directly.

---

## 2. `<Seo>` Component — Unified Head Metadata

A single component replaces all manual `<head>` management:

```astro
---
import Seo from '@jdevalk/astro-seo-graph/Seo.astro';
---

<Seo
    title="My Post | My Site"
    description="A concise description for search engines."
    canonical="https://example.com/my-post/"
    ogType="article"
    ogImage="https://example.com/og/my-post.jpg"
    ogImageAlt="My Post"
    ogImageWidth={1200}
    ogImageHeight={675}
    siteName="My Site"
    twitter={{ card: 'summary_large_image', site: '@handle' }}
    article={{ publishedTime: publishDate, tags: ['Astro', 'SEO'] }}
    graph={graph}
    extraLinks={[
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'sitemap', href: '/sitemap-index.xml' },
        { rel: 'alternate', type: 'application/rss+xml', href: '/feed.xml', title: 'RSS' },
    ]}
/>
```

### Automatic behaviors

- **Canonical** derived from Astro's `site` config, query params stripped by default (UTMs don't create duplicates)
- **Robots** always includes `max-snippet:-1`, `max-image-preview:large`, `max-video-preview:-1`
- **Canonical omitted when `noindex: true`** (per Google's recommendation)
- **Duplicate Twitter tags suppressed** — Twitter falls back to OG automatically
- **hreflang alternates** with BCP 47 normalization and automatic `x-default`
- **`og:locale:alternate`** emitted automatically from the `alternates` prop

---

## 3. Connected JSON-LD Graph (`@graph`)

A standalone `BlogPosting` isn't enough. The goal is an interlinked graph via `@id`:

```typescript
// src/utils/schema.ts
import {
    buildWebSite, buildBlog, buildPerson,
    buildWebPage, buildArticle, buildBreadcrumbList,
    makeIds,
} from '@jdevalk/seo-graph-core';

const SITE_URL = 'https://example.com';
const ids = makeIds({ siteUrl: SITE_URL });

export function buildBlogPostGraph(post: { title: string; url: string; publishDate: Date; description: string }) {
    return {
        '@context': 'https://schema.org',
        '@graph': [
            buildWebSite({
                url: SITE_URL,
                name: 'My Site',
                publisher: { '@id': ids.person },
                potentialAction: {
                    '@type': 'SearchAction',
                    target: { '@type': 'EntryPoint', urlTemplate: `${SITE_URL}/search?q={search_term_string}` },
                    'query-input': 'required name=search_term_string',
                },
            }, ids),
            buildBlog({ url: `${SITE_URL}/blog/`, name: 'Blog', publisher: { '@id': ids.person } }, ids),
            buildPerson({
                url: SITE_URL,
                name: 'Your Name',
                knowsAbout: ['Astro', 'SEO', 'Web Development'],
                sameAs: ['https://github.com/your-user', 'https://linkedin.com/in/your-user'],
            }, ids),
            buildWebPage({
                url: post.url,
                name: post.title,
                isPartOf: { '@id': ids.website },
                breadcrumb: { '@id': ids.breadcrumb(post.url) },
                datePublished: post.publishDate,
            }, ids),
            buildArticle({
                url: post.url,
                isPartOf: { '@id': ids.webPage(post.url) },
                author: { '@id': ids.person },
                publisher: { '@id': ids.person },
                headline: post.title,
                description: post.description,
                datePublished: post.publishDate,
            }, ids, 'BlogPosting'),
        ],
    };
}
```

### Trust Signals in the Schema

Include these to strengthen authority:

| Property | Where | Purpose |
|---|---|---|
| `publishingPrinciples` | `WebSite` / `Person` | Editorial policy |
| `copyrightHolder` + `copyrightYear` | `WebPage` | Copyright ownership |
| `knowsAbout` | `Person` | Topical authority |
| `SearchAction` | `WebSite` | Tells agents how to search the site |
| `sameAs` | `Person` / `Organization` | Social profiles = identity verification |

### `articleBody` in Schema

Include full text (up to 10K chars) so agents can access content via structured data without scraping:

```typescript
buildArticle({
    // ...
    articleBody: post.bodyText.slice(0, 10000),
}, ids, 'BlogPosting'),
```

---

## 4. Breadcrumbs Linked to the Graph

```typescript
import { breadcrumbsFromUrl } from '@jdevalk/astro-seo-graph';
import { buildBreadcrumbList, makeIds } from '@jdevalk/seo-graph-core';

const ids = makeIds({ siteUrl: 'https://example.com' });

const items = breadcrumbsFromUrl({
    url: Astro.url,
    siteUrl: 'https://example.com',
    pageName: post.data.title,
    names: { blog: 'Blog', category: 'Category' },
});

const breadcrumb = buildBreadcrumbList({ url: Astro.url.href, items }, ids);
```

Each breadcrumb item can reference a graph entity via `@id`, communicating the structural relationship between page and section.

---

## 5. Content Schema Validation (Zod)

```typescript
// src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { seoSchema, imageSchema } from '@jdevalk/astro-seo-graph';

const blog = defineCollection({
    schema: ({ image }) => z.object({
        title: z.string(),
        publishDate: z.coerce.date(),
        featureImage: imageSchema(image).optional(),
        seo: seoSchema(image).optional(),
    }),
});
```

- `seoSchema` validates title (5–120 chars) and description (15–160 chars) — build fails if outside limits
- `imageSchema` requires `alt` — image without alt won't compile

---

## 6. Build-Time Validation

```typescript
// astro.config.mjs
import seoGraph from '@jdevalk/astro-seo-graph/integration';

export default defineConfig({
    integrations: [
        seoGraph({
            // All enabled by default:
            validateH1: true,                  // 0 or >1 H1 = warning
            validateUniqueMetadata: true,      // Duplicate title/desc across pages
            validateImageAlt: true,            // <img> without alt
            validateMetadataLength: {          // SERP-safe bounds
                title: { min: 30, max: 65 },
                description: { min: 70, max: 200 },
            },
            validateInternalLinks: {           // Broken internal links or missing trailing slash
                skip: (href) => href.startsWith('/api/'),
            },
        }),
    ],
});
```

### What each validation catches:

- **H1**: Templates with duplicate or missing H1
- **Duplicates**: Paginated pages sharing the same title (corpus-level bug)
- **Alt text**: Images missed over the years
- **Meta length**: Titles truncated in SERP or invisible descriptions
- **Internal links**: `/about-me` without trailing slash that works via 301 but wastes a round-trip

### CI: External Broken Link Checker

For external links (internal validation doesn't cover), use [lychee](https://github.com/lycheeverse/lychee-action) in GitHub Actions:

```yaml
# .github/workflows/links.yml
name: Check Links
on:
  push:
    paths: ['src/content/**']
  schedule:
    - cron: '0 6 * * 1' # Weekly for link rot

jobs:
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v2
        with:
          args: --verbose --no-progress 'src/content/**/*.md'
```

---

## 7. Advanced Sitemaps

### Per-Collection with chunks

```typescript
import sitemap from '@astrojs/sitemap';

sitemap({
    entryLimit: 1000,
    chunks: {
        posts: (item) => {
            if (/^\/blog\/[^/]+/.test(new URL(item.url).pathname)) return item;
        },
        pages: (item) => item, // default bucket
    },
});
```

Produces: `sitemap-posts-0.xml`, `sitemap-pages-0.xml` — makes debugging easier in Google Search Console.

### Git-based lastmod

```typescript
import { gitLastmod } from '@jdevalk/astro-seo-graph';

// In the sitemap serialize callback:
serialize(item) {
    const filePath = urlToFilePath(item.url); // your logic
    const lastmod = gitLastmod(filePath, {
        excludeCommits: ['abc1234'], // bulk imports that don't count
    });
    return { ...item, lastmod: lastmod ?? item.lastmod };
}
```

`gitLastmod` uses `git log` for the real timestamp of the last commit that touched the file — doesn't depend on filesystem `mtime` (which resets on CI).

---

## 8. IndexNow — Active Notification

IndexNow notifies Bing, Yandex, and others that URLs changed, instead of waiting for passive crawl.

### Configuration

```typescript
// astro.config.mjs
seoGraph({
    indexNow: {
        key: process.env.INDEXNOW_KEY!,
        host: 'example.com',
        siteUrl: 'https://example.com',
        filter: (url) => !/^\/blog\/\d+\/$/.test(new URL(url).pathname), // Exclude pagination
    },
});
```

### Key Route (ownership verification)

```typescript
// src/pages/[your-key-here].txt.ts
import { createIndexNowKeyRoute } from '@jdevalk/astro-seo-graph';

export const GET = createIndexNowKeyRoute({ key: 'your-key-here' });
```

### Deploy order matters

1. Deploy the key route first
2. Confirm `https://example.com/your-key.txt` returns 200
3. Only then enable `indexNow` in the integration

> Submissions before the key is reachable = HTTP 403 and key permanently invalidated.

### Direct IndexNow API

For manual or custom submission:

```bash
# Single URL
curl "https://api.indexnow.org/indexnow?url=https://example.com/new-post/&key=YOUR_KEY"

# Batch (up to 10,000 URLs per POST)
curl -X POST https://api.indexnow.org/indexnow \
  -H "Content-Type: application/json" \
  -d '{
    "host": "example.com",
    "key": "YOUR_KEY",
    "urlList": [
      "https://example.com/post-1/",
      "https://example.com/post-2/"
    ]
  }'
```

---

## 9. Auto-Generated OG Images

Pipeline: **satori** (JSX → SVG) → **sharp** (SVG → JPEG)

```typescript
// src/pages/og/[...slug].jpg.ts
import satori from 'satori';
import sharp from 'sharp';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
    const posts = await getCollection('blog');
    return posts.map((p) => ({ params: { slug: p.id } }));
}

export async function GET({ params }) {
    const posts = await getCollection('blog');
    const post = posts.find((p) => p.id === params.slug);
    if (!post) return new Response('Not found', { status: 404 });

    const fontData = await fetch('https://cdn.example.com/fonts/Inter-Bold.ttf')
        .then((r) => r.arrayBuffer());

    const svg = await satori(
        {
            type: 'div',
            props: {
                style: {
                    width: '100%', height: '100%',
                    display: 'flex', flexDirection: 'column',
                    justifyContent: 'center', padding: '60px',
                    background: 'linear-gradient(135deg, #1a1a2e, #16213e)',
                    color: '#ffffff', fontFamily: 'Inter',
                },
                children: [
                    { type: 'div', props: { style: { fontSize: '48px', fontWeight: 700, lineHeight: 1.2 }, children: post.data.title } },
                    { type: 'div', props: { style: { fontSize: '24px', marginTop: '20px', opacity: 0.8 }, children: 'example.com' } },
                ],
            },
        },
        { width: 1200, height: 675, fonts: [{ name: 'Inter', data: fontData, weight: 700 }] },
    );

    const jpeg = await sharp(Buffer.from(svg)).jpeg({ quality: 80 }).toBuffer();

    return new Response(jpeg, {
        headers: { 'Content-Type': 'image/jpeg', 'Cache-Control': 'public, max-age=31536000, immutable' },
    });
}
```

**Why JPEG and not WebP/AVIF?** Social platforms don't reliably support modern formats yet.

**Size: 1200×675** — Google Discover requires ≥1200px width, and 16:9 works well cross-platform.

The `<Seo>` component derives the OG image URL from the slug automatically:

```typescript
const slug = Astro.url.pathname.replace(/^\/|\/$/g, '');
const ogImage = new URL(`/og/${slug || 'index'}.jpg`, SITE_URL).toString();
```

---

## 10. Agent Discovery

### Schema Endpoints (corpus-wide JSON-LD)

```typescript
// src/pages/schema/post.json.ts
import { getCollection } from 'astro:content';
import { createSchemaEndpoint } from '@jdevalk/astro-seo-graph';
import { buildArticle, buildWebPage, makeIds } from '@jdevalk/seo-graph-core';

const ids = makeIds({ siteUrl: 'https://example.com' });

export const GET = createSchemaEndpoint({
    entries: () => getCollection('blog'),
    mapper: (post) => {
        const url = `https://example.com/${post.id}/`;
        return [
            buildWebPage({ url, name: post.data.title, isPartOf: { '@id': ids.website }, datePublished: post.data.publishDate }, ids),
            buildArticle({ url, isPartOf: { '@id': ids.webPage(url) }, author: { '@id': ids.person }, headline: post.data.title, description: post.data.description ?? '', datePublished: post.data.publishDate }, ids, 'BlogPosting'),
        ];
    },
});
```

### Schema Map (`/schemamap.xml`)

```typescript
// src/pages/schemamap.xml.ts
import { createSchemaMap } from '@jdevalk/astro-seo-graph';

export const GET = createSchemaMap({
    siteUrl: 'https://example.com',
    entries: [
        { path: '/schema/post.json', lastModified: new Date() },
        { path: '/schema/page.json', lastModified: new Date() },
    ],
});
```

### API Catalog (RFC 9727)

```typescript
// src/pages/.well-known/api-catalog.ts
import { createApiCatalog } from '@jdevalk/astro-seo-graph';

export const GET = createApiCatalog({
    siteUrl: 'https://example.com',
    schemaEndpoints: [
        { path: '/schema/post.json', schemaType: 'BlogPosting', serviceDoc: '/about/' },
    ],
    schemaMap: { path: '/schemamap.xml' },
});
```

### Markdown Alternates

Serve a `.md` version of every page so agents can consume content without HTML parsing:

```typescript
// src/pages/blog/[...slug].md.ts
import { getCollection } from 'astro:content';
import { createMarkdownEndpoint } from '@jdevalk/astro-seo-graph';

export const getStaticPaths = async () => {
    const posts = await getCollection('blog');
    return posts.map((p) => ({ params: { slug: p.id } }));
};

export const GET = createMarkdownEndpoint({
    entries: () => getCollection('blog'),
    mapper: (post, slug) =>
        post.id !== slug ? null : {
            frontmatter: { title: post.data.title, canonical: `https://example.com/blog/${post.id}/`, pubDate: post.data.publishDate },
            body: post.body ?? '',
        },
});
```

Enable the discovery link:

```typescript
// astro.config.mjs
seoGraph({ markdownAlternate: true });
```

Emits `<link rel="alternate" type="text/markdown" href="…">` on every page.

### Content Negotiation via Cloudflare (no SSR)

Transform Rule in the dashboard (works on free plan):

```
When: http.request.headers["accept"][0] contains "text/markdown"
  AND ends_with(http.request.uri.path, "/")
  AND NOT starts_with(http.request.uri.path, "/_")

Rewrite URI path (dynamic): wildcard_replace(http.request.uri.path, "*/", "${1}.md")
```

Turns `/blog/post/` → `/blog/post.md` before cache lookup. No need for `Vary: Accept` header — Cloudflare strips custom Vary values.

### llms.txt

```typescript
seoGraph({
    llmsTxt: {
        title: 'My Site',
        siteUrl: 'https://example.com',
        summary: 'A blog about web development, Astro, and SEO.',
    },
});
```

Generates `/llms.txt` automatically at build time listing all pages.

### NLWeb Discovery

`<link>` tag for conversational endpoint (Microsoft protocol):

```html
<link rel="nlweb" href="https://example.com/api/nlweb" />
```

NLWeb allows AI agents to make conversational queries against site content via schema.org structured data. Still early days but the setup is trivial.

---

## 11. Performance SEO

### No-Vary-Search

UTM params break caching: `?utm_source=linkedin` and `?utm_source=email` are different resources to the browser. Header that fixes it:

```
No-Vary-Search: key-order, params=("utm_source" "utm_medium" "utm_campaign" "utm_content" "utm_term")
```

**Status:** IETF draft (`draft-ietf-httpbis-no-vary-search`), supported in Chrome, degrades gracefully elsewhere.

Configure in `_headers` (Cloudflare Pages / Netlify):

```
/*
  No-Vary-Search: key-order, params=("utm_source" "utm_medium" "utm_campaign" "utm_content" "utm_term")
```

### CDN Cache Headers

```
# _headers (Cloudflare Pages)
/_astro/*
  Cache-Control: public, max-age=31536000, immutable

/og/*
  Cache-Control: public, max-age=31536000, immutable
```

Hashed assets under `/_astro/` never need revalidation — the filename changes when content changes.

### View Transitions Prefetch

```astro
---
// src/layouts/Base.astro
import { ClientRouter } from 'astro:transitions';
---
<head>
    <ClientRouter defaultStrategy="viewport" />
</head>
```

`defaultStrategy: 'viewport'` prefetches links as they scroll into view, making navigation feel instant while keeping initial load minimal.

### Font Preloading

```html
<link rel="preload" href="/fonts/Inter.woff2" as="font" type="font/woff2" crossorigin />
```

---

## 12. Redirects

### Per platform

| Platform | File | Format |
|---|---|---|
| Cloudflare Pages | `public/_redirects` | `/old /new 301` |
| Netlify | `public/_redirects` or `netlify.toml` | Same format |
| Vercel | `vercel.json` | `{ "source": "/old", "destination": "/new", "permanent": true }` |

### FuzzyRedirect on 404

Safety net for URLs that slip through redirect tables:

```astro
---
// src/pages/404.astro
import FuzzyRedirect from '@jdevalk/astro-seo-graph/FuzzyRedirect.astro';
---

<html lang="en">
<head><title>Page not found</title></head>
<body>
    <h1>Page not found</h1>
    <p>The page you're looking for doesn't exist.</p>
    <FuzzyRedirect />
    <p><a href="/">Go to the homepage</a></p>
</body>
</html>
```

Behavior:
- Fetches `/sitemap-index.xml`, computes Levenshtein similarity
- **0.6–0.85 similarity**: shows "Did you mean /correct-path/?"
- **>0.85**: auto-redirects with `window.location.replace`
- **<0.6**: does nothing

---

## 13. RSS with Full Content

```typescript
// src/pages/rss.xml.ts
import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
    const posts = await getCollection('blog');
    return rss({
        title: 'My Blog',
        description: 'Latest posts',
        site: context.site,
        items: posts.map((post) => ({
            title: post.data.title,
            pubDate: post.data.publishDate,
            description: post.data.description,
            link: `/blog/${post.id}/`,
            content: post.body, // Full content, not excerpts
        })),
    });
}
```

**Include full content in the feed** — truncated feeds frustrate readers and give AI systems less to work with.

---

## 14. Dynamic robots.txt

```typescript
// src/pages/robots.txt.ts
export function GET() {
    return new Response(
`User-agent: *
Allow: /

Sitemap: https://example.com/sitemap-index.xml
Schemamap: https://example.com/schemamap.xml
`,
        { headers: { 'Content-Type': 'text/plain' } },
    );
}
```

The `Schemamap:` directive points agents to the schema map — similar to `Sitemap:` but for structured data.

---

## 15. Implementation Checklist

- [ ] `@jdevalk/astro-seo-graph` installed and `<Seo>` in all layouts
- [ ] JSON-LD `@graph` with full entities (WebSite, Person, WebPage, Article, BreadcrumbList)
- [ ] Trust signals: `publishingPrinciples`, `knowsAbout`, `SearchAction`
- [ ] `seoSchema` in content collection with title/desc validation
- [ ] `seoGraph()` integration with all validations enabled
- [ ] Per-collection sitemaps with `gitLastmod`
- [ ] IndexNow configured and key route deployed
- [ ] Auto-generated OG images (1200×675 JPEG)
- [ ] Schema endpoints + `/schemamap.xml`
- [ ] Markdown alternates with `<link rel="alternate" type="text/markdown">`
- [ ] `llms.txt` generated automatically
- [ ] `<link rel="nlweb">` (when endpoint available)
- [ ] `No-Vary-Search` header for UTM params
- [ ] CDN cache: immutable for `/_astro/*`
- [ ] View Transitions with viewport prefetch
- [ ] FuzzyRedirect on 404
- [ ] RSS with full content
- [ ] `robots.txt` with Sitemap + Schemamap
- [ ] Lychee in CI for broken external links
- [ ] `/.well-known/api-catalog` (RFC 9727)

---

## References

- [astro-seo-graph README](https://github.com/jdevalk/seo-graph/tree/main/packages/astro-seo-graph)
- [astro-seo-graph AGENTS.md](https://github.com/jdevalk/seo-graph/blob/main/AGENTS.md) — 3000+ lines with recipes for 14 site types
- [seo-graph-core](https://github.com/jdevalk/seo-graph/tree/main/packages/seo-graph-core)
- [IndexNow documentation](https://www.indexnow.org/documentation)
- [NLWeb protocol](https://github.com/nlweb-ai/NLWeb)
- [satori](https://github.com/vercel/satori) — JSX → SVG
- [sharp](https://sharp.pixelplumbing.com/) — SVG → JPEG/PNG
- [No-Vary-Search (MDN)](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/No-Vary-Search)
- [RFC 9727 — API Catalog](https://www.rfc-editor.org/rfc/rfc9727)
- [llms.txt standard](https://llmstxt.org)
- [Joost: Astro SEO definitive guide](https://joost.blog/astro-seo-complete-guide/)
- [Joost: Agent-ready static blog](https://joost.blog/agent-ready/)
