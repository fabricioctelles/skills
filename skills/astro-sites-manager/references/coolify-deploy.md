# Deploying Astro on Coolify

Production-tested patterns for deploying Astro sites on self-hosted Coolify (v4.x). Based on 17+ live deployments.

---

## Build Pack Decision

| Scenario | build_pack | Notes |
|----------|-----------|-------|
| Astro v6+ (requires Node ≥22.12.0) | `dockerfile` | Nixpacks can't pin minor version |
| Astro v5 or earlier | `nixpacks` | `NIXPACKS_NODE_VERSION=22` works |
| Astro `output: 'static'` with package.json | `nixpacks` | start: `npx serve dist -l 80 -s` |
| Astro `output: 'static'` (Dockerfile) | `dockerfile` | nginx serves directly |
| HTML/CSS only (no package.json) | `static` | `static_image: nginx:alpine` |

**Rule:** For Astro v6+ and v7, always use `dockerfile`. Nixpacks resolves Node 22.11.0 from its internal nixpkgs archive, but Astro v6+ requires ≥22.12.0.

**Astro v7 Docker base image rule:** Use `node:22-slim` (Debian/glibc) for the build stage, NOT `node:22-alpine`. Sätteri's native binding only supports glibc. The runtime stage can still use Alpine/Caddy since it only serves files.

---

## Dockerfile — Astro SSR (Node Adapter)

> **Requires `@astrojs/node@^11.0.0`** for Astro v7. The v10 adapter crashes at runtime with `TypeError: app.getAdapterLogger is not a function`.

```dockerfile
# Use node:22-slim (NOT alpine) — Sätteri needs glibc for Astro v7
FROM node:22-slim AS build
WORKDIR /app
ENV NODE_OPTIONS="--max-old-space-size=512"

# Coolify injects env vars as ARG — must convert to ENV for npm run build
ARG MY_API_KEY
ARG PUBLIC_SITE_URL
ENV MY_API_KEY=$MY_API_KEY
ENV PUBLIC_SITE_URL=$PUBLIC_SITE_URL

COPY package*.json .npmrc ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-slim
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./
ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "dist/server/entry.mjs"]
```

## Dockerfile — Astro Static (nginx)

```dockerfile
# Use node:22-slim (NOT alpine) — Sätteri needs glibc
FROM node:22-slim AS build
WORKDIR /app
ENV NODE_OPTIONS="--max-old-space-size=512"
COPY package*.json .npmrc ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
```

---

## Critical Gotchas

### ARG vs ENV — Build-time secrets

Coolify injects variables as Docker `ARG`. But `ARG` does NOT become an environment variable for child processes like `npm run build`. Astro/Vite resolves `import.meta.env.VAR` during build — if the variable doesn't exist in the process environment, it silently becomes `undefined`.

**Fix:** For every secret the build needs:
```dockerfile
ARG RESEND_API_KEY
ENV RESEND_API_KEY=$RESEND_API_KEY
```

### OOM on Resource-Limited Servers

The `astro build` process can die with exit code 255 and no clear error message on servers with limited RAM (~2GB).

**Fix:** Add to build stage:
```dockerfile
ENV NODE_OPTIONS="--max-old-space-size=512"
```

### Nixpacks Node Version

Nixpacks only accepts **major version**. `NIXPACKS_NODE_VERSION=22` can resolve to 22.11.0, causing:
```
Node.js v22.11.0 is not supported by Astro!
```

**Fix options:**
1. Use Dockerfile instead (recommended for Astro v6+)
2. Set `NIXPACKS_NODE_VERSION=24` (skips a major)
3. Pin nixpkgs archive via `nixpacks.toml`:
   ```toml
   [phases.setup]
   nixpkgsArchive = "5ef6c8a1bf89a0bfe4e15e7baf5bab7feeff86a5"
   ```

### Nixpacks Timeout

Nixpacks downloads ~600MB nixpkgs archive during build. On servers with limited bandwidth, build dies silently during `unpacking` step.

**Fix:** Switch to Dockerfile. `node:22-alpine` is ~50MB vs ~600MB.

### Sätteri Native Binding on Alpine (Astro v7)

