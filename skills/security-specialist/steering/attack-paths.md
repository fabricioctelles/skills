# Attack Path Tracing

## Purpose

Map the exploitation path for a confirmed or suspected vulnerability. Starts from a finding, traces backward to entry point and forward to impact. Produces a realistic severity assessment based on actual exploitability — not theoretical worst-case.

## When to Use

- A finding from `steering/full-scan.md` or `steering/discovery.md` needs severity validation
- Triaging whether a vulnerability is actually reachable
- Building proof-of-concept narratives for critical findings
- Disputing or confirming a severity rating

## Step 1: Start from the Finding

Document the vulnerability anchor:

- **What:** The vulnerable code (file, line, function)
- **Class:** Injection, auth bypass, IDOR, SSRF, path traversal, etc.
- **Primitive:** What the attacker gains if this fires (read arbitrary data, execute code, escalate privilege)

## Step 2: Trace Entry Point → Vulnerability

Work backward. How does attacker-controlled input reach the vulnerable code?

Map the chain:

```
Entry Point (HTTP route, message queue, CLI arg)
  → Input processing (parsing, deserialization)
    → Validation (what checks exist between entry and sink)
      → Intermediate transforms (encoding, type conversion, mapping)
        → Vulnerable code (the sink)
```

At each hop, document:
- What data flows through
- What transformations or filters apply
- Whether the attacker retains control over the data

If a hop breaks the chain (e.g., input is cast to integer before reaching SQL query), the path is dead. Document why and downgrade.

## Step 3: Identify Prerequisites

What must be true for the attack to work?

| Factor | Questions |
|---|---|
| **Authentication** | Does the attacker need a valid session? What role? |
| **Network position** | Must they be on the internet, internal network, localhost? |
| **Application state** | Does a specific condition need to exist (feature flag, data in DB)? |
| **Race condition** | Is timing critical? How tight is the window? |
| **User interaction** | Does a victim need to click/visit something? |
| **Chaining** | Does this require another vulnerability to be exploitable first? |

Each prerequisite reduces exploitability. Stack them honestly.

## Step 4: Map Impact Forward

From the vulnerable code, what happens when it fires?

```
Vulnerable code triggers
  → Immediate effect (SQL executes, file reads, command runs)
    → Data accessed/modified (what exactly)
      → Lateral movement possible? (pivot to other services, escalate)
        → Final impact (data breach, RCE, account takeover, DoS)
```

Be specific about impact scope:
- Single user's data vs. all users
- Read-only vs. read-write
- Contained to one service vs. cross-service pivot
- Persistent vs. one-shot

## Step 5: Check Existing Mitigations

Before finalizing severity, verify what's already blocking this path:

- **WAF/rate limiting** — does it catch this payload pattern?
- **Framework protections** — auto-escaping, parameterized queries, CSRF tokens
- **Network policy** — is the target service isolated?
- **Monitoring/alerting** — would exploitation trigger alerts?
- **Input validation upstream** — is there a check we missed?

If mitigations exist, document them and assess residual risk. A mitigated path is still a finding (defense in depth matters), but severity drops.

## Step 6: Assign Severity

Use this matrix — exploitability × impact:

| | Critical Impact | High Impact | Medium Impact | Low Impact |
|---|---|---|---|---|
| **Easy to exploit** (unauth, no prereqs) | Critical | High | Medium | Low |
| **Moderate** (auth required, simple chain) | High | High | Medium | Low |
| **Difficult** (multi-step chain, race, internal network) | High | Medium | Low | Info |
| **Very difficult** (requires prior RCE, admin, physical) | Medium | Low | Info | Info |

Impact levels:
- **Critical** — RCE, full data breach, complete auth bypass
- **High** — significant data exposure, privilege escalation, account takeover
- **Medium** — limited data leak, single-user impact, partial bypass
- **Low** — information disclosure, minor integrity issue

## Step 7: Document the Path

Output format:

```
## Attack Path: <Title>

**Finding Reference:** <link to finding in scan DB>
**Final Severity:** <Critical/High/Medium/Low/Info>

### Chain

1. Attacker sends [specific input] to [entry point]
2. Input passes through [component] where [transform happens]
3. Reaches [vulnerable code] at [file:line]
4. Triggers [primitive] resulting in [immediate effect]
5. Attacker gains [final impact]

### Prerequisites
- [List each requirement]

### Mitigations Present
- [List what partially blocks this]

### Mitigations Absent
- [List what should exist but doesn't]

### Evidence
[Code snippets, data flow diagram, or PoC outline]
```

## Step 8: Recommend Action

Based on the path analysis:

- **Critical/High with easy exploit** → Fix immediately, consider if already exploited
- **Medium** → Fix in next sprint, add detection
- **Low/Info** → Track, fix opportunistically
- **Mitigated but structurally present** → Harden, don't ignore. Mitigations fail.

## Notes

- Real severity comes from the PATH, not the pattern. SQLi behind three auth gates and only reaching a public data table is not critical.
- Conversely, a "low-severity" IDOR that leaks all customer records is critical regardless of what the textbook says about IDORs.
- If you can't trace a complete path from entry to impact, the finding might be theoretical. Say so explicitly rather than inflating.
- Attack paths compound. Two medium findings that chain into a critical outcome should be reported as critical.
