# ============================================================
#  main.py — Email Marketing Automation
#  Author  : Sandeep Kumar
#  Program : M.Tech – Computer Science & Engineering
#  Project : Minor Project – Email Marketing Automation
# ============================================================

from src.mailchimp_client import get_subscribers
from src.segmentation     import segment_subscribers, print_segment_summary
from src.workflows        import (
    welcome_series,
    abandoned_cart_recovery,
    post_purchase_followup,
    reengagement_campaign,
    vip_loyalty_program
)
from src.analytics import fetch_all_reports, save_report_json


def run():
    print("\n" + "=" * 50)
    print("   EMAIL MARKETING AUTOMATION SYSTEM")
    print("   Author : Sandeep Kumar | M.Tech CSE")
    print("=" * 50)

    # Step 1: Fetch subscribers
    print("\n[STEP 1] Fetching subscribers...")
    subscribers = get_subscribers()

    # Step 2: Segment subscribers
    print("\n[STEP 2] Segmenting subscribers...")
    segments = segment_subscribers(subscribers)
    print_segment_summary(segments)

    # Step 3: Run automation workflows
    print("\n[STEP 3] Running automation workflows...")

    welcome_series(segments["new_subscribers"])
    abandoned_cart_recovery(segments["cart_abandoners"])
    post_purchase_followup(segments["active_buyers"])
    reengagement_campaign(segments["inactive_users"])
    vip_loyalty_program(segments["vip_customers"])

    # Step 4: Fetch & save analytics
    print("\n[STEP 4] Fetching campaign analytics...")
    reports = fetch_all_reports()
    save_report_json(reports)

    print("\n✅ All workflows completed successfully!")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    run()
