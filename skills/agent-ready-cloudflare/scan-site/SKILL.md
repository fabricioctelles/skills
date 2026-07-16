---
name: agent-ready-scan-site
description: >
  Sub-skill de agent-ready-cloudflare: Skill: Scan Site for Agent Readiness
---
# Skill: Scan Site for Agent Readiness

## What This Skill Does

Scans any website URL and checks whether it implements the standards and protocols that make it accessible to AI agents. Checks 18 standards across 5 categories: discoverability, content accessibility, bot access control, API/auth/MCP discovery, and commerce. Returns a readiness level (0-5), the status of all 18 checks, and fix instructions for any failing checks.

## When to Use It

- Checking whether a site supports agent protocols (MCP, robots.txt, Link headers, etc.)
- Debugging why a site is missing specific agent-readiness checks
- Getting actionable fix instructions to improve a site's agent readiness
- Comparing agent readiness across multiple sites

## How to Call It

Send a POST request to the scan API:

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://example.com", "format": "agent"}
```

### Parameters

- `url` (required): The URL to scan. Must be a valid HTTP or HTTPS URL.
- `format` (optional): Set to `"agent"` for a markdown response with fix instructions, or `"json"` (default) for structured data.

### Using the MCP Server

Alternatively, connect to the MCP server at:

```
https://isitagentready.com/mcp
```

Call the `scan_site` tool with a `url` parameter.

## How to Interpret Results

### JSON Format

The response includes:

- `level`: Integer 0-5 indicating overall readiness
- `levelName`: Human-readable level name (e.g., "Agent-Readable")
- `checks`: Object with 5 categories, each containing individual check results
- `nextLevel`: What's needed to reach the next level
- Each check has `status` ("pass", "fail", or "unableToCheck") and a `message`

### Agent Format

Returns a markdown document listing:
- The site's current score (e.g., "3/5 Agent-Readable")
- All failing checks with descriptions and fix instructions
- If all checks pass, a confirmation message

### Level Scale

| Level | Name | Key Requirements |
|-------|------|-----------------|
| 0 | Not Ready | Fewer than 2 of: robots.txt, sitemap, Link headers |
| 1 | Basic Web Presence | 2 of 3: robots.txt, sitemap, Link headers |
| 2 | Bot-Aware | Level 1 + both: AI bot rules in robots.txt, Content Signals |
| 3 | Agent-Readable | Level 2 + markdown content negotiation |
| 4 | Agent-Integrated | Level 3 + 1 of 4: MCP Server Card, agent skills, API catalog, WebMCP |
| 5 | Agent-Native | Level 4 + 2 of 4: Web Bot Auth, all integrations, commerce (UCP/x402), auth metadata |
