"""
Lead Nurture Sequence - Core Logic
"""
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class Channel(Enum):
    EMAIL = "email"
    SMS = "sms"

class LeadStatus(Enum):
    ACTIVE = "active"
    ENGAGED = "engaged"
    COLD = "cold"
    CONVERTED = "converted"

@dataclass
class SequenceStep:
    day: int
    channel: Channel
    subject: str

@dataclass
class Lead:
    email: str
    name: str
    company: str
    source: str
    status: LeadStatus = LeadStatus.ACTIVE
    engagement_score: int = 0

NURTURE_SEQUENCE = [
    SequenceStep(day=0, channel=Channel.EMAIL, subject="Welcome - Here's your free guide"),
    SequenceStep(day=1, channel=Channel.SMS, subject="Quick follow-up"),
    SequenceStep(day=2, channel=Channel.EMAIL, subject="How [Similar Company] solved this"),
    SequenceStep(day=3, channel=Channel.SMS, subject="Social proof"),
    SequenceStep(day=5, channel=Channel.EMAIL, subject="Common questions we hear"),
    SequenceStep(day=7, channel=Channel.SMS, subject="Offer expires soon"),
    SequenceStep(day=10, channel=Channel.EMAIL, subject="Last question"),
    SequenceStep(day=14, channel=Channel.SMS, subject="Final push"),
]

BEHAVIOR_SIGNALS = {
    "email_opened": 5,
    "link_clicked": 15,
    "page_visited": 10,
    "form_started": 20,
    "reply_sent": 50,
}

def get_next_step(current_day: int) -> SequenceStep:
    for step in NURTURE_SEQUENCE:
        if step.day > current_day:
            return step
    return None

def update_engagement(lead: Lead, signal: str) -> int:
    score = BEHAVIOR_SIGNALS.get(signal, 0)
    lead.engagement_score += score
    if lead.engagement_score >= 50:
        lead.status = LeadStatus.ENGAGED
    return lead.engagement_score

def should_escalate_to_sales(lead: Lead) -> bool:
    return lead.engagement_score >= 50

def personalize_message(template: str, lead: Lead) -> str:
    first_name = lead.name.split()[0] if lead.name else "there"
    return template.replace("{{first_name}}", first_name).replace("{{company}}", lead.company)

if __name__ == "__main__":
    test_lead = Lead(email="test@example.com", name="John Smith", company="Acme Corp", source="website")
    print(f"Sequence loaded with {len(NURTURE_SEQUENCE)} steps")
    print(f"Test lead engagement: {test_lead.engagement_score}")
