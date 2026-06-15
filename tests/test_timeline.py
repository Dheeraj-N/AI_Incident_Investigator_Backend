from app.timeline.builder import (
    TimelineBuilder
)

from app.services.data_loader import (
    load_json
)

evidence = {
    "incident":
        load_json(
            "incidents.json"
        )[0],

    "deployments":
        load_json(
            "deployments.json"
        ),

    "metrics":
        load_json(
            "metrics.json"
        ),

    "outages":
        load_json(
            "outages.json"
        )
}

builder = TimelineBuilder()

timeline = (
    builder.build(
        evidence
    )
)

print(timeline)