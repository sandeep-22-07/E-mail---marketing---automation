# ============================================================
#  analytics.py — Campaign Performance Tracker
#  Author: Sandeep Kumar | M.Tech CSE
# ============================================================

import json
import os
from datetime import datetime
from src.mailchimp_client import get_all_campaigns, get_campaign_report

OUTPUT_DIR = "output"


def fetch_all_reports():
    """Fetch performance report for all campaigns."""
    campaigns = get_all_campaigns()
    reports   = []

    print("\n" + "=" * 60)
    print("   CAMPAIGN PERFORMANCE REPORT")
    print(f"   Generated: {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
    print("=" * 60)
    print(f"  {'Campaign':<30} {'Open%':>7} {'Click%':>8} {'Sent':>6}")
    print("-" * 60)

    for campaign in campaigns:
        campaign_id = campaign.get("id")
        subject     = campaign.get("settings", {}).get("subject_line", "N/A")
        report      = get_campaign_report(campaign_id)

        open_rate  = round(report.get("open_rate", 0) * 100, 1)
        click_rate = round(report.get("click_rate", 0) * 100, 1)
        sent       = report.get("emails_sent", 0)

        print(f"  {subject[:30]:<30} {open_rate:>6}% {click_rate:>7}% {sent:>6}")

        reports.append({
            "campaign_id": campaign_id,
            "subject":     subject,
            "emails_sent": sent,
            "open_rate":   f"{open_rate}%",
            "click_rate":  f"{click_rate}%",
        })

    print("=" * 60)
    return reports


def save_report_json(reports):
    """Save report to output/report.json."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "campaign_report.json")

    with open(path, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "campaigns":    reports
        }, f, indent=2)

    print(f"\n  ✅ Report saved to {path}")
