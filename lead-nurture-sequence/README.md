# Lead Nurture Sequence

Automated multi-channel follow-up (email + SMS) that warms cold leads and reactivates dead prospects over 14 days.

## The Problem

Your leads are going cold. You spent money on ads. They filled out a form. Then... nothing.

**80% of leads never hear back.**
**Most leads aren't "no" - they're "not yet."**

## The Solution

This sequence automates follow-up across email and SMS. Sends the right message at the right time. No lead gets left behind.

## What It Does

- Triggers automatically on new leads
- Sends personalized emails and SMS
- Delivers case studies and social proof
- Creates urgency with deadlines
- Alerts when leads engage
- Escalates hot leads to sales

## The 14-Day Sequence

| Day | Channel | What |
|-----|---------|------|
| Day 0 | Email | Welcome + free value |
| Day 1 | SMS | Quick follow-up |
| Day 2 | Email | Case study (similar company) |
| Day 3 | SMS | Social proof (if opened Day 0) |
| Day 5 | Email | FAQ + objections |
| Day 7 | SMS | Urgency + offer |
| Day 10 | Email | Soft close |
| Day 14 | SMS | Final push |

## Engagement Triggers

| Signal | Score |
|--------|-------|
| Email opened | +5 |
| Link clicked | +15 |
| Visited pricing | +10 |
| Form started | +20 |
| Replied | +50 |

Score 50+ → Alert sales immediately

## Tech Stack

SendGrid + Twilio + n8n + HubSpot/GoHighLevel

## Results

| Metric | Before | After |
|--------|--------|-------|
| Cold lead response | 3% | 18% |
| Dead lead reactivation | 5% | 24% |
| Lead-to-opportunity | 12% | 31% |
| Avg response time | 72 hrs | 4 hrs |

## Files

- `nurture_sequence.py` - Core sequence logic
- `n8n-workflow.json` - n8n workflow template
- `templates/` - Email/SMS copy

---

Built by [Space Digital & AI Consulting](https://hoo.be/spacedigitalconsulting)
