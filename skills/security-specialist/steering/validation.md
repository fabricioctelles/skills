# Steering: Validate a Finding

Determine whether a reported finding is real and exploitable. Produce a verdict: `confirmed`, `false-positive`, or `needs-more-info`.

## Step 1: Load Finding Details

```bash
python3 scripts/scan_db.py show --finding-id <id>
```

Extract:
- The claimed vulnerability type (CWE)
- The location (file, line, function, or endpoint)
- The source of the report (which scanner, or manual)
- Any existing evidence or PoC

## Step 2: Read the Code at the Finding Location

Open the file. Read the function. Understand what it does. Don't rely on the scanner's snippet — scanners truncate context and miss surrounding logic.

Questions to answer:
- Does the pattern the scanner flagged actually exist here?
- Is this dead code? (unreachable, commented out, behind a permanent feature flag)
- Has it been refactored since the scan? (check git log for the file)

If the code doesn't match what the scanner reported → likely **false positive** from stale results.

## Step 3: Trace the Data Flow

This is the core of validation. You need to prove (or disprove) that attacker-controlled data reaches a dangerous operation.

### Identify the Source
Where does external input enter? Common sources:
- HTTP request parameters (query, body, headers, cookies)
- File uploads
- Database records (if populated by user input elsewhere)
- Environment variables (rarely attacker-controlled, but check)
- Message queues / event payloads

### Trace Through Transformations
Follow the data from source to the flagged location:
- Is it validated? (type check, regex, allowlist)
- Is it sanitized? (HTML encoding, SQL escaping, shell quoting)
- Is it transformed into a safe type? (parsed as integer, resolved as enum)
- Does it pass through a framework-level protection? (ORM parameterization, template auto-escape)

### Identify the Sink
The dangerous operation where the data lands:
- SQL query execution
- HTML rendering
- OS command execution
- File system operations
- Redirect targets
- Deserialization

### Document the Chain
Write it out explicitly:
```
Source: req.query.search (user-controlled, string, no length limit)
  → passed to: buildQuery(search) at db/queries.js:45
  → buildQuery concatenates into SQL string (NO parameterization)
  → executed via: db.raw(query) at db/queries.js:52
Sink: raw SQL execution
Mitigations: none found
Verdict: CONFIRMED — classic SQL injection
```

## Step 4: Check for Mitigating Controls

Even if the code pattern looks vulnerable, check for layers that might prevent exploitation:

- **WAF rules** — check for relevant WAF config (Cloudflare rules, AWS WAF, ModSecurity)
- **Input validation upstream** — a middleware or decorator that rejects malicious patterns before the code is reached
- **Framework protections** — auto-escaping, CSRF tokens, SameSite cookies, CSP
- **Network isolation** — is the vulnerable endpoint only accessible internally?
- **Authentication requirements** — does exploitation require a valid session?
- **Rate limiting** — does it prevent brute-force-style exploitation?

Mitigations don't make a finding false-positive — they reduce severity or exploitability. Note them but still confirm the underlying code flaw.

## Step 5: Attempt Proof-of-Concept (When Feasible)

If you can safely demonstrate exploitation without causing damage:

**For injection flaws:** Construct a payload that produces an observable side effect (e.g., time delay for blind SQLi, distinctive string in response for XSS).

**For auth bypasses:** Show the request that reaches protected resources without valid credentials.

**For path traversal:** Show the path that resolves outside the intended directory.

Document the PoC:
```
PoC: GET /api/search?q=' OR 1=1--
Expected: returns all records instead of filtered results
Observed: [what actually happened, or what WOULD happen based on code analysis]
```

### When Dynamic Testing Isn't Feasible

If you can't run the app (no local env, production-only, complex setup):
- Rely on static trace: source → transforms → sink
- State explicitly: "Static analysis only — no dynamic confirmation"
- Note what would be needed to confirm dynamically
- This is still valid for a `confirmed` verdict if the static trace is unambiguous

## Step 6: Render Verdict

| Verdict | Criteria |
|---------|----------|
| **confirmed** | Attacker-controlled data reaches a dangerous sink with insufficient protection. Exploit path is clear. |
| **false-positive** | The pattern doesn't exist, code is unreachable, or mitigations fully prevent exploitation at all layers. |
| **needs-more-info** | Can't determine from available evidence. Specify exactly what's missing (e.g., "need to check if WAF blocks this pattern," "need runtime testing"). |

## Step 7: Record the Validation Result

```bash
python3 scripts/scan_db.py validate \
  --finding-id <id> \
  --verdict <confirmed|false-positive|needs-more-info> \
  --evidence "source: req.query.q → sink: db.raw() at queries.js:52, no parameterization, no WAF" \
  --poc "GET /api/search?q=' OR 1=1--" \
  --notes "Static trace only, no dynamic confirmation"
```

## Principles

- A finding without a traceable data flow is not confirmed — it's a hypothesis.
- Scanners report patterns, not exploits. Your job is to determine if the pattern is exploitable in context.
- False positives are fine. Document why and move on. Don't waste cycles defending a scanner's output.
- "Needs-more-info" is honest. Better than guessing. State exactly what evidence would resolve it.
- Mitigations reduce risk but don't eliminate findings. A SQLi behind a WAF is still a SQLi — the WAF might get bypassed.
