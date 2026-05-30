---
title: "Monitoring and uptime"
category: resilience
status: recommended
updated: "2026-05-29T09:13:20.000Z"
sources:
  - title: "Google SRE Book — Monitoring Distributed Systems"
    url: "https://sre.google/sre-book/monitoring-distributed-systems/"
    publisher: "Google SRE"
  - title: "web.dev — User-centric performance metrics"
    url: "https://web.dev/articles/user-centric-performance-metrics"
    publisher: "web.dev"
  - title: "Google SRE Workbook — SLO engineering case studies"
    url: "https://sre.google/workbook/implementing-slos/"
    publisher: "Google SRE"
licence: CC-BY-4.0
---

# Monitoring and uptime

> Monitor the site from outside your own infrastructure, combine synthetic checks with real user data, and run a status page on a separate host so it stays up when the site does not.

## What it is

Monitoring is the continuous check that the site is reachable, correct, and fast. Uptime is the headline number — the percentage of time the site responded successfully over a window. Together they answer two questions: is the site up right now, and how often has it been down this month?

Three layers cover most needs:

1. **Synthetic monitoring** — a script in another data centre requests the site on a schedule and alerts when the response is wrong.
2. **Real User Monitoring (RUM)** — JavaScript on the page reports real visitor experience: load times, errors, Core Web Vitals.
3. **A public status page** — a page on a separate host where users can check whether the issue is yours or theirs.

## Why it matters

Internal dashboards go down with the application. A check that runs inside the same VPC as the database cannot tell you the DNS provider has failed, the TLS certificate has expired, or the CDN is serving stale content. External monitoring catches the failures your users see first.

Synthetic checks tell you whether the site works. RUM tells you whether it works **for the people who use it** — on real devices, on real networks, in the regions you actually serve. The two are complementary: synthetic is fast feedback in a controlled environment, RUM is ground truth.

A status page reduces support load during incidents. When the homepage is down, "is it just me?" is the first question every user asks. A status page on a separate domain answers it without a support ticket.

## How to implement

For synthetic monitoring, pick one external service and run checks every minute from multiple regions:

- **Hosted**: UptimeRobot, Pingdom, StatusCake, Better Stack, Checkly, Datadog Synthetics.
- **Self-hosted**: Uptime Kuma, Healthchecks.io.

Check more than the homepage. A login flow, a search endpoint, and a checkout step catch problems the home page does not. Validate the response body, not just the status code, so a `200 OK` returning the maintenance page still trips an alert.

For RUM, send Core Web Vitals (LCP, INP, CLS) and JavaScript errors to a collector. The `web-vitals` library, Sentry, Datadog RUM, and Cloudflare Web Analytics all do this in a few kilobytes.

Run the status page on a different host and a different DNS provider from the main site. Common pattern: `status.example.com` resolved through a CDN-fronted static site, with the status records stored at a third-party provider (Statuspage, Instatus, BetterStack, or a static site you update manually). The point is that when the primary site is unreachable, the status page must not be unreachable too.

## Common mistakes

- A monitor that hits the homepage from one region every five minutes and reports 100% uptime while half the world cannot reach the site.
- Checking only the status code, so a 200 OK returning an error page passes.
- Status page on the same domain as the site. When the site is down, so is the status page.
- Alerting on every blip. Pages every five minutes train operators to ignore the alert.
- No on-call rota, so alerts go to an inbox no one reads at 3am.

## Verification

- Trigger a controlled outage in staging. Confirm the monitor alerts within the expected window.
- Check that the status page resolves when the main site's CDN is blocked at the network level.
- Review the past month's incidents and confirm RUM data and synthetic checks agree on when the site was degraded.
