---
name: agent-ready-cloudflare
description: >
  Audit and improve website readiness for AI agents using the Cloudflare
  "Is It Agent Ready?" scanner (isitagentready.com). Covers scanning via API,
  interpreting results, generating implementation prompts, and fixing every check.
  Use when the user mentions "agent ready", "isitagentready", "AI agent scan",
  "agent readiness", "agent-ready score", "MCP server card", "agent skills index",
  "markdown for agents", "content signals", "web bot auth", "agent discovery",
  "RFC 9727", "RFC 8288", "RFC 9728", "SEP-1649", "WebMCP", "x402", "UCP", "ACP",
  or wants to make a website discoverable and usable by AI agents.
metadata:
  author: Cloudflare / isitagentready.com
  version: "2.0"
  date: 2026-04-18
  source: https://isitagentready.com
---

# Agent Ready — Cloudflare Scanner

Audit any website for AI agent readiness, generate actionable fix prompts, and
implement improvements to increase the agent-ready score.

---

## 0. Operational Flow

Follow this flow every time this skill is activated:

### Step 1 — Get the domain

If the user did not provide a domain, ask:

> Which domain do you want to scan on isitagentready.com?

### Step 2 — Scan via API

```bash
curl -s -X POST 'https://isitagentready.com/api/scan' \
  -H 'Content-Type: application/json' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Referer: https://isitagentready.com/' \
  -H 'Origin: https://isitagentready.com' \
  -d '{"url":"https://DOMAIN/","enabledChecks":["robotsTxt","sitemap","linkHeaders","markdownNegotiation","robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog","oauthDiscovery","oauthProtectedResource","mcpServerCard","agentSkills","webMcp","x402","ucp","acp"]}'
```

Replace `DOMAIN` with the target domain.

### Step 3 — Generate the Markdown report

Use the API response to build a report with this structure:

```markdown
# Agent Ready Scan — {domain}

> **Score:** Level {level} — {levelName}
> **Scanned:** {scannedAt}
> **Link:** [View online](https://isitagentready.com/{domain})

## Summary

| Category | Score |
|----------|-------|
| Discoverability | {passed}/{total} |
| Content | {passed}/{total} |
| Bot Access Control | {passed}/{total} |
| API, Auth, MCP & Skill Discovery | {passed}/{total} |
| Commerce (Optional) | {passed}/{total} |

## Details

### Discoverability ({passed}/{total})

- ✅ **robots.txt** — {message}
- ❌ **sitemap.xml** — {message}
  (... for each check ...)

### (... repeat for each category ...)

## 🔧 How to Implement — Agent Prompts

(... one block per failing check, see Step 4 ...)

## Next Level

**Level {nextLevel.target} — {nextLevel.name}**

To reach the next level, implement:
- {nextLevel.requirements[].description}
```

### Step 4 — Generate "How to Implement" prompts

For every check with `status: "fail"` or `status: "neutral"`, generate a prompt
block using the **Prompt Templates** in Section 8 below. The prompt combines:

1. The **Goal** and **Fix** from the template (static per check)
2. The **Issue** from the API response (`checks.{category}.{check}.message`)
3. The **Skill URL** pointing to the sub-skill
4. The **Docs** links to the relevant RFCs/specs

Format each prompt as a fenced code block the user can copy-paste into a coding agent:

````markdown
#### ❌ {check name}

**Issue:** {message from API}

```
Goal: {goal from template}

Issue: {message from API}

Fix: {fix from template}

Skill: https://isitagentready.com/.well-known/agent-skills/{skill-folder}/SKILL.md

Docs: {docs URLs from template}
```

> 📖 Reference: [{skill-folder}/SKILL.md]({skill-folder}/SKILL.md)
````

### Step 5 — Deliver

Present the full Markdown report to the user. If they want to save it to a file,
write it to the requested path.

---

## 1. What It Checks

