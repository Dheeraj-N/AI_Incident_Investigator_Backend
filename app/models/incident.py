from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str
    service: str
    severity: str
    timestamp: str
