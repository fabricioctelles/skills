# OKF Bundle Examples (v0.2)

Complete, conformant bundles demonstrating v0.2 features: provenance (`sources`), trust (`generated`, `verified`), lifecycle (`status`, `stale_after`), and Attested Computations.

---

## 1. Finance Analytics with Attested Computations

A financial reporting bundle with sanctioned, verifiable calculations.

```
finance/
├── index.md
├── log.md
├── metrics/
│   ├── index.md
│   └── income-statement.md
├── computations/
│   ├── index.md
│   ├── revenue.md
│   └── gross-profit.md
└── references/
    ├── skills/
    │   └── run-on-bq.md
    └── attesters/
        └── sql-equality.py
```

### index.md (bundle root)

```markdown
---
okf_version: "0.2"
---

# Finance Analytics Bundle

Knowledge base for financial reporting and KPIs.

- [Metrics](./metrics/) - Business KPIs and financial statements
- [Computations](./computations/) - Sanctioned calculations (attestable)
- [References](./references/) - Skills and attesters for execution
```

### metrics/income-statement.md

```markdown
---
type: Metric
title: Income statement (fiscal year)
description: Headline income-statement figures for a fiscal year.
tags: [finance, income-statement, kpi]
status: stable
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: fpa-handbook
    resource: https://wiki.acme/finance/fpa-handbook
    title: FP&A reporting handbook
    author: team:finance-fpa
    last_modified: 2026-03-15T00:00:00Z
---

# Definition

The income statement reports [revenue](../computations/revenue.md) and
[gross profit](../computations/gross-profit.md) for a fiscal year, per the 
FP&A reporting handbook.[^fpa-handbook]

Each figure is produced by a sanctioned, attestable computation; this 
concept only narrates them.

## Key Figures

| Figure | Computation | Status |
|--------|-------------|--------|
| Revenue | [revenue.md](../computations/revenue.md) | Human-verified |
| Gross Profit | [gross-profit.md](../computations/gross-profit.md) | Machine-confirmed |

[^fpa-handbook]: FP&A reporting handbook
```

### computations/revenue.md (Attested Computation)

```markdown
---
type: Attested Computation
title: Revenue for fiscal year
description: Recognized revenue for a fiscal year, per Finance's definition.
tags: [finance, revenue]
status: stable
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: /references/skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: /references/attesters/sql-equality.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-28T14:00:00Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: rev-policy
    resource: https://wiki.acme/finance/revenue-recognition
    title: Revenue recognition policy
    author: team:finance-fpa
    last_modified: 2026-04-02T00:00:00Z
  - id: exec-rev-dash
    resource: dashboards/exec-revenue
    title: Executive revenue dashboard
    author: team:finance-fpa
    usage_count: 5000
    last_modified: 2026-06-18T00:00:00Z
usage_window: { from: 2026-06-01T00:00:00Z, to: 2026-06-30T00:00:00Z }
---

# Computation

```sql
SELECT SUM(amount) AS revenue
FROM finance.recognized_revenue
WHERE fiscal_year = @year
```

Recognized revenue per the recognition policy,[^rev-policy] corroborated by
the executive revenue dashboard.[^exec-rev-dash]

# Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `year` | integer | Yes | Fiscal year (e.g., 2026) |

# Usage

```python
# Agent fills parameters only, never edits computation
result = executor.run(year=2026)
verdict = attester.verify(result.receipt)
```

[^rev-policy]: Revenue recognition policy
[^exec-rev-dash]: Executive revenue dashboard
```

### computations/gross-profit.md (Attested Computation - dbt)

