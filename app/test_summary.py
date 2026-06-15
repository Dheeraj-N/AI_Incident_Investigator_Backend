import asyncio

from app.services.ai_summary_service import (
    AISummaryService
)

correlation_result = {
    "possible_causes": [
        {
            "source":
                "Stripe Outage",

            "confidence":
                0.95
        }
    ]
}

timeline = [
    {
        "event":
            "Deployment Released"
    },
    {
        "event":
            "Stripe Degraded"
    },
    {
        "event":
            "Incident Triggered"
    }
]

async def main():

    service = AISummaryService()

    result = (
        await service
        .generate_summary(
            correlation_result,
            timeline
        )
    )

    print(result)

asyncio.run(main())