Astro v7 uses Sätteri (Rust-based Markdown) by default. Sätteri ships native bindings but **only for glibc** (`@bruits/satteri-linux-x64-gnu`). Alpine uses musl libc — no musl binding exists, and the WASM fallback has a cpu platform check that also fails.

```
Cannot find module '@bruits/satteri-linux-x64-musl'
```

**Fix:** Use `node:22-slim` (Debian/glibc) for the build stage. The runtime stage can still use Alpine since it only serves static files:

```dockerfile
FROM node:22-slim AS build    # glibc — satteri works
WORKDIR /app
COPY package*.json .npmrc ./
RUN npm ci
COPY . .
RUN npm run build

FROM caddy:2-alpine           # runtime doesn't need Node
COPY --from=build /app/dist /srv
```

**Affected projects:** Any Astro v7 project using Sätteri (default) or Starlight 0.40+ on Alpine.
**Not affected:** Projects using `unified()` processor explicitly (they bypass Sätteri).

### legacy-peer-deps and npm ci in Docker

When using `--legacy-peer-deps` locally (required for Astro v7 due to transient peer dep conflicts in Starlight plugins), Docker's `npm ci` will fail unless the `.npmrc` is copied into the container.

**Fix:** Always copy `.npmrc` before `npm ci`:

```dockerfile
COPY package*.json .npmrc ./
RUN npm ci
```

The `.npmrc` must contain:
```
legacy-peer-deps=true
```

### @astrojs/node Must Be v11+ for Astro v7

Astro v7's runtime API changed — `app.getAdapterLogger()` was added and the standalone entry module depends on it. If `@astrojs/node` stays at v10, the container builds fine but **crashes at startup**:

```
TypeError: app.getAdapterLogger is not a function
    at createAppHandler (dist/server/entry.mjs)
```

Coolify shows `restarting:unknown` or `exited:unhealthy` — the build log looks green, but the container crash-loops.

**Fix:** Always upgrade `@astrojs/node` to v11 together with Astro v7:
```bash
npm install astro@latest @astrojs/node@latest
```

**Checklist for SSR v7 migration:**
- `astro` → `^7.0.0`
- `@astrojs/node` → `^11.0.0`
- `@astrojs/mdx` → `^7.0.0` (if used)

### pnpm approve-builds in Docker (pnpm 11.9+)

pnpm 11.9+ blocks install scripts (postinstall, install) by default. Packages like `esbuild` and `sharp` need native binaries built after install. Without approval, `pnpm install --frozen-lockfile` fails:

```
[ERR_PNPM_IGNORED_BUILDS] Ignored build scripts: esbuild@0.28.1, sharp@0.34.5
Run "pnpm approve-builds" to pick which dependencies should be allowed to run scripts.
```

**Fix:** Run `pnpm approve-builds` locally, which creates `pnpm-workspace.yaml` with:
```yaml
allowBuilds:
  esbuild: true
  sharp: true
```

Then **copy `pnpm-workspace.yaml` into the Docker container** alongside the lockfile:
```dockerfile
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./
RUN pnpm install --frozen-lockfile
```

Missing this file = build fails in CI/Docker but works locally (because local node_modules already has the binaries).

### package-lock.json Desync After Major Upgrade

After `npm install --legacy-peer-deps` for a major version upgrade, the lockfile may reference packages that `npm ci` (strict mode) cannot resolve. Symptoms: `npm ci` fails with "lock file's X does not satisfy Y".

**Fix:** Delete lockfile and regenerate:
```bash
rm package-lock.json node_modules -rf
npm install --legacy-peer-deps
# Then test: npm ci must pass
```

---

## Coolify API — Create App

```bash
COOLIFY_URL="https://cool.example.com/api/v1"
COOLIFY_KEY="your-token"

curl -sS -X POST "$COOLIFY_URL/applications/private-deploy-key" \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "project_uuid": "PROJECT_UUID",
    "environment_name": "production",
    "server_uuid": "SERVER_UUID",
    "private_key_uuid": "SSH_KEY_UUID",
    "git_repository": "git@gitlab.com:user/project.git",
    "git_branch": "main",
    "build_pack": "dockerfile",
    "dockerfile_location": "/Dockerfile",
    "ports_exposes": "4321",
    "name": "my-astro-site"
  }'
```

