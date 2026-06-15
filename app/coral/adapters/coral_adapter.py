from app.coral.client import (
    CoralClient
)

from app.coral import queries


class CoralAdapter:

    def __init__(self):

        self.client = CoralClient()

    async def get_incident(
        self,
        incident_id: str
    ):

        return await self.client.execute(
            queries.GET_INCIDENT
        )

    async def get_deployments(
        self,
        service: str
    ):

        return await self.client.execute(
            queries.GET_DEPLOYMENTS
        )

    async def get_metrics(
        self,
        service: str
    ):

        return await self.client.execute(
            queries.GET_METRICS
        )

    async def get_outages(
        self
    ):

        return await self.client.execute(
            queries.GET_OUTAGES
        )