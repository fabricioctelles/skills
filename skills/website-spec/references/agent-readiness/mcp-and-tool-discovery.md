---
title: "MCP and tool discovery"
category: agent-readiness
status: optional
updated: "2026-05-29T12:14:17.000Z"
sources:
  - title: "Model Context Protocol"
    url: "https://modelcontextprotocol.io/"
    publisher: "Anthropic / MCP project"
  - title: "MCP specification"
    url: "https://modelcontextprotocol.io/specification"
    publisher: "MCP project"
  - title: "Is It Agent Ready?"
    url: "https://isitagentready.com/"
    publisher: "Is It Agent Ready?"
licence: CC-BY-4.0
---

# MCP and tool discovery

> The Model Context Protocol is an emerging way for sites to expose queryable tools to agents over JSON-RPC. Relevant whenever your content has structure worth filtering — even for a static reference site like this one.

## What it is

The Model Context Protocol (MCP) is an open protocol, originally proposed by Anthropic in late 2024, that defines how language-model clients talk to external tools and data sources. Instead of an agent scraping your UI, you expose an MCP server that declares a set of tools, resources, and prompts; the agent calls them directly.

MCP is built on JSON-RPC over a few transports — stdio for local servers, HTTP plus Server-Sent Events for remote ones. A tool definition includes a name, a description, and a JSON Schema for inputs.

This is relevant when your site exposes actions a user might want an agent to take: search a catalogue, create a ticket, book an appointment, query an account. For static content sites and blogs, MCP often adds little — well-cached HTML and a feed are enough. The exception is structured content sites where the data is filterable: a documentation set, a spec, a knowledge base. There an MCP server lets an agent ask "list all required SEO topics" or "give me the canonical CSP page" in a single typed call, instead of crawling and parsing.

This site ships such a server as a worked example. See [mcp.specification.website](https://mcp.specification.website/) for the live endpoint, [`/.well-known/mcp/server-card.json`](/.well-known/mcp/server-card.json) for the discovery document, and the [`mcp/` directory of the source repo](https://github.com/jdevalk/specification.website/tree/main/mcp) for a ~300-line Cloudflare Worker implementation.

## Why it matters

- Agents call your functionality through a defined contract instead of guessing from a UI. Behaviour is predictable and auditable.
- One MCP server can be reused across Claude, ChatGPT (via connectors), and any other MCP-aware client. No per-vendor integration.
- Authorisation is explicit. Tools declare what they do; the agent (and the user) consents before calling.
- The same server is useful for your own internal automation, not just public agents.

Adoption is real but uneven. Treat it as an emerging convention worth investing in if your product is API-shaped, and as overkill if it is not.

## How to implement

- Decide what you want agents to do. Read-only tools (`search_products`, `get_order_status`) are a safe first step; write tools (`create_ticket`, `update_address`) come with stronger auth requirements.
- Build an MCP server. The reference SDKs cover TypeScript, Python, and others; see [modelcontextprotocol.io](https://modelcontextprotocol.io/).
- Host it at a discoverable URL such as `/mcp` or a subdomain like `mcp.example.com`. Document the endpoint in your developer docs and link it from [/llms.txt](../agent-readiness/llms-txt.md).
- **Publish a server card.** Ship `/.well-known/mcp/server-card.json` describing the server's name, version, transport, endpoint URL, capabilities, tools, and prompts. Add a `Link: </.well-known/mcp/server-card.json>; rel="mcp"` header on your main site so the card is discoverable without guessing the path — see [HTTP Link headers](../agent-readiness/link-headers.md) and [`/.well-known/api-catalog`](../well-known/api-catalog.md).
- Use OAuth 2.1 (the MCP spec aligns with it) for any tool that touches user data. Never accept long-lived API keys in tool calls.
- Keep tool descriptions short and precise. Agents pick which tool to call from the description.
- Version the schema. Renaming a tool or changing its input shape is a breaking change.

## Common mistakes

- Exposing every internal API as an MCP tool. Curate; agents reason better about a small, well-named surface.
- Skipping rate limits and audit logs. An MCP endpoint that an agent can call repeatedly is an abuse vector.
- Mixing read and write tools without clear naming. Make destructive actions obvious in the tool name.
- Treating MCP as a replacement for documentation. It complements it; it does not replace it.

## Verification

- Connect your server with the MCP Inspector or a reference client and confirm tools list, call, and return as expected.
- Review the OAuth flow end to end.
- Watch logs after a public launch for unexpected call patterns.