### Discoverability (3 checks)
| Check | API Key | Pass criteria |
|-------|---------|---------------|
| robots.txt | `robotsTxt` | Returns 200 with `text/plain` containing at least one `User-agent` directive |
| sitemap.xml | `sitemap` | `/sitemap.xml` returns valid XML, or `Sitemap` directive found in robots.txt |
| Link headers | `linkHeaders` | Homepage includes `Link` headers with agent-useful relations (`service-desc`, `api-catalog`, etc.) |

### Content (1 check)
| Check | API Key | Pass criteria |
|-------|---------|---------------|
| Markdown for Agents | `markdownNegotiation` | `Accept: text/markdown` returns `Content-Type: text/markdown` |

### Bot Access Control (3 checks)
| Check | API Key | Pass criteria |
|-------|---------|---------------|
| AI bot rules | `robotsTxtAiRules` | robots.txt contains `User-agent` entries for known AI bots (GPTBot, Claude-Web, Google-Extended, etc.) |
| Content Signals | `contentSignals` | robots.txt contains `Content-Signal` directives with ai-train/search/ai-input |
| Web Bot Auth | `webBotAuth` | `/.well-known/http-message-signatures-directory` exists with valid JWKS (informational — neutral does not affect score) |

### API, Auth, MCP & Skill Discovery (7 checks)
| Check | API Key | Pass criteria |
|-------|---------|---------------|
| API Catalog | `apiCatalog` | `/.well-known/api-catalog` returns valid `linkset+json` with API entries |
| OAuth/OIDC | `oauthDiscovery` | `/.well-known/openid-configuration` or `oauth-authorization-server` with valid OAuth metadata |
| OAuth Protected Resource | `oauthProtectedResource` | `/.well-known/oauth-protected-resource` with `resource` and `authorization_servers` |
| MCP Server Card | `mcpServerCard` | Valid card at `/.well-known/mcp/server-card.json`, `server-cards.json`, or `mcp.json` with `serverInfo.name` |
| A2A Agent Card | `a2aAgentCard` | `/.well-known/agent-card.json` with `name`, `version`, and `supportedInterfaces` |
| Agent Skills Index | `agentSkills` | `/.well-known/agent-skills/index.json` with valid `skills` array (legacy `/.well-known/skills/` also accepted) |
| WebMCP | `webMcp` | Page exposes MCP tools via `navigator.modelContext.provideContext()` |

### Commerce — Optional (4 checks, scored only if e-commerce signals detected)
| Check | API Key | Pass criteria |
|-------|---------|---------------|
| x402 | `x402` | API routes return HTTP 402 with valid x402 payment headers |
| UCP | `ucp` | `/.well-known/ucp` with `protocol_version` and `services` |
| ACP | `acp` | `/.well-known/acp.json` with `protocol.name`, `api_base_url`, `transports`, `capabilities.services` |
| AP2 | `ap2` | A2A Agent Card includes AP2 extension with role information |

---

## 2. Levels

| Level | Name | Requirements |
|-------|------|-------------|
| 0 | Not Ready | Does not meet Level 1 criteria |
| 1 | Basic Web Presence | Pass 2 of 3: robots.txt, sitemap, link headers |
| 2 | Bot-Aware | Level 1 + both: AI bot rules AND Content Signals in robots.txt |
| 3 | Agent-Readable | Level 2 + markdown content negotiation |
| 4 | Agent-Integrated | Level 3 + 1 of 4: MCP Server Card, A2A Agent Card, Agent Skills, API Catalog |
| 5 | Agent-Native | Level 4 + 2 of 3: Web Bot Auth, all four integration checks, auth metadata (OAuth discovery or OAuth Protected Resource) |

---

## 3. API Reference

### Endpoint

```
POST https://isitagentready.com/api/scan
Content-Type: application/json
```

### Required Headers (Cloudflare protection)

