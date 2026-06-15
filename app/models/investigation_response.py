from pydantic import BaseModel


class TimelineEvent(BaseModel):
    timestamp: str
    event: str


class Cause(BaseModel):
    source: str
    confidence: float
    evidence: list[str]


class Recommendation(BaseModel):
    action: str


class AIAnalysis(BaseModel):
    root_cause: str
    confidence: float
    reasoning: list[str]
    conclusion: str


class ExecutiveIncidentReport(BaseModel):
    incident_summary: str
    business_impact: str
    root_cause: str
    actions_taken: list[str]
    preventive_actions: list[str]
    executive_recommendation: str


class Hypothesis(BaseModel):
    cause: str
    confidence: float
    reasoning: str
    supporting_evidence: list[str]


class HypothesisAnalysis(BaseModel):
    primary_hypothesis: Hypothesis
    alternative_hypotheses: list[Hypothesis]


class InvestigationReport(BaseModel):
    incident_id: str
    timeline: list[TimelineEvent]
    possible_causes: list[Cause]
    ai_analysis: AIAnalysis
    hypothesis_analysis: HypothesisAnalysis
    ai_summary: str
    recommendations: list[Recommendation]
    executive_report: ExecutiveIncidentReport
