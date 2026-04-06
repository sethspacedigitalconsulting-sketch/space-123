"""
Voice AI Lead Qualifier - Core Agent Logic
"""
from dataclasses import dataclass
from enum import Enum

class LeadScore(Enum):
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"

@dataclass
class Lead:
    name: str
    company: str
    budget: str
    timeline: str
    decision_maker: bool
    pain_point: str = ""
    score: LeadScore = LeadScore.COLD

QUALIFICATION_QUESTIONS = [
    {"key": "industry", "question": "What industry is your business in?"},
    {"key": "challenge", "question": "What's your biggest challenge right now?"},
    {"key": "timeline", "question": "What's your timeline to solve this?"},
    {"key": "budget", "question": "What's your budget range for a solution like this?"},
    {"key": "decision_maker", "question": "Are you the decision-maker?"},
]

OBJECTION_RESPONSES = {
    "too expensive": "I understand. Many clients felt the same initially. When they saw 3x ROI in the first quarter, it became a no-brainer. Want me to show you how?",
    "need to think": "Totally fair. What specifically would you want to consider? I can help address that now.",
    "not the right time": "Got it. What timing works better for you? I have slots available this week or next.",
    "sending info": "Happy to send details. What email should I use?",
}

def score_lead(budget: str, timeline: str, is_decision_maker: bool, has_pain_point: bool) -> LeadScore:
    score = 0
    
    if "k" in budget.lower() or "thousand" in budget.lower():
        score += 30
    elif budget:
        score += 20
    
    if timeline in ["immediately", "this week", "asap"]:
        score += 25
    elif timeline in ["this month", "soon"]:
        score += 15
    
    if is_decision_maker:
        score += 25
    
    if has_pain_point:
        score += 20
    
    if score >= 70:
        return LeadScore.HOT
    elif score >= 40:
        return LeadScore.WARM
    return LeadScore.COLD

def handle_objection(objection: str) -> str:
    objection_lower = objection.lower()
    for key, response in OBJECTION_RESPONSES.items():
        if key in objection_lower:
            return response
    return "I appreciate you sharing that. Let me make sure I understand your concern fully."

def create_calendar_event(lead: Lead) -> dict:
    return {
        "summary": f"Discovery Call - {lead.name}",
        "description": f"Qualified lead from Voice AI\n\nCompany: {lead.company}\nBudget: {lead.budget}\nTimeline: {lead.timeline}\nPain Point: {lead.pain_point}\nScore: {lead.score.value}",
        "duration_minutes": 30,
    }

if __name__ == "__main__":
    test_lead = Lead(
        name="John Smith",
        company="Acme Corp",
        budget="$5k",
        timeline="this week",
        decision_maker=True,
        pain_point="lead generation"
    )
    test_lead.score = score_lead(test_lead.budget, test_lead.timeline, test_lead.decision_maker, bool(test_lead.pain_point))
    print(f"Lead scored: {test_lead.score.value}")
