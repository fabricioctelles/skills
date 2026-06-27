---
name: coolify-operator
description: Master Coolify operator for self-hosted deployment platform. Use when the user mentions 'coolify', 'deploy on coolify', 'list/restart/redeploy applications', 'view coolify logs', 'coolify API/CLI', 'manage coolify servers/databases/apps', or 'coolify context'. Automates deployments and management via REST API or official CLI.
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-08
  license: MIT
  category: ci-cd-and-deployment
---

# Coolify Operator

Skill for operating Coolify instances through the **REST API** or **official CLI**. Coolify is a self-hosted open-source platform alternative to Heroku/Vercel/Netlify for deploying applications, databases, and services.

## When to use this skill

- Connect to Coolify instances (via API or CLI)
- List and manage applications, services, databases, and servers
- Deploy, restart, or stop applications
- View logs and deployment status
- Manage environment variables
- Operate multiple Coolify instances (contexts)
- Troubleshoot Coolify connection issues

## Fundamental concepts

### Authentication

**REST API:**
- Base endpoint: `https://YOUR-HOST/api/v1` (always with `/api/v1` at the end)
- Authentication: `Authorization: Bearer YOUR_TOKEN`
- Token obtained at: Coolify Dashboard → Keys & Tokens → API Tokens

**CLI:**
- Installs contexts that store HOST + TOKEN
- HOST in context is WITHOUT `/api/v1` (just the base URL)
- CLI adds `/api/v1` automatically

### Configuration with pipe in token

⚠️ **IMPORTANT**: Coolify tokens often contain `|` (e.g., `3|abc123...`). Never use `source .env` as this breaks in the shell.

**Safe .env reading:**
```bash
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)
```

**Expected .env format:**
```bash
COOLIFY_KEY=3|abc123def456...
COOLIFY=http://192.168.1.XXX:8000/api/v1
```

### UUIDs

Coolify uses UUIDs to identify resources:
- Applications: `app-uuid`
- Servers: `server-uuid`
- Databases: `db-uuid`
- Services: `service-uuid`

## CLI Operations

### Initial setup

```bash
# Read token from .env safely
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)

# Add context (URL WITHOUT /api/v1)
coolify context add -d -f my-coolify http://192.168.1.XXX:8000 "$COOLIFY_KEY"

# Use the context
coolify context use my-coolify

# Verify connection
coolify context verify

# Check API version
coolify context version
```

### Context management

```bash
# List contexts
coolify context list

# Add multiple contexts
coolify context add prod https://prod.coolify.io "$PROD_TOKEN" --default
coolify context add staging https://staging.coolify.io "$STAGING_TOKEN"
coolify context add dev https://dev.coolify.io "$DEV_TOKEN"

# Switch default context
coolify context use staging

# Use specific context in a command
coolify --context=prod app list

# Update token for a context
coolify context set-token prod new-token-here

# Remove context
coolify context delete dev
```

### Application operations

```bash
# List all applications
coolify app list

# View application details
coolify app get <uuid>

# --- LIFECYCLE ---
# Start (deploy) application
coolify app start <uuid>

# Stop application
coolify app stop <uuid>

# Restart application
coolify app restart <uuid>

# --- LOGS ---
# View application logs
coolify app logs <uuid>

# --- ENVIRONMENT VARIABLES ---
# List environment variables
coolify app env list <uuid>

# Create environment variable
coolify app env create <uuid> --key API_KEY --value secret123

# Sync environment variables from .env file
coolify app env sync <uuid> --file .env
coolify app env sync <uuid> --file .env.production --build-time --preview
```

### Server operations

```bash
# List servers
coolify server list

# View server details (including resources)
coolify server get <uuid> --resources

# Add new server (with validation)
coolify server add myserver 192.168.1.100 <key-uuid> --validate
```

### Team operations

```bash
# List available teams
coolify team list

# View current team
coolify team current

# List team members
coolify team members list
```

### Global flags

```bash
# Specify context
coolify --context <name> ...

# Override host
coolify --host <fqdn> ...

# Direct token (bypasses context)
coolify --token <token> ...

# Output format (table, json, pretty)
coolify --format json ...

# Show sensitive data
coolify -s ...
coolify --show-sensitive ...

# Force operation
coolify -f ...
coolify --force ...

# Debug mode
coolify --debug ...
```

## REST API Operations

### Authentication and testing

```bash
# Read credentials from .env safely
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
COOLIFY=$(sed -n 's/^COOLIFY=//p' .env)

# Test connection
curl -sS -i \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/version"

# Expected result: HTTP 200 + {"version": "4.0.0-beta.xxx"}
```

### Applications

```bash
# List applications
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications"

# View application details
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}"

# Start (deploy) application
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/start"

# Query param flags:
# ?force=true          - Force rebuild
# ?instant_deploy=true - Skip queue

# Stop application
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/stop"

# Restart application
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/restart"

# Example response:
# {
#   "message": "Restart request queued.",
#   "deployment_uuid": "doogksw"
# }
```

### Deployments

```bash
# List all ongoing deployments
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/deployments"

# List deployments for an application (with pagination)
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/deployments/applications/{uuid}?skip=0&take=10"
```

### Servers

```bash
# List servers
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/servers"

# View server details
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/servers/{uuid}"
```

### Databases

```bash
# List databases
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases"

# Start database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/start"

# Stop database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/stop"

# Restart database
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/databases/{uuid}/restart"
```

### Services

