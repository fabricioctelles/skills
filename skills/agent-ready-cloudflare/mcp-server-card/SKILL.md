# Implement MCP Server Card

Publish an MCP Server Card for agent discovery per
[SEP-1649](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127).

## Requirements

- Serve JSON at `/.well-known/mcp/server-card.json` with HTTP 200
- Include `serverInfo` with `name` and `version`
- Include a transport `endpoint` URL (e.g., `/mcp` for Streamable HTTP)
- List `capabilities` (tools, resources, prompts) the server supports

## Cloudflare

[Agents SDK](https://developers.cloudflare.com/agents/) and
[Workers](https://developers.cloudflare.com/workers/) make it straightforward
to build and deploy MCP servers with server card support.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.mcpServerCard.status` is `"pass"`.