```
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Referer: https://isitagentready.com/
Origin: https://isitagentready.com
```

### Request Body

```json
{
  "url": "https://example.com/",
  "enabledChecks": [
    "robotsTxt", "sitemap", "linkHeaders",
    "markdownNegotiation",
    "robotsTxtAiRules", "contentSignals", "webBotAuth",
    "apiCatalog", "oauthDiscovery", "oauthProtectedResource",
    "mcpServerCard", "agentSkills", "webMcp",
    "x402", "ucp", "acp"
  ]
}
```

All checks are optional — pass only the ones you want to run.

Set `"format": "agent"` to get a markdown response with fix instructions instead
of JSON (useful for piping directly to an LLM).

### MCP Server

The scanner is also available as an MCP server:

```
https://isitagentready.com/mcp
```

Call the `scan_site` tool with a `url` parameter. See [scan-site/SKILL.md](scan-site/SKILL.md).

### Discovered Endpoints (isitagentready.com itself)

The scanner practices what it preaches. These are its own agent-ready endpoints:

| Endpoint | Content |
|----------|---------|
| `/.well-known/api-catalog` | RFC 9727 linkset with scan API and MCP server entries |
| `/.well-known/mcp/server-card.json` | MCP Server Card (Streamable HTTP transport) |
| `/.well-known/mcp.json` | Same MCP Server Card (alternate path) |
| `/.well-known/agent-skills/index.json` | 20 skills in Agent Skills Discovery v0.2.0 format |
| `/llms.txt` | LLM-friendly overview of the scanner |
| `/llms-full.txt` | Full documentation — canonical reference for all 18 checks, pass criteria, and level system |
| `/api/health` | Health check (`{"status":"ok"}`) |
| `/mcp` | Streamable HTTP MCP server with `scan_site` tool |

The API Catalog links the scan API to its documentation (`/llms-full.txt`),
its service description (`/.well-known/mcp/server-card.json`), and its health
endpoint (`/api/health`).

### Response Structure

```json
{
  "url": "https://example.com",
  "scannedAt": "2026-04-18T13:10:58.788Z",
  "level": 1,
  "levelName": "Basic Web Presence",
  "isCommerce": false,
  "commerceSignals": [],
  "nextLevel": {
    "target": 2,
    "name": "Bot-Aware",
    "requirements": [
      {
        "check": "contentSignals",
        "description": "...",
        "shortPrompt": "...",
        "prompt": "Full implementation prompt...",
        "specUrls": ["https://..."],
        "skillUrl": "https://isitagentready.com/.well-known/agent-skills/.../SKILL.md"
      }
    ]
  },
  "checks": {
    "<category>": {
      "<checkKey>": {
        "status": "pass|fail|neutral",
        "message": "Human-readable conclusion",
        "durationMs": 42,
        "evidence": [
          {
            "action": "fetch|parse|conclude",
            "label": "GET /robots.txt",
            "request": { "url": "...", "method": "GET" },
            "response": {
              "status": 200,
              "headers": { "content-type": "..." },
              "bodyPreview": "..."
            },
            "finding": {
              "outcome": "positive|negative|neutral",
              "summary": "..."
            }
          }
        ]
      }
    }
  }
}
```

### Status Values

| Status | Icon | Meaning |
|--------|------|---------|
| `pass` | ✅ | Check passed |
| `fail` | ❌ | Action needed |
| `neutral` | ⬜ | Not applicable / informational |

---

## 4. Web Interface vs API

| Feature | API | Web UI |
|---------|-----|--------|
| Score & Level | ✅ | ✅ |
| Check status + message | ✅ | ✅ |
| Evidence (audit details) | ✅ Full | ✅ Same |
| "How to implement" prompts | ⚠️ Only `nextLevel` (1 prompt) | ✅ All failing checks |
| Skill URLs | ⚠️ Only `nextLevel` | ✅ All checks |

