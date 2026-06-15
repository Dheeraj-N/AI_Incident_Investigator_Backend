import asyncio

from app.coral.client import CoralClient
from app.coral.queries import INCIDENT_CORRELATION_QUERY


async def main():

    client = CoralClient()

    response = await client.execute(INCIDENT_CORRELATION_QUERY)

    print(response)


asyncio.run(main())
