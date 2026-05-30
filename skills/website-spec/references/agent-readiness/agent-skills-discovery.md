---
title: "Agent Skills discovery"
category: agent-readiness
status: recommended
updated: "2026-05-29T11:27:49.000Z"
sources:
  - title: "Agent Skills Discovery via Well-Known URIs (RFC draft)"
    url: "https://github.com/cloudflare/agent-skills-discovery-rfc"
    publisher: "Cloudflare"
  - title: "Agent Skills specification"
    url: "https://agentskills.io/specification"
    publisher: "agentskills.io"
  - title: "RFC 8615 — Well-Known URIs"
    url: "https://datatracker.ietf.org/doc/html/rfc8615"
    publisher: "IETF"
  - title: "Is It Agent Ready?"
    url: "https://isitagentready.com/"
    publisher: "Is It Agent Ready?"
licence: CC-BY-4.0
---

# Agent Skills discovery

> A well-known URI that lists Agent Skills — short, scoped instructions an AI agent can load to work better with your site. Emerging convention via a Cloudflare-led RFC; still draft, still cheap to ship.

## What it is

An Agent Skill is a small Markdown file — a `SKILL.md` with YAML frontmatter — that gives an AI agent a focused capability: when to use it, how to call your APIs, which conventions to follow. The format originated with Anthropic; the [agentskills.io specification](https://agentskills.io/specification) documents it.

Agent Skills Discovery is the convention for *publishing* those skills so any agent can find them. Per the Cloudflare-led [discovery RFC](https://github.com/cloudflare/agent-skills-discovery-rfc) (currently draft v0.2.0), publishers ship a JSON index at:

```
/.well-known/agent-skills/index.json
```

Each entry in the index has a `name`, `type` (`skill-md` or `archive`), `description`, `url`, and a `sha256` digest of the artefact. A top-level `$schema` field identifies the index version.

This site publishes one such skill: [`/.well-known/agent-skills/specification-website/SKILL.md`](/.well-known/agent-skills/specification-website/SKILL.md), advertised in [`/.well-known/agent-skills/index.json`](/.well-known/agent-skills/index.json). It teaches an agent how to query the spec via Markdown endpoints, [llms.txt](../agent-readiness/llms-txt.md), and the [MCP server](../agent-readiness/mcp-and-tool-discovery.md).

## Why it matters

- One URL answers "what skills does this site publish for agents?" — no scraping, no per-vendor registry.
- Skills are vendor-neutral Markdown. The same file works in Claude, in agent harnesses, and in anything else that loads the format.
- The `digest` field gives clients cheap change detection and integrity verification.
- It composes with other agent-readiness signals: a skill can teach an agent to prefer your `.md` endpoints, hit your MCP server, or follow your structured-data conventions.

Adoption is early. Treat it as a low-cost bet, not a settled standard.

## How to implement

- Author one or more `SKILL.md` files. Each MUST start with YAML frontmatter containing `name` (lowercase, hyphens, 1–64 chars) and `description` (≤1024 chars, written so an agent can decide whether to load the full body).
- Host each skill at `/.well-known/agent-skills/<name>/SKILL.md`. Serve as `text/markdown`.
- Publish `/.well-known/agent-skills/index.json` with `$schema` set to `https://schemas.agentskills.io/discovery/0.2.0/schema.json` and a `skills` array. Each entry needs `name`, `type`, `description`, `url`, and `digest`.
- Compute the digest as `sha256:<hex>` over the raw bytes of the artefact. Recompute and update the index every time the artefact changes.
- Advertise the index in [`/.well-known/api-catalog`](../well-known/api-catalog.md) and as a [`Link`](../agent-readiness/link-headers.md) header: `rel="agent-skills"; type="application/json"`.
- Serve both files with CORS open (`Access-Control-Allow-Origin: *`) so browser-based agents can fetch them.

## Common mistakes

- Letting the `digest` drift from the file. A mismatch makes the artefact unverifiable; compliant clients will refuse it.
- Writing the description as marketing copy. It is the only thing most agents read — front-load the *when to use this* signal.
- Bundling many unrelated capabilities into one skill. Prefer several small skills with sharp descriptions over one omnibus file.
- Forgetting `$schema`. Without it, clients fall back to v0.1.0 parsing and your entries may be ignored.
- Hosting `SKILL.md` with the wrong content type. `text/html` will confuse agents that fetch it directly.

## Verification

- `curl -sI https://example.com/.well-known/agent-skills/index.json` — confirm `200`, `Content-Type: application/json`.
- Parse the JSON and verify `$schema` matches the v0.2.0 URI.
- For each entry, fetch the `url`, hash the bytes, and confirm the result equals the `digest`.
- Validate with [isitagentready.com](https://isitagentready.com/) — `checks.discovery.agentSkills.status` should report `pass`.