```markdown
---
type: Attested Computation
title: Gross profit for fiscal year
description: Gross profit by segment for a fiscal year, per the cost-allocation standard.
tags: [finance, profit]
status: stable
runtime: dbt
parameters:
  - { name: year, type: integer, required: true }
  - { name: segment, type: string, required: true }
executor:
  resource: /references/skills/run-dbt.md
  receipt: [run_id, compiled_sql, result]
attester:
  resource: /references/attesters/dbt-binding.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-14T14:00:00Z }
verified: { by: process:finance-nightly, at: 2026-06-12T08:00:00Z }
stale_after: 2026-06-15T00:00:00Z
sources:
  - id: cost-alloc
    resource: https://wiki.acme/finance/cost-allocation
    title: Cost allocation standard
    author: team:finance-fpa
---

# Computation

```sql
SELECT gross_profit
FROM {{ ref('fct_income_statement') }}
WHERE fiscal_year = {{ var('year') }}
  AND segment = {{ var('segment') }}
```

Gross profit by segment per the cost-allocation standard.[^cost-alloc]

[^cost-alloc]: Cost allocation standard
```

---

## 2. E-commerce Analytics (v0.2)

```
ecommerce/
├── index.md
├── tables/
│   ├── index.md
│   ├── orders.md
│   └── customers.md
└── metrics/
    ├── index.md
    └── gross-revenue.md
```

### tables/orders.md

```markdown
---
type: BigQuery Table
title: Orders
description: One row per completed customer order across all channels.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders, revenue]
status: stable
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-05-28T14:30:00Z }
verified:
  - { by: human:data-steward, at: 2026-05-30T10:00:00Z }
  - { by: process:schema-validator, at: 2026-06-01T02:00:00Z }
sources:
  - id: bq-schema
    resource: https://cloud.google.com/bigquery/docs/schemas
    title: BigQuery schema documentation
    author: team:google-cloud-docs
  - id: internal-erd
    resource: /references/sales-erd.md
    title: Sales domain ERD
    author: human:data-architect
    last_modified: 2026-04-15T00:00:00Z
---

# Schema

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | STRING | Globally unique order identifier |
| `customer_id` | STRING | FK to [customers](./customers.md) |
| `total_usd` | NUMERIC | Order total in US dollars |
| `placed_at` | TIMESTAMP | When the customer submitted the order |
| `channel` | STRING | Acquisition channel (web, mobile, pos) |

# Joins

- Join with [customers](./customers.md) on `customer_id`
- Referenced by [gross revenue](/metrics/gross-revenue.md) metric

# Data Quality

- Validated nightly by `process:schema-validator`
- `order_id` uniqueness enforced at ingestion

[^bq-schema]: BigQuery schema documentation
```

### tables/customers.md

```markdown
---
type: BigQuery Table
title: Customers
description: One row per registered customer with profile and lifetime data.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=customers
tags: [sales, customers, pii]
status: stable
generated: { by: human:data-engineer, at: 2026-05-28T14:30:00Z }
verified: { by: human:data-steward, at: 2026-05-30T10:00:00Z }
sources:
  - id: internal-erd
    resource: /references/sales-erd.md
    title: Sales domain ERD
---

# Schema

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | STRING | Primary key |
| `email` | STRING | Customer email (hashed in prod) |
| `created_at` | TIMESTAMP | Registration date |
| `ltv_usd` | NUMERIC | Lifetime value in USD |

# Joins

- Referenced by [orders](./orders.md) on `customer_id`

# Privacy Note

PII fields are hashed in production. See [internal ERD](/references/sales-erd.md) 
for the full privacy classification.[^internal-erd]

[^internal-erd]: Sales domain ERD
```

### metrics/gross-revenue.md

```markdown
---
type: Metric
title: Gross Revenue
description: Total revenue before refunds and discounts.
tags: [revenue, finance, kpi]
status: stable
generated: { by: human:analyst, at: 2026-05-28T14:30:00Z }
verified: { by: human:finance-lead, at: 2026-06-01T09:00:00Z }
stale_after: 2026-12-31T00:00:00Z
sources:
  - id: gaap-rev
    resource: https://www.fasb.org/revenue-recognition
    title: GAAP Revenue Recognition Standard
    author: org:fasb
---

# Definition

Sum of `total_usd` from [orders](/tables/orders.md) for a given period.[^gaap-rev]
Does not subtract refunds — see Net Revenue for that.

# SQL

```sql
SELECT DATE_TRUNC(placed_at, MONTH) as month,
       SUM(total_usd) as gross_revenue
