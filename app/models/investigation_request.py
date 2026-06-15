from pydantic import BaseModel


class InvestigationRequest(BaseModel):
    incident_id: str
