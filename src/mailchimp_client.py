# ============================================================
#  mailchimp_client.py — Mailchimp API Integration
#  Author: Sandeep Kumar | M.Tech CSE
# ============================================================

import requests
import json
from config import MAILCHIMP_API_KEY, MAILCHIMP_SERVER, MAILCHIMP_LIST_ID, DEMO_MODE

BASE_URL = f"https://{MAILCHIMP_SERVER}.api.mailchimp.com/3.0"
HEADERS  = {
    "Authorization": f"apikey {MAILCHIMP_API_KEY}",
    "Content-Type": "application/json"
}

# ── Demo subscribers used when DEMO_MODE = True ─────────────
DEMO_SUBSCRIBERS = [
    {"email": "alice@example.com",   "fname": "Alice",   "status": "subscribed", "purchases": 5,  "cart": True,  "days_inactive": 10},
    {"email": "bob@example.com",     "fname": "Bob",     "status": "subscribed", "purchases": 0,  "cart": False, "days_inactive": 5},
    {"email": "charlie@example.com", "fname": "Charlie", "status": "subscribed", "purchases": 1,  "cart": True,  "days_inactive": 70},
    {"email": "diana@example.com",   "fname": "Diana",   "status": "subscribed", "purchases": 3,  "cart": False, "days_inactive": 2},
    {"email": "ethan@example.com",   "fname": "Ethan",   "status": "subscribed", "purchases": 0,  "cart": False, "days_inactive": 65},
]


def get_subscribers():
    """Fetch all subscribers from Mailchimp audience (or demo data)."""
    if DEMO_MODE:
        print("[DEMO] Loaded demo subscribers.")
        return DEMO_SUBSCRIBERS

    url      = f"{BASE_URL}/lists/{MAILCHIMP_LIST_ID}/members"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        members = response.json().get("members", [])
        print(f"[API] Fetched {len(members)} subscribers.")
        return members
    else:
        print(f"[ERROR] Failed to fetch subscribers: {response.text}")
        return []


def add_subscriber(email, first_name, last_name=""):
    """Add a new subscriber to the Mailchimp audience."""
    if DEMO_MODE:
        print(f"[DEMO] Would add subscriber: {email}")
        return {"status": "subscribed", "email_address": email}

    url     = f"{BASE_URL}/lists/{MAILCHIMP_LIST_ID}/members"
    payload = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {"FNAME": first_name, "LNAME": last_name}
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))

    if response.status_code == 200:
        print(f"[API] Subscriber added: {email}")
    else:
        print(f"[ERROR] Could not add subscriber: {response.text}")

    return response.json()


def get_campaign_report(campaign_id):
    """Fetch open rate, click rate, conversions for a campaign."""
    if DEMO_MODE:
        print(f"[DEMO] Returning mock report for campaign: {campaign_id}")
        return {
            "campaign_id":  campaign_id,
            "emails_sent":  120,
            "open_rate":    0.68,
            "click_rate":   0.32,
            "bounce_rate":  0.02,
            "unsubscribes": 1
        }

    url      = f"{BASE_URL}/reports/{campaign_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return {
            "campaign_id":  campaign_id,
            "emails_sent":  data.get("emails_sent", 0),
            "open_rate":    data.get("open_rate", 0),
            "click_rate":   data.get("click_rate", 0),
            "bounce_rate":  data.get("bounces", {}).get("hard_bounces", 0),
            "unsubscribes": data.get("unsubscribes", 0)
        }
    else:
        print(f"[ERROR] Failed to fetch report: {response.text}")
        return {}


def get_all_campaigns():
    """List all campaigns in the Mailchimp account."""
    if DEMO_MODE:
        print("[DEMO] Returning mock campaign list.")
        return [
            {"id": "camp_001", "settings": {"subject_line": "Welcome! Here's 10% off"}, "status": "sent"},
            {"id": "camp_002", "settings": {"subject_line": "You left something behind..."}, "status": "sent"},
            {"id": "camp_003", "settings": {"subject_line": "We miss you!"}, "status": "sent"},
        ]

    url      = f"{BASE_URL}/campaigns"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json().get("campaigns", [])
    else:
        print(f"[ERROR] {response.text}")
        return []
