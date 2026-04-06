"""
CRM Auto-Enrichment Service
"""
import os
import requests
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class EnrichedLead:
    email: str
    name: str = ""
    company: str = ""
    company_size: str = ""
    industry: str = ""
    revenue: str = ""
    linkedin_url: str = ""
    tech_stack: list[str] = field(default_factory=list)
    confidence_score: int = 0
    sources: list[str] = field(default_factory=list)

class EnrichmentService:
    def __init__(self):
        self.apollo_key = os.getenv("APOLLO_API_KEY")
        self.clearbit_key = os.getenv("CLEARBIT_API_KEY")
        self.hunter_key = os.getenv("HUNTER_API_KEY")
    
    def enrich_by_email(self, email: str) -> EnrichedLead:
        lead = EnrichedLead(email=email)
        
        if self.apollo_key:
            apollo_data = self._enrich_apollo(email)
            if apollo_data:
                lead = self._merge(lead, apollo_data)
                lead.sources.append("apollo")
        
        if self.clearbit_key:
            clearbit_data = self._enrich_clearbit(email)
            if clearbit_data:
                lead = self._merge(lead, clearbit_data)
                lead.sources.append("clearbit")
        
        lead.confidence_score = self._calculate_score(lead)
        return lead
    
    def _enrich_apollo(self, email: str) -> Optional[dict]:
        try:
            response = requests.post(
                "https://api.apollo.io/v1/people/enrich",
                headers={"Authorization": f"Bearer {self.apollo_key}"},
                json={"email": email}
            )
            if response.status_code == 200:
                data = response.json().get("person", {})
                return {
                    "name": f"{data.get('first_name', '')} {data.get('last_name', '')}".strip(),
                    "company": data.get("organization", {}).get("name", ""),
                    "linkedin_url": data.get("linkedin_url", ""),
                }
        except:
            pass
        return None
    
    def _enrich_clearbit(self, email: str) -> Optional[dict]:
        try:
            response = requests.get(
                f"https://person.clearbit.com/v2/combined/find?email={email}",
                auth=(self.clearbit_key, "")
            )
            if response.status_code == 200:
                data = response.json()
                company = data.get("company", {})
                return {
                    "company": company.get("name", ""),
                    "company_size": company.get("metrics", {}).get("employees", ""),
                    "industry": company.get("category", {}).get("industry", ""),
                    "revenue": company.get("metrics", {}).get("annualRevenue", ""),
                }
        except:
            pass
        return None
    
    def _merge(self, lead: EnrichedLead, data: dict) -> EnrichedLead:
        for key, value in data.items():
            if value and not getattr(lead, key, None):
                setattr(lead, key, value)
        return lead
    
    def _calculate_score(self, lead: EnrichedLead) -> int:
        score = 0
        if lead.name: score += 20
        if lead.company: score += 20
        if lead.linkedin_url: score += 15
        if lead.company_size: score += 15
        if lead.industry: score += 10
        if lead.revenue: score += 10
        if lead.tech_stack: score += 10
        return min(score, 100)

if __name__ == "__main__":
    enricher = EnrichmentService()
    print("Enrichment service ready")
