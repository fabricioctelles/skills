# Related Content com Vector Embeddings

Conteúdo relacionado semântico para Astro content collections usando `@philnash/astro-related-content`. Gera sugestões de posts relacionados via vector embeddings locais (transformers.js) sem depender de APIs externas em runtime.

---

## Conceito

A integração calcula similaridade semântica entre posts usando embeddings (vetores numéricos que representam o "significado" do texto). Posts com vetores próximos são semanticamente similares. Tudo roda em build time — zero impacto no visitante.

---

## Instalação

```bash
npm install @philnash/astro-related-content
```

---

## Configuração Básica

```typescript
// astro.config.ts
import astroRelatedContent from '@philnash/astro-related-content'

export default defineConfig({
  integrations: [
    astroRelatedContent({
      collections: ['blog'],
      generation: {
        limit: 4,        // posts relacionados por item
        watch: false,    // não regenerar em dev mode (economiza CPU)
      },
      embeddings: {
        model: 'onnx-community/embeddinggemma-300m-ONNX',
        dtype: 'fp32',
        pooling: 'mean',
        batchSize: 1,
      },
    }),
  ],
})
```

---

## Escolha de Modelo

| Modelo | Idiomas | Context | Tamanho | Pooling | Uso |
|--------|---------|---------|---------|---------|-----|
| `Xenova/all-MiniLM-L6-v2` | EN only | 256 tokens | ~22MB | `mean` | Default, ruim para PT-BR |
| `onnx-community/embeddinggemma-300m-ONNX` | Multilingual | 2048 tokens | ~300MB | `mean` | **Recomendado para PT-BR** |
| `onnx-community/Qwen3-Embedding-0.6B-ONNX` | Multilingual | 32k tokens | ~600MB | `last_token` | Posts muito longos |
| `onnx-community/granite-embedding-small-english-r2-ONNX` | EN | 8192 tokens | ~130MB | `cls` | EN com context longo |

**Regra:** Para conteúdo em português, NUNCA usar o modelo default (`all-MiniLM-L6-v2`). Use `embeddinggemma-300m-ONNX` ou superior.

---

## Custom Provider (LiteLLM, OpenAI, etc.)

A integração aceita custom providers via interface `EmbeddingProvider`:

```typescript
// litellm-provider.ts
import { createEmbeddingProvider } from '@philnash/astro-related-content/providers'

export const litellmProvider = createEmbeddingProvider({
  name: 'litellm',
  version: '1.0.0',

  async embed(texts, options) {
    const response = await fetch(`${options.baseUrl}/embeddings`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${options.apiKey}`,
      },
      body: JSON.stringify({ model: options.model, input: texts }),
    })
    const data = await response.json()
    return data.data.map((item: any) => item.embedding)
  },

  getMetadata(options) {
    return { model: options.model, baseUrl: options.baseUrl }
  },
})
```

```typescript
// astro.config.ts
import { litellmProvider } from './litellm-provider'

astroRelatedContent({
  collections: ['blog'],
  embeddings: {
    provider: litellmProvider,
    baseUrl: 'http://localhost:4000',
    apiKey: 'sk-...',
    model: 'text-embedding-3-small',
    batchSize: 10,
  },
})
```

---

## Artefatos Gerados

A integração gera na pasta `.astro-related-content/`:

| Arquivo | Conteúdo | Tamanho típico (32 posts) |
|---------|----------|---------------------------|
| `data.json` | Rankings (top N related por post) | ~14KB |
| `vectors.json` | Cache de embeddings + metadata | ~736KB |

O modelo ONNX é cacheado em `.astro/astro-related-content/models/` (não vai pro repo — `.astro/` está no `.gitignore`).

---

## Uso no Componente

### Bug de compatibilidade Astro v7

O `getRelatedContent()` do virtual module não funciona com Astro v7 glob loader. O motivo: a integração gera IDs como `slug/index` no `data.json`, mas o Astro v7 usa `slug` (sem `/index`) como `entry.id`.

**Workaround:** Usar `getRelatedContentMatches()` + lookup manual:

```astro
---
// RelatedPosts.astro
import { getPostRoute } from '@/lib/data-utils'
import { formatDate } from '@/lib/utils'
import { Icon } from 'astro-icon/components'
import { Image } from 'astro:assets'
import { getCollection, type CollectionEntry } from 'astro:content'
import { getRelatedContentMatches } from 'virtual:astro-related-content'
import Link from './Link.astro'

