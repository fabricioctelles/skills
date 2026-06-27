# Skill Categories Reference

Sources:
- [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) — Anthropic, Jun 2026
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices) — Agent Skills spec
- [Extend Claude with skills](https://code.claude.com/docs/en/skills) — Claude Code docs

---

## 1. `library-and-api-reference`

Skills that explain how to correctly use a library, CLI, or SDK. Can be internal or public libraries that the model struggles with. Often include reference code snippets and gotchas lists.

**Signals:** Has API endpoint docs, CLI command reference, code examples, "how to call X" patterns.

**Examples:** billing-lib, internal-platform-cli, sandbox-proxy

---

## 2. `product-verification`

Skills that describe how to test or verify code is working. Often paired with Playwright, tmux, or other external tools. These have the most measurable impact on output quality — worth investing an engineer-week.

**Signals:** Has test scripts, assertion patterns, Playwright/Cypress flows, "verify that X" instructions.

**Examples:** signup-flow-driver, checkout-verifier, tmux-cli-driver

---

## 3. `data-fetching-and-analysis`

Skills that connect to data and monitoring stacks. Include libraries to fetch data with credentials, dashboard IDs, common query patterns.

**Signals:** Has database queries, dashboard references, metric/event schemas, "how to find X in our data" patterns.

**Examples:** funnel-query, cohort-compare, grafana, datadog

---

## 4. `business-process-automation`

Skills that automate repetitive workflows into one command. Usually simple instructions but may depend on other skills or MCPs. Saving results in log files helps consistency.

**Signals:** Has "do this weekly/daily" patterns, aggregates from multiple sources, posts to Slack/channels, formats structured output.

**Examples:** standup-post, create-ticket, weekly-recap

---

## 5. `code-scaffolding-and-templates`

Skills that generate framework boilerplates for a specific function. May combine with composable scripts. Especially useful when scaffolding has natural-language requirements beyond pure code.

**Signals:** Has templates, "new X" generators, boilerplate structures, asset files to copy.

**Examples:** new-workflow, new-migration, create-app

---

## 6. `code-quality-and-review`

Skills that enforce code quality and help review code. Can include deterministic scripts for robustness. May run as hooks or in GitHub Actions.

**Signals:** Has style rules, review checklists, linting patterns, "reject if X" logic, adversarial review patterns.

**Examples:** adversarial-review, code-style, testing-practices

---

## 7. `ci-cd-and-deployment`

Skills that help fetch, push, and deploy code. May reference other skills to collect data.

**Signals:** Has deploy commands, build pipelines, PR management, rollout/rollback logic, environment configs.

**Examples:** babysit-pr, deploy-service, cherry-pick-prod

---

## 8. `runbooks`

Skills that take a symptom (alert, error, Slack thread) and walk through multi-tool investigation producing a structured report.

**Signals:** Has symptom→tool→diagnosis flows, "if you see X check Y" decision trees, report templates.

**Examples:** service-debugging, oncall-runner, log-correlator

---

## 9. `infrastructure-operations`

Skills that perform routine maintenance and ops, some involving destructive actions with guardrails. Make it easier to follow best practices in critical operations.

**Signals:** Has cleanup/orphan detection, cost investigation, dependency approval, confirmation gates for destructive actions.

**Examples:** resource-orphans, dependency-management, cost-investigation

---

## Classification Decision Tree

1. Does it primarily teach how to **call an API/CLI/SDK**? → `library-and-api-reference`
2. Does it **verify** that something works (test, assert, validate)? → `product-verification`
3. Does it **query data** from monitoring/analytics/databases? → `data-fetching-and-analysis`
4. Does it **automate a repeating team process** (standup, report, ticket)? → `business-process-automation`
5. Does it **generate new code/files** from templates? → `code-scaffolding-and-templates`
6. Does it **review/lint/enforce quality** on existing code? → `code-quality-and-review`
7. Does it **build/deploy/ship** code to environments? → `ci-cd-and-deployment`
8. Does it **diagnose problems** from symptoms to structured findings? → `runbooks`
9. Does it perform **infrastructure maintenance/cleanup** with guardrails? → `infrastructure-operations`

If a skill spans multiple categories, pick the one that describes its **primary action** — what the user gets when they invoke it.
