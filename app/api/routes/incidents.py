import json
from pathlib import Path
from fastapi import APIRouter, HTTPException
from app.models.incident import Incident
from app.core.exceptions import IncidentNotFoundError

router = APIRouter()

MOCK_DATA_PATH = Path(__file__).parent.parent.parent / "mock_data" / "incidents.json"

try:
    _INCIDENTS: list[Incident] = [
        Incident(**item) for item in json.loads(MOCK_DATA_PATH.read_text())
    ]
except (FileNotFoundError, json.JSONDecodeError) as e:
    raise RuntimeError(f"Failed to load incidents mock data: {e}") from e

_INCIDENTS_BY_ID: dict[str, Incident] = {inc.incident_id: inc for inc in _INCIDENTS}


@router.get(
    "/incidents",
    tags=["Incidents"],
    summary="List incidents",
    description="Retrieve available incidents.",
    response_model=dict[str, list[Incident]],
)
async def get_incidents():
    return {"incidents": _INCIDENTS}


@router.get(
    "/incidents/{incident_id}",
    tags=["Incidents"],
    summary="Get incident",
    description="Retrieve a single incident by ID.",
    response_model=Incident,
)
async def get_incident(incident_id: str):
    incident = _INCIDENTS_BY_ID.get(incident_id)
    if not incident:
        raise IncidentNotFoundError(f"Incident {incident_id} not found")
    return incident


@router.get(
    "/incidents/{incident_id}/executive-report",
    tags=["Incidents"],
    summary="Get executive report",
    description="Retrieve the executive report for a previously investigated incident.",
)
async def get_executive_report(incident_id: str):
    if incident_id not in _INCIDENTS_BY_ID:
        raise IncidentNotFoundError(f"Incident {incident_id} not found")

    from app.services.incident_service import IncidentService
    report = IncidentService.get_cached_report(incident_id)
    if report is None:
        raise HTTPException(
            status_code=404,
            detail=f"No investigation found for {incident_id}. Run POST /api/investigate first.",
        )
    return report["executive_report"]
