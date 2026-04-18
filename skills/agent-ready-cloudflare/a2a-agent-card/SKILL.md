# Implement A2A Agent Card

Publish an A2A Agent Card for agent-to-agent discovery per the
[A2A Protocol Specification](https://a2a-protocol.org/latest/specification/).

## Requirements

- Serve JSON at `/.well-known/agent-card.json` with HTTP 200
- Include `name`, `version`, and `description`
- Include `supportedInterfaces` with service URL and transport protocol
- List `capabilities` and `skills` (each with `id`, `name`, `description`)

See [Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/)
for the full schema.

## Cloudflare

[Agents SDK](https://developers.cloudflare.com/agents/) supports building
A2A-compatible agents on Workers.

## Validate

```
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discovery.a2aAgentCard.status` is `"pass"`.