This is why this skill includes the full prompt templates below — to reconstruct
the web-quality prompts from API data.

---

## 5. Batch Scanning

For multiple domains, add a 2-second delay between requests. Write results
incrementally to avoid data loss:

```python
import json, time, urllib.request

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 ...",
    "Referer": "https://isitagentready.com/",
    "Origin": "https://isitagentready.com"
}
CHECKS = ["robotsTxt","sitemap","linkHeaders","markdownNegotiation",
          "robotsTxtAiRules","contentSignals","webBotAuth","apiCatalog",
          "oauthDiscovery","oauthProtectedResource","mcpServerCard",
          "agentSkills","webMcp","x402","ucp","acp"]

for domain in domains:
    body = json.dumps({"url": f"https://{domain}/", "enabledChecks": CHECKS}).encode()
    req = urllib.request.Request("https://isitagentready.com/api/scan",
                                data=body, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read())
    # process data...
    time.sleep(2)
```

---

## 6. Sub-Skills (Implementation Guides)

### Discoverability
- [robots-txt/SKILL.md](robots-txt/SKILL.md) — Publish `/robots.txt` (RFC 9309)
- [sitemap/SKILL.md](sitemap/SKILL.md) — Publish `/sitemap.xml`
- [link-headers/SKILL.md](link-headers/SKILL.md) — Add `Link` response headers (RFC 8288)
- [llms-txt/SKILL.md](llms-txt/SKILL.md) — Publish `/llms.txt` (llmstxt.org)
- [llms-full-txt/SKILL.md](llms-full-txt/SKILL.md) — Publish `/llms-full.txt`

### Content
- [markdown-negotiation/SKILL.md](markdown-negotiation/SKILL.md) — Return markdown on `Accept: text/markdown`

### Bot Access Control
- [ai-rules/SKILL.md](ai-rules/SKILL.md) — AI bot `User-agent` rules in robots.txt
- [content-signals/SKILL.md](content-signals/SKILL.md) — `Content-Signal` directives
- [web-bot-auth/SKILL.md](web-bot-auth/SKILL.md) — JWKS for request signing

### API, Auth, MCP & Skill Discovery
- [api-catalog/SKILL.md](api-catalog/SKILL.md) — API Catalog (RFC 9727)
- [oauth-discovery/SKILL.md](oauth-discovery/SKILL.md) — OAuth/OIDC discovery (RFC 8414)
- [oauth-protected-resource/SKILL.md](oauth-protected-resource/SKILL.md) — Protected Resource Metadata (RFC 9728)
- [mcp-server-card/SKILL.md](mcp-server-card/SKILL.md) — MCP Server Card (SEP-1649)
- [a2a-agent-card/SKILL.md](a2a-agent-card/SKILL.md) — A2A Agent Card (Google A2A Protocol)
- [agent-skills/SKILL.md](agent-skills/SKILL.md) — Agent Skills Discovery Index
- [webmcp/SKILL.md](webmcp/SKILL.md) — WebMCP browser API

### Commerce (Optional)
- [x402/SKILL.md](x402/SKILL.md) — x402 HTTP payment protocol
- [ucp/SKILL.md](ucp/SKILL.md) — Universal Commerce Protocol
- [acp/SKILL.md](acp/SKILL.md) — Agent Commerce Protocol

### Meta
- [scan-site/SKILL.md](scan-site/SKILL.md) — Scan any site for agent readiness (includes MCP server endpoint)

---

## 7. Priority Order for Maximum Impact

1. `robots.txt` + `sitemap.xml` → Level 1
2. `Content Signals` in robots.txt → Level 2
3. `Markdown for Agents` + `Link headers` → toward Level 3
4. `MCP Server Card` + `Agent Skills Index` → toward Level 4
5. `OAuth discovery` + `API Catalog` → full agent interoperability

---

## 8. Prompt Templates per Check

