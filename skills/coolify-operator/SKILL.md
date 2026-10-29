---
name: coolify-operator
description: Master Coolify operator for self-hosted deployment platform. Use when the user mentions 'coolify', 'deploy on coolify', 'list/restart/redeploy applications', 'view coolify logs', 'coolify API/CLI', 'manage coolify servers/databases/apps', or 'coolify context'. Automates deployments and management via REST API or official CLI.
metadata:
  author: ft.ia.br
  version: "3.4"
  date: 2026-10-29
  license: MIT
  category: ci-cd-and-deployment
  coolify_cli_version: "1.11.0"
  coolify_version: "4.5.3"
  upstream_commit: "3738289a2a47050fa70007a571fbed00cb1c6d6e"
---

# Coolify Operator

Skill for operating Coolify instances through the **official CLI** or **REST API**. Coolify is a self-hosted open-source platform alternative to Heroku/Vercel/Netlify for deploying applications, databases, and services.

**Pinned upstream:** coolify-cli **v1.11.0** (`3738289a2a47050fa70007a571fbed00cb1c6d6e`) — Coolify v4 surface. Prefer command forms from `llms.txt` / `llms-full.txt` on that tag.

**Release notes reviewed:** Coolify v4.5.3 (October 2026). This records upstream changes; it does not assert that every homelab instance has been upgraded.

### CLI v1.11.0 Highlights

- **New:** `coolify server hostinger catalog|data-centers|templates|ssh-keys|post-install-scripts <cloud_token_uuid>` — inspect plans/prices, data centers, OS templates, SSH keys, and post-install scripts before provisioning (`catalog` alias: `plans`)
- **New:** `coolify server hostinger create` — buys a Hostinger VPS and adds it as a Coolify server. Paid and recurring: see **Server Provisioning on Hostinger** under Servers
- **New:** `coolify cloud-token create --provider hostinger` — Hostinger joins hetzner, digitalocean, and vultr
- **Security:** sensitive fields (tokens, passwords, private keys, secrets, IPs, emails) are now masked as `********` in `json` and `pretty` output too, not only in `table`; `-s` / `--show-sensitive` reveals them in every format. Scripts that read secrets from `--format json` must add `-s`
- **Changed:** `coolify context get` now uses the token-free view — it never prints the saved API token, in any format, even with `--show-sensitive`

### CLI v1.10.0 Highlights

- **New:** `coolify database import start|upload|status` and `coolify service database import ...` — restore backups from a local file, a previous upload, S3, or a server path
- **New:** `coolify audit list` — team audit log (admins/owners)
- **New:** `coolify integration-token create` + `coolify app secret-manager set` — Doppler / Infisical / Vault secret managers
- **New:** `coolify app previews logs`, `coolify teams update --build-server-fallback`, `coolify project environments get`
- **New:** `sqlite` database type (`--sqlite-databases`)
- `coolify service application logs` accepts `-n, --lines`

### CLI v1.9.0 Highlights

- **New:** `coolify app previews list|get|create|update` (preview deployments API, Coolify v4.4.0+)
- **New:** `coolify server registry list|login|check|logout` — Docker registry logins on servers
- **New:** `coolify mcp enable|disable` — toggle the instance MCP endpoint (requires a root team API token)
- **New:** `coolify server remove --force` / `--delete-from-provider`
- **New:** `--server-role deployment|build|both` on `server add` / `server update` (`--is-build-server` deprecated)
- **Changed:** `coolify server get <uuid> --resources` now calls `GET /servers/{uuid}/resources` and prints a flat list (`uuid`, `name`, `type`, `status`) instead of the server details
- GitHub App commands also accept the numeric app ID

### CLI v1.8.0 Highlights

- **New:** Commands for instance-wide SMTP/Resend settings (`coolify settings email get/update`)
- **Security:** API tokens redacted by default in `context list` output (use `--show-sensitive` to reveal); since v1.11.0 every output format masks sensitive fields, see CLI v1.11.0 Highlights
- **Fix:** `is_buildtime` field now correctly sent on app env create/update
- **Breaking:** `--retention-max-storage-locally` and `--retention-max-storage-s3` accept **numeric GB** (e.g., `1`, `10.5`), not unit-suffixed strings

## When to use this skill

- Connect to Coolify instances (via CLI contexts or API)
- Create, list, and manage applications, services, databases, and servers
- Deploy, restart, or stop resources
- View logs and deployment status
- Manage environment variables, shared envs, and storage
- Configure backups for databases
- Operate multiple Coolify instances (contexts)
- Integrate with GitHub / GitLab Apps for private repositories
- Configure notifications and instance email (SMTP/Resend)
- Manage cloud-init scripts and provision servers (Hetzner, DigitalOcean, Vultr, and Hostinger since CLI v1.11.0)
- Restore database backups (database import), read the team audit log, configure external secret managers, and manage Docker registry logins on servers

---

## Recent Changes (v4.5.x)

