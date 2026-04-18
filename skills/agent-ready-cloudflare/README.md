# 🤖 Agent Ready — Cloudflare Scanner Skill

Scan any website for AI agent readiness and get actionable fix prompts — powered by [isitagentready.com](https://isitagentready.com).

This skill wraps the Cloudflare "Is It Agent Ready?" scanner into a reusable agent skill with full API documentation, 20 implementation sub-skills, and copy-paste prompts for every failing check.

---

## What It Does

Give it a domain. It scans 18 checks across 5 categories and tells you:

- **What level** your site is at (0–5)
- **What's passing** and what's failing
- **How to fix** every failure — with a prompt you can paste into any coding agent
- **What to prioritize** to reach the next level

```
You: "Scan example.com for agent readiness"

Agent: Scans via API → generates Markdown report → includes fix prompts for every failure
```

---

## Quick Start

### 1. Scan a single domain

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://example.com/"}'
```

### 2. Get a markdown report (for LLMs)

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://example.com/","format":"agent"}'
```

### 3. Use the MCP server

Connect your agent to the MCP endpoint:

```
https://isitagentready.com/mcp
```

Call the `scan_site` tool with `{"url": "https://example.com"}`.

---

## The 18 Checks

### Discoverability

| # | Check | What passes |
|---|-------|-------------|
| 1 | **robots.txt** | `/robots.txt` returns 200 with `text/plain` and `User-agent` directives |
| 2 | **sitemap.xml** | `/sitemap.xml` returns valid XML, or `Sitemap:` directive in robots.txt |
| 3 | **Link headers** | Homepage `Link` headers include agent-useful relations (`api-catalog`, `service-desc`, etc.) |

### Content

| # | Check | What passes |
|---|-------|-------------|
| 4 | **Markdown for Agents** | `Accept: text/markdown` → response with `Content-Type: text/markdown` |

### Bot Access Control

| # | Check | What passes |
|---|-------|-------------|
| 5 | **AI bot rules** | robots.txt has `User-agent` entries for GPTBot, Claude-Web, Google-Extended, etc. |
| 6 | **Content Signals** | robots.txt has `Content-Signal:` directives (ai-train, search, ai-input) |
| 7 | **Web Bot Auth** | `/.well-known/http-message-signatures-directory` with valid JWKS *(informational)* |

### API, Auth, MCP & Skill Discovery

| # | Check | What passes |
|---|-------|-------------|
| 8 | **API Catalog** | `/.well-known/api-catalog` returns `application/linkset+json` (RFC 9727) |
| 9 | **OAuth/OIDC** | `/.well-known/openid-configuration` or `oauth-authorization-server` with valid metadata |
| 10 | **OAuth Protected Resource** | `/.well-known/oauth-protected-resource` with `resource` + `authorization_servers` (RFC 9728) |
| 11 | **MCP Server Card** | `/.well-known/mcp/server-card.json` with `serverInfo`, transport, capabilities (SEP-1649) |
| 12 | **A2A Agent Card** | `/.well-known/agent-card.json` with name, version, supportedInterfaces |
| 13 | **Agent Skills Index** | `/.well-known/agent-skills/index.json` with skills array (v0.2.0) |
| 14 | **WebMCP** | Page calls `navigator.modelContext.provideContext()` with tool definitions |

### Commerce *(optional — scored only for e-commerce sites)*

| # | Check | What passes |
|---|-------|-------------|
| 15 | **x402** | API routes return HTTP 402 with x402 payment headers |
| 16 | **UCP** | `/.well-known/ucp` with protocol_version and services |
| 17 | **ACP** | `/.well-known/acp.json` with protocol metadata |
| 18 | **AP2** | A2A Agent Card includes AP2 extension with role |

---

## Level System

```
Level 0  Not Ready           — Fails basic checks
Level 1  Basic Web Presence  — 2 of 3: robots.txt, sitemap, link headers
Level 2  Bot-Aware           — Level 1 + AI bot rules + Content Signals
Level 3  Agent-Readable      — Level 2 + markdown content negotiation
Level 4  Agent-Integrated    — Level 3 + 1 of: MCP card, A2A card, agent skills, API catalog
Level 5  Agent-Native        — Level 4 + 2 of: Web Bot Auth, all integrations, auth metadata
```

---

## Example Output

Scanning a site at Level 1 produces a report like:

```markdown
# Agent Ready Scan — example.com

> **Score:** Level 1 — Basic Web Presence
> **Scanned:** 2026-04-18T13:10:58Z
> **Link:** [View online](https://isitagentready.com/example.com)

## Summary

| Category                          | Score |
|-----------------------------------|-------|
| Discoverability                   | 2/3   |
| Content                           | 0/1   |
| Bot Access Control                | 1/3   |
| API, Auth, MCP & Skill Discovery  | 0/7   |

## Details

### Discoverability (2/3)

- ✅ **robots.txt** — robots.txt exists with valid format
- ✅ **sitemap.xml** — sitemap.xml exists with valid structure
- ❌ **Link headers** — No Link headers found on homepage

### Content (0/1)

- ❌ **Markdown for Agents** — Site does not support Markdown for Agents

(... more categories ...)

## 🔧 How to Implement — Agent Prompts

#### ❌ Link headers

**Issue:** No Link headers found on homepage

​```
Goal: Include Link response headers for agent discovery (RFC 8288)

Issue: No Link headers found on homepage

Fix: Add Link response headers to your homepage that point agents to useful
resources. For example: Link: </.well-known/api-catalog>; rel="api-catalog"

Skill: https://isitagentready.com/.well-known/agent-skills/link-headers/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc8288
​```

> 📖 Reference: [link-headers/SKILL.md](link-headers/SKILL.md)

(... one block per failing check ...)

## Next Level

**Level 2 — Bot-Aware**

To reach the next level, implement:
- Content Signals in robots.txt
```

---

## Fix Prompts

Every failing check gets a prompt block you can copy-paste into any coding agent (Cursor, Copilot, Claude, etc.). The format matches the isitagentready.com web UI:

```
Goal: <what the check expects>
Issue: <what was found (dynamic from scan)>
Fix: <step-by-step implementation>
Skill: <URL to the detailed SKILL.md>
Docs: <links to RFCs and specs>
```

The SKILL.md contains templates for all 20 checks. The `{issue}` placeholder is replaced with the actual message from the API response.

---

## Batch Scanning

Scan multiple domains with a 2-second delay between requests:

```python
import json, time, urllib.request

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ...",
    "Referer": "https://isitagentready.com/",
    "Origin": "https://isitagentready.com"
}

domains = ["example.com", "another.com", "third.com"]

for domain in domains:
    body = json.dumps({"url": f"https://{domain}/"}).encode()
    req = urllib.request.Request(
        "https://isitagentready.com/api/scan",
        data=body, headers=HEADERS
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    
    level = data["level"]
    name = data["levelName"]
    print(f"{domain}: Level {level} — {name}")
    time.sleep(2)
```

---

## API Response Shape

```json
{
  "url": "https://example.com",
  "scannedAt": "2026-04-18T13:10:58.788Z",
  "level": 1,
  "levelName": "Basic Web Presence",
  "isCommerce": false,
  "checks": {
    "discoverability": {
      "robotsTxt": {
        "status": "pass",
        "message": "robots.txt exists with valid format",
        "evidence": [ ... ],
        "durationMs": 42
      }
    }
  },
  "nextLevel": {
    "target": 2,
    "name": "Bot-Aware",
    "requirements": [
      {
        "check": "contentSignals",
        "description": "...",
        "prompt": "...",
        "skillUrl": "...",
        "specUrls": ["..."]
      }
    ]
  }
}
```

| Status | Meaning |
|--------|---------|
| `pass` | ✅ Check passed |
| `fail` | ❌ Action needed |
| `neutral` | ⬜ Not applicable / informational |

---

## Skill Structure

```
agent-ready-cloudflare/
├── README.md                          ← You are here
├── SKILL.md                           ← Main skill (operational flow, API docs, prompt templates)
│
├── scan-site/SKILL.md                 ← Meta: scan API + MCP server docs
│
│   Discoverability
├── robots-txt/SKILL.md                ← Implement robots.txt (RFC 9309)
├── sitemap/SKILL.md                   ← Implement sitemap.xml
├── link-headers/SKILL.md              ← Link response headers (RFC 8288)
├── llms-txt/SKILL.md                  ← Publish /llms.txt
├── llms-full-txt/SKILL.md             ← Publish /llms-full.txt
│
│   Content
├── markdown-negotiation/SKILL.md      ← Accept: text/markdown negotiation
│
│   Bot Access Control
├── ai-rules/SKILL.md                  ← AI bot User-agent rules
├── content-signals/SKILL.md           ← Content-Signal directives
├── web-bot-auth/SKILL.md              ← Web Bot Auth (JWKS)
│
│   API, Auth, MCP & Skill Discovery
├── api-catalog/SKILL.md               ← API Catalog (RFC 9727)
├── oauth-discovery/SKILL.md           ← OAuth/OIDC discovery (RFC 8414)
├── oauth-protected-resource/SKILL.md  ← Protected Resource Metadata (RFC 9728)
├── mcp-server-card/SKILL.md           ← MCP Server Card (SEP-1649)
├── a2a-agent-card/SKILL.md            ← A2A Agent Card (Google A2A)
├── agent-skills/SKILL.md              ← Agent Skills Discovery Index
├── webmcp/SKILL.md                    ← WebMCP browser API
│
│   Commerce
├── x402/SKILL.md                      ← x402 payment protocol
├── ucp/SKILL.md                       ← Universal Commerce Protocol
└── acp/SKILL.md                       ← Agent Commerce Protocol
```

**21 files** — 1 main skill + 20 implementation sub-skills.

---

## Sources

| Resource | URL |
|----------|-----|
| Scanner | https://isitagentready.com |
| API endpoint | `POST https://isitagentready.com/api/scan` |
| MCP server | `https://isitagentready.com/mcp` |
| API Catalog | https://isitagentready.com/.well-known/api-catalog |
| Agent Skills Index | https://isitagentready.com/.well-known/agent-skills/index.json |
| MCP Server Card | https://isitagentready.com/.well-known/mcp/server-card.json |
| Full docs (llms-full.txt) | https://isitagentready.com/llms-full.txt |
| Cloudflare Agents | https://developers.cloudflare.com/agents/ |
| MCP Protocol | https://modelcontextprotocol.io/ |
| Content Signals | https://contentsignals.org/ |
| Agent Skills Discovery | https://github.com/cloudflare/agent-skills-discovery-rfc |