These templates replicate the "How to implement — paste into your coding agent"
prompts from the web UI. When generating the report (Step 4), use the `{issue}`
placeholder with the actual `message` from the API response.

### `robotsTxt`

```
Goal: Publish /robots.txt with clear crawl rules

Issue: {issue}

Fix: Create /robots.txt at the site root with explicit User-agent directives and allow/disallow rules for key paths. Ensure it is plain text and returns 200.

Skill: https://isitagentready.com/.well-known/agent-skills/robots-txt/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9309
```

Sub-skill: [robots-txt/SKILL.md](robots-txt/SKILL.md)

### `sitemap`

```
Goal: Publish /sitemap.xml with canonical URLs

Issue: {issue}

Fix: Generate /sitemap.xml listing canonical URLs, keep it updated on publish, and reference it from /robots.txt.

Skill: https://isitagentready.com/.well-known/agent-skills/sitemap/SKILL.md

Docs: https://www.sitemaps.org/protocol.html
```

Sub-skill: [sitemap/SKILL.md](sitemap/SKILL.md)

### `linkHeaders`

```
Goal: Include Link response headers for agent discovery (RFC 8288)

Issue: {issue}

Fix: Add Link response headers to your homepage that point agents to useful resources. For example: Link: </.well-known/api-catalog>; rel="api-catalog" to advertise your API catalog, or Link: </docs/api>; rel="service-doc" for API documentation. See RFC 8288 for the Link header format and IANA Link Relations for registered relation types.

Skill: https://isitagentready.com/.well-known/agent-skills/link-headers/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc8288, https://www.rfc-editor.org/rfc/rfc9727#section-3
```

Sub-skill: [link-headers/SKILL.md](link-headers/SKILL.md)

### `markdownNegotiation`

```
Goal: Return HTML responses as markdown when agents request it

Issue: {issue}

Fix: Enable Markdown for Agents so requests with Accept: text/markdown return a markdown version of your HTML response while HTML stays the default for browsers. Confirm the response uses Content-Type: text/markdown (and x-markdown-tokens if available).

Skill: https://isitagentready.com/.well-known/agent-skills/markdown-negotiation/SKILL.md

Docs: https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/
```

Sub-skill: [markdown-negotiation/SKILL.md](markdown-negotiation/SKILL.md)

### `robotsTxtAiRules`

```
Goal: Add User-agent rules for AI crawlers like GPTBot, Claude-Web, and others

Issue: {issue}

Fix: Add explicit User-agent entries for AI crawlers (GPTBot, OAI-SearchBot, Claude-Web, Google-Extended) with allow/disallow rules that match your policy.

Skill: https://isitagentready.com/.well-known/agent-skills/ai-rules/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9309, https://developers.cloudflare.com/ai-crawl-control/
```

Sub-skill: [ai-rules/SKILL.md](ai-rules/SKILL.md)

### `contentSignals`

```
Goal: Declare AI content usage preferences with Content Signals in robots.txt

Issue: {issue}

Fix: Add Content-Signal directives to your robots.txt declaring preferences for ai-train, search, and ai-input. For example:
Content-Signal: ai-train=no, search=yes, ai-input=no

Skill: https://isitagentready.com/.well-known/agent-skills/content-signals/SKILL.md

Docs: https://contentsignals.org/, https://datatracker.ietf.org/doc/draft-romm-aipref-contentsignals/
```

Sub-skill: [content-signals/SKILL.md](content-signals/SKILL.md)

### `webBotAuth`

```
Goal: Let your site identify itself as a bot with Web Bot Auth

Issue: {issue}

Fix: Publish a JWKS at /.well-known/http-message-signatures-directory so your site can identify itself when it sends bot or agent requests. Receiving sites can use it to verify those signed requests.

Skill: https://isitagentready.com/.well-known/agent-skills/web-bot-auth/SKILL.md

Docs: https://datatracker.ietf.org/wg/webbotauth/about/, https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/
```

