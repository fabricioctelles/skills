# Agent Plugins 1.0.0 Conformance Checklist

Use this snapshot for Agent Plugins `1.0.0`. The canonical normative text at
<https://agent-plugins.org/specification> governs; JSON Schemas are supporting
validation artifacts. Version 1.0.0 was published as a Working Draft, so verify
the canonical source when evaluating another version or a request for “latest.”

## 1. Package and manifest

- Require a regular `plugin.json` at the plugin root. Its resolved path and all
  package-supplied paths must remain inside the resolved plugin root.
- Require a JSON object with canonical `$schema` and `name`.
- For 1.0.0, require
  `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`.
- Permit only `$schema`, `name`, `version`, `description`, `author`, `homepage`,
  `repository`, `license`, `keywords`, and `extensions` at the top level.
- Constrain `name` to 1–64 lowercase `a-z`, digits, hyphens, and periods; start
  and end alphanumeric; reject `--` and `..`.
- Validate optional field types. `author` may contain only string-valued
  `name`, `email`, and `url`. Semantic Versioning and SPDX are recommended,
  not required by type validation.
- Treat unknown top-level fields as reported-and-ignored schema violations,
  not fatal loader errors. Treat a non-object `extensions` similarly. Other
  manifest schema violations reject the plugin.

## 2. Discovery and skills

- Discover Skills only from immediate child directories of `skills/` that
  contain a regular file named exactly `SKILL.md`; do not recurse deeper.
- Validate every discovered skill against <https://agentskills.io/specification>.
  Skip an invalid skill without disabling valid siblings or MCP.
- Treat an absent `skills/` as valid. If present but not a directory, mark the
  Skills component type invalid while continuing with other types.
- Do not treat client-native folders or manifest entries as portable component
  discovery. Agent Plugins v1 defines exactly Skills and MCP servers.

## 3. MCP configuration

- Discover MCP only from regular root `mcp.json`. If absent, MCP is simply not
  provided. If present with the wrong filesystem kind, MCP is invalid.
- Require a JSON object containing only `$schema` and `mcpServers`, both
  required. For 1.0.0 use
  `https://agent-plugins.org/schemas/1.0.0/mcp.schema.json`.
- Require the MCP schema version to match `plugin.json`. A top-level MCP error
  disables MCP but not Skills.
- Validate each server independently as exactly one closed variant:

  - `stdio`: required string `command`; optional string-array `args`,
    string-map `env`, and string `cwd`.
  - `streamable-http` or deprecated `sse`: required absolute `url`; optional
    string-map `headers`.

- For `stdio`, keep `command` one executable token: a bare executable or a
  plugin-relative path beginning `./`. Do not expand placeholders in it.
- Allow `cwd` only as `./...`, `${PLUGIN_ROOT}[/...]`, or
  `${PLUGIN_DATA}[/...]`, with post-resolution containment.
- Expand exactly `${PLUGIN_ROOT}` and `${PLUGIN_DATA}`, once and
  non-recursively, only in `args`, `env` values, and `cwd`. Preserve unknown
  placeholder-like text literally. Forbid reserved names in configured `env`.
- For remote transports, require absolute HTTP(S), no userinfo or fragment,
  and HTTPS except exact localhost or loopback IPs. Treat header names
  case-insensitively and reject duplicates by casing.
- Never embed credentials in `env` or `headers`. Agent Plugins v1 has no
  portable OAuth or credential-reference fields.

## 4. Client extensions

- Put client-specific manifest data under `extensions` keys using stable
  reverse-domain namespaces whose values are objects.
- Put client-specific files in root directories named exactly after their
  namespaces. Either manifest data or a directory may exist independently.
- Do not assign portable semantics to extension contents. Evaluate an
  extension against its owning client's specification only when the user asks
  for that compatibility profile.

## 5. Failure boundaries and evaluation gate

| Finding | Official loading boundary | Evaluation gate |
|---|---|---|
| Missing/unreadable root manifest, unsupported schema, invalid required field, or fatal manifest schema error | Reject plugin; load no components | `FAIL` |
| Package or configured path resolves outside allowed root/data boundary | Reject/skip at the narrowest normative boundary; deny access | `FAIL` when the root manifest escapes; otherwise `PARTIAL` at the affected boundary |
| Unknown root manifest field or non-object `extensions` | Report and ignore field; continue | `PARTIAL` |
| `skills/` or `mcp.json` present with wrong filesystem kind | Disable that component type; continue | `PARTIAL` |
| Invalid individual Skill | Skip that Skill; continue | `PARTIAL` |
| Invalid MCP top level or version mismatch | Disable MCP; continue | `PARTIAL` |
| Invalid/unsupported/failing MCP server entry | Skip that server; continue | `PARTIAL` |
| Missing optional component location | No error | No downgrade |
| Confirmed embedded credential in visible package config | Unsafe to release | `FAIL` |

A secret-like field name or literal is not confirmation by itself. Keep a
heuristic match as a redacted suspicion until corroborated by a recognized live
credential format, trusted scanner, repository provenance, or the user. Do not
authenticate with a suspected value as a validation technique.

Do not promote `PARTIAL` to `FAIL` merely because one component fails. Do not
downgrade a normative MUST violation to a recommendation because a specific
client is permissive.

## 6. Primary sources

- [Agent Plugins overview](https://agent-plugins.org/)
- [Agent Plugins Specification 1.0.0](https://agent-plugins.org/specification)
- [Plugin JSON Schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)
- [MCP JSON Schema 1.0.0](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json)
- [Vercel announcement](https://vercel.com/blog/introducing-agent-plugins)

The Vercel announcement is useful context for the portability goal but is not
normative. Client-specific creator tooling (e.g., OpenAI plugin-creator,
Anthropic Claude Desktop, Cursor MCP integration) is a compatibility reference,
not a replacement for the portable specification.