FROM `acme.sales.orders`
GROUP BY 1
```

# Related

- Source table: [orders](/tables/orders.md)
- Counterpart: Net Revenue (gross minus refunds)

[^gaap-rev]: GAAP Revenue Recognition Standard
```

---

## 3. SaaS Incident Playbooks (v0.2)

```
incidents/
├── index.md
├── alerts/
│   ├── index.md
│   ├── api-latency-p99.md
│   └── db-connections.md
└── runbooks/
    ├── index.md
    └── escalate-incident.md
```

### alerts/api-latency-p99.md

```markdown
---
type: Alert
title: API Latency P99 > 2s
description: Fires when 99th percentile API latency exceeds 2 seconds for 5 minutes.
tags: [api, latency, critical]
status: stable
generated: { by: human:sre-lead, at: 2026-06-01T09:00:00Z }
verified: { by: human:oncall-rotation, at: 2026-06-15T14:00:00Z }
stale_after: 2026-09-01T00:00:00Z
sources:
  - id: sla-doc
    resource: https://wiki.internal/sla/api-latency
    title: API Latency SLA Definition
    author: team:platform-eng
    last_modified: 2026-03-01T00:00:00Z
---

# Trigger Condition

```promql
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 2
```

# Impact

Users experience timeouts. Downstream services may cascade-fail.

# Response

1. Check [DB connections alert](./db-connections.md) — often the root cause
2. Follow [escalation runbook](/runbooks/escalate-incident.md) if not resolved in 10 min
3. Check deployment log for recent changes

# SLA Context

Per the SLA definition,[^sla-doc] P99 latency must stay under 2s during 
business hours. Violations trigger PagerDuty.

[^sla-doc]: API Latency SLA Definition
```

### runbooks/escalate-incident.md

```markdown
---
type: Runbook
title: Escalate Incident
description: Steps to escalate when on-call cannot resolve within SLA.
tags: [oncall, incident, escalation]
status: stable
generated: { by: human:sre-manager, at: 2026-06-01T09:00:00Z }
verified:
  - { by: human:oncall-rotation, at: 2026-06-10T14:00:00Z }
  - { by: process:runbook-tester, at: 2026-06-12T02:00:00Z }
sources:
  - id: incident-policy
    resource: https://wiki.internal/incident-management-policy
    title: Incident Management Policy
    author: team:engineering-leadership
---

# When to Escalate

Per the incident management policy:[^incident-policy]

- Alert not resolved within 10 minutes
- Customer-facing impact confirmed
- Multiple alerts firing simultaneously

# Steps

1. Post in #incidents Slack channel with alert link
2. Page the secondary on-call (PagerDuty)
3. If P1: page Engineering Manager
4. Start incident document from template
5. Update status page if customer-facing

# Contacts

| Role | Who | Method |
|------|-----|--------|
| Secondary on-call | Rotation | PagerDuty |
| Eng Manager | @manager | Slack DM |
| Infra lead | @infra-lead | Slack DM |

[^incident-policy]: Incident Management Policy
```

---

## 4. API Documentation (v0.2)

```
api/
├── index.md
├── auth/
│   ├── index.md
│   └── oauth2-flow.md
├── endpoints/
│   ├── index.md
│   └── create-order.md
└── policies/
    ├── index.md
    └── rate-limits.md
```

### endpoints/create-order.md

