---
name: "pier-cloud"
description: "This skill should be used when the user needs to consume the Pier Cloud (Lighthouse) API for cloud cost management — including JWT authentication, listing contexts, workspaces, and FinOps data views. Trigger whenever there is a need to integrate, automate, or debug calls to the Pier Cloud platform via Python, Node.js, or cURL."
metadata:
  author: ft.ia.br
  version: "1.1"
  date: 2026-03-05
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
  keywords: ["pier", "piercloud", "lighthouse", "api", "finops", "cloud", "costs"]
  category: library-and-api-reference
---

# Pier Cloud API

## Prerequisites

### Credentials

Locate the `.env` file in the skill directory with the following variables:

```env
PIERCLOUD_CLIENT_ID=your_client_id
PIERCLOUD_CLIENT_SECRET=your_client_secret
PIERCLOUD_TENANCY_ID=your_tenancy_id
```

If the `.env` file does not exist, inform the user that credentials must be obtained from the Pier Cloud platform before proceeding. Do not proceed without the `.env` file.

> Note: `PIERCLOUD_TENANCY_ID` is equivalent to the former `PIERCLOUD_BUSINESS_ID`. Scripts accept both as fallback.

### Python Dependencies

```bash
pip install requests python-dotenv
```

## Basic Configuration

The API uses JWT authentication. Required flow:

1. Authenticate via `POST /auth` with `client_id` and `client_secret` to obtain a JWT token
2. Include the token in all requests: `Authorization: Bearer {token}`
3. Renew the token upon expiration (default validity: 1 hour)

**Base URL**: `https://api.piercloud.io`

Verify the connection by running:

```bash
python scripts/pier-cloud-auth.py
```

## Available Scripts

Ready-to-use scripts in `scripts/`. See `scripts/README.md` for detailed instructions.

| Script | Description |
|--------|-------------|
| `pier-cloud-auth.py` | Authenticate and obtain JWT token |
| `pier-cloud-list-contexts.py` | List available contexts |
| `pier-cloud-list-workspaces.py` | List workspaces with pagination |
| `pier-cloud-get-workspace.py` | Get specific workspace details |
| `pier-cloud-get-all-workspaces.py` | Get all workspaces (automatic pagination) |
| `pier-cloud-list-views.py` | List views for a workspace |
| `pier-cloud-get-view.py` | Get specific view information |
| `pier-cloud-get-view-data.py` | Get view data with filters |
| `pier_cloud_client.py` | Robust client with CLI and reusable library |

> Note: Workspace-groups scripts (`pier-cloud-list-workspace-groups.py`, `pier-cloud-get-workspace-group.py`) do not work — the corresponding endpoints do not exist in the current API.

## Workflows

Follow the detailed workflows with request and response examples in `references/REFERENCE.md`:

- **Workflow 1** — Authentication and Token Retrieval
- **Workflow 2** — List Contexts
- **Workflow 3** — List Workspaces
- **Workflow 4** — Get Workspace Details
- **Workflow 5** — Get All Workspaces (Automatic Pagination)
- **Workflow 6** — Robust Client with Retry and Token Renewal
- **Workflow 9** — List Workspace Views
- **Workflow 10** — Get View Information
- **Workflow 11** — Get View Data with Filters

For endpoint reference, parameters, response structures, and cURL examples, see `references/REFERENCE.md`.

For error diagnosis (401, 403, 404, timeout, rate limiting), see `references/TROUBLESHOOTING.md`.

## Additional Resources

- **API Docs**: https://docs.piercloud.com/api-docs-pier-cloud
- **Pier Cloud Platform**: https://piercloud.com/en/

## Quality Checklist

- [ ] `.env` file present with `PIERCLOUD_CLIENT_ID`, `PIERCLOUD_CLIENT_SECRET`, and `PIERCLOUD_TENANCY_ID`
- [ ] Python dependencies installed (`requests`, `python-dotenv`)
- [ ] Authentication successful (JWT token obtained without errors)
- [ ] Correct endpoint being used (default `/lighthouse/tenancies/{tenancy_id}/...`)
- [ ] Token being renewed before expiration in long sessions
- [ ] Workspace/view IDs confirmed via listing before using directly
- [ ] Errors handled per `references/TROUBLESHOOTING.md`
