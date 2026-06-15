from app.services.data_loader import (
    load_json
)


class MockAdapter:

    async def get_incident(
        self,
        incident_id: str
    ):

        incidents = load_json(
            "incidents.json"
        )

        return next(
            (
                item
                for item in incidents
                if item["incident_id"]
                == incident_id
            ),
            None
        )

    async def get_deployments(
        self,
        service: str
    ):

        return load_json(
            "deployments.json"
        )

    async def get_metrics(
        self,
        service: str
    ):

        return load_json(
            "metrics.json"
        )

    async def get_outages(
        self
    ):

        return load_json(
            "outages.json"
        )