Highlights for operators, based on the [v4.5.0](https://github.com/coollabsio/coolify/releases/tag/v4.5.0) through [v4.5.3](https://github.com/coollabsio/coolify/releases/tag/v4.5.3) releases:

- **Security and access:** v4.5.0 encrypts secrets at rest, scopes deployment queries to the caller's team, and enforces instance IP allow-lists on the MCP endpoint. v4.5.1 uses Cloudflare's client IP for API allow-lists and audit logs when requests pass through Cloudflare. Confirm the source IP behavior before tightening allow-lists behind a proxy.
- **Sensitive API data:** v4.5.2 gates application commands/configuration, service configuration, custom database config, and custom Docker options by team role or the API token's `read:sensitive` ability. Grant that ability only when the operator needs those fields; treat returned values as secrets.
- **Service deletion:** v4.5.1 removed “Remove from Coolify only”. The `delete_from_coolify_only` services API option now returns HTTP 422. Do not use it as a way to unregister an unreachable service; ordinary deletion is designed to work when its server cannot be reached.
- **Timeouts and retries:** v4.5.3 stops retrying HTTP requests that timed out after being sent, to avoid duplicate actions. For state-changing API calls, a timeout is an unknown outcome: inspect the resource/deployment state before manually retrying.
- **Deploy/build fixes:** v4.5.3 preserves a Dockerfile `HEALTHCHECK`, fixes Compose builds whose required variable exists only at runtime, and fixes concurrent Railpack builds. If a deployment fails on these paths, first confirm the instance includes this release before changing the app configuration.
- **Preview variables:** v4.5.2 preserves production values when an existing PR preview is redeployed; newly created previews use their own variables. Check preview-specific environment values when diagnosing differences between a new preview and a redeploy.
- **Updates and recovery:** v4.5.0 adds an automatic database backup before Coolify updates. Still confirm backup health and recovery requirements before a maintenance window. v4.5.1 also adds per-server security patching in beta; inspect server scope and policy before enabling it.
- **v4.4 users:** v4.4.7 fixes multiple critical dependency CVEs. Upgrade at least to that patch if staying on the 4.4 line, or follow the appropriate security patch for the installed release line.

### New REST API operations in v4.5.0

Comparing the official OpenAPI specs for v4.4.7 and v4.5.0, these operations were added. The v4.5.0–v4.5.3 specs show no further added or removed REST operations:

| Operation | Purpose |
|---|---|
| `GET /hostinger/data-centers` | List Hostinger VPS data centers |
| `GET /hostinger/catalog` | List Hostinger VPS plans and prices |
| `GET /hostinger/templates` | List Hostinger OS templates |
| `GET /hostinger/ssh-keys` | List SSH keys in the connected Hostinger account |
| `GET /hostinger/post-install-scripts` | List Hostinger post-install scripts |
| `POST /servers/hostinger` | Purchase a Hostinger VPS and create its Coolify server record |
| `POST /servers/{uuid}/migrate` | Start a server migration to another Coolify instance |
| `GET /servers/{uuid}/transfer` | Check transfer progress/status |
| `GET /servers/import/check` | Check whether a transfer bundle can be imported |
| `POST /servers/import` | Import a server transfer bundle |
| `POST /servers/{uuid}/transfer/complete` | Mark a server transfer complete |

Server migrations run in the background. Check transfer status before treating a migration as complete. Hostinger provisioning can incur provider charges, so inspect the selected plan and data center before calling `POST /servers/hostinger`.

**Other v4.5.0 API contract changes (existing routes):** application updates accept `dockerfile` and `github_app_uuid`; database updates apply `redis_password` and `instant_deploy`; service creation accepts `connect_to_docker_network`. The application write API uses `domains` rather than `fqdn`, and `force_domain_override` is honored for `docker_compose_domains` on create.

### Built-in MCP server (v4.5.0+)

Coolify exposes its MCP server at `https://<coolify-host>/mcp` using Streamable HTTP. This is separate from the REST API base `/api/v1`. The instance MCP setting and the token's team MCP setting must both allow access. The endpoint also obeys the instance IP allow-list.

```bash
# Enable or disable the instance MCP endpoint (requires a root team API token)
coolify mcp enable
coolify mcp disable

# REST API equivalents
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/mcp/enable"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/mcp/disable"
```

Create a team-scoped token and configure the MCP client with the instance URL plus `/mcp` and `Authorization: Bearer <token>`. Use `read` for inventory/inspection, add `read:sensitive` only for supported sensitive output, and add `deploy` for deploy/start/stop/restart/cancel actions. Avoid `root` for routine MCP use. Resource-management tools include inventory and discovery (`get_infrastructure_overview`, `search_resources`, `list_unhealthy_resources`), plus application, database, service, deployment, log, and lifecycle operations. Ask `coolify_help` or inspect MCP tool capabilities on the connected instance because available tools depend on version and token permissions. MCP responses do not return environment values or file contents; log summaries are limited and best-effort redacted.

The v4.5.0 release also notes that MCP API-token creation works while REST API access is disabled. This does not remove MCP's own instance/team enablement and IP-allow-list checks.

**Coolify application console command:** v4.5.0 adds Laravel Artisan `php artisan app-key:reencrypt` to re-encrypt stored secrets after rotating `APP_KEY`. It is not a `coolify` CLI subcommand; run it only in the Coolify application container as part of a planned key rotation, after reviewing the release instructions and taking a recoverable backup.

**CLI/API coverage:** the pinned coolify-cli v1.11.0 documents `coolify mcp enable|disable`, and since v1.11.0 it also covers Hostinger provisioning (`coolify server hostinger catalog|data-centers|templates|ssh-keys|post-install-scripts` and `coolify server hostinger create`, see **Server Provisioning on Hostinger** under Servers). Server transfer/migration is still not exposed by the CLI. Use the REST API/OpenAPI schema for those request bodies and permissions; do not invent a CLI equivalent.

### Operational checks after upgrading to v4.5.x

1. Verify the deployed Coolify version before relying on new behavior; the `coolify_version` metadata above tracks reviewed release notes, not the state of each instance.
2. For Cloudflare-proxied API access, validate the IP seen by Coolify before changing allow-lists, and confirm the access path still works.
3. Use least-privilege API tokens. Add `read:sensitive` only for operations that require protected configuration or audit details.
4. After a timed-out mutation, query the affected resource or deployment before issuing another request.
5. Review release-specific breaking changes before deleting services or changing preview environment variables.

## Recent Changes (v4.4.x)

### v4.4.0 — Major feature release
Highlights relevant to CLI/API operators (see the [v4.4.0 release](https://github.com/coollabsio/coolify/releases/tag/v4.4.0)):

- **SQLite** as a standalone database type (experimental)
- **Third-party secret managers** (Doppler, Infisical, HashiCorp Vault). `{{vault.KEY}}` references are resolved at deployment/database start and never stored in Coolify
- **Team audit log** (`GET /audit-events`, admins/owners only; events pruned after 90 days)
- **Database import API** for standalone and service databases (upload, server path, or S3). Upload/start need `write`; a server-path import also needs `deploy`
- **Server roles** (`server_role`: deployment / build / both); `is_build_server` is deprecated. Team setting decides whether builds fall back to the deployment server
- **Docker registry logins** per server (`GET/POST /servers/{uuid}/registries`, `.../{registry}/check`, `DELETE .../{registry}`). Coolify runs `docker login` on the server and does not store the token
- **Preview deployments API** (`GET /applications/{uuid}/previews[/{pr_id}]`, `POST /applications/{uuid}/previews` needs `deploy`)
- Delete a server from its cloud provider: `DELETE /servers/{uuid}?delete_from_provider=true`
- Named volumes for new mounts (existing bind mounts keep their paths)

**Behavior changes to watch:**
- Single-database PostgreSQL restores no longer drop existing objects by default — pass `replace_existing` (`--replace-existing`) to get the old `--clean` behavior; owners/privileges are skipped unless `keep_owners` (`--keep-owners`)
- Env var names must match `[A-Za-z_][A-Za-z0-9_.]*` (invalid build-time names stop builds)
- Container labels use UUIDs (`coolify.applicationUuid`, `coolify.serviceUuid`, `coolify.databaseUuid`); generated container names use an ISO 8601 suffix
- Container log and scheduled-task output endpoints require `read:sensitive` in the API
- Multi-server applications: extra servers must use the same proxy and pull the primary server's image; persistent volumes and Docker Compose apps can no longer be combined with multiple servers

### v4.4.1 – v4.4.6
- v4.4.1: volume backup notifications and missing-volume-backup alerts; Sentinel 1.0.2
- v4.4.2: GitHub Actions runners on deployment+build servers; per-server traffic analytics IP storage controls
- v4.4.3: static-site PR previews fixed; nested Base64 custom labels fixed in API updates
- v4.4.4: optional Cloudflare proxy mode for new DNS records; IPv6 fixes; Infisical reference expansion fix
- v4.4.5: removed the 5 GB free-space requirement that blocked updates
- v4.4.6: pinned PHP base image to fix self-hosted startup failures

## Breaking Changes (v4.3.x)

### v4.3.22 — Host Path Removal
**Removed:** `host_path` configuration for persistent volumes. API requests including `host_path` are now rejected.

```bash
# WRONG (no longer works)
coolify app storage create <uuid> \
  --type persistent \
  --mount-path /data \
  --host-path /opt/data  # ❌ Rejected

# CORRECT (use named volumes only)
coolify app storage create <uuid> \
  --type persistent \
  --mount-path /data \
  --name my-volume
```

### v4.3.21 — Restart Limits Now Opt-In
Restart limits are now **opt-in** for applications, preview deployments, and service applications. Existing resources with the previous default limit of 10 restarts were reset to unlimited.

### v4.3.19 — Sentinel Mandatory
**Sentinel is now mandatory** on regular servers. Existing servers were enabled automatically, and the enable/disable setting became read-only. This is required for upcoming features — Sentinel will have increased responsibilities.

- Sentinel upgraded: 0.0.22 → 1.0.1
- Hourly version checks restored for enabled servers

## CLI Installation

```bash
# Linux/macOS (recommended)
curl -fsSL https://raw.githubusercontent.com/coollabsio/coolify-cli/main/scripts/install.sh | bash

# Homebrew (macOS/Linux)
brew install coollabsio/coolify-cli/coolify-cli

# Windows (PowerShell)
irm https://raw.githubusercontent.com/coollabsio/coolify-cli/main/scripts/install.ps1 | iex

# Go install
go install github.com/coollabsio/coolify-cli/coolify@latest
```

Pin a version on Windows with `$env:COOLIFY_VERSION='v1.11.0'` before `irm ... | iex`. User-local install: `$env:COOLIFY_USER_INSTALL=1`.

## Fundamental Concepts

### Authentication

**CLI:**
- Contexts store HOST + TOKEN
- HOST is WITHOUT `/api/v1` (CLI adds it automatically)
- Token obtained at: Coolify Dashboard → Security → API Tokens

**REST API:**
- Base endpoint: `https://YOUR-HOST/api/v1` (always with `/api/v1`)
- Header: `Authorization: Bearer YOUR_TOKEN`

### Configuration with pipe in token

Coolify tokens often contain `|` (e.g., `3|abc123...`). Never use `source .env`.

```bash
# Safe .env reading
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)
```

### Global Flags

All commands support these flags (match coolify-cli v1.11.0):

```bash
--context <name>              # Use specific context instead of default
--token <token>               # Override authentication token
--format table|json|pretty    # Output format (default: table)
-s, --show-sensitive          # Reveal masked fields (tokens, passwords, keys, IPs, emails) in any format — v1.11.0+
--debug                       # Enable debug mode
```

Config file holds plaintext tokens — never commit `~/.config/coolify/config.json` (Windows: `%APPDATA%\coolify\config.json`).

---

## CLI Operations

### Utility Commands

```bash
# Update CLI to latest version
coolify update

# Show current CLI version
coolify version

# Show configuration file location
coolify config

# Generate shell completion
coolify completion bash   # or: zsh, fish, powershell
```

### Context Management

Since CLI v1.11.0, fields the CLI marks sensitive (tokens, passwords, private keys, secrets, IPs, emails) are masked as `********` by default in every output format — `table`, `json`, and `pretty`. Pass `-s` / `--show-sensitive` to reveal them. `coolify context get` uses the token-free view and never prints the saved API token, even with `--show-sensitive`. The config file still stores plaintext tokens — do not commit it.

```bash
# List all configured contexts (redacted by default — v1.8.0+ security fix)
coolify context list
coolify context list --show-sensitive  # reveal tokens

# Add new context
coolify context add <context_name> <url> <token>
coolify context add -d my-coolify http://192.168.1.100:8000 "$TOKEN"  # -d sets as default
coolify context add -f prod https://prod.coolify.io "$TOKEN"          # -f force overwrite

# For Coolify Cloud
coolify context set-token cloud <token>

# Get context details
coolify context get <context_name>

# Delete context
coolify context delete <context_name>

# Update context token
coolify context set-token <context_name> <new_token>

# Set default context
coolify context set-default <context_name>
coolify context use <context_name>  # alias

# Update context properties
coolify context update <context_name> --name <new_name>
coolify context update <context_name> --url <new_url>
coolify context update <context_name> --token <new_token>

# Verify connection and authentication
coolify context verify

# Get Coolify API version
coolify context version
```

### Projects

Primary form is singular `coolify project` (alias `projects` still works).

```bash
# List all projects
coolify project list

# Get project details / environments
coolify project get <uuid>
coolify project environments list <project_uuid>

# Create new project
coolify project create --name "My Project" --description "Description"

# Get one environment and its applications, databases and services (v1.10.0+, alias: env)
coolify project environments get <project_uuid> <environment_name_or_uuid>
```

### Resources

```bash
# List all resources (apps, databases, services)
coolify resource list
```

### Command aliases (v1.10)

Prefer primary forms from `llms.txt`. These aliases still work:

- `coolify app` | `apps` | `application` | `applications`
- `coolify service` | `services` | `svc`
- `coolify database` | `databases` | `db` | `dbs`
- `coolify project` | `projects`
- `coolify resource` | `resources`
- `coolify server` | `servers`
- `coolify teams` | `team`
- `coolify github` | `gh` (and GitLab: `gitlab` | `gl` | `gitlab-app`)
- `coolify audit` | `audit-events` | `audit-log`
- `coolify integration-token` | `integration-tokens`
- `coolify server registry` | `registries`; `coolify database import` | `imports`

---

## Applications

### List and View

```bash
# List all applications
coolify app list

# Get application details
coolify app get <uuid>
```

### Create Application

#### From Public Git Repository

```bash
coolify app create public \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --git-repository "https://github.com/user/repo" \
  --git-branch main \
  --build-pack nixpacks \
  --ports-exposes 3000 \
  --domains "app.example.com" \
  --instant-deploy

# Build packs: nixpacks, static, dockerfile, dockercompose
# Additional flags:
#   --name, --description, --base-directory, --publish-directory
#   --build-command, --start-command, --install-command
#   --health-check-enabled, --health-check-path
#   --limits-memory, --limits-cpus, --ports-mappings
#   --git-commit-sha, --destination-uuid, --dockerfile-target-build
#   --tag, --tags (for tagging)
#   --compose-domain <service>=<url> (for Docker Compose)
```

#### From Private GitHub Repository (via GitHub App)

```bash
coolify app create github \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --github-app-uuid <github-app-uuid> \
  --git-repository "owner/repo" \
  --git-branch main \
  --build-pack nixpacks \
  --ports-exposes 3000
```

#### From Private Repository (via Deploy Key)

```bash
coolify app create deploy-key \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --private-key-uuid <key-uuid> \
  --git-repository "git@github.com:owner/repo.git" \
  --git-branch main \
  --build-pack nixpacks \
  --ports-exposes 3000
```

#### From Dockerfile

```bash
coolify app create dockerfile \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --dockerfile "FROM node:20\nCOPY . .\nRUN npm install\nCMD [\"npm\", \"start\"]"
```

#### From Docker Image

```bash
coolify app create dockerimage \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --docker-registry-image-name nginx \
  --docker-registry-image-tag latest \
  --ports-exposes 80
```

### Update Application

```bash
coolify app update <uuid> \
  --name "New Name" \
  --description "New description" \
  --git-branch develop \
  --git-repository "https://github.com/user/repo" \
  --domains "app.example.com,www.example.com" \
  --compose-domain web=https://web.example.com \
  --build-command "npm run build" \
  --start-command "npm start" \
  --install-command "npm install" \
  --base-directory "/app" \
  --publish-directory "/app/dist" \
  --dockerfile "FROM node:20..." \
  --docker-image nginx \
  --docker-tag latest \
  --ports-exposes "3000,8080" \
  --ports-mappings "3000:3000" \
  --health-check-enabled \
  --health-check-path "/health"
```

### Per-Domain Internal Port Overrides (v4.3.15+)

Applications, Docker Compose services, and preview deployments now support internal port overrides per domain. Public URLs remain portless while internal routing uses the specified port.

```bash
# Via API: PATCH /api/v1/applications/{uuid}
# Use domains array with port_override field
curl -sS -X PATCH -H "Authorization: Bearer $COOLIFY_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "domains": [
      {"fqdn": "app.example.com", "port_override": 3000},
      {"fqdn": "api.example.com", "port_override": 8080}
    ]
  }' \
  "$COOLIFY/applications/{uuid}"

# Note: The UI shows effective ports and warns about unrecognized ports
# Works with both Traefik and Caddy proxies
```

### Lifecycle Management

```bash
# Start application
coolify app start <uuid>

# Stop application
coolify app stop <uuid>

# Restart application
coolify app restart <uuid>

# Delete application
coolify app delete <uuid>
coolify app delete <uuid> -f  # skip confirmation

# Move to another environment
coolify app move <uuid> --environment-uuid <env-uuid>
```

### Application Logs

```bash
# Get logs
coolify app logs <uuid>

# Follow logs (like tail -f)
coolify app logs <uuid> -f

# Limit lines (or use 'all' / -1 for unlimited — v4.3.20+)
coolify app logs <uuid> -n 50
coolify app logs <uuid> -n all

# Show timestamps
coolify app logs <uuid> --show-timestamps

# Logs for specific Docker Compose service
coolify app logs <uuid> --service web
```

### Application Tags

```bash
# List tags
coolify app tag list <uuid>

# Add tag
coolify app tag add <uuid> <tag-name>

# Remove tag
coolify app tag remove <uuid> <tag-name>
```

### Application Environment Variables

```bash
# List all env vars
coolify app env list <uuid>

# Get specific env var
coolify app env get <uuid> <env_uuid_or_key>

# Create env var
coolify app env create <uuid> \
  --key API_KEY \
  --value secret123 \
  --preview \
  --build-time \
  --runtime \
  --comment "API key for external service" \
  --is-literal \
  --is-multiline

# Update env var
coolify app env update <uuid> <env_uuid_or_key> \
  --value new-value \
  --key NEW_KEY  # optional, for renaming

# Delete env var
coolify app env delete <uuid> <env_uuid>
coolify app env delete <uuid> <env_uuid> --force

# Sync from .env file (updates existing, creates new, keeps others)
coolify app env sync <uuid> --file .env
coolify app env sync <uuid> --file .env.production --build-time --runtime --preview --is-literal
# short form also valid: -f .env
```

### Application Storage

```bash
# List storages
coolify app storage list <uuid>

# Create persistent volume (named volume only — host_path removed in v4.3.22)
coolify app storage create <uuid> \
  --type persistent \
  --mount-path /data \
  --name my-volume

# Create file mount
coolify app storage create <uuid> \
  --type file \
  --mount-path /app/config.json \
  --content '{"key": "value"}'

# Create directory mount
coolify app storage create <uuid> \
  --type file \
  --mount-path /app/config \
  --is-directory \
  --fs-path /opt/config

# Update storage
coolify app storage update <uuid> \
  --uuid <storage-uuid> \
  --type persistent \
  --is-preview-suffix-enabled

# Delete storage
coolify app storage delete <uuid> <storage-uuid>
```

### Application Deployments

```bash
# List deployments
coolify app deployments list <uuid>

# Get deployment logs (latest)
coolify app deployments logs <uuid>

# Get specific deployment logs
coolify app deployments logs <uuid> <deployment-uuid>

# Follow deployment logs
coolify app deployments logs <uuid> -f

# Limit lines
coolify app deployments logs <uuid> -n 50

# Show debug logs
coolify app deployments logs <uuid> --debuglogs
```

### Application Previews

Full CRUD since CLI v1.9.0 (logs since v1.10.0). Requires Coolify v4.4.0+ for list/get/create (`create` needs a token with `deploy`).

```bash
# List / get preview deployments
coolify app previews list <app_uuid>
coolify app previews get <app_uuid> <pr_id>

# Open (or redeploy) a preview and queue its deployment (aliases: open, deploy)
coolify app previews create <app_uuid> 42 --git-type github
coolify app previews create <app_uuid> 42 --git-type bitbucket --commit 1a2b3c4d
coolify app previews create <app_uuid> 42 --docker-tag pr-42     # Docker Image apps
coolify app previews create <app_uuid> 42 --git-type gitlab --no-deploy
# --git-type github|gitlab|gitea|bitbucket (not needed for GitHub App / GitLab App sources)
# --url <pr-url>, --force (rebuild without cache)

# Replace the domains of a preview (--domains and --compose-domain are mutually exclusive)
coolify app previews update <app_uuid> 42 --domains "pr-42.example.com"
coolify app previews update <app_uuid> 42 --compose-domain web=https://pr-42.example.com
coolify app previews update <app_uuid> 42 --domains "pr-42.example.com" --force-domain-override

# Runtime logs of a preview (v1.10.0+)
coolify app previews logs <app_uuid> 42
coolify app previews logs <app_uuid> 42 -n -1 --show-timestamps   # -1 = all lines
coolify app previews logs <app_uuid> 42 -f --service web

# Delete preview deployment
coolify app previews delete <app_uuid> <pr_id>
coolify app previews delete <app_uuid> <pr_id> --force

# API equivalent for logs (v4.3.23+; token needs read:sensitive since v4.4.0): lines (int or "all"), timestamps (bool)
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/previews/{pr_id}/logs?lines=100&timestamps=true"
```

### Application Secret Manager (v1.10.0+)

Point an application at an external secret manager (Doppler, Infisical, HashiCorp Vault). Create the integration token first (see [Secret Manager Integration Tokens](#secret-manager-integration-tokens)), then reference secrets as `{{vault.KEY}}` in env values. Values are resolved at deployment and never stored in Coolify.

```bash
coolify app secret-manager set <app_uuid> --integration-token <token_uuid>
coolify app secret-manager set <app_uuid> --integration-token <token_uuid> \
  --settings '{"mount":"secret","path":"apps/web"}'

# --settings per provider (JSON object):
#   doppler    {"project":"...","config":"..."}   (required for service account tokens)
#   infisical  {"project_id":"...","environment":"...","secret_path":"/"}
#   vault      {"mount":"...","path":"..."}
```

---

## Databases

### List and View

```bash
# List all databases
coolify database list

# Get database details
coolify database get <uuid>
```

### Create Database

```bash
# Supported types: postgresql, mysql, mariadb, mongodb, redis, keydb, clickhouse, dragonfly, sqlite (v1.10.0+)

coolify database create postgresql \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --name mydb \
  --description "Production database" \
  --image postgres:16 \
  --instant-deploy \
  --is-public \
  --public-port 5432 \
  --limits-memory 2g \
  --limits-cpus 2

# Database-specific flags available (postgres-user, mysql-root-password, etc.)
# Supports --tag and --tags for tagging

# SQLite (Coolify v4.4.0+, experimental) — no --is-public / --public-port
coolify database create sqlite \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --sqlite-databases app.db,cache.db
```

### Update and Delete

```bash
# Update database configuration
coolify database update <uuid> --name "New Name"
coolify database update <uuid> --sqlite-databases app.db,cache.db  # SQLite only

# Delete database
coolify database delete <uuid> \
  --delete-configurations \
  --delete-volumes \
  --docker-cleanup \
  --delete-connected-networks
```

### Lifecycle Management

```bash
coolify database start <uuid>
coolify database stop <uuid>
coolify database restart <uuid>
coolify database logs <uuid>
coolify database move <uuid> --environment-uuid <env-uuid>
```

### Database Tags

```bash
coolify database tag list <uuid>
coolify database tag add <uuid> <tag-name>
coolify database tag remove <uuid> <tag-name>
```

### Database Environment Variables

```bash
# Same structure as app env commands
coolify database env list <uuid>
coolify database env get <uuid> <env_uuid_or_key>
coolify database env create <uuid> --key DB_DEBUG --value true
coolify database env update <uuid> <env_uuid_or_key> --value new-value
coolify database env delete <uuid> <env_uuid> --force
coolify database env sync <uuid> --file .env
```

### Database Storage

```bash
# Same structure as app storage commands
coolify database storage list <uuid>
coolify database storage create <uuid> --type persistent --mount-path /data
coolify database storage update <uuid> --uuid <storage-uuid> --type persistent
coolify database storage delete <uuid> <storage-uuid>
```

### Database Backups

> **Retention storage units:** `--retention-max-storage-locally` / `--retention-max-storage-s3` are **float64 GB** (e.g. `1` or `10`). Do **not** pass suffixes like `1GB` / `10GB`.
>
> **v4.3.18+**: S3-only volume archives stream directly to S3 (no temporary local disk required).
>
> **v4.3.18+**: Configurable alerts when scheduled backups miss X days (see `--alert-after-missing-days`).

```bash
# List backup configurations
coolify database backup list <uuid>

# Create backup configuration
coolify database backup create <uuid> \
  --frequency "0 2 * * *" \
  --enabled \
  --save-s3 \
  --s3-storage-uuid <uuid> \
  --databases-to-backup "db1,db2" \
  --dump-all \
  --retention-amount-locally 10 \
  --retention-days-locally 7 \
  --retention-max-storage-locally 1 \
  --retention-amount-s3 30 \
  --retention-days-s3 30 \
  --retention-max-storage-s3 10 \
  --timeout 3600 \
  --disable-local-backup

# Update backup configuration
coolify database backup update <uuid> <backup-uuid> --frequency "0 3 * * *"

# Delete backup configuration
coolify database backup delete <uuid> <backup-uuid>

# Trigger immediate backup
coolify database backup trigger <uuid> <backup-uuid>

# List backup executions
coolify database backup executions <uuid> <backup-uuid>

# Delete backup execution
coolify database backup delete-execution <uuid> <backup-uuid> <execution-uuid>
```

### Database Import (Restore) — v1.10.0+

Requires Coolify v4.4.0+. Give `start` **exactly one** source: `--file`, `--upload-id`, `--s3-storage-uuid` + `--s3-path`, or `--server-path`. Uploading and starting need a token with `write`; `--server-path` also needs `deploy`. Local files max 10 GiB (uploaded in 10 MB chunks).

```bash
# Upload a local dump and import it, waiting for the result (non-zero exit on failure)
coolify database import start <database_uuid> --file ./dump.sql.gz --wait

# Two-step: upload first (prints an upload ID), then import
coolify database import upload <database_uuid> ./dump.sql.gz
coolify database import start <database_uuid> --upload-id <upload_id>

# From S3 storage or from a file already on the database's server
coolify database import start <database_uuid> --s3-storage-uuid <s3-uuid> --s3-path /backups/db.dump
coolify database import start <database_uuid> --server-path /path/on/server/db.dump

# Check status (activity ID is printed by start); --wait to follow, --poll-interval (default 3s)
coolify database import status <database_uuid> <activity_id> --wait

# Restore options
#   --dump-all              backup contains all databases
#   --replace-existing      PostgreSQL: drop matching objects first (old --clean behavior; off by default since v4.4.0)
#   --keep-owners           PostgreSQL: restore owners and privileges
#   --restore-mysql-users   MySQL/MariaDB all-databases: also restore users/passwords/privileges
#   --sqlite-database app.db  SQLite: target database file
```

---

## Services (One-Click)

### List and View

```bash
# List all services
coolify service list

# Get service details
coolify service get <uuid>

# List available service types
coolify service create --list-types
```

### Create Service

```bash
# Examples: wordpress-with-mysql, ghost, n8n, etc.
coolify service create wordpress-with-mysql \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --name "My WordPress" \
  --description "Company blog" \
  --docker-compose "custom compose content" \
  --destination-uuid <uuid> \
  --instant-deploy \
  --tag production \
  --tags "blog,cms"
```

### Lifecycle Management

```bash
coolify service start <uuid>
coolify service stop <uuid>
coolify service restart <uuid>
coolify service delete <uuid>
coolify service move <uuid> --environment-uuid <env-uuid>

# Get logs (requires sub-service name)
coolify service logs <uuid> --sub-service-name wordpress
```

### Service Tags

```bash
coolify service tag list <uuid>
coolify service tag add <uuid> <tag-name>
coolify service tag remove <uuid> <tag-name>
```

### Service Applications (sub-resources)

```bash
# List applications in service
coolify service application list <service-uuid>

# Get application details
coolify service application get <service-uuid> <app-uuid>

# Update application
coolify service application update <service-uuid> <app-uuid>

# Get logs (-n/--lines, default 100 — v1.10.0+)
coolify service application logs <service-uuid> <app-uuid>
coolify service application logs <service-uuid> <app-uuid> -n 500

# Lifecycle
coolify service application start <service-uuid> <app-uuid>
coolify service application restart <service-uuid> <app-uuid>
coolify service application stop <service-uuid> <app-uuid>
```

### Service Databases (sub-resources)

```bash
# List databases in service
coolify service database list <service-uuid>

# Get database details
coolify service database get <service-uuid> <db-uuid>

# Update database (image, log drain, public access)
coolify service database update <service-uuid> <db-uuid>

# Get logs
coolify service database logs <service-uuid> <db-uuid>

# Lifecycle
coolify service database start <service-uuid> <db-uuid>
coolify service database restart <service-uuid> <db-uuid>
coolify service database stop <service-uuid> <db-uuid>

# Import a backup into a service database (v1.10.0+, same source/option flags as `database import start`)
coolify service database import start <service-uuid> <db-uuid> \
  --s3-storage-uuid <s3-uuid> --s3-path /backups/db.dump
coolify service database import upload <service-uuid> <db-uuid> ./dump.sql.gz
coolify service database import status <service-uuid> <db-uuid> <activity_id> --wait
```

### Service Environment Variables

```bash
# Same structure as app env (without --preview)
coolify service env list <uuid>
coolify service env get <uuid> <env_uuid_or_key>
coolify service env create <uuid> --key KEY --value value --build-time --runtime
coolify service env update <uuid> <env_uuid_or_key> --value new-value
coolify service env delete <uuid> <env_uuid> --force
coolify service env sync <uuid> --file .env --build-time --runtime
```

### Service Storage

```bash
coolify service storage list <uuid>

# Requires --resource-uuid (app or db that owns the storage)
coolify service storage create <uuid> \
  --resource-uuid <app-or-db-uuid> \
  --type persistent \
  --mount-path /data

coolify service storage update <uuid> --uuid <storage-uuid> --type persistent
coolify service storage delete <uuid> <storage-uuid>
```

---

## Deployments

### Deploy Resources

```bash
# Deploy by UUID
coolify deploy uuid <uuid>
coolify deploy uuid <uuid> --force
coolify deploy uuid <uuid> --pull-request-id 123
coolify deploy uuid <uuid> --docker-tag 1.2.3  # requires Coolify 4.0.0-beta.471+

# Deploy by name (easier)
coolify deploy name my-application
coolify deploy name my-application --force

# Deploy multiple at once
coolify deploy batch api,worker,frontend
coolify deploy batch api,worker --force
```

### Monitor Deployments

```bash
# List all deployments
coolify deploy list

# Get deployment details
coolify deploy get <deployment-uuid>

# Cancel deployment
coolify deploy cancel <deployment-uuid>
coolify deploy cancel <deployment-uuid> -f
```

---

## Servers

### List and View

```bash
# List all servers
coolify server list
coolify servers list  # alias

# Get server details
coolify server get <uuid>

# List resources deployed on the server (v1.9.0+ shape)
coolify server get <uuid> --resources
coolify server get <uuid> --resources --format json | jq -r '.[] | "\(.type)\t\(.name)\t\(.status)"'
# Since CLI v1.9.0 this calls GET /servers/{uuid}/resources and returns a flat JSON array of
# {id, uuid, name, type, status, created_at, updated_at} — it no longer prints the server
# details, and there is no top-level `resources` key (old: GET /servers/{uuid}?resources=true).

# Get server domains
coolify server domains <uuid>
```

### Add and Remove

```bash
# Add new server
coolify server add <name> <ip> <private_key_uuid>
coolify server add myserver 192.168.1.100 <key-uuid> -p 22 -u root --validate
coolify server add builder 192.168.1.101 <key-uuid> --server-role build   # v1.9.0+

# Update a server (only the given flags change)
coolify server update <uuid> --server-role deployment   # deployment|build|both
# 'deployment' requires another usable build server in the team.
# --is-build-server is deprecated (true → build, false → both) and cannot be combined with --server-role.
# Other flags: --name, --description, --ip, --port, --user, --private-key-uuid, --proxy-type, ...

# Remove server
coolify server remove <uuid>
coolify server remove <uuid> --force                          # also delete all resources on it (v1.9.0+)
coolify server remove <uuid> --force --delete-from-provider   # also delete the VM at Hetzner/Vultr/DigitalOcean — irreversible

# Validate server connection
coolify server validate <uuid>
```

### Server Docker Registries (v1.9.0+)

Requires Coolify v4.4.0+. Coolify runs `docker login` on the server and does not store the password. There is **no password flag** — pipe it with `--password-stdin` or enter it at the no-echo prompt.

```bash
# List registry logins and which resources use them (token needs read:sensitive; -s shows usernames)
coolify server registry list <server_uuid>

# Log in on one or more servers
echo "$GHCR_TOKEN" | coolify server registry login <server_uuid> \
  --registry ghcr.io --username octocat --password-stdin
coolify server registry login <uuid_1> <uuid_2> --registry registry.example.com:5000 -u deploy

# Check that a saved login still works / log out
coolify server registry check <server_uuid> ghcr.io
coolify server registry logout <server_uuid> ghcr.io -f
```

### Server Destinations

```bash
# List destinations
coolify server destinations list <server-uuid>

# Create destination
coolify server destinations create <server-uuid>
```

### Cloud Providers

```bash
# List provider options and provision servers
coolify server hetzner
coolify server digitalocean
coolify server vultr

# Optional: pass --cloud-init '<yaml>' on create (see Cloud-init Scripts)
```

### Server Provisioning on Hostinger (CLI v1.11.0+)

The CLI can now buy a Hostinger VPS and register it in Coolify. This needs a Hostinger cloud token stored in Coolify (`coolify cloud-token create --provider hostinger`) and a Coolify instance with the v4.5.0 Hostinger routes (`/hostinger/*`, `POST /servers/hostinger`).

> **Paid, recurring purchase.** `coolify server hostinger create` buys a VPS that renews until cancelled in Hostinger. Confirm the plan, billing period, data center, and price with the operator before running it, and **do not pass `--force` / `-f`** — that flag skips the purchase confirmation. Declining the prompt, an empty answer, or EOF sends no request.

```bash
# 1. Inspect what you are about to buy (every listing takes the cloud token UUID)
coolify cloud-token list
coolify server hostinger catalog <cloud_token_uuid>            # alias: plans — item_id is the value for --item-id
coolify server hostinger data-centers <cloud_token_uuid>
coolify server hostinger templates <cloud_token_uuid>          # OS images
coolify server hostinger ssh-keys <cloud_token_uuid>           # key contents hidden unless --show-sensitive
coolify server hostinger post-install-scripts <cloud_token_uuid>

# 2. Buy the VPS and add it as a server (paid, recurring)
coolify server hostinger create \
  --cloud-token <cloud_token_uuid> \
  --item-id hostingercom-vps-kvm1-usd-1m \
  --data-center-id <id> \
  --template-id <id> \
  --private-key <coolify_private_key_uuid> \
  --name my-hostinger-vps \
  --validate
```

`catalog` prints one row per plan and billing period; prices are in cents and include the first period. `--item-id` takes the `item_id` from that listing (plan + billing period), `--data-center-id` and `--template-id` take the numeric IDs from the listings above, and `--private-key` is the **Coolify** private key UUID, not a Hostinger key. Optional flags: `--name`, `--ssh-key-ids` (Hostinger SSH key IDs), `--post-install-script-id`, `--enable-backups` (weekly Hostinger backups, **extra cost**, off by default), `--validate`. There is no `--cloud-init` flag on this provider; use `post-install-scripts` instead.

The CLI sends the purchase request exactly once and does not retry on 5xx/429, so a manual retry after an ambiguous error can buy a second VPS:

- **HTTP 202** — Hostinger is still processing the payment and no server exists yet. Check the Hostinger account before retrying.
- **5xx including `hostinger_virtual_machine_id`** — the VM may already have been bought.
- **422** — per-field validation details; **429** — retry after the `Retry-After` value.

---

## GitHub Apps

```bash
# List all GitHub Apps
coolify github list

# Get GitHub App details
coolify github get <app-uuid>

# Create GitHub App integration
coolify github create \
  --name "My GitHub App" \
  --api-url "https://api.github.com" \
  --html-url "https://github.com" \
  --app-id 123456 \
  --installation-id 789012 \
  --client-id "Iv1.abc123" \
  --client-secret "secret" \
  --private-key-uuid <key-uuid> \
  --organization "my-org" \
  --custom-user git \
  --custom-port 22 \
  --webhook-secret "webhook-secret" \
  --system-wide  # cloud only

# Update GitHub App
coolify github update <app-uuid>

# Delete GitHub App
coolify github delete <app-uuid>
coolify github delete <app-uuid> -f

# List accessible repositories
coolify github repos <app-uuid>

# List branches for a repository
coolify github branches <app-uuid> owner/repo
```

---

## GitLab Apps

GitLab App integration (aliases: `gl`, `gitlab-app`, `gitlab-apps`).

```bash
# List / get
coolify gitlab list
coolify gitlab get <app_id_or_uuid>

# Create
coolify gitlab create \
  --name "My GitLab App" \
  --html-url "https://gitlab.com" \
  --client-id "<oauth-app-id>" \
  --client-secret "<oauth-secret>" \
  --redirect-uri "https://<coolify-host>/webhooks/source/gitlab/events/app" \
  --api-url "https://gitlab.com/api/v4" \
  --custom-user git \
  --custom-port 22 \
  --group-name "my-group" \
  --webhook-token "<optional-secret>"

# Update / delete (must not be used by any applications)
coolify gitlab update <app_id_or_uuid> --name "Renamed"
coolify gitlab delete <app_id_or_uuid>
coolify gitlab delete <app_id_or_uuid> -f
```

### Creating an Application from a GitLab App

Confirmed in Coolify `4.3.23` and still true in `4.4.6` (no `private-gitlab-app` route). The API creates the OAuth **source**. The **application** linked to that source is created via UI under "Git Repository (with GitLab App)".

`POST /api/v1/gitlab-apps` only stores the source (`name`, `html_url`, credentials). There is no `POST /api/v1/applications/private-gitlab-app` — this route returns 404. The only application create endpoints are:

- `POST /api/v1/applications/public`
- `POST /api/v1/applications/private-github-app` (`github_app_uuid`)
- `POST /api/v1/applications/private-deploy-key` (`private_key_uuid`)
- `POST /api/v1/applications/dockerfile`
- `POST /api/v1/applications/dockerimage`

After the UI creates the application, `source_type` becomes `App\Models\GitlabApp` and `source_id` is the numeric ID of the source. From there, the API can edit normally: `PATCH /api/v1/applications/{uuid}`, envs, and storages.

While `build_pack` is `dockercompose`, `domains` is rejected with "The domains field cannot be used for dockercompose applications". Change the pack first (`build_pack: dockerfile`, `dockerfile_location`, `ports_exposes`), then send `domains`. Define `ports_exposes` before the first deploy that generates `custom_labels`; changing the port afterward won't regenerate Traefik labels.

Coolify does not create the webhook on the GitLab project. Push-triggered deploys require a project hook at `POST /webhooks/source/gitlab/events` with the source's webhook token. The UI suggests the Git App manages this, but there's no call to `POST /api/v4/projects/:id/hooks` in the code (issue `coollabsio/coolify#11602`).

---

## Notifications

Channels: `email`, `discord`, `slack`, `telegram`, `pushover`, `webhook`. Configure via get/update + `--json`.

```bash
coolify notification get webhook
coolify notification update webhook --json '{"webhook_enabled":true}'

coolify notification get discord
coolify notification update slack --json '{"slack_enabled":true}'
```

---

## Shared Environment Variables

Shared envs at **environment**, **project**, **server**, or **team** scope (`shared-envs` / `sharedenv` aliases).

```bash
# Environment scope
coolify shared-env environment list <project_uuid> <environment>
coolify shared-env environment create <project_uuid> production \
  --key SHARED_API_URL --value "https://api.example.com"
coolify shared-env environment update <project_uuid> production <id> --value "https://api.new.example.com"
coolify shared-env environment delete <project_uuid> production <id>

# Project scope
coolify shared-env project list <project_uuid>
coolify shared-env project create <project_uuid> --key PROJECT_FLAG --value "1"
coolify shared-env project update <project_uuid> <id> --value "0"
coolify shared-env project delete <project_uuid> <id>

# Server scope
coolify shared-env server list <server_uuid>
coolify shared-env server create <server_uuid> --key NODE_ROLE --value "worker"
coolify shared-env server update <server_uuid> <id> --value "api"
coolify shared-env server delete <server_uuid> <id>

# Team scope
coolify shared-env team list
coolify shared-env team create --key ORG_NAME --value "acme"
coolify shared-env team update <id> --value "acme-corp"
coolify shared-env team delete <id>
```

Optional flags on create/update: `--comment`, `--literal`, `--multiline`, `--shown-once`.

---

## Cloud-init Scripts

CRUD for reusable cloud-init scripts. Server create on Hetzner / DigitalOcean / Vultr accepts `--cloud-init` (inline YAML).

```bash
coolify cloud-init list
coolify cloud-init get <uuid>

coolify cloud-init create --name bootstrap --script-file ./cloud-init.yaml
# or: --script "#!/bin/bash\necho hi"

coolify cloud-init update <uuid> --name bootstrap-v2 --script-file ./cloud-init-v2.yaml
coolify cloud-init delete <uuid>

# Attach when provisioning (example)
coolify server hetzner create \
  --cloud-token <cloud-token-uuid> \
  --location <location> \
  --server-type <type> \
  --image <id> \
  --cloud-init "$(cat ./cloud-init.yaml)"
```

Aliases: `cloudinit`, `cloud-init-script`.

---

## Settings (email)

Instance-wide SMTP / Resend settings. **Requires** a root-team admin/owner token with `write:sensitive`.

```bash
coolify settings email get

# Update fields via JSON
coolify settings email update --json '{"smtp_ehlo_domain":"coolify.example.com"}'

# Reset EHLO domain to system default
coolify settings email update --json '{"smtp_ehlo_domain":null}'
```

---

## Secret Manager Integration Tokens

v1.10.0+ / Coolify v4.4.0+. Providers: `doppler`, `infisical`, `vault`. There is **no flag for the provider token** and it is never printed: pipe it with `--provider-token-stdin`, set `COOLIFY_INTEGRATION_TOKEN`, or enter it at the no-echo prompt.

```bash
echo "$DOPPLER_TOKEN" | coolify integration-token create \
  --provider doppler --name prod --provider-token-stdin

# Infisical / Vault need --metadata
#   infisical {"base_url":"...","client_id":"..."}
#   vault     {"base_url":"...","namespace":"..."}   (namespace optional)
echo "$VAULT_TOKEN" | coolify integration-token create \
  --provider vault --name vault --provider-token-stdin \
  --metadata '{"base_url":"https://vault.example.com"}'
```

Then attach it to an app with `coolify app secret-manager set` (see Applications).

---

## Audit Log

v1.10.0+ / Coolify v4.4.0+. Only team admins and owners can read audit events (newest first).

```bash
coolify audit list
coolify audit list --source api --per-page 50
coolify audit list --action deleted --search my-app --page 2
coolify audit list --format json

# --per-page 1-100 (default 25), --page (default 1), --search <text>
# --action created|updated|deleted|... (all = every action)
# --source all|ui|api|mcp|webhook|system|scheduler
# Actor e-mail, token, metadata, changes, IP and user agent are returned only for
# tokens with read:sensitive — use --format json to see them.
```

---

## Tags

```bash
# List all tags for current team
coolify tag list
```

---

## Destinations

```bash
# List Docker network destinations
coolify destination list
coolify destination list --server <server-uuid>

# Get destination
coolify destination get <uuid>

# Create destination
coolify destination create --server <uuid> --network my-network --type standalone
# Types: standalone, swarm

# Delete unused destination
coolify destination delete <uuid>
```

---

## Cloud Provider Tokens

```bash
# Manage Hetzner, DigitalOcean, Vultr, and Hostinger API tokens (hostinger since v1.11.0)
coolify cloud-token list
coolify cloud-token get <uuid>
coolify cloud-token create
coolify cloud-token update <uuid>
coolify cloud-token delete <uuid>
coolify cloud-token validate <uuid>

# Note: Token values redacted by default. Use --show-sensitive with sensitive-data permission
```

---

## Teams

```bash
# List all teams
coolify team list

# Get team details
coolify team get <team_id>

# Get current team
coolify team current

# Allow/deny build fallback to the deployment server when no build server is usable (v1.10.0+)
coolify teams update --build-server-fallback
coolify teams update --build-server-fallback=false

# List team members
coolify team members list
coolify team members list <team_id>
```

---

## Private Keys

```bash
# Commands: private-key, private-keys, key, keys (aliases)

# List all private keys
coolify private-key list

# Add new private key (content or file path)
coolify private-key add <key_name> <private_key_or_file>
coolify private-key add mykey ~/.ssh/id_rsa
coolify private-key add mykey "-----BEGIN OPENSSH PRIVATE KEY-----..."

# Remove private key
coolify private-key remove <uuid>
```

---

## REST API Operations

For direct API access when CLI is not available:

### Authentication

```bash
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)  # includes /api/v1

# Test connection
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/version"
```

### Applications (API)

```bash
# List
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications"

# Get details
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}"

# Start (POST required since v4.2.0)
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/start"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/start?force=true"

# Stop
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/stop"

# Restart
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/restart"
```

### Databases (API)

```bash
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/databases"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/databases/{uuid}/start"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/databases/{uuid}/stop"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/databases/{uuid}/restart"
```

### Services (API)

```bash
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/services/{uuid}/restart"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/services/{uuid}/restart?latest=true"
```

### Deployments (API)

```bash
# List all ongoing
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/deployments"

# List for application
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/deployments/applications/{uuid}?skip=0&take=10"
```

### Servers (API)

```bash
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}"

# Resources deployed on a server (flat array)
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}/resources"

# Registry logins (v4.4.0+)
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}/registries"
```

#### Hostinger provisioning and server transfer (v4.5.0+)

```bash
# Inspect provider catalog before provisioning
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/hostinger/data-centers"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/hostinger/catalog"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/hostinger/templates"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/hostinger/ssh-keys"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/hostinger/post-install-scripts"

# Transfer lifecycle; POST bodies follow the instance's OpenAPI schema
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}/migrate"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}/transfer"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/import/check"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/import"
curl -sS -X POST -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/servers/{uuid}/transfer/complete"
```

These are route sketches, not complete request examples. POST bodies are required where defined by the instance's OpenAPI schema; do not send empty bodies copied from these sketches. Hostinger provisioning is a separate paid operation; inspect plan and data center before purchase.

### Previews, Imports, Audit (API, v4.4.0+)

```bash
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/previews"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/applications/{uuid}/previews/{pr_id}"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/databases/{uuid}/imports/{activity_id}"
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" "$COOLIFY/audit-events"
# Service databases: /services/{uuid}/databases/{database_uuid}/imports
```

---

## Multi-Instance Environments

When operating multiple Coolify instances (e.g., production, staging, development on separate servers), follow these conventions to avoid confusion.

### Environment Variable Naming

Use suffixed variable names to distinguish instances:

```bash
# .env structure for multi-instance
COOLIFY_KEY_PROD=3|abc...      # Production instance token
COOLIFY_PROD=https://cool.prod.example.com/api/v1

COOLIFY_KEY_STAGING=5|def...   # Staging instance token  
COOLIFY_STAGING=https://cool.staging.example.com/api/v1

COOLIFY_KEY_DEV=2|ghi...       # Dev instance token
COOLIFY_DEV=https://cool.dev.example.com/api/v1
```

### CLI Context Setup for Multi-Instance

```bash
# Add all instances as named contexts
coolify context add prod https://cool.prod.example.com "$COOLIFY_KEY_PROD"
coolify context add staging https://cool.staging.example.com "$COOLIFY_KEY_STAGING"
coolify context add dev https://cool.dev.example.com "$COOLIFY_KEY_DEV"

# Set default (usually prod)
coolify context set-default prod

# Always verify which context is active before operations
coolify context list
```

### Finding Which Instance Hosts an App

When you don't know which instance hosts a specific application:

```bash
# Search across all contexts
for ctx in prod staging dev; do
  echo "=== $ctx ==="
  coolify --context=$ctx app list --format json 2>/dev/null | \
    jq -r '.[] | "\(.name) | \(.fqdn // "no-fqdn")"' | \
    grep -i "your-app-name" || echo "(not found)"
done
```

---

## Diagnosing Failed Deployments

### Quick Diagnosis Workflow

```bash
# 1. List recent deployments for the app
coolify app deployments list <app-uuid> --format json | jq '.[0:3]'

# 2. Check status of latest deployment
coolify app deployments list <app-uuid> --format json | jq '.[0] | {status, commit, finished_at}'

# 3. Get deployment logs (latest)
coolify app deployments logs <app-uuid>

# 4. Get detailed debug logs (shows Docker build output)
coolify app deployments logs <app-uuid> --debuglogs

# 5. Get logs for specific deployment
coolify app deployments logs <app-uuid> <deployment-uuid> --debuglogs
```

### Common Build Failures

#### YAML Frontmatter Parsing Error (Astro/MDX sites)

```
incomplete explicit mapping pair; a key node is missed
```

**Cause:** Unquoted colons (`:`) in YAML frontmatter values.

```yaml
# WRONG - colon breaks YAML parser
description: Install this tool: it's great

# CORRECT - quote the value
description: "Install this tool: it's great"
```

#### npm ci / npm install Failures

```
npm ERR! Could not resolve dependency
```

**Cause:** Lock file mismatch or missing dependencies.

```bash
# Fix locally, then push
rm -rf node_modules package-lock.json
npm install
git add package-lock.json
git commit -m "fix: regenerate lock file"
git push
```

#### Dockerfile Build Failures

```
ERROR: failed to solve: process "/bin/sh -c npm run build" did not complete successfully
```

**Cause:** Build command fails inside container. Check the lines above the error for the actual failure (often a code/config issue, not Docker).

#### Health Check Timeout

```
Healthcheck failed after X attempts
```

**Cause:** App didn't respond on the configured health check path/port in time.

```bash
# Check health check config
coolify app get <uuid> --format json | jq '{health_check_enabled, health_check_path, health_check_port}'

# Common fixes:
# - Increase start period in Coolify UI
# - Verify the health check path returns 200
# - Check if app binds to 0.0.0.0, not 127.0.0.1
```

### Interpreting Deployment Logs JSON

The `logs` field in deployment JSON contains an array of log entries:

```bash
# Extract just error messages
coolify app deployments list <uuid> --format json | \
  jq -r '.[0].logs' | jq -r '.[] | select(.type == "stderr") | .output'

# Find the actual failure point
coolify app deployments list <uuid> --format json | \
  jq -r '.[0].logs' | jq -r '.[] | select(.output | test("error|ERROR|failed|FAILED"; "i")) | .output'
```

---

## Troubleshooting

### Error: 405 Method Not Allowed (v4.2.0+)

State-changing endpoints require POST method:

```bash
# WRONG
curl -sS "$COOLIFY/applications/{uuid}/start"

# CORRECT
curl -sS -X POST "$COOLIFY/applications/{uuid}/start"
```

Affected endpoints: `/start`, `/stop`, `/restart`, `/enable`, `/disable`

### Error: 403 "You are not allowed to access the API"

1. Verify API is enabled at `<INSTANCE_URL>/settings/advanced`
2. Check IP allowlist
3. **Member role is read-only (v4.2.0+)** - promote to higher role for write access
4. Regenerate token at Dashboard → Security → API Tokens

### Error: 401 "Unauthenticated"

```bash
# Verify Bearer prefix
Authorization: Bearer YOUR_TOKEN

# CLI: verify context
coolify context verify
```

### Error: 400 on Persistent Storage with host_path (v4.3.22+)

`host_path` was removed from persistent volumes. API rejects requests including it.

```bash
# WRONG (v4.3.22+)
--host-path /opt/data  # ❌ Rejected

# CORRECT: use named volumes only
--name my-volume
```

### Error: Invalid Environment Variable Name (v4.3.15+)

Build-time env var names are now validated before builds start. Invalid names are rejected with specific error messages.

```bash
# WRONG
MY-VAR=value      # Hyphens not allowed
2NDVAR=value      # Cannot start with number

# CORRECT
MY_VAR=value
SECOND_VAR=value
```

### Restart Limit Reached — Container Invisible (fixed v4.3.15)

Fixed: Stopped containers are now visible after reaching restart limit. Actions available: Retry deployment, Remove container.

### GitLab App Does Not Create Application via API

`POST /applications/private-gitlab-app` returns 404 in Coolify 4.3.x. Create the application via UI with the GitLab App, then edit via `PATCH /applications/{uuid}`. With `build_pack=dockercompose`, use `docker_compose_domains`, not `domains`. See the "GitLab Apps" section for details.

### Error: 404 on context verify

```bash
# CLI context: URL WITHOUT /api/v1
coolify context add my-coolify http://192.168.1.100:8000 "$TOKEN"

# Direct API: URL WITH /api/v1
COOLIFY=http://192.168.1.100:8000/api/v1
```

### Token with pipe (|) breaks shell

```bash
# WRONG
source .env

# CORRECT
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
```

### DNS Resolution Failures (v4.3.22+ fallback)

If configured DNS resolvers return no address records, Coolify now falls back to the system DNS resolver automatically.

### HTTP 400 with Large Cookie Headers (fixed v4.3.18)

nginx request header buffers were increased. If you're on an older version, large Cookie headers may return HTTP 400 before reaching Coolify.

---

## Common Workflows

### Deploy New Application

```bash
# 1. Setup context
coolify context add prod https://coolify.example.com "$TOKEN" --default
coolify context verify

# 2. List servers
coolify server list

# 3. Create application
coolify app create public \
  --server-uuid <server-uuid> \
  --project-uuid <project-uuid> \
  --environment-name production \
  --git-repository "https://github.com/user/repo" \
  --git-branch main \
  --build-pack nixpacks \
  --ports-exposes 3000 \
  --instant-deploy

# 4. Monitor deployment
coolify app deployments logs <uuid> -f
```

### Multi-Environment Setup

```bash
# Add contexts
coolify context add prod https://prod.coolify.io "$PROD_TOKEN" --default
coolify context add staging https://staging.coolify.io "$STAGING_TOKEN"
coolify context add dev https://dev.coolify.io "$DEV_TOKEN"

# Use different contexts
coolify --context=prod app list
coolify --context=staging deploy name api
coolify --context=dev resource list
```

### Batch Deploy

```bash
# Deploy multiple services at once
coolify deploy batch api,worker,frontend --force

# Monitor
coolify deploy list
```

### Database with Scheduled Backups

```bash
# Create database
coolify database create postgresql \
  --server-uuid <uuid> \
  --project-uuid <uuid> \
  --environment-name production \
  --name mydb \
  --instant-deploy

# Configure backup
coolify database backup create <db-uuid> \
  --frequency "0 2 * * *" \
  --enabled \
  --retention-days-locally 7 \
  --save-s3 \
  --s3-storage-uuid <s3-uuid>
```

### Environment Variables from File

```bash
# Sync .env file (updates existing, creates new, keeps others)
coolify app env sync <uuid> --file .env.production --build-time --runtime

# Restart to apply
coolify app restart <uuid>
```

---

## LLM / AI Agent Integration

For AI agents using Coolify CLI (prefer the **v1.11.0** pin this skill targets):
- Quick instructions (tag): https://raw.githubusercontent.com/coollabsio/coolify-cli/v1.11.0/llms.txt
- Full command catalog (tag): https://raw.githubusercontent.com/coollabsio/coolify-cli/v1.11.0/llms-full.txt
- Latest on main: https://raw.githubusercontent.com/coollabsio/coolify-cli/main/llms.txt and `llms-full.txt`

---

## References

- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **CLI Releases**: https://github.com/coollabsio/coolify-cli/releases
- **CLI v1.11.0 tag**: https://github.com/coollabsio/coolify-cli/tree/v1.11.0 (`3738289a2a47050fa70007a571fbed00cb1c6d6e`)
- **Coolify v4.5.3 OpenAPI schema**: https://raw.githubusercontent.com/coollabsio/coolify/v4.5.3/openapi.json
- **Coolify MCP docs**: https://coolify.io/docs/mcp/overview
- **Coolify v4.4.0 release notes**: https://github.com/coollabsio/coolify/releases/tag/v4.4.0
- **Coolify Releases**: https://github.com/coollabsio/coolify/releases
- **Official Docs**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **Coolify Core**: https://github.com/coollabsio/coolify

---

## Changelog

### v3.4 (2026-10-29)
- Pinned coolify-cli v1.11.0 (`3738289`) — Coolify surface unchanged, still v4.5.3
- Added `server hostinger catalog|data-centers|templates|ssh-keys|post-install-scripts` and `server hostinger create` (paid VPS purchase)
- Added a Hostinger provisioning section: inspect first, no `--force`, `--enable-backups` extra cost, and 202/5xx/429 purchase safety
- Corrected the CLI/API coverage note — Hostinger is in the CLI now, server transfer/migration is still API-only
- Documented sensitive-field masking in `table`, `json`, and `pretty` since v1.11.0, and that `context get` never prints the token
- Added `--provider hostinger` to cloud token docs

### v3.3 (2026-10-28)
- Reviewed Coolify releases through v4.5.3 and updated the version metadata without implying all instances are upgraded
- Documented v4.5 sensitive-data permissions, Cloudflare client IP allow-lists, service deletion change, and timeout retry behavior
- Added operational notes for preview variables, build fixes, update backups, server patching beta, and the v4.4.7 security update
- Added CLI `mcp enable|disable`, MCP endpoint setup/permissions and v4.5 resource-management capabilities
- Compared v4.4.7 and v4.5.0–v4.5.3 OpenAPI specs; documented new Hostinger/server-transfer routes and v4.5 request contract changes

### v3.2 (2026-10-19)
- Pinned coolify-cli v1.10.0 (`e1d6094`) and Coolify v4.4.6
- Added `app previews list/get/create/update/logs` (full preview CRUD + runtime logs)
- Added `database import start/upload/status` and `service database import ...` (restore from file, upload, S3, server path)
- Added `audit list`, `integration-token create`, `app secret-manager set` (Doppler/Infisical/Vault)
- Added `server registry list/login/check/logout`, `server remove --force/--delete-from-provider`, `--server-role` on `server add/update`
- Documented the new `server get --resources` shape (flat array from `GET /servers/{uuid}/resources`)
- Added `sqlite` database type, `teams update --build-server-fallback`, `project environments get`, `service application logs -n`
- Added Coolify v4.4.x changes (secret managers, audit log, server roles, restore defaults, registry logins)

### v3.1 (2026-09-22)
- Updated for Coolify v4.3.23
- Documented breaking changes: `host_path` removal (v4.3.22), Sentinel mandatory (v4.3.19), restart limits opt-in (v4.3.21)
- Added per-domain internal port overrides (v4.3.15+)
- Added preview deployment runtime logs endpoint (v4.3.23)
- Added `lines=all` parameter for log APIs (v4.3.20)
- Updated backup docs: S3 streaming, missing backup alerts (v4.3.18)
- Added new troubleshooting entries: host_path rejection, env var validation, DNS fallback
- CLI v1.8.0 highlights: token redaction, SMTP/Resend settings, retention storage numeric values

### v3.0 (2026-09-19)
- Initial v3 release with CLI v1.8.0 pin
