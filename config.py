# ============================================================
#  Email Marketing Automation — Config
#  Author: Sandeep Kumar | M.Tech CSE
# ============================================================

# Mailchimp API Settings
MAILCHIMP_API_KEY = "your-api-key-here"       # Replace with your Mailchimp API key
MAILCHIMP_SERVER  = "us1"                      # e.g. us1, us2 (found in your API key)
MAILCHIMP_LIST_ID = "your-audience-id-here"   # Found in Mailchimp Audience Settings

# Demo Mode — set True if you don't have an API key yet
DEMO_MODE = True

# Campaign Delay Settings (in hours)
WELCOME_EMAIL_DELAYS    = [0, 48, 120]   # Immediate, 2 days, 5 days
CART_EMAIL_DELAYS       = [1, 24, 48]    # 1hr, 24hr, 48hr
POSTPURCHASE_DELAYS     = [0, 72, 168]   # Immediate, 3 days, 7 days
REENGAGEMENT_DELAYS     = [0, 168]       # Immediate, 7 days

# Segment Definitions (days)
INACTIVE_DAYS           = 60
NEW_SUBSCRIBER_DAYS     = 7
VIP_PURCHASE_COUNT      = 3
