import asyncio

from app.services.incident_service import IncidentService


async def main():

    service = IncidentService()

    result = await service.investigate("INC-101")

    print(result)


asyncio.run(main())
