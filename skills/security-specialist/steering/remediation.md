# Steering: Remediation

Fix a specific confirmed vulnerability. The goal is a minimal, correct patch that closes the security gap without introducing regressions.

## Step 1: Understand the Root Cause

Read the finding details from the scan database:
```bash
python3 scripts/scan_db.py show --finding-id <id>
```

Then answer:
- What is the **root cause**? (not the symptom — the actual design flaw or missing control)
- Where does untrusted data enter the system? (the source)
- What dangerous operation consumes it? (the sink)
- What check/transform is missing between source and sink?

Example: The symptom is "XSS in search results page." The root cause is "user input from query parameter is interpolated into HTML without encoding." The fix isn't "sanitize this one field" — it's "ensure all template output is auto-escaped, and this specific path uses the escaping mechanism."

## Step 2: Identify the Minimal Correct Fix

Pick the fix that:
1. Addresses the root cause, not just the specific instance
2. Uses the framework's built-in security mechanisms when available
3. Doesn't change unrelated behavior
4. Is consistent with how the rest of the codebase handles the same pattern

### Common Fix Patterns

**Injection (SQLi, NoSQLi, command injection):**
- Use parameterized queries / prepared statements. Never string concatenation.
- For OS commands: use array-based exec (no shell interpretation), or better — avoid shelling out entirely.

**Cross-Site Scripting (XSS):**
- Enable auto-escaping in the template engine (most modern frameworks do this by default).
- For cases requiring raw HTML: use a strict allowlist sanitizer (DOMPurify, bleach).
- Set `Content-Security-Policy` headers as defense-in-depth.

**Authentication/Authorization:**
- Add the missing auth check at the correct layer (middleware/decorator, not deep in business logic).
- Use the existing auth framework — don't invent a new check.
- Verify the check covers all HTTP methods, not just GET.

**Path Traversal:**
- Resolve the path, then verify it's within the allowed directory (use `realpath` comparison).
- Never rely on blacklisting `../` — normalize first, check after.

**SSRF:**
- Validate the target URL against an allowlist of permitted hosts/schemes.
- Block private IP ranges (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 169.254.0.0/16, fd00::/8).
- Disable redirects or re-validate after each redirect.

**Insecure Deserialization:**
- Don't deserialize untrusted data with unsafe deserializers (pickle, Java ObjectInputStream, PHP unserialize).
- Use data-only formats (JSON, protobuf) with schema validation.

**Secrets/Credentials:**
- Remove the hardcoded secret from code.
- Load from environment variable or secrets manager.
- Rotate the exposed credential immediately.

## Step 3: Implement the Fix

Write the patch. Keep the diff small and focused:
- Touch only files relevant to the vulnerability.
- If you discover a systemic issue (same pattern in 20 places), fix them all — but in a way that's reviewable (e.g., introduce a helper function, then replace all call sites).
- Add a code comment referencing the finding ID if the fix is non-obvious: `// Fix for SEC-042: parameterize user input`

## Step 4: Verify No Regressions

Run the project's existing test suite:
```bash
# Whatever the project uses — detect from package.json, Makefile, etc.
npm test / pytest / go test ./... / cargo test
```

If tests fail, the fix is wrong or incomplete. Adjust until green.

If no tests cover the affected code path, write a minimal test that exercises the fixed path with safe input and confirms it still works.

## Step 5: Verify the Fix Closes the Vulnerability

Re-run the scanner or analysis that found the issue:
```bash
python3 scripts/run_scan.py --target <file_or_dir> --rules <relevant_rule_id>
```

The finding should no longer appear. If it does, the fix is incomplete.

For manually-validated findings: re-trace the data flow. Confirm the dangerous operation is no longer reachable with attacker-controlled input, or that proper sanitization/validation now gates it.

## Step 6: Update the Scan Database

Mark the finding as fixed:
```bash
python3 scripts/scan_db.py update-status \
  --finding-id <id> \
  --status fixed
```

## Step 7: Document

If the fix introduced a new security pattern (new helper function, new middleware, new validation rule), document it briefly so future code follows the same pattern. Update the project's security guidelines or CONTRIBUTING.md if appropriate.

## Principles

- Fix the class of bug, not just the instance — but only if the codebase supports it without massive refactoring.
- The best fix uses mechanisms already present in the framework. Don't add a custom sanitizer when the template engine has auto-escape.
- A fix that breaks functionality is not a fix. Tests must pass.
- If the correct fix requires significant architectural change, flag it and propose a phased approach.
