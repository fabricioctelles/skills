# Targeted Vulnerability Discovery

## Purpose

Focused security analysis on a subset of files. Used after a threat model identifies high-risk components, after a dependency alert, or when investigating a specific concern. More surgical than a full scan — assumes you already know WHERE to look.

## When to Use

- Threat model flagged specific components as high-risk
- A new entry point or data flow was added
- Dependency alert requires assessing blast radius
- Post-incident investigation of specific modules
- Reviewer wants depth on auth, payments, or other critical subsystems

## Step 1: Receive Target Scope

Input is one of:
- A file list (explicit paths)
- A component/module name (resolve to files)
- A directory subtree
- A functional area ("all auth code", "payment processing")

If given a vague scope, resolve to concrete files before proceeding.

## Step 2: Generate Ranked Worklist

```bash
python3 scripts/rank_files.py --files <file1> <file2> ... --output worklist.json
```

The ranker scores files by:
- Proximity to entry points (routes, handlers, consumers)
- Presence of security-sensitive patterns (SQL, exec, file I/O, crypto, auth checks)
- Complexity metrics (cyclomatic complexity, line count)
- History of changes (frequently modified = higher churn risk)

Output: ordered list of files with priority scores and reason tags.

## Step 3: Analyze Each File

Work through the worklist in priority order. For each file:

### 3a. Understand Role
- What does this file do in the system?
- What data flows through it?
- Who calls it? What does it call?
- What trust level is the caller at?

### 3b. Check Input Boundaries
- Where does external data enter this code?
- Is it validated before use? (type, format, length, range)
- Are there implicit assumptions about input shape?

### 3c. Check Security Controls
- Authentication enforced? At what level?
- Authorization checked? Against what?
- Rate limiting present?
- Error handling safe? (no stack traces, no sensitive data in errors)

### 3d. Check Dangerous Operations
- SQL/NoSQL queries — parameterized or string-built?
- Command execution — input reaches shell?
- File operations — path controlled by user?
- Deserialization — untrusted data deserialized?
- Crypto usage — correct algorithms, modes, key management?
- Logging — sensitive data written to logs?

### 3e. Check Framework-Specific Issues

Adapt to the stack:
- **Node/Express** — prototype pollution, ReDoS, missing helmet headers
- **Python/Django/Flask** — template injection, pickle deserialization, debug mode
- **Go** — integer overflow, unsafe pointer use, goroutine leaks with user input
- **Java/Spring** — SpEL injection, XXE in XML parsing, actuator exposure
- **Ruby/Rails** — mass assignment, unsafe render, YAML deserialization
- **Rust** — unsafe blocks, FFI boundary issues, panic in handlers

## Step 4: Record Findings

For each issue discovered:

```bash
python3 scripts/scan_db.py add-finding \
  --severity <critical|high|medium|low|info> \
  --category <auth|injection|crypto|data-exposure|config|logic> \
  --file <relative-path> \
  --line <line-number> \
  --title "<concise title>" \
  --evidence "<vulnerable code snippet>" \
  --impact "<what an attacker gains>" \
  --recommendation "<specific fix, not generic advice>"
```

### Evidence Standard

Every finding requires:
- Exact location (file + line range)
- The vulnerable code, quoted
- A concrete attack scenario: "An attacker with [access level] sends [input] to [endpoint], which reaches [this code] and causes [effect]"
- Why existing protections (if any) don't prevent it

## Step 5: Cross-Reference

After analyzing all files in the worklist:

- Do any findings chain together? (e.g., IDOR + missing auth = account takeover)
- Do findings contradict the threat model assumptions?
- Are there patterns? (same mistake repeated = systemic issue, not one-off)

If chains exist, document them using `steering/attack-paths.md`.

## Step 6: Report Findings

Output a summary scoped to this discovery pass:

```
## Discovery: <Area Name>
Date: <date>
Scope: <file count> files in <component>
Findings: <count by severity>

### Critical
### High
### Medium
### Low
### Observations (no finding, but notable)
```

## Completion Criteria

Discovery is complete when:
- Every file in the worklist has been analyzed
- All findings are recorded in the scan DB
- Cross-references and chains are documented
- No file was skipped without explicit justification

## Notes

- Discovery is depth-first, not breadth-first. Go deep on each file rather than skimming many.
- If a file pulls in dependencies you haven't seen, follow the call chain. Vulnerabilities hide in utility code.
- "No findings" for a critical file is a valid and useful result. Record it — confirms the component is clean as of this review.
- If you discover the scope should be wider (e.g., auth module calls a helper that's not in the target list), expand and document why.
