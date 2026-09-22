---
name: coolify-operator
description: Master Coolify operator for self-hosted deployment platform. Use when the user mentions 'coolify', 'deploy on coolify', 'list/restart/redeploy applications', 'view coolify logs', 'coolify API/CLI', 'manage coolify servers/databases/apps', or 'coolify context'. Automates deployments and management via REST API or official CLI.
metadata:
  author: ft.ia.br
  version: "3.1"
  date: 2026-09-22
  license: MIT
  category: ci-cd-and-deployment
  coolify_cli_version: "1.8.0"
  coolify_version: "4.3.23"
  upstream_commit: "ff0ea90fc40e2d5f10e993f79759f705e5e6af10"
---

# Coolify Operator

Skill for operating Coolify instances through the **official CLI** or **REST API**. Coolify is a self-hosted open-source platform alternative to Heroku/Vercel/Netlify for deploying applications, databases, and services.

**Pinned upstream:** coolify-cli **v1.8.0** (`ff0ea90fc40e2d5f10e993f79759f705e5e6af10`) — Coolify v4 surface. Prefer command forms from `llms.txt` / `llms-full.txt` on that tag.

**Coolify version tested:** v4.3.23 (September 2026)

### CLI v1.8.0 Highlights

- **New:** Commands for instance-wide SMTP/Resend settings (`coolify settings email get/update`)
- **Security:** API tokens redacted by default in `context list` output (use `--show-sensitive` to reveal)
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
- Manage cloud-init scripts and provision servers (Hetzner, DigitalOcean, Vultr)

---

## Recent Breaking Changes (v4.3.x)

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

Pin a version on Windows with `$env:COOLIFY_VERSION='v1.8.0'` before `irm ... | iex`. User-local install: `$env:COOLIFY_USER_INSTALL=1`.

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

All commands support these flags (match coolify-cli v1.8.0):

```bash
--context <name>              # Use specific context instead of default
--token <token>               # Override authentication token
--format table|json|pretty    # Output format (default: table)
-s, --show-sensitive          # Reveal sensitive fields (tokens, IPs, emails)
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

Tokens, IPs, and emails are **hidden by default** in `coolify context list` / `get` (v1.8.0+). Pass `-s` / `--show-sensitive` to reveal them. The config file still stores plaintext tokens — do not commit it.

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
```

### Resources

```bash
# List all resources (apps, databases, services)
coolify resource list
```

### Command aliases (v1.8)

Prefer primary forms from `llms.txt`. These aliases still work:

- `coolify app` | `apps` | `application` | `applications`
- `coolify service` | `services` | `svc`
- `coolify database` | `databases` | `db` | `dbs`
- `coolify project` | `projects`
- `coolify resource` | `resources`
- `coolify server` | `servers`
- `coolify teams` | `team`
- `coolify github` | `gh` (and GitLab: `gitlab` | `gl` | `gitlab-app`)

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

```bash
# Delete preview deployment
coolify app previews delete <app_uuid> <pr_id>
coolify app previews delete <app_uuid> <pr_id> --force

# Get runtime logs for preview deployment (v4.3.23+)
# API: GET /api/v1/applications/{uuid}/previews/{pr_id}/logs
# Params: lines (int or "all"), timestamps (bool)
curl -sS -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/previews/{pr_id}/logs?lines=100&timestamps=true"
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
# Supported types: postgresql, mysql, mariadb, mongodb, redis, keydb, clickhouse, dragonfly

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
```

### Update and Delete

```bash
# Update database configuration
coolify database update <uuid> --name "New Name"

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

# Get logs
coolify service application logs <service-uuid> <app-uuid>

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

# Get server with resources status
coolify server get <uuid> --resources

# Get server domains
coolify server domains <uuid>
```

### Add and Remove

```bash
# Add new server
coolify server add <name> <ip> <private_key_uuid>
coolify server add myserver 192.168.1.100 <key-uuid> -p 22 -u root --validate

# Remove server
coolify server remove <uuid>

# Validate server connection
coolify server validate <uuid>
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

Confirmed in Coolify `4.3.23`. The API creates the OAuth **source**. The **application** linked to that source is created via UI under "Git Repository (with GitLab App)".

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
# Manage Hetzner, DigitalOcean, Vultr API tokens
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

For AI agents using Coolify CLI (prefer the **v1.8.0** pin this skill targets):
- Quick instructions (tag): https://raw.githubusercontent.com/coollabsio/coolify-cli/v1.8.0/llms.txt
- Full command catalog (tag): https://raw.githubusercontent.com/coollabsio/coolify-cli/v1.8.0/llms-full.txt
- Latest on main: https://raw.githubusercontent.com/coollabsio/coolify-cli/main/llms.txt and `llms-full.txt`

---

## References

- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **CLI Releases**: https://github.com/coollabsio/coolify-cli/releases
- **CLI v1.8.0 tag**: https://github.com/coollabsio/coolify-cli/tree/v1.8.0 (`ff0ea90fc40e2d5f10e993f79759f705e5e6af10`)
- **Coolify Releases**: https://github.com/coollabsio/coolify/releases
- **Official Docs**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **Coolify Core**: https://github.com/coollabsio/coolify

---

## Changelog

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
