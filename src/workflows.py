# ============================================================
#  workflows.py — Email Automation Workflow Engine
#  Author: Sandeep Kumar | M.Tech CSE
# ============================================================

from config import WELCOME_EMAIL_DELAYS, CART_EMAIL_DELAYS, POSTPURCHASE_DELAYS, REENGAGEMENT_DELAYS


def send_email(to_email, fname, subject, body):
    """Simulate sending an email (prints to console in demo mode)."""
    print(f"\n  📧 TO      : {to_email}")
    print(f"     NAME    : {fname}")
    print(f"     SUBJECT : {subject}")
    print(f"     BODY    : {body[:80]}...")
    print(f"     STATUS  : ✅ Sent (Demo)")


# ── Workflow 1: Welcome Series ───────────────────────────────
def welcome_series(subscribers):
    print("\n" + "=" * 50)
    print("   WORKFLOW 1 — WELCOME SERIES")
    print("=" * 50)

    emails = [
        {
            "delay":   WELCOME_EMAIL_DELAYS[0],
            "subject": "Welcome! Here's 10% off your first order 🎉",
            "body":    "Hi {fname}, welcome aboard! We're so glad you joined us. Use code WELCOME10 for 10% off your first order. Shop now and explore our latest collection!"
        },
        {
            "delay":   WELCOME_EMAIL_DELAYS[1],
            "subject": "Our story — why we started this brand",
            "body":    "Hi {fname}, we started this brand with a simple belief: quality shouldn't be expensive. Here's a little about who we are and what we stand for..."
        },
        {
            "delay":   WELCOME_EMAIL_DELAYS[2],
            "subject": "Our bestsellers — picked just for you ⭐",
            "body":    "Hi {fname}, here are the products our customers love most. These are our top picks this season — don't miss out!"
        },
    ]

    for subscriber in subscribers:
        email = subscriber.get("email")
        fname = subscriber.get("fname", "there")
        for i, em in enumerate(emails):
            send_email(
                email, fname,
                em["subject"],
                em["body"].replace("{fname}", fname)
            )
            print(f"     DELAY   : Send after {em['delay']} hours")


# ── Workflow 2: Abandoned Cart Recovery ─────────────────────
def abandoned_cart_recovery(subscribers):
    print("\n" + "=" * 50)
    print("   WORKFLOW 2 — ABANDONED CART RECOVERY")
    print("=" * 50)

    emails = [
        {
            "delay":   CART_EMAIL_DELAYS[0],
            "subject": "Hey, you left something behind! 🛒",
            "body":    "Hi {fname}, looks like you left some items in your cart. Don't worry — they're still waiting for you. Complete your order before they sell out!"
        },
        {
            "delay":   CART_EMAIL_DELAYS[1],
            "subject": "Your cart is about to expire ⏳",
            "body":    "Hi {fname}, your cart is almost gone! Items in your cart are in high demand. Grab them before someone else does."
        },
        {
            "delay":   CART_EMAIL_DELAYS[2],
            "subject": "Last chance — 10% off your cart today only! 🔥",
            "body":    "Hi {fname}, this is your final reminder. We're giving you an exclusive 10% discount to complete your order. Use code CART10 at checkout. Expires in 24 hours!"
        },
    ]

    for subscriber in subscribers:
        email = subscriber.get("email")
        fname = subscriber.get("fname", "there")
        for em in emails:
            send_email(
                email, fname,
                em["subject"],
                em["body"].replace("{fname}", fname)
            )
            print(f"     DELAY   : Send after {em['delay']} hours")


# ── Workflow 3: Post-Purchase Follow Up ─────────────────────
def post_purchase_followup(subscribers):
    print("\n" + "=" * 50)
    print("   WORKFLOW 3 — POST-PURCHASE FOLLOW UP")
    print("=" * 50)

    emails = [
        {
            "delay":   POSTPURCHASE_DELAYS[0],
            "subject": "Order Confirmed! Here's your summary 📦",
            "body":    "Hi {fname}, thank you for your order! Your items are being packed and will be with you soon. Estimated delivery: 3–5 business days."
        },
        {
            "delay":   POSTPURCHASE_DELAYS[1],
            "subject": "How are you liking your order? ⭐",
            "body":    "Hi {fname}, we hope your order arrived safely! We'd love to know what you think. Leave a quick review — it helps us improve and helps other shoppers too!"
        },
        {
            "delay":   POSTPURCHASE_DELAYS[2],
            "subject": "Customers who bought this also loved... 🛍️",
            "body":    "Hi {fname}, based on your recent purchase, we thought you might love these too. Here are some hand-picked recommendations just for you!"
        },
    ]

    for subscriber in subscribers:
        email = subscriber.get("email")
        fname = subscriber.get("fname", "there")
        for em in emails:
            send_email(
                email, fname,
                em["subject"],
                em["body"].replace("{fname}", fname)
            )
            print(f"     DELAY   : Send after {em['delay']} hours")


# ── Workflow 4: Re-engagement Campaign ──────────────────────
def reengagement_campaign(subscribers):
    print("\n" + "=" * 50)
    print("   WORKFLOW 4 — RE-ENGAGEMENT CAMPAIGN")
    print("=" * 50)

    emails = [
        {
            "delay":   REENGAGEMENT_DELAYS[0],
            "subject": "We miss you, {fname}! Here's a special offer 💌",
            "body":    "Hi {fname}, it's been a while! We've added so many new things since you last visited. Come back and explore — here's 15% off as a welcome back gift. Code: MISSYOU15"
        },
        {
            "delay":   REENGAGEMENT_DELAYS[1],
            "subject": "Should we say goodbye? 👋",
            "body":    "Hi {fname}, we noticed you haven't been around lately. We don't want to clutter your inbox — if you'd like to stay subscribed, just click the button below. Otherwise, no hard feelings!"
        },
    ]

    for subscriber in subscribers:
        email = subscriber.get("email")
        fname = subscriber.get("fname", "there")
        for em in emails:
            send_email(
                email, fname,
                em["subject"].replace("{fname}", fname),
                em["body"].replace("{fname}", fname)
            )
            print(f"     DELAY   : Send after {em['delay']} hours")


# ── Workflow 5: VIP Loyalty Program ─────────────────────────
def vip_loyalty_program(subscribers):
    print("\n" + "=" * 50)
    print("   WORKFLOW 5 — VIP LOYALTY PROGRAM")
    print("=" * 50)

    for subscriber in subscribers:
        email = subscriber.get("email")
        fname = subscriber.get("fname", "there")
        send_email(
            email, fname,
            subject=f"You're a VIP, {fname}! Early access to new arrivals 👑",
            body=f"Hi {fname}, as one of our most valued customers, you get FIRST access to our new collection before anyone else. Plus, here's an exclusive discount code just for you: VIP20"
        )
