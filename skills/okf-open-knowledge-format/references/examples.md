# OKF Bundle Examples

Three complete, conformant bundles across different domains.

---

## 1. E-commerce Analytics

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
timestamp: 2026-05-28T14:30:00Z
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

# Citations

[1] [BigQuery schema docs](https://cloud.google.com/bigquery/docs/schemas)
```

### tables/customers.md

```markdown
---
type: BigQuery Table
title: Customers
description: One row per registered customer with profile and lifetime data.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=customers
tags: [sales, customers]
timestamp: 2026-05-28T14:30:00Z
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
```

### metrics/gross-revenue.md

```markdown
---
type: Metric
title: Gross Revenue
description: Total revenue before refunds and discounts.
tags: [revenue, finance, kpi]
timestamp: 2026-05-28T14:30:00Z
---

# Definition

Sum of `total_usd` from [orders](/tables/orders.md) for a given period.
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
```

### index.md (root)

```markdown
# E-commerce Analytics Bundle

- [Tables](./tables/) - Database tables powering the analytics stack
- [Metrics](./metrics/) - Business KPIs derived from tables
```

---

## 2. SaaS Incident Playbooks

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
severity: critical
timestamp: 2026-06-01T09:00:00Z
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

# Citations

[1] [SLA definition](https://wiki.internal/sla/api-latency)
```

### runbooks/escalate-incident.md

```markdown
---
type: Runbook
title: Escalate Incident
description: Steps to escalate when on-call cannot resolve within SLA.
tags: [oncall, incident, escalation]
timestamp: 2026-06-01T09:00:00Z
---

# When to Escalate

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
```

---

## 3. API Documentation

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
method: POST
timestamp: 2026-05-20T10:00:00Z
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
```

### policies/rate-limits.md

```markdown
---
type: Policy
title: Rate Limits
description: Per-plan rate limits for all API endpoints.
tags: [policy, rate-limit, api]
timestamp: 2026-05-20T10:00:00Z
---

# Limits by Plan

| Plan | Requests/min | Burst |
|------|-------------|-------|
| Free | 60 | 10 |
| Pro | 600 | 100 |
| Enterprise | 6000 | 1000 |

# Response Headers

Every response includes:
- `X-RateLimit-Limit`: max requests per window
- `X-RateLimit-Remaining`: requests left in window
- `X-RateLimit-Reset`: Unix timestamp of window reset

# When Exceeded

Returns `429 Too Many Requests`. Retry after `X-RateLimit-Reset`.
Applies to all endpoints including [create order](/endpoints/create-order.md).
```
