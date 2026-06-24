# Threat Model

## Purpose

Build or update a structured threat model for the repository. Output is `.security/threat-model.md` — a living document that informs scan priorities and attack path analysis.

## Step 1: Identify the System

Answer these questions by reading the codebase:

- **What does it do?** — Core functionality in one paragraph
- **Who uses it?** — User roles (anonymous, authenticated, admin, service-to-service)
- **Where does it run?** — Cloud provider, container orchestration, serverless, bare metal, edge
- **What data does it handle?** — PII, financial, credentials, health data, public content
- **What's the deployment model?** — Single tenant, multi-tenant, self-hosted, managed

Document answers at the top of the threat model.

## Step 2: Map Trust Boundaries

Draw the lines between zones of different trust:

- **External → Application** — internet-facing load balancer, API gateway
- **Application → Database** — app server to data store
- **Application → External Services** — third-party APIs, payment processors
- **User tiers** — anonymous vs authenticated vs admin
- **Service-to-service** — internal microservice communication
- **CI/CD → Production** — deployment pipeline access

For each boundary, note:
- What crosses it (data, commands, credentials)
- How it's protected (TLS, auth tokens, network policy, nothing)

## Step 3: Identify Entry Points

Every place external input enters the system:

| Entry Point | Protocol | Auth Required | Input Type |
|---|---|---|---|
| `POST /api/login` | HTTPS | No | JSON body |
| `GET /api/users/:id` | HTTPS | Yes (JWT) | URL param |
| WebSocket `/ws` | WSS | Yes (session) | Messages |
| Message queue consumer | AMQP | Service account | Serialized events |
| CLI commands | Local | OS user | Arguments + stdin |
| File upload endpoint | HTTPS | Yes | Multipart binary |

Be exhaustive. Every entry point is a potential attack vector.

## Step 4: Map Data Flows

For each significant data type, trace its lifecycle:

1. **Ingestion** — where it enters the system
2. **Processing** — what transforms or validates it
3. **Storage** — where it persists (DB, cache, file, log)
4. **Transmission** — where it's sent (other services, external APIs, user responses)
5. **Deletion** — how/when it's purged

Flag any data flow that crosses a trust boundary without adequate protection.

## Step 5: Enumerate Threats (STRIDE)

For each entry point and data flow, apply STRIDE:

| Category | Question |
|---|---|
| **Spoofing** | Can an attacker impersonate a legitimate user or service? |
| **Tampering** | Can data be modified in transit or at rest without detection? |
| **Repudiation** | Can actions be performed without audit trail? |
| **Information Disclosure** | Can sensitive data leak through errors, logs, side channels? |
| **Denial of Service** | Can the system be exhausted or crashed? |
| **Elevation of Privilege** | Can a low-privilege user gain higher access? |

For each identified threat, document:

```
### T-<number>: <Title>

**Category:** Spoofing / Tampering / Repudiation / Info Disclosure / DoS / EoP
**Entry Point:** <where the attack starts>
**Affected Component:** <what's at risk>
**Likelihood:** High / Medium / Low
**Impact:** Critical / High / Medium / Low
**Current Mitigations:** <what's already in place, or "None">
**Residual Risk:** <what remains after mitigations>
```

## Step 6: Assess Likelihood and Impact

Likelihood considers:
- Is the entry point internet-facing or internal-only?
- Does exploitation require authentication?
- Is the vulnerability pattern common and well-tooled?
- Are there known exploits in the wild for this class?

Impact considers:
- What data is compromised? (PII = high, public content = low)
- Can the attacker pivot to other systems?
- Is there financial, legal, or reputational damage?
- How many users are affected?

## Step 7: Document Assumptions

Every threat model rests on assumptions. Make them explicit:

- "Internal network is trusted" — is it?
- "Admin users are not adversaries" — always true?
- "TLS terminates at the load balancer" — verified?
- "Database is not internet-accessible" — checked?
- "Third-party dependencies are not compromised" — hope so

These assumptions are the first thing to revisit when the system changes.

## Step 8: Write Output

Save to `.security/threat-model.md` with this structure:

```
# Threat Model — <Project Name>
Last updated: <date>

## System Description
## Trust Boundaries
## Entry Points
## Data Flows
## Threats
## Assumptions
## Review History
```

## When to Update

- New entry point added (route, consumer, endpoint)
- Architecture change (new service, new data store, new external dependency)
- Deployment model change (moved to different infra, added multi-tenancy)
- After a security incident (assumptions proved wrong)
- Every 6 months as a hygiene check

## Notes

- A threat model isn't a findings list. It's a map of WHERE to look and WHAT to worry about.
- Don't over-enumerate. Focus on threats with realistic attack paths, not theoretical exercises.
- If the system is simple (static site, no user data), keep the model proportionally simple. One page is fine.