```markdown
---
type: API Endpoint
title: Create Order
description: Creates a new order for an authenticated customer.
resource: https://api.acme.com/v2/orders
tags: [orders, write, v2]
status: stable
generated: { by: openapi-importer/1.0, at: 2026-05-20T10:00:00Z }
verified: { by: human:api-owner, at: 2026-05-25T14:00:00Z }
stale_after: 2026-11-20T00:00:00Z
sources:
  - id: openapi-spec
    resource: /references/openapi.yaml
    title: OpenAPI Specification v2
    author: team:api-platform
    last_modified: 2026-05-18T00:00:00Z
---

# POST /v2/orders

Creates a new order. Requires [OAuth2 authentication](/auth/oauth2-flow.md).

# Request

```json
{
  "customer_id": "cust_abc123",
  "items": [{"sku": "WIDGET-01", "quantity": 2}],
  "idempotency_key": "unique-request-id"
}
```

# Response (201 Created)

```json
{
  "order_id": "ord_xyz789",
  "status": "pending",
  "total_usd": 49.98,
  "created_at": "2026-05-20T10:30:00Z"
}
```

# Errors

| Code | Meaning |
|------|---------|
| 400 | Invalid request body |
| 401 | Missing or invalid auth token |
| 409 | Duplicate idempotency_key |
| 429 | [Rate limit](/policies/rate-limits.md) exceeded |

# Rate Limits

Subject to [rate limiting](/policies/rate-limits.md). See `X-RateLimit-*` headers.

[^openapi-spec]: OpenAPI Specification v2
```

### policies/rate-limits.md

```markdown
---
type: Policy
title: Rate Limits
description: Per-plan rate limits for all API endpoints.
tags: [policy, rate-limit, api]
status: stable
generated: { by: human:api-product-manager, at: 2026-05-20T10:00:00Z }
verified: { by: human:engineering-lead, at: 2026-05-22T16:00:00Z }
sources:
  - id: pricing-page
    resource: https://acme.com/pricing
    title: Pricing Page
    author: team:marketing
    usage_count: 50000
    last_modified: 2026-04-01T00:00:00Z
usage_window: { from: 2026-05-01T00:00:00Z, to: 2026-05-31T00:00:00Z }
---

# Limits by Plan

| Plan | Requests/min | Burst |
|------|-------------|-------|
| Free | 60 | 10 |
| Pro | 600 | 100 |
| Enterprise | 6000 | 1000 |

Plan limits are defined on our [pricing page].[^pricing-page]

# Response Headers

Every response includes:
- `X-RateLimit-Limit`: max requests per window
- `X-RateLimit-Remaining`: requests left in window
- `X-RateLimit-Reset`: Unix timestamp of window reset

# When Exceeded

Returns `429 Too Many Requests`. Retry after `X-RateLimit-Reset`.
Applies to all endpoints including [create order](/endpoints/create-order.md).

[^pricing-page]: Pricing Page
```

---

## 5. Minimal Bundle (v0.2 Conformant)

The absolute minimum for conformance — just `type` is required:

```
minimal/
└── concept.md
```

### concept.md

```markdown
---
type: Note
---

This is a minimal conformant OKF v0.2 document.
```

---

## Trust Tier Examples

### Unverified (no `verified` key)

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T10:00:00Z }
# No verified key = unverified
```

### Machine-confirmed (non-human verifier)

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T10:00:00Z }
verified: { by: process:schema-validator, at: 2026-06-21T02:00:00Z }
```

### Human-reviewed (human verifier)

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T10:00:00Z }
verified:
  - { by: process:schema-validator, at: 2026-06-21T02:00:00Z }
  - { by: human:domain-expert, at: 2026-06-22T14:00:00Z }
```

---

## Lifecycle Examples

### Draft concept

```yaml
status: draft
generated: { by: human:author, at: 2026-06-20T10:00:00Z }
# No verified, no stale_after — work in progress
```

### Stable with expiration

```yaml
status: stable
generated: { by: human:author, at: 2026-06-20T10:00:00Z }
verified: { by: human:reviewer, at: 2026-06-25T14:00:00Z }
stale_after: 2026-12-31T00:00:00Z
```

### Deprecated

```yaml
status: deprecated
generated: { by: human:author, at: 2026-01-15T10:00:00Z }
# Kept for links and history, no longer current
```
