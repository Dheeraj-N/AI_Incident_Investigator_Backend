from pydantic import BaseModel


class Evidence(BaseModel):
    source: str
    confidence: float
