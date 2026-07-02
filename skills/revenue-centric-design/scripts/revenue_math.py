#!/usr/bin/env python3
"""Revenue math from the RCD principles — run these instead of estimating.

  sample-size   minimum per-variant n for an A/B test (don't start a test you can't finish)
  churn-ltv     churn -> LTV, plus the cash impact of cutting churn N points
  cac           CAC per *closed deal*, not per lead

Examples:
  revenue_math.py sample-size --baseline 0.03 --mde 0.20
  revenue_math.py churn-ltv --arpu 120 --churn 0.25 --new-churn 0.20 --users 1000
  revenue_math.py cac --spend 50000 --leads 500 --closes 10
"""
import argparse
import math
import sys

# two-sided z for common alphas / one-sided z for power
Z = {0.80: 0.8416, 0.90: 1.2816, 0.95: 1.6449, 0.975: 1.9600, 0.995: 2.5758}


def z_for(p: float) -> float:
    if p in Z:
        return Z[p]
    # Acklam-style rational approximation, good to ~1e-4 for 0.5 < p < 1
    t = math.sqrt(-2.0 * math.log(1.0 - p))
    return t - (2.30753 + 0.27061 * t) / (1.0 + 0.99229 * t + 0.04481 * t * t)


def sample_size(baseline: float, mde_rel: float, alpha: float, power: float) -> int:
    """Per-variant n for detecting a relative lift `mde_rel` over `baseline` (two-sided)."""
    p1 = baseline
    p2 = baseline * (1.0 + mde_rel)
    if not (0 < p1 < 1 and 0 < p2 < 1):
        sys.exit("baseline and baseline*(1+mde) must be within (0, 1)")
    za = z_for(1.0 - alpha / 2.0)
    zb = z_for(power)
    pbar = (p1 + p2) / 2.0
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def cmd_sample_size(a):
    n = sample_size(a.baseline, a.mde, a.alpha, a.power)
    print(f"per-variant sample size: {n:,}  (total for A/B: {2 * n:,})")
    print(f"detects {a.baseline:.2%} -> {a.baseline * (1 + a.mde):.2%} "
          f"(relative +{a.mde:.0%}) at alpha={a.alpha}, power={a.power}")
    if a.traffic:
        weeks = 2 * n / (a.traffic / 4.345)  # weekly visitors from monthly
        print(f"at {a.traffic:,.0f} visitors/month: ~{weeks:.1f} weeks to conclude")
        if weeks > 8:
            print("verdict: underpowered in reasonable time — decide by qualitative "
                  "research instead (five good interviews beat this test)")


def cmd_churn_ltv(a):
    if not 0 < a.churn < 1:
        sys.exit("churn must be a fraction, e.g. 0.25 for 25%/month")
    ltv = a.arpu / a.churn
    print(f"LTV at {a.churn:.1%} monthly churn: {ltv:,.2f}  (avg lifetime {1 / a.churn:.1f} months)")
    if a.users:
        replace = a.users * a.churn
        print(f"treadmill: {replace:,.0f} new users/month just to stay flat at {a.users:,} users")
    if a.new_churn:
        new_ltv = a.arpu / a.new_churn
        print(f"LTV at {a.new_churn:.1%}: {new_ltv:,.2f}  (delta per user: {new_ltv - ltv:+,.2f})")
        if a.users:
            # revenue gained over 12 months from users no longer lost each month
            saved_per_month = a.users * (a.churn - a.new_churn)
            annual = sum(saved_per_month * a.arpu * (12 - m) for m in range(12)) / 12
            print(f"~{annual:,.0f}/year in retained revenue at {a.users:,} users, "
                  f"ARPU {a.arpu:,.0f} — no price change, no extra acquisition")


def cmd_cac(a):
    cpl = a.spend / a.leads
    closes = a.closes if a.closes else a.leads * a.close_rate
    if closes <= 0:
        sys.exit("need --closes or a positive --close-rate")
    print(f"cost per lead: {cpl:,.2f}")
    print(f"CAC per closed deal: {a.spend / closes:,.2f}  ({closes:.0f} closes from {a.leads:,} leads)")
    print("lever: filter on the landing page (specific copy, visible pricing, qualification "
          "question) — fewer, better leads lowers this number at the same spend")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sample-size", help="minimum per-variant n for an A/B test")
    s.add_argument("--baseline", type=float, required=True, help="current conversion rate, e.g. 0.03")
    s.add_argument("--mde", type=float, required=True, help="relative lift to detect, e.g. 0.20 for +20%%")
    s.add_argument("--alpha", type=float, default=0.05)
    s.add_argument("--power", type=float, default=0.80)
    s.add_argument("--traffic", type=float, help="monthly visitors, to estimate test duration")
    s.set_defaults(fn=cmd_sample_size)

    c = sub.add_parser("churn-ltv", help="churn -> LTV and the cash value of cutting churn")
    c.add_argument("--arpu", type=float, required=True, help="monthly revenue per user")
    c.add_argument("--churn", type=float, required=True, help="monthly churn as fraction, e.g. 0.25")
    c.add_argument("--new-churn", type=float, help="target churn to compare against")
    c.add_argument("--users", type=int, help="current paying users, for cash impact")
    c.set_defaults(fn=cmd_churn_ltv)

    k = sub.add_parser("cac", help="CAC per closed deal, not per lead")
    k.add_argument("--spend", type=float, required=True)
    k.add_argument("--leads", type=float, required=True)
    k.add_argument("--closes", type=float, help="deals actually closed")
    k.add_argument("--close-rate", type=float, help="fraction of leads that close, e.g. 0.02")
    k.set_defaults(fn=cmd_cac)

    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
