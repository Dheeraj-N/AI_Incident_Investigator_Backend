import asyncio

from app.services.evidence_service import (
    EvidenceService
)

async def main():

    service = EvidenceService()

    evidence = (
        await service.get_evidence(
            "INC-101"
        )
    )

    print(evidence)


asyncio.run(main())