Sub-skill: [web-bot-auth/SKILL.md](web-bot-auth/SKILL.md)

### `apiCatalog`

```
Goal: Publish an API catalog for automated API discovery (RFC 9727)

Issue: {issue}

Fix: Create /.well-known/api-catalog returning application/linkset+json with a "linkset" array. Each entry should include an "anchor" URL for the API and link relations for service-desc (OpenAPI spec), service-doc (documentation), and status (health endpoint). See RFC 9727 Appendix A for examples.

Skill: https://isitagentready.com/.well-known/agent-skills/api-catalog/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9727, https://www.rfc-editor.org/rfc/rfc9264
```

Sub-skill: [api-catalog/SKILL.md](api-catalog/SKILL.md)

### `oauthDiscovery`

```
Goal: Publish OAuth/OIDC discovery metadata so agents can authenticate with your APIs

Issue: {issue}

Fix: If your site has protected APIs, publish /.well-known/openid-configuration (for OpenID Connect) or /.well-known/oauth-authorization-server (for pure OAuth 2.0) with your issuer, authorization_endpoint, token_endpoint, jwks_uri, and grant_types_supported. This allows AI agents to programmatically discover how to authenticate.

Skill: https://isitagentready.com/.well-known/agent-skills/oauth-discovery/SKILL.md

Docs: http://openid.net/specs/openid-connect-discovery-1_0.html, https://www.rfc-editor.org/rfc/rfc8414
```

Sub-skill: [oauth-discovery/SKILL.md](oauth-discovery/SKILL.md)

### `oauthProtectedResource`

```
Goal: Publish OAuth Protected Resource Metadata so agents can discover how to authenticate

Issue: {issue}

Fix: Publish /.well-known/oauth-protected-resource with your resource identifier, authorization_servers (list of OAuth/OIDC issuer URLs that can issue tokens for this resource), and scopes_supported. This tells agents how to obtain access tokens for your protected APIs.

Skill: https://isitagentready.com/.well-known/agent-skills/oauth-protected-resource/SKILL.md

Docs: https://www.rfc-editor.org/rfc/rfc9728
```

Sub-skill: [oauth-protected-resource/SKILL.md](oauth-protected-resource/SKILL.md)

### `mcpServerCard`

```
Goal: Publish an MCP Server Card for agent discovery

Issue: {issue}

Fix: Serve an MCP Server Card (SEP-1649) at /.well-known/mcp/server-card.json with serverInfo (name, version), transport endpoint, and capabilities. The schema is being standardized at https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127

Skill: https://isitagentready.com/.well-known/agent-skills/mcp-server-card/SKILL.md

Docs: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127
```

Sub-skill: [mcp-server-card/SKILL.md](mcp-server-card/SKILL.md)

### `agentSkills`

```
Goal: Publish an agent skills discovery index

Issue: {issue}

Fix: Publish a skills discovery index at /.well-known/agent-skills/index.json (per the Agent Skills Discovery RFC v0.2.0). Include a $schema field, and a skills array where each entry has name, type, description, url, and a sha256 digest.

Skill: https://isitagentready.com/.well-known/agent-skills/agent-skills/SKILL.md

Docs: https://github.com/cloudflare/agent-skills-discovery-rfc, https://agentskills.io/
```

Sub-skill: [agent-skills/SKILL.md](agent-skills/SKILL.md)

### `webMcp`

```
Goal: Support WebMCP to expose site tools to AI agents via the browser

Issue: {issue}

Fix: Implement the WebMCP API by calling navigator.modelContext.provideContext() with tool definitions that expose your site's key actions to AI agents. Each tool needs a name, description, inputSchema (JSON Schema), and an execute callback function.

Skill: https://isitagentready.com/.well-known/agent-skills/webmcp/SKILL.md

Docs: https://webmachinelearning.github.io/webmcp/, https://developer.chrome.com/blog/webmcp-epp
```