### Set Domain

```bash
# Use "domains", NOT "fqdn" — fqdn returns "field not allowed"
curl -sS -X PATCH "$COOLIFY_URL/applications/$APP_UUID" \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domains": "https://mysite.com"}'
```

### Set Environment Variables

```bash
curl -sS -X POST "$COOLIFY_URL/applications/$APP_UUID/envs" \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  -H "Content-Type: application/json" \
  -d '{"key": "MY_VAR", "value": "secret-value", "is_preview": false}'
```

> Do NOT send `is_build_time` — API rejects it.

### GitLab Webhook (auto-deploy on push)

```bash
curl -sS -X POST "https://gitlab.com/api/v4/projects/$PROJECT_ID/hooks" \
  -H "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://cool.example.com/webhooks/source/gitlab/events/manual",
    "token": "WEBHOOK_SECRET_FROM_APP",
    "push_events": true,
    "enable_ssl_verification": true
  }'
```

> **Critical:** The secret goes in the `"token"` field (sent as `X-Gitlab-Token` header), NEVER as `?secret=` query parameter in the URL. With secret in URL, Coolify returns 200 but does NOT trigger deploy.

### Deploy and Validate

```bash
# Trigger deploy (Coolify 4.1+ — uses GET, NOT POST)
# The /deploy endpoint accepts uuid as query param, force=true rebuilds from scratch
curl -sS -X GET "$COOLIFY_URL/deploy?uuid=$APP_UUID&force=true" \
  -H "Authorization: Bearer $COOLIFY_KEY"
# Returns: {"deployments":[{"message":"Application X deployment queued.","resource_uuid":"...","deployment_uuid":"..."}]}

# ⚠️ POST /applications/$UUID/deploy returns "Not found" in Coolify 4.1
# ⚠️ POST /applications/$UUID/restart only restarts existing container (no rebuild)
#    Use restart when image is already built. Use /deploy?uuid=...&force=true for rebuild.

# Check status (~60s wait for build + container start)
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY_URL/applications/$APP_UUID" | python3 -c "
import sys,json; d=json.load(sys.stdin); print(d['status'])"

# Verify HTTP response
curl -sS -o /dev/null -w "HTTP %{http_code}\n" https://mysite.com
```

**Status interpretation:**
| Status | Meaning |
|--------|---------|
| `running:healthy` | Container up and health check passing |
| `running:unknown` | Container up, no health check configured |
| `restarting:unknown` | Container crash-looping — check runtime logs |
| `exited:unhealthy` | Container stopped — likely build or startup failure |

---

## Astro Config for Coolify SSR

```typescript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

export default defineConfig({
  output: 'server', // or hybrid with per-page prerender
  adapter: node({ mode: 'standalone' }),
  server: { host: '0.0.0.0', port: 4321 },
});
```

For static output, no adapter needed — the Dockerfile handles nginx serving.

---

## Port Configuration

| Output Mode | Port | CMD |
|-------------|------|-----|
| SSR (Node adapter) | 4321 | `node dist/server/entry.mjs` |
| Static (nginx) | 80 | nginx default |
| Static (serve) | 80 | `npx serve dist -l 80 -s` |

Set `ports_exposes` in Coolify to match.

---

## Recommended Stack (Homelab-Tested)

Based on 17 production Astro sites:

```javascript
import seoGraph from '@jdevalk/astro-seo-graph/integration';
import agentmarkup from '@agentmarkup/astro';
import UnoCSS from '@unocss/astro';
import critters from 'astro-critters';
import compress from '@playform/compress';

// Key: compress() MUST be last integration
integrations: [mdx(), UnoCSS(), sitemap(), seoGraph(), agentmarkup(), critters(), compress()]
```

| Tool | Why |
|------|-----|
| UnoCSS > Tailwind | 5x faster build, smaller bundle |
| @playform/compress > astro-compress | Better maintained |
| astro-critters | Critical CSS inlining |
| @jdevalk/astro-seo-graph | All-in-one SEO (replaces astro-seo + robots-txt + indexnow) |
| @agentmarkup/astro | LLM visibility (llms.txt, markdown mirrors) |
| Plausible > GA4 | 1kb script, no cookie banner, self-hosted |
