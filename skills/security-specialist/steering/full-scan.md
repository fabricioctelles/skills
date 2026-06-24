# Full Repository Security Scan

## Purpose

Systematic security audit of an entire repository. Produces a structured findings database and a sealed final report.

## Step 1: Initialize Scan

```bash
python3 scripts/scan_db.py init --repo <path>
```

This creates the scan directory (`.security/scans/<timestamp>/`) with metadata, empty findings DB, and scope manifest.

## Step 2: Identify Scope

Read the repo top-down. Determine:

- **Languages & frameworks** — check package manifests (`package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`, `pom.xml`, etc.)
- **Entry points** — HTTP routes, CLI commands, message consumers, cron jobs, serverless handlers
- **Data stores** — databases, caches, file storage, external APIs called
- **Auth mechanisms** — session management, JWT, OAuth, API keys, mTLS
- **Deployment context** — Dockerfile, k8s manifests, serverless config, CI/CD pipelines

Record scope in the scan directory as `scope.md`.

## Step 3: Check for Existing Threat Model

Look for `.security/threat-model.md`. If absent or stale (last modified > 6 months), run the `steering/threat-model.md` workflow first. The threat model informs priority ordering.

## Step 4: Systematic Analysis — Priority Order

Analyze files grouped by risk category. Within each category, start with the most exposed code (public-facing, unauthenticated).

### Priority 1: Authentication & Authorization
- Session management, token generation/validation
- Role checks, permission gates, middleware
- Password handling, credential storage
- OAuth flows, API key validation

### Priority 2: Input Handling
- Request parsing, deserialization
- SQL/NoSQL query construction
- Command execution, file path construction
- Template rendering, output encoding

### Priority 3: Cryptography
- Key generation, storage, rotation
- Encryption/decryption implementations
- Hashing (passwords, integrity checks)
- TLS configuration, certificate handling

### Priority 4: Data Storage & Transmission
- Database queries (injection surface)
- File read/write operations
- Logging (sensitive data exposure)
- API calls to external services (credential leakage)

### Priority 5: Configuration & Infrastructure
- Environment variable handling
- Secret management
- CORS, CSP, security headers
- Dependency versions (known CVEs)

## Step 5: Record Findings

For each issue found, record it with full evidence:

```bash
python3 scripts/scan_db.py add-finding \
  --severity <critical|high|medium|low|info> \
  --category <auth|injection|crypto|data-exposure|config|dependency> \
  --file <relative-path> \
  --line <line-number> \
  --title "<short description>" \
  --evidence "<code snippet or explanation>" \
  --impact "<what an attacker gains>" \
  --recommendation "<specific fix>"
```

### Evidence Requirements

Every finding MUST include:
- The exact code (file + line range) that's vulnerable
- A concrete attack scenario (not "could be exploited" — HOW)
- The prerequisite access level needed (unauth, authenticated user, admin, local)
- A specific remediation, not generic advice

## Step 6: Validate High-Severity Findings

For any finding rated `critical` or `high`:

1. Trace the data flow from entry point to vulnerable code — confirm it's reachable
2. Check for existing mitigations (WAF rules, input validation upstream, framework protections)
3. If a mitigation exists, downgrade or annotate accordingly
4. If no mitigation, confirm the attack path (reference `steering/attack-paths.md` for complex cases)

## Step 7: Dependency Audit

- Check lock files for known CVEs (cross-reference with advisory databases)
- Flag dependencies with no recent maintenance (2+ years stale)
- Identify transitive dependencies pulling in vulnerable versions

## Step 8: Generate Final Report

```bash
python3 scripts/finalize.py --scan-dir <dir>
```

This seals the scan — produces `report.md` with:
- Executive summary (finding counts by severity)
- Scope description
- Findings ordered by severity, each with evidence and remediation
- Dependency audit results
- Recommendations prioritized by effort/impact ratio

## Output

- `.security/scans/<timestamp>/report.md` — human-readable report
- `.security/scans/<timestamp>/findings.json` — machine-readable findings DB
- `.security/scans/<timestamp>/scope.md` — what was analyzed

## Notes

- Don't skip files because they "look safe." Utility modules often contain injection sinks.
- Framework defaults aren't always secure. Verify — don't assume.
- If the repo is large (>500 files), split into batches using `steering/discovery.md` for targeted passes after the initial sweep.
