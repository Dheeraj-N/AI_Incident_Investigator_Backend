from fastapi import APIRouter

from app.core.logger import logger

from app.services.incident_service import IncidentService

from app.models.investigation_request import InvestigationRequest

from app.models.investigation_response import (
    InvestigationReport
)

router = APIRouter()

incident_service = IncidentService()


@router.post("/investigate",tags=["Investigations"],

    summary=
        "Run an incident investigation",

    description=
        (
            "Collect evidence, "
            "perform correlation, "
            "generate timeline, "
            "produce recommendations "
            "and return an "
            "investigation report."
        ),

    response_model=
        InvestigationReport)

async def investigate(request: InvestigationRequest):
    logger.info("POST /investigate called")
    return await incident_service.investigate(request.incident_id)


"""@router.post(
    "/investigate",
    summary="Investigate Incident"
)
async def investigate():

    result = await incident_service.investigate(
        incident_id="INC001"
    )

    return result
"""

"""from fastapi import APIRouter

router = APIRouter()


@router.post("/investigate")
async def investigate():

    return {
        "status": "success"
    }
"""
