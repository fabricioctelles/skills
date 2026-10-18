---
name: agent-ready-personal-agent-protocol
description: >
  Sub-skill: Implement Personal Agent Protocol (Poppy) discovery. Publish
  /.well-known/poppy.json (draft 0.1) and validate its OAuth issuer binding.
  Informational check; does not affect level or score.
---
# Implement Personal Agent Protocol (Poppy) discovery

Publish public discovery metadata for the [Personal Agent Protocol draft
0.1](https://personalagentprotocol.org/docs/spec#3-discovery). This check is
informational and does not affect readiness levels or percentage scores.

## Website-only discovery

Serve JSON at `https://YOUR-DOMAIN/.well-known/poppy.json`:

```json
{
  "protocol_version": "0.1",
  "organization": { "name": "Example Company", "domain": "example.com" },
  "web": {}
}
```

Replace the example organization with your actual name and domain. The domain
must match the hostname of the requested well-known URL, ignoring leading
`www.`. HTTPS redirects to a hosting provider are allowed, but that provider's
hostname must not replace your organization domain. Return JSON, not your SPA's
HTML fallback. Unknown fields and optional extensions are allowed.

## Session-enabled interfaces

Declare the interfaces you actually implement: `agent.protocols` entries with
`type` and HTTPS `endpoint`, `apis` entries with `type`, HTTPS `url`, and
`description`, or `web.browser_session_endpoint`. Agent/API declarations and
browser-session endpoints require `auth.issuer`.

The issuer must publish RFC 8414 metadata with:

- `issuer` exactly matching `auth.issuer`;
- `poppy_domains` containing `organization.domain`;
- HTTPS `token_endpoint` and `revocation_endpoint`;
- `authorization_endpoint` when `auth.direct` is declared;
- `device_authorization_endpoint` when `auth.device` is declared.

For issuer `https://auth.example.com/tenant`, publish metadata at
`https://auth.example.com/.well-known/oauth-authorization-server/tenant`.
Direct, device, and mediated sign-in declarations contain scope arrays. Mediated
sign-in also describes its endpoint and credential fields; never put actual
credentials or secrets in discovery metadata.

Publish only capabilities backed by working implementations. Passing this check
confirms public discovery and issuer binding, not functioning sessions, sign-in,
API authorization, or conversations. The draft may change before version 1.0.

## Verify

Scan your site and inspect `checks.discovery.personalAgentProtocol`. Its
`details.issuerValidation` reports `verified`, `notRequired`, `unverified`,
`invalid`, or `notChecked`. Use the audit evidence to diagnose invalid fields,
redirects, and issuer/domain mismatches. Network failures and unsupported major
versions return `unableToCheck` while retaining available discovery evidence.
