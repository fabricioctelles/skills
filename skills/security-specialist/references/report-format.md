# Report Format Specification

The final report is a **self-contained HTML file** (`security-report.html`). It opens in any browser, uses no external dependencies, and includes interactive features (collapsible sections, filters, color-coded severity).

---

## Output Format

Single HTML file with embedded CSS and JS. No external CDN, no build step. The report must work offline when opened with `file://`.

---

## Severity Color System

| Severity | Color | Badge HTML |
|----------|-------|-----------|
| Critical | `#dc2626` (red-600) | `<span class="badge badge-critical">CRITICAL</span>` |
| High | `#ea580c` (orange-600) | `<span class="badge badge-high">HIGH</span>` |
| Medium | `#ca8a04` (yellow-600) | `<span class="badge badge-medium">MEDIUM</span>` |
| Low | `#16a34a` (green-600) | `<span class="badge badge-low">LOW</span>` |
| Info | `#6b7280` (gray-500) | `<span class="badge badge-info">INFO</span>` |

---

## HTML Template

Generate the report using this structure. Replace `{{placeholders}}` with actual data.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Security Audit — {{repo-name}}</title>
<style>
  :root {
    --critical: #dc2626; --high: #ea580c; --medium: #ca8a04;
    --low: #16a34a; --info: #6b7280; --pass: #16a34a; --fail: #dc2626;
    --bg: #0f172a; --surface: #1e293b; --surface-2: #334155;
    --text: #f1f5f9; --text-muted: #94a3b8; --border: #475569;
    --code-bg: #0f172a; --accent: #3b82f6;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', -apple-system, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem; max-width: 1200px; margin: 0 auto; }
  h1 { font-size: 1.75rem; margin-bottom: 0.25rem; }
  h2 { font-size: 1.35rem; margin: 2.5rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--border); }
  h3 { font-size: 1.1rem; margin: 1.5rem 0 0.5rem; }
  p, li { color: var(--text-muted); }
  a { color: var(--accent); }
  code { background: var(--code-bg); border: 1px solid var(--border); padding: 0.15em 0.4em; border-radius: 4px; font-size: 0.85em; }
  pre { background: var(--code-bg); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; overflow-x: auto; margin: 0.75rem 0; }
  pre code { border: none; padding: 0; background: none; }

  /* Badges */
  .badge { display: inline-block; padding: 0.2em 0.6em; border-radius: 4px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: white; }
  .badge-critical { background: var(--critical); }
  .badge-high { background: var(--high); }
  .badge-medium { background: var(--medium); }
  .badge-low { background: var(--low); }
  .badge-info { background: var(--info); }
  .badge-pass { background: var(--pass); }
  .badge-fail { background: var(--fail); }

  /* Summary cards */
  .summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1rem; margin: 1rem 0; }
  .summary-card { background: var(--surface); border-radius: 8px; padding: 1rem; text-align: center; border-left: 4px solid var(--border); }
  .summary-card .count { font-size: 2rem; font-weight: 700; }
  .summary-card .label { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; }
  .summary-card.critical { border-left-color: var(--critical); }
  .summary-card.critical .count { color: var(--critical); }
  .summary-card.high { border-left-color: var(--high); }
  .summary-card.high .count { color: var(--high); }
  .summary-card.medium { border-left-color: var(--medium); }
  .summary-card.medium .count { color: var(--medium); }
  .summary-card.low { border-left-color: var(--low); }
  .summary-card.low .count { color: var(--low); }
  .summary-card.info { border-left-color: var(--info); }
  .summary-card.info .count { color: var(--info); }

  /* Tables */
  table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }
  th, td { padding: 0.6rem 0.8rem; text-align: left; border-bottom: 1px solid var(--border); }
  th { background: var(--surface); color: var(--text); font-weight: 600; position: sticky; top: 0; }
  tr:hover { background: var(--surface); }

  /* Finding cards */
  .finding { background: var(--surface); border-radius: 8px; padding: 1.25rem; margin: 1rem 0; border-left: 4px solid var(--border); }
  .finding.critical { border-left-color: var(--critical); }
  .finding.high { border-left-color: var(--high); }
  .finding.medium { border-left-color: var(--medium); }
  .finding.low { border-left-color: var(--low); }
  .finding.info { border-left-color: var(--info); }
  .finding-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem; }
  .finding-title { font-weight: 600; font-size: 1rem; }
  .finding-meta { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.5rem; }

  /* Pentest results */
  .pentest-item { background: var(--surface); border-radius: 8px; padding: 1rem; margin: 0.75rem 0; }
  .pentest-item .result-pass { color: var(--pass); font-weight: 700; }
  .pentest-item .result-fail { color: var(--fail); font-weight: 700; }

  /* Collapsible */
  details { margin: 0.5rem 0; }
  details summary { cursor: pointer; padding: 0.5rem; border-radius: 4px; font-weight: 600; }
  details summary:hover { background: var(--surface-2); }
  details[open] summary { margin-bottom: 0.5rem; }

  /* CVE table */
  .cve-exploitable { color: var(--fail); font-weight: 700; }
  .cve-not-exploitable { color: var(--pass); }

  /* Filters */
  .filters { display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 1rem 0; }
  .filter-btn { padding: 0.4em 0.8em; border-radius: 4px; border: 1px solid var(--border); background: var(--surface); color: var(--text-muted); cursor: pointer; font-size: 0.8rem; transition: 0.2s; }
  .filter-btn:hover, .filter-btn.active { background: var(--accent); color: white; border-color: var(--accent); }

  /* Metadata */
  .meta-grid { display: grid; grid-template-columns: auto 1fr; gap: 0.25rem 1rem; font-size: 0.9rem; margin: 1rem 0; }
  .meta-grid dt { color: var(--text-muted); }
  .meta-grid dd { color: var(--text); }

  @media (max-width: 768px) {
    body { padding: 1rem; }
    .summary-grid { grid-template-columns: repeat(3, 1fr); }
  }
