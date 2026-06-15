from fastapi import APIRouter

from app.services.evidence_service import EvidenceService
from app.timeline.builder import TimelineBuilder

router = APIRouter()


@router.get(
    "/timeline/{incident_id}",

    tags=["Timeline"],

    summary=
        "Get incident timeline",

    description=
        "Retrieve the timeline "
        "generated for an incident."
)
async def timeline(incident_id: str):

    evidence = await EvidenceService().collect(incident_id)

    events = TimelineBuilder().build(evidence)

    return {"events": events}