```bash
# Restart service
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/services/{uuid}/restart"

# Query params:
# ?latest=true - Pull latest images

# Response:
# {"message": "Service restaring request queued."}
```

## Troubleshooting

### Error: 403 "You are not allowed to access the API"

**Cause:** Invalid token or no permission for the instance.

**Solution:**
1. Ask the user to verify in the instance at <INSTANCE_URL>/settings/advanced whether the API is enabled and the client IP is allowed
2. Regenerate token at: Dashboard → Keys & Tokens → API Tokens
3. Update `.env` or CLI context
4. Verify that the correct instance is being used

### Error: 401 "Unauthenticated"

**Cause:** Incorrect authentication header or token not sent.

**Solution:**
```bash
# Verify that Bearer is being used (not just "Token")
Authorization: Bearer YOUR_TOKEN

# CLI: verify context
coolify context verify
```

### Error: 404 on context verify

**Cause:** CLI context URL is incorrect (probably with `/api/v1` in the wrong place).

**Solution:**
```bash
# CLI context must have URL WITHOUT /api/v1
coolify context add my-coolify http://192.168.1.XXX:8000 "$TOKEN"

# Direct API must have URL WITH /api/v1
COOLIFY=http://192.168.1.XXX:8000/api/v1
```

### Cloudflare Tunnel is not the cause

If the API already returns valid JSON from Coolify (even if it's an auth error), the Cloudflare tunnel is working. The problem is authentication, not connectivity.

### Token with pipe (|) breaks shell

```bash
# ❌ WRONG - breaks with pipe
source .env

# ✅ CORRECT - safe reading
COOLIFY_KEY=$(sed -n 's/^COOLIFY_KEY=//p' .env)
```

## Common workflows

### Full deploy of a new application

```bash
# 1. Connect to Coolify
coolify context add prod https://coolify.your-domain.com "$TOKEN" --default
coolify context verify

# 2. List available servers
coolify server list

# 3. Deploy (via dashboard UI or API)
# Note: app creation is better via UI, API is for operations

# 4. List apps to get UUID
coolify app list

# 5. Start the application
coolify app start <uuid>

# 6. View deploy logs
coolify app logs <uuid>
```

### Redeploy with force rebuild

```bash
# Via CLI
coolify app restart <uuid>

# Via API with forced rebuild
curl -sS \
  -H "Authorization: Bearer $COOLIFY_KEY" \
  "$COOLIFY/applications/{uuid}/start?force=true"
```

### Update environment variables

```bash
# Option 1: Sync from file
coolify app env sync <uuid> --file .env.production

# Option 2: Create individually
coolify app env create <uuid> --key API_URL --value https://api.example.com
coolify app env create <uuid> --key API_KEY --value secret123

# 3. Restart to apply changes
coolify app restart <uuid>
```

### Multi-environment monitoring

```bash
# Production
coolify --context=prod app list
coolify --context=prod app logs <prod-app-uuid>

# Staging
coolify --context=staging app list
coolify --context=staging app logs <staging-app-uuid>

# Development
coolify --context=dev app list
coolify --context=dev server list
```

## Important resources

### API response structure

**Application:**
```json
{
  "id": 123,
  "uuid": "app-uuid-123",
  "name": "my-app",
  "fqdn": "app.example.com",
  "status": "running",
  "git_repository": "https://github.com/user/repo",
  "git_branch": "main",
  "git_commit_sha": "abc123",
  "build_pack": "nixpacks",
  "ports_exposes": "3000",
  "health_check_enabled": true,
  "environment_id": 1,
  "destination_id": 1
}
```

**Server:**
```json
{
  "id": 1,
  "uuid": "server-uuid-123",
  "name": "main-server",
  "ip": "192.168.1.100",
  "user": "root",
  "port": 22,
  "settings": {
    "is_reachable": true,
    "is_usable": true,
    "concurrent_builds": 1
  }
}
```

**Deployment:**
```json
{
  "id": 456,
  "uuid": "deployment-uuid-456",
  "status": "finished",
  "deployment_uuid": "dep-123",
  "application_id": 123
}
```

## Usage tips

1. **Always verify UUIDs**: Use `coolify app list` or API to confirm UUIDs before operations
2. **Contexts for multi-environment**: Configure one context for each environment (dev/staging/prod)
3. **Real-time logs**: Use `coolify app logs <uuid>` during deploys
4. **Force rebuild when needed**: `?force=true` on start ensures complete rebuild
5. **Token security**: Never commit tokens. Use `.env` with `.gitignore`
6. **JSON format for scripts**: Use `--format json` in CLI for parsing with `jq`

## Quality Checklist

Before executing any operation, verify:

- [ ] `.env` file present with correct `COOLIFY_KEY` and `COOLIFY`
- [ ] Token read safely (using `sed` or appropriate method, not `source`)
- [ ] Correct context selected (`coolify context use <name>`)
- [ ] Connection verified (`coolify context verify`)
- [ ] UUIDs confirmed before destructive operations
- [ ] Endpoint URL correct (API has `/api/v1`, CLI context does not)
- [ ] Authentication headers included in API calls (`Authorization: Bearer <token>`)
- [ ] Error handling implemented (401, 403, 404, 500)
- [ ] Logs checked in case of deploy failure
- [ ] Critical operations (delete, stop) executed with confirmation

## References

- **Official documentation**: https://coolify.io/docs
- **API Reference**: https://coolify.io/docs/api-reference
- **CLI GitHub**: https://github.com/coollabsio/coolify-cli
- **Coolify Core**: https://github.com/coollabsio/coolify
