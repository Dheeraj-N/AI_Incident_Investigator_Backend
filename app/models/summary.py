from pydantic import BaseModel


class InvestigationSummary(BaseModel):
    summary: str

    root_cause: str