Sub-skill: [webmcp/SKILL.md](webmcp/SKILL.md)

### `x402`

```
Goal: Support x402 protocol for agent-native HTTP payments

Issue: {issue}

Fix: Add x402 payment middleware to your API routes to enable AI agents to pay for access via HTTP. Use @x402/express, @x402/hono, or @x402/next middleware with a facilitator URL and wallet address. Protected routes will return HTTP 402 with payment requirements that agents can fulfill automatically.

Skill: https://isitagentready.com/.well-known/agent-skills/x402/SKILL.md

Docs: https://x402.org, https://github.com/coinbase/x402, https://docs.x402.org
```

Sub-skill: [x402/SKILL.md](x402/SKILL.md)

### `ucp`

```
Goal: Enable content payments via Universal Commerce Protocol

Issue: {issue}

Fix: Serve /.well-known/ucp with protocol version, services, capabilities, and endpoints, and ensure spec URLs and schemas are reachable.

Skill: https://isitagentready.com/.well-known/agent-skills/ucp/SKILL.md

Docs: https://ucp.dev/specification/overview/
```

Sub-skill: [ucp/SKILL.md](ucp/SKILL.md)

### `acp`

```
Goal: Publish ACP discovery metadata so agents can discover your commerce API

Issue: {issue}

Fix: Serve /.well-known/acp.json at the origin root with protocol.name "acp", protocol.version, api_base_url, supported transports, and capabilities.services so agents can discover your ACP implementation without creating a checkout session first.

Skill: https://isitagentready.com/.well-known/agent-skills/acp/SKILL.md

Docs: https://agenticcommerce.dev, https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/pull/137
```

Sub-skill: [acp/SKILL.md](acp/SKILL.md)

### `a2aAgentCard`

```
Goal: Publish an A2A Agent Card for agent-to-agent discovery

Issue: {issue}

Fix: Serve JSON at /.well-known/agent-card.json with name, version, description, supportedInterfaces (service URL and transport), capabilities, and skills (each with id, name, description). See the A2A Protocol Specification for the full schema.

Skill: https://isitagentready.com/.well-known/agent-skills/a2a-agent-card/SKILL.md

Docs: https://a2a-protocol.org/latest/specification/, https://a2a-protocol.org/latest/topics/agent-discovery/
```

Sub-skill: [a2a-agent-card/SKILL.md](a2a-agent-card/SKILL.md)

### `llmsTxt`

```
Goal: Publish an LLM-friendly overview at /llms.txt

Issue: {issue}

Fix: Serve /llms.txt as plain text (UTF-8) with HTTP 200. Start with an H1 title line, include a short summary paragraph, and link to the most important content sections for agents. Optionally link to /llms-full.txt for expanded content.

Skill: https://isitagentready.com/.well-known/agent-skills/llms-txt/SKILL.md

Docs: https://llmstxt.org/
```

Sub-skill: [llms-txt/SKILL.md](llms-txt/SKILL.md)

### `llmsFullTxt`

```
Goal: Publish expanded LLM content at /llms-full.txt

Issue: {issue}

Fix: Serve /llms-full.txt as plain text (UTF-8) with HTTP 200. Include structured, detailed content suitable for LLM ingestion covering key topics, APIs, and documentation. Link to it from your /llms.txt file.

Skill: https://isitagentready.com/.well-known/agent-skills/llms-full-txt/SKILL.md

Docs: https://llmstxt.org/
```

Sub-skill: [llms-full-txt/SKILL.md](llms-full-txt/SKILL.md)

### `ap2`

```
Goal: Declare AP2 support in your A2A Agent Card for agent payments

Issue: {issue}

Fix: Add AP2 extension to your A2A Agent Card at /.well-known/agent-card.json with your role (merchant, shopper, etc.) so agents can discover your payment capabilities.

Docs: https://ap2-protocol.org/
```
