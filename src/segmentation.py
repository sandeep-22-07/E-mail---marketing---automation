# ============================================================
#  segmentation.py — Subscriber Segmentation Logic
#  Author: Sandeep Kumar | M.Tech CSE
# ============================================================

from config import INACTIVE_DAYS, NEW_SUBSCRIBER_DAYS, VIP_PURCHASE_COUNT


def segment_subscribers(subscribers):
    """
    Segments a list of subscribers into 5 groups:
      - new_subscribers
      - active_buyers
      - cart_abandoners
      - inactive_users
      - vip_customers
    """
    segments = {
        "new_subscribers":  [],
        "active_buyers":    [],
        "cart_abandoners":  [],
        "inactive_users":   [],
        "vip_customers":    [],
    }

    for subscriber in subscribers:
        email         = subscriber.get("email", "")
        fname         = subscriber.get("fname", "User")
        purchases     = subscriber.get("purchases", 0)
        cart          = subscriber.get("cart", False)
        days_inactive = subscriber.get("days_inactive", 0)

        # VIP — 3 or more purchases
        if purchases >= VIP_PURCHASE_COUNT:
            segments["vip_customers"].append(subscriber)

        # New Subscriber — signed up in last 7 days, no purchases
        elif days_inactive <= NEW_SUBSCRIBER_DAYS and purchases == 0:
            segments["new_subscribers"].append(subscriber)

        # Inactive — no activity in 60+ days
        elif days_inactive >= INACTIVE_DAYS:
            segments["inactive_users"].append(subscriber)

        # Cart Abandoner — has items in cart, hasn't purchased
        elif cart and purchases == 0:
            segments["cart_abandoners"].append(subscriber)

        # Active buyer — at least one purchase, recently active
        elif purchases >= 1 and days_inactive < INACTIVE_DAYS:
            segments["active_buyers"].append(subscriber)

    return segments


def print_segment_summary(segments):
    """Print a clean summary of how subscribers are segmented."""
    print("\n" + "=" * 50)
    print("   SUBSCRIBER SEGMENTATION SUMMARY")
    print("=" * 50)
    for segment, members in segments.items():
        label = segment.replace("_", " ").title()
        print(f"  {label:<25} → {len(members)} subscribers")
    print("=" * 50)
    total = sum(len(v) for v in segments.values())
    print(f"  {'Total Segmented':<25} → {total} subscribers")
    print("=" * 50 + "\n")