</style>
</head>
<body>

<h1>🛡️ Security Audit Report</h1>
<dl class="meta-grid">
  <dt>Repository</dt><dd>{{repo-name}}</dd>
  <dt>Date</dt><dd>{{date}}</dd>
  <dt>Target</dt><dd>{{target-urls}}</dd>
  <dt>Methodology</dt><dd>SAST + DAST (localhost) + DAST (production) + Pentest</dd>
</dl>

<!-- Section: Summary Cards -->
<h2>Resumo</h2>
<div class="summary-grid">
  <div class="summary-card critical"><div class="count">{{critical-count}}</div><div class="label">Critical</div></div>
  <div class="summary-card high"><div class="count">{{high-count}}</div><div class="label">High</div></div>
  <div class="summary-card medium"><div class="count">{{medium-count}}</div><div class="label">Medium</div></div>
  <div class="summary-card low"><div class="count">{{low-count}}</div><div class="label">Low</div></div>
  <div class="summary-card info"><div class="count">{{info-count}}</div><div class="label">Info</div></div>
</div>
<p>{{executive-summary-paragraph}}</p>

<!-- Section: Findings with filters -->
<h2>Achados</h2>
<div class="filters">
  <button class="filter-btn active" onclick="filterFindings('all')">Todos</button>
  <button class="filter-btn" onclick="filterFindings('critical')">Critical</button>
  <button class="filter-btn" onclick="filterFindings('high')">High</button>
  <button class="filter-btn" onclick="filterFindings('medium')">Medium</button>
  <button class="filter-btn" onclick="filterFindings('low')">Low</button>
  <button class="filter-btn" onclick="filterFindings('info')">Info</button>
</div>

<!-- Repeat this block for each finding -->
<div class="finding {{severity}}" data-severity="{{severity}}">
  <div class="finding-header">
    <span class="badge badge-{{severity}}">{{SEVERITY}}</span>
    <span class="finding-title">{{finding-title}}</span>
  </div>
  <div class="finding-meta">📁 <code>{{file}}:{{line}}</code></div>
  <p>{{description}}</p>
  <details>
    <summary>Evidência</summary>
    <pre><code>{{evidence-code}}</code></pre>
  </details>
  <details>
    <summary>Remediação</summary>
    <p>{{remediation-text}}</p>
    <pre><code>{{remediation-code}}</code></pre>
  </details>
</div>
<!-- End finding block -->

