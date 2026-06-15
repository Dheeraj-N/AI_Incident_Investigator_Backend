import pytest

from app.services.incident_service import (
    IncidentService
)


@pytest.mark.asyncio
async def test_investigation_service():

    service = IncidentService()

    result = await service.investigate(
        "INC001"
    )

    assert (
        result["incident_id"]
        == "INC001"
    )