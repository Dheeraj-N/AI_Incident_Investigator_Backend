from app.core.exceptions import (
    IncidentNotFoundError
)

from app.core.settings import (
    settings
)

from app.coral.adapters.mock_adapter import (
    MockAdapter
)

from app.coral.adapters.coral_adapter import (
    CoralAdapter
)


class EvidenceService:

    def __init__(self):

        self.repository = (
            self._build_repository()
        )

    def _build_repository(self):

        if settings.DATA_SOURCE == "mock":
            return MockAdapter()

        if settings.DATA_SOURCE == "coral":
            return CoralAdapter()

        raise ValueError(
            f"Unsupported DATA_SOURCE: "
            f"{settings.DATA_SOURCE}"
        )

    async def collect(
        self,
        incident_id: str
    ) -> dict:

        # -------------------------
        # Incident
        # -------------------------

        incident = (
            await self.repository
            .get_incident(
                incident_id
            )
        )

        if incident is None:

            raise IncidentNotFoundError(
                f"Incident "
                f"{incident_id} "
                f"not found"
            )

        service = incident["service"]

        # -------------------------
        # Deployments
        # -------------------------

        deployments = (
            await self.repository
            .get_deployments(
                service
            )
        )

        # -------------------------
        # Metrics
        # -------------------------

        metrics = (
            await self.repository
            .get_metrics(
                service
            )
        )

        # -------------------------
        # Outages
        # -------------------------

        outages = (
            await self.repository
            .get_outages()
        )

        return {
            "incident": incident,
            "deployments": deployments,
            "metrics": metrics,
            "outages": outages
        }



"""from app.services.data_loader import (
    load_json
)

from app.core.exceptions import (
    IncidentNotFoundError
)

class EvidenceService:

    async def get_evidence(
        self,
        incident_id: str
    ):

        incidents = load_json(
            "incidents.json"
        )

        deployments = load_json(
            "deployments.json"
        )

        metrics = load_json(
            "metrics.json"
        )

        outages = load_json(
            "outages.json"
        )

        incident = next(
            (
                i
                for i in incidents
                if i["incident_id"]
                == incident_id
            ),
            None
        )

        if incident is None:

            raise IncidentNotFoundError(
            f"Incident {incident_id} not found"
            )

        return {
            "incident": incident,
            "deployments": deployments,
            "metrics": metrics,
            "outages": outages
        }

"""

"""
from app.coral.client import CoralClient
from app.coral.queries import INCIDENT_CORRELATION_QUERY


class EvidenceService:
    def __init__(self):

        self.coral_client = CoralClient()

    async def get_evidence(self, incident_id: str):

        response = await self.coral_client.execute(INCIDENT_CORRELATION_QUERY)

        return response
"""