interface Props {
  postId: string
}

const { postId } = Astro.props
const matches = getRelatedContentMatches('blog', `${postId}/index`)

let relatedContent: { entry: CollectionEntry<'blog'>; score: number }[] = []
if (matches.length > 0) {
  const allEntries = await getCollection('blog')
  const entryById = new Map(allEntries.map((e) => [e.id, e]))

  relatedContent = matches.flatMap((match) => {
    // match.id = "slug/index", entry.id no Astro v7 = "slug"
    const normalizedId = match.id.replace(/\/index$/, '')
    const entry = entryById.get(normalizedId) || entryById.get(match.id)
    return entry ? [{ entry, score: match.score }] : []
  })
}
---

{
  relatedContent.length > 0 && (
    <section class="mt-12 border-t pt-8">
      <h2 class="mb-6 flex items-center gap-2 text-xl font-medium">
        <Icon name="lucide:sparkles" class="size-5" />
        Leitura Relacionada
      </h2>
      <div class="grid gap-4 sm:grid-cols-2">
        {relatedContent.map((item) => (
          <Link
            href={getPostRoute(item.entry)}
            class="hover:bg-muted/50 flex gap-3 rounded-xl border p-3 transition-colors duration-300"
          >
            {item.entry.data.image && (
              <div class="hidden w-16 shrink-0 sm:block">
                <Image
                  src={item.entry.data.image}
                  alt={item.entry.data.title}
                  width={128}
                  height={67}
                  class="rounded-md object-cover"
                />
              </div>
            )}
            <div class="min-w-0">
              <h3 class="mb-1 truncate text-sm font-medium">
                {item.entry.data.title}
              </h3>
              <p class="text-muted-foreground text-xs">
                {formatDate(item.entry.data.date)}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </section>
  )
}
```

---

## Deploy no Coolify — Sem Baixar Modelo em Produção

### O Problema

Na primeira build Docker, a integração baixa o modelo ONNX (~300MB) e processa todos os embeddings. Em um servidor com bandwidth limitada, isso pode levar 20+ minutos e esgotar disco.

### A Solução: Dual-Mode (Local + CI)

**Princípio:** Gerar embeddings localmente, commitar o cache, e em CI usar apenas o `data.json` pré-gerado via Vite plugin leve (sem modelo, sem transformers.js).

#### 1. Commitar os artefatos

Garantir que `.astro-related-content/` **NÃO** está no `.gitignore`:

```bash
# Verificar
grep "astro-related-content" .gitignore
# Se aparecer, remover a linha

# Commitar cache
git add .astro-related-content/
git commit -m "chore: cache embeddings related content"
```

#### 2. Configuração condicional no astro.config.ts

```typescript
import { existsSync } from 'node:fs'
import { resolve } from 'node:path'
import astroRelatedContent from '@philnash/astro-related-content'

// Em CI: usa data.json pré-gerado sem baixar modelo
// Local: roda integração completa com embeddings
const isCI = Boolean(process.env.CI || process.env.DOCKER)
const dataJsonPath = resolve('.astro-related-content/data.json')
const hasPrebuiltData = existsSync(dataJsonPath)

const relatedContentIntegrations = isCI && hasPrebuiltData
  ? [] // Virtual module vem do Vite plugin abaixo
  : [
      astroRelatedContent({
        collections: ['blog'],
        generation: { limit: 4 },
        embeddings: {
          model: 'onnx-community/embeddinggemma-300m-ONNX',
          dtype: 'fp32',
          pooling: 'mean',
          batchSize: 1,
        },
      }),
    ]

// Plugin Vite leve para CI — serve virtual module do data.json commitado
function relatedContentVitePlugin() {
  const VIRTUAL_ID = 'virtual:astro-related-content'
  const RESOLVED_ID = '\0' + VIRTUAL_ID
  return {
    name: 'related-content-prebuilt',
    resolveId(id: string) {
      if (id === VIRTUAL_ID) return RESOLVED_ID
    },
    load(id: string) {
      if (id !== RESOLVED_ID) return
      const absPath = resolve('.astro-related-content/data.json')
      return `
import { getCollection } from "astro:content";
import relatedContentData from ${JSON.stringify(`/@fs/${absPath}`)};

export function getRelatedContentMatches(collection, id) {
  const collectionData = relatedContentData[collection];
  if (!collectionData) return [];
  const matches = collectionData[id];
  return Array.isArray(matches) ? matches.map((m) => ({ ...m })) : [];
}

export function getRelatedContentIds(collection, id) {
  return getRelatedContentMatches(collection, id).map((m) => m.id);
}

export async function getRelatedContent(collection, id) {
  const matches = getRelatedContentMatches(collection, id);
  const entries = await getCollection(collection);
  const entryById = new Map(
    entries.flatMap((entry) => {
      const normalizedId = String(entry.id).replace(/\\.(md|mdx)$/, "");
      return normalizedId === entry.id
        ? [[entry.id, entry]]
        : [[entry.id, entry], [normalizedId, entry]];
    }),
  );
  return matches.flatMap((match) => {
    const entry = entryById.get(match.id);
    return entry ? [{ entry, score: match.score }] : [];
  });
}
`
    },
  }
}

export default defineConfig({
  integrations: [
    // ... outras integrações
    ...relatedContentIntegrations,
  ],
  vite: {
    plugins: [
      // ... outros plugins
      ...(isCI && hasPrebuiltData ? [relatedContentVitePlugin()] : []),
    ],
  },
})
```

#### 3. Dockerfile com `ENV CI=true`

```dockerfile
FROM node:22-slim AS build
WORKDIR /app
ENV CI=true
ENV NODE_OPTIONS="--max-old-space-size=512"
COPY package*.json .npmrc ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
```

O `ENV CI=true` ativa o Vite plugin leve. Nenhum modelo é baixado. Build completa em ~10-30s.

---

## Workflow Operacional

| Ação | Onde | O que acontece |
|------|------|----------------|
| Novo post | Local | `astro build` → regenera embedding só do post novo → commit cache → push |
| Editar post | Local | `astro build` → recalcula embedding do editado → commit cache → push |
| Deploy | Coolify | Usa `data.json` pré-commitado → build rápido (~30s) |
| Primeiro setup | Local | Download modelo (~300MB) + embeddings de todos os posts (1-20min) |

### Tempos Reais (32 posts, EmbeddingGemma 300m)

| Etapa | Tempo |
|-------|-------|
| Primeira geração (download modelo + 32 embeddings) | ~22 min |
| Build subsequente local (cache hit) | ~10 s |
| Build CI com data.json pré-gerado | ~10 s |
| Build CI sem cache (modelo baixando) | ~22+ min ❌ |

---

## Checklist de Implementação

- [ ] `npm install @philnash/astro-related-content`
- [ ] Configurar integração no `astro.config.ts` (com lógica CI/local)
- [ ] Criar componente `RelatedPosts.astro` (com workaround Astro v7)
- [ ] Integrar componente no template de post (`[...id].astro` ou similar)
- [ ] Rodar `astro build` localmente para gerar embeddings
- [ ] Verificar `.astro-related-content/` NÃO está no `.gitignore`
- [ ] Commitar `data.json` + `vectors.json`
- [ ] Setar `ENV CI=true` no Dockerfile
- [ ] Deploy e validar no Coolify

---

## Troubleshooting

### Build no Coolify demora 20+ minutos
**Causa:** `CI=true` não setado no Dockerfile, ou `.astro-related-content/data.json` não commitado. A integração completa está rodando e baixando o modelo.
**Fix:** Setar `ENV CI=true` no Dockerfile E commitar a pasta `.astro-related-content/`.

### Related posts não renderizam (array vazio)
**Causa:** Bug de ID entre integração e Astro v7. O `getRelatedContent()` do virtual module não faz match porque IDs diferem.
**Fix:** Usar `getRelatedContentMatches()` + lookup manual com `normalizedId = match.id.replace(/\/index$/, '')`.

### Embeddings ruins para português
**Causa:** Usando modelo default (`all-MiniLM-L6-v2`) que é English-only.
**Fix:** Usar `onnx-community/embeddinggemma-300m-ONNX` (multilingual).

### Cache invalidado a cada build
**Causa:** A metadata do provider (model, dtype, pooling, version) mudou entre builds. A integração invalida todo o cache quando metadata difere.
**Fix:** Não alterar configuração de embeddings após gerar o cache. Se precisar mudar modelo, regenerar tudo localmente e re-commitar.

### `Cannot find module '@huggingface/transformers'` em CI
**Causa:** O pacote `@huggingface/transformers` é dependência transitiva só necessária quando a integração completa roda. Em CI com o Vite plugin, não é necessário.
**Fix:** Se usar o dual-mode (CI plugin), isso não acontece. Se rodar integração em CI, garantir que `npm ci` instala todas deps.
