from app.core.exceptions import (
    TimelineBuildFailedError
)

class TimelineBuilder:

    def build(
        self,
        evidence: dict
    ):

        try:

            timeline = []

            if evidence["deployments"]:
                deployment = evidence["deployments"][0]
                timeline.append(
                    {
                        "timestamp":
                        deployment["timestamp"],

                        "event":
                        "Deployment Released"
                    }
                )

            if evidence["outages"]:
                outage = evidence["outages"][0]
                timeline.append(
                    {
                        "timestamp":
                            outage["start_time"],

                        "event":
                            f'{outage["provider"]} Degraded'
                    }
                )

            if evidence["metrics"]:
                metrics = evidence["metrics"][0]
                timeline.append(
                    {
                        "timestamp":
                            metrics["timestamp"],

                        "event":
                            "Error Rate Spike"
                    }
                )

            incident = (
                evidence["incident"]
            )

            timeline.append(
                {
                    "timestamp":
                        incident["timestamp"],

                    "event":
                        "Incident Triggered"
                }
            )

            timeline.sort(
                key=lambda x:
                    x["timestamp"]
            )

            return timeline
    
        except Exception as exc:

            raise TimelineBuildFailedError(
            str(exc)
            )