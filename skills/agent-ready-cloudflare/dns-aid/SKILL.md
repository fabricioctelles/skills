---
name: agent-ready-dns-aid
description: >
  Sub-skill de agent-ready-cloudflare: Implement DNS for AI Discovery (DNS-AID)
---
# Implement DNS for AI Discovery (DNS-AID)

Publish DNS for AI Discovery (DNS-AID) records so agents can discover your agent endpoints through DNS.

## Requirements

- Publish DNS for AI Discovery (DNS-AID) records under your domain's `_agents` namespace, such as `_index._agents.example.com` or `_a2a._agents.example.com`
- Use ServiceMode `SVCB` records, or `HTTPS` records for HTTPS endpoints, with `alpn` and endpoint connection parameters
- Use numeric `keyNNNNN` SvcParamKey names for experimental DNS for AI Discovery (DNS-AID) custom parameters until they are registered
- Sign public DNS for AI Discovery (DNS-AID) discovery zones with DNSSEC so validating resolvers return authenticated data

## Example

```dns
_a2a._agents.example.com. 3600 IN SVCB 1 agent.example.com. alpn="a2a" port=443 mandatory=alpn,port
```

## Validate

The scanner validates DNS for AI Discovery (DNS-AID) via DNS-over-HTTPS. By default, the scanner uses Cloudflare's `https://cloudflare-dns.com/dns-query` with automatic fallback to `https://dns.google/resolve` on resolver-level failures. Library callers can override the resolver with `ScanOptions.dohResolverUrl` (disables fallback).

```http
POST https://isitagentready.com/api/scan
Content-Type: application/json

{"url": "https://YOUR-SITE.com"}
```

Check that `checks.discoverability.dnsAid.status` is `"pass"`.

## References

- [draft-mozleywilliams-dnsop-dnsaid](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/)
- [RFC 9460 — SVCB and HTTPS Resource Records](https://www.rfc-editor.org/info/rfc9460)
