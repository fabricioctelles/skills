---
name: agent-ready-ard
description: >
  Sub-skill: Implement ARD (Agentic Resource Discovery). Publish
  /.well-known/ai-catalog.json so agents can discover MCP servers, A2A agents,
  skills and API tools (agenticresourcediscovery.org / ai-catalog).
---
# Implement ARD (Agentic Resource Discovery)

Publish a capability manifest so agents can discover your MCP servers, A2A
agents, skills and API tools, per the
[ARD spec](https://agenticresourcediscovery.org/) and the
[ai-catalog](https://github.com/Agent-Card/ai-catalog) data model.

The ARD spec is a v0.9 draft, so the scanner validates structure only and
reports non-conformant identifiers and media types without failing the check.

Note that `specVersion` refers to the ai-catalog data model, not the ARD spec
version, which is why the example below reads `1.0`. The scanner only requires
it to be a non-empty string.

## Requirements

- Serve `/.well-known/ai-catalog.json` from the origin root with
  `Content-Type: application/json`, HTTP 200, and `Access-Control-Allow-Origin: *`
- Include a `specVersion` string and a non-empty `entries` array
- Add a `host` object with `displayName` and a stable `identifier`
- Each entry needs an `identifier`, a `displayName`, and a `type` media type
- Each entry needs **exactly one** of `url` or `data` — never both, never neither
  (spec §3.4)
- Use `urn:air:<your-fqdn>:<namespace>:<name>` for entry identifiers
- Add 2-5 `representativeQueries` per entry so registries can build semantic
  embeddings

## Example

```json
{
  "specVersion": "1.0",
  "host": {
    "displayName": "Example Systems",
    "identifier": "did:web:example.com"
  },
  "entries": [
    {
      "identifier": "urn:air:example.com:server:weather",
      "displayName": "Weather Telemetry Server",
      "type": "application/mcp-server-card+json",
      "url": "https://example.com/mcp/weather.json",
      "representativeQueries": [
        "what is the wind speed in Chicago",
        "get the 5-day forecast for Seattle"
      ]
    }
  ]
}
```

## Additional discovery mechanisms

The well-known path is the primary mechanism. Any of the following can point
agents at a manifest hosted elsewhere (spec §6.1), and the scanner reports which
ones you publish:

- **robots.txt**: add an `Agentmap: https://example.com/ai-catalog.json` directive
- **HTML**: add `<link rel="ai-catalog" href="/.well-known/ai-catalog.json">` to
  `<head>`
- **DNS**: publish a `_catalog._agents.example.com` TXT record containing
  `url=https://example.com/.well-known/ai-catalog.json`
- **DNS**: publish a `_search._agents.example.com` SRV record to advertise a
  semantic search endpoint (reported only; the scanner never queries it)

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.ard.status` is `"pass"`.