<!-- Section: CVE Analysis -->
<h2>Análise de CVEs × Contexto do Projeto</h2>
<table>
  <thead>
    <tr><th>#</th><th>Advisory</th><th>Sev. Genérica</th><th>Precondição</th><th>Presente?</th><th>Sev. Real</th><th>Razão</th></tr>
  </thead>
  <tbody>
    <!-- Repeat per CVE -->
    <tr>
      <td>{{n}}</td>
      <td><a href="{{advisory-url}}">{{advisory-id}}</a></td>
      <td><span class="badge badge-{{generic-sev}}">{{generic-sev}}</span></td>
      <td>{{precondition}}</td>
      <td class="{{cve-exploitable|cve-not-exploitable}}">{{yes-no}}</td>
      <td><span class="badge badge-{{real-sev}}">{{real-sev}}</span></td>
      <td>{{rationale}}</td>
    </tr>
  </tbody>
</table>

<!-- Section: Pentest Results -->
<h2>Pentest — Testes Ativos</h2>

<!-- Repeat per test -->
<div class="pentest-item">
  <strong>P{{n}}: {{test-name}}</strong>
  <span class="{{result-pass|result-fail}}">{{PASS|FAIL}}</span>
  <details>
    <summary>Detalhes</summary>
    <p><strong>Objetivo:</strong> {{objective}}</p>
    <pre><code>{{command-or-payload}}</code></pre>
    <p><strong>Resposta:</strong> {{response-summary}}</p>
  </details>
</div>
<!-- End pentest block -->

<!-- Section: Verified Secure -->
<h2>Verificado Seguro ✅</h2>
<table>
  <thead><tr><th>Teste</th><th>Resultado</th><th>Evidência</th></tr></thead>
  <tbody>
    <!-- Repeat per negative finding -->
    <tr>
      <td>{{test-name}}</td>
      <td><span class="badge badge-pass">PASS</span></td>
      <td>{{evidence}}</td>
    </tr>
  </tbody>
</table>

<!-- Section: Recommendations -->
<h2>Remediação Prioritária</h2>
<table>
  <thead><tr><th>#</th><th>Ação</th><th>Esforço</th><th>Impacto</th></tr></thead>
  <tbody>
    <!-- Repeat per recommendation -->
    <tr><td>{{n}}</td><td>{{action}}</td><td>{{effort}}</td><td>{{impact}}</td></tr>
  </tbody>
</table>

<script>
function filterFindings(severity) {
  document.querySelectorAll('.finding').forEach(el => {
    el.style.display = (severity === 'all' || el.dataset.severity === severity) ? '' : 'none';
  });
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.toLowerCase() === severity || (severity === 'all' && btn.textContent === 'Todos'));
  });
}
</script>

<footer style="margin-top:4rem;padding-top:1.5rem;border-top:1px solid var(--border);text-align:center;font-size:0.8rem;color:var(--text-muted);">
  Generated by <strong>security-specialist</strong> skill by <a href="https://github.com/fabriciotelles/skills" style="color:var(--accent);">github.com/fabriciotelles/skills</a>
</footer>
</body>
</html>
```

---

## Generation Rules

1. **Output a single `.html` file** — not markdown. Name it `security-report.html` in the repo root.
2. **Replace all `{{placeholders}}`** with actual data from the scan.
3. **Repeat blocks** as indicated by comments (`<!-- Repeat per finding -->`, etc.).
4. **Sort findings** by severity descending (critical first), then alphabetically.
5. **Collapsible evidence/remediation** — keeps the report scannable without hiding info.
6. **Filter buttons** — JS filters findings by severity interactively.
7. **Code in evidence** — use `<pre><code>` blocks, HTML-escape all special characters.
8. **Links in CVE table** — advisory IDs link to the GitHub advisory URL.
9. **No external dependencies** — no CDN fonts, no JS libs. Pure HTML/CSS/JS.
10. **Dark theme by default** — matches terminal-native developer workflows.

---

## Content Rules (unchanged from markdown era)

- Every finding needs source location, data flow trace, and concrete exploitability.
- Never truncate evidence to the point where it loses meaning.
- Keep descriptions factual. No speculative language.
- The report must be self-contained.
- Include ALL tests performed (pentest section), including those that passed.
- CVE analysis table is mandatory when dependency vulns exist.
- Negative results table is mandatory — reader needs to know what was tested and found secure.
