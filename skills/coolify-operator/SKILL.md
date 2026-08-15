---
name: coolify-operator
description: Master Coolify operator for self-hosted deployment platform. Use when the user mentions 'coolify', 'deploy on coolify', 'list/restart/redeploy applications', 'view coolify logs', 'coolify API/CLI', 'manage coolify servers/databases/apps', or 'coolify context'. Automates deployments and management via REST API or official CLI.
metadata:
  author: ft.ia.br
  version: "2.0"
  date: 2026-08-15
  license: MIT
  category: ci-cd-and-deployment
  coolify_cli_version: "latest"
---

# Coolify Operator

Skill for operating Coolify instances through the **official CLI** or **REST API**. Coolify is a self-hosted open-source platform alternative to Heroku/Vercel/Netlify for deploying applications, databases, and services.

## When to use this skill

- Connect to Coolify instances (via CLI contexts or API)
- Create, list, and manage applications, services, databases, and servers
- Deploy, restart, or stop resources
- View logs and deployment status
- Manage environment variables and storage
- Configure backups for databases
- Operate multiple Coolify instances (contexts)
- Integrate with GitHub Apps for private repositories
- Provision servers on cloud providers (Hetzner, DigitalOcean, Vultr)

## CLI Installation

```bash
# Linux/macOS (recommended)
curl -fsSL https://raw.githubusercontent.com/coollabsio/coolify-cli/main/scripts/install.sh | bash

# Homebrew (macOS/Linux)
brew install coollabsio/coolify-cli/coolify-cli

# Go install
go install github.com/coollabsio/coolify-cli/coolify@latest
```

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

All commands support these flags:

```bash
--context <name>     # Use specific context instead of default
--token <token>      # Override authentication token
--format <format>    # Output: table (default), json, pretty
-s, --show-sensitive # Show sensitive information (tokens, IPs)
--debug              # Enable debug mode
```

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

```bash
# List all configured contexts
coolify context list

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

```bash
# List all projects
coolify projects list

# Get project environments
coolify projects get <uuid>

# Create new project
coolify projects create --name "My Project" --description "Description"
```

### Resources

```bash
# List all resources (apps, databases, services)
coolify resources list
```

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

# Limit lines
coolify app logs <uuid> -n 50

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
coolify app env sync <uuid> -f .env
coolify app env sync <uuid> -f .env.production --build-time --runtime --preview --is-literal
```

### Application Storage

```bash
# List storages
coolify app storage list <uuid>

# Create persistent volume
coolify app storage create <uuid> \
  --type persistent \
  --mount-path /data \
  --name my-volume \
  --host-path /opt/data

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
coolify database env sync <uuid> -f .env
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
  --retention-max-storage-locally "1GB" \
  --retention-amount-s3 30 \
  --retention-days-s3 30 \
  --retention-max-storage-s3 "10GB" \
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
coolify service env sync <uuid> -f .env --build-time --runtime
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
coolify --context=dev resources list
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
coolify app env sync <uuid> -f .env.production --build-time --runtime

# Restart to apply
coolify app restart <uuid>
```

---

## LLM / AI Agent Integration

For AI agents using Coolify CLI:
- Quick instructions: https://raw.githubusercontent.com/coollabsio/coolify-cli/main/llms.txt
- Full command catalog: https://raw.githubusercontent.com/coollabsio/coolify-cli/main/llms-full.txt

---

## References

- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **Official Docs**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **Coolify Core**: https://github.com/coollabsio/coolify
