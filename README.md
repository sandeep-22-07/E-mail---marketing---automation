# 📧 Email Marketing Automation

> **Minor Project** | M.Tech – Computer Science & Engineering  
> **Author:** Sandeep Kumar  
> **Platform:** Mailchimp API v3.0 | Python

---

## 📌 Project Overview

This project automates email marketing campaigns using **Mailchimp's API**. It handles subscriber segmentation, behavior-triggered email workflows, and campaign performance tracking — all from a clean Python codebase.

The system simulates a real e-commerce email automation setup with 5 complete workflows.

---

## ⚙️ Features

- ✅ **Subscriber Segmentation** — Automatically groups users into 5 segments based on behavior
- ✅ **5 Automation Workflows** — Welcome series, cart recovery, post-purchase, re-engagement, VIP loyalty
- ✅ **Mailchimp API Integration** — Fetch subscribers, add members, pull campaign reports
- ✅ **Analytics Dashboard** — Open rate, click rate, conversion tracking via API
- ✅ **Demo Mode** — Runs fully without a real API key for testing/demo purposes

---

## 🗂️ Folder Structure

```
email-marketing-automation/
│
├── main.py                  # Entry point — runs all workflows
├── config.py                # API keys and settings
├── requirements.txt         # Python dependencies
│
├── src/
│   ├── mailchimp_client.py  # Mailchimp API calls (fetch, add, report)
│   ├── segmentation.py      # Subscriber segmentation logic
│   ├── workflows.py         # All 5 email automation workflows
│   └── analytics.py        # Campaign performance reporting
│
└── output/
    └── campaign_report.json # Auto-generated analytics report
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/email-marketing-automation.git
cd email-marketing-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API (optional)
Open `config.py` and add your Mailchimp API key:
```python
MAILCHIMP_API_KEY = "your-api-key-here"
MAILCHIMP_SERVER  = "us1"
MAILCHIMP_LIST_ID = "your-audience-id"
DEMO_MODE         = False   # Set False to use real API
```
> 💡 **No API key?** Leave `DEMO_MODE = True` — the project runs with sample data.

### 4. Run the project
```bash
python main.py
```

---

## 📊 Automation Workflows

| Workflow | Trigger | Emails |
|---|---|---|
| Welcome Series | New signup | 3 emails over 5 days |
| Abandoned Cart Recovery | Cart not checked out | 3 emails over 48 hrs |
| Post-Purchase Follow Up | Order confirmed | 3 emails over 7 days |
| Re-engagement Campaign | Inactive 60+ days | 2 emails over 7 days |
| VIP Loyalty Program | 3+ purchases | Monthly exclusive email |

---

## 📈 Sample Output

```
==================================================
   EMAIL MARKETING AUTOMATION SYSTEM
   Author : Sandeep Kumar | M.Tech CSE
==================================================

[STEP 1] Fetching subscribers...
[DEMO] Loaded demo subscribers.

[STEP 2] Segmenting subscribers...
==================================================
   SUBSCRIBER SEGMENTATION SUMMARY
==================================================
  New Subscribers          →  1 subscribers
  Active Buyers            →  1 subscribers
  Cart Abandoners          →  1 subscribers
  Inactive Users           →  1 subscribers
  Vip Customers            →  1 subscribers
==================================================

[STEP 3] Running automation workflows...
...

✅ All workflows completed successfully!
```

---

## 🔗 API Reference

This project uses **Mailchimp Marketing API v3.0**  
Docs: https://mailchimp.com/developer/marketing/api/

Key endpoints used:
- `GET /lists/{list_id}/members` — Fetch subscribers
- `POST /lists/{list_id}/members` — Add subscriber
- `GET /reports/{campaign_id}` — Campaign analytics
- `GET /campaigns` — List all campaigns

---

## 👤 Author

**Sandeep Kumar**  
M.Tech – Computer Science & Engineering  
Digital Marketing Strategist | SEO Analyst  
Greater Coimbatore Area, Tamil Nadu
