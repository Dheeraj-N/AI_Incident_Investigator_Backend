# Phase 25
from datetime import datetime

from app.correlation.scoring import (
    deployment_score,
    metric_score,
    outage_score,
    weighted_confidence
)


class CorrelationEngine:

    def investigate(
        self,
        evidence: dict
    ):

        possible_causes = []

        # -------------------------
        # Incident
        # -------------------------

        incident = evidence["incident"]

        # -------------------------
        # Deployment Analysis
        # -------------------------

        deployment = (
            evidence["deployments"][0]
        )

        incident_time = datetime.fromisoformat(
            incident["timestamp"]
        )

        deployment_time = datetime.fromisoformat(
            deployment["timestamp"]
        )

        gap_minutes = (
            incident_time
            - deployment_time
        ).total_seconds() / 60

        deployment_confidence = (
            deployment_score(
                int(gap_minutes)
            )
        )

        # -------------------------
        # Metrics Analysis
        # -------------------------

        metrics = evidence["metrics"][0]

        metric_confidence = (
            metric_score(
                metrics["error_rate"],
                metrics["latency_ms"]
            )
        )

        # -------------------------
        # Outage Analysis
        # -------------------------

        outage = evidence["outages"][0]

        outage_confidence = (
            outage_score(
                outage["status"]
            )
        )

        # -------------------------
        # Final Weighted Confidence
        # -------------------------

        final_confidence = (
            weighted_confidence(
                deployment_confidence,
                metric_confidence,
                outage_confidence
            )
        )

        # -------------------------
        # Outage Cause
        # -------------------------

        if outage_confidence > 0:

            possible_causes.append(
                {
                    "source":
                        f'{outage["provider"]} Outage',

                    "confidence":
                        final_confidence,

                    "evidence": [
                        (
                            f'{outage["provider"]} '
                            f'status reported '
                            f'{outage["status"]}'
                        )
                    ]
                }
            )

        # -------------------------
        # Error Rate Cause
        # -------------------------

        if metrics["error_rate"] > 70:

            possible_causes.append(
                {
                    "source":
                        "High Error Rate",

                    "confidence":
                        final_confidence,

                    "evidence": [
                        (
                            f'Error rate reached '
                            f'{metrics["error_rate"]}%'
                        )
                    ]
                }
            )

        # -------------------------
        # Latency Cause
        # -------------------------

        if metrics["latency_ms"] > 3000:

            possible_causes.append(
                {
                    "source":
                        "Latency Spike",

                    "confidence":
                        final_confidence,

                    "evidence": [
                        (
                            f'Latency reached '
                            f'{metrics["latency_ms"]}ms'
                        )
                    ]
                }
            )

        # -------------------------
        # Deployment Cause
        # -------------------------

        if deployment_confidence > 0:

            possible_causes.append(
                {
                    "source":
                        "Recent Deployment",

                    "confidence":
                        final_confidence,

                    "evidence": [
                        (
                            f'Deployment occurred '
                            f'{int(gap_minutes)} '
                            f'minutes before incident'
                        )
                    ]
                }
            )

        # -------------------------
        # Sort Causes
        # -------------------------

        possible_causes.sort(
            key=lambda cause:
                cause["confidence"],
            reverse=True
        )

        return {
            "possible_causes":
                possible_causes,

            "overall_confidence":
                final_confidence
        }



"""from datetime import datetime

from app.correlation.scoring import (
    deployment_score,
    metric_score,
    outage_score,
    weighted_confidence
)


class CorrelationEngine:

    def investigate(
        self,
        evidence: dict
    ):

        possible_causes = []

        # -------------------------
        # Incident
        # -------------------------

        incident = evidence["incident"]

        # -------------------------
        # Deployment Analysis
        # -------------------------

        deployment = (
            evidence["deployments"][0]
        )

        incident_time = datetime.fromisoformat(
            incident["timestamp"]
        )

        deployment_time = datetime.fromisoformat(
            deployment["timestamp"]
        )

        gap_minutes = (
            incident_time
            - deployment_time
        ).total_seconds() / 60

        deployment_confidence = (
            deployment_score(
                int(gap_minutes)
            )
        )

        # -------------------------
        # Metrics Analysis
        # -------------------------

        metrics = evidence["metrics"][0]

        metric_confidence = (
            metric_score(
                metrics["error_rate"],
                metrics["latency_ms"]
            )
        )

        # -------------------------
        # Outage Analysis
        # -------------------------

        outage = evidence["outages"][0]

        outage_confidence = (
            outage_score(
                outage["status"]
            )
        )

        # -------------------------
        # Final Confidence
        # -------------------------

        final_confidence = (
            weighted_confidence(
                deployment_confidence,
                metric_confidence,
                outage_confidence
            )
        )

        # -------------------------
        # Possible Causes
        # -------------------------

        if outage_confidence > 0:

            possible_causes.append(
                {
                    "source":
                        f'{outage["provider"]} Outage',

                    "confidence":
                        final_confidence,

                    "evidence": [
            (
                f"Deployment occurred "
                f"{int(gap_minutes)} "
                f"minutes before incident"
            )
        ]
                }
            )

        if metric_confidence > 0:

            if metrics["error_rate"] > 70:

                possible_causes.append(
                    {
                        "source":
                            "High Error Rate",

                        "confidence":
                            final_confidence
                    }
                )

            if metrics["latency_ms"] > 3000:

                possible_causes.append(
                    {
                        "source":
                            "Latency Spike",

                        "confidence":
                            final_confidence
                    }
                )

        if deployment_confidence > 0:

            possible_causes.append(
                {
                    "source":
                        "Recent Deployment",

                    "confidence":
                        final_confidence
                }
            )

        # -------------------------
        # Sort Results
        # -------------------------

        possible_causes.sort(
            key=lambda cause:
                cause["confidence"],
            reverse=True
        )

        return {
            "possible_causes":
                possible_causes
        }
"""

"""
from app.correlation.scoring import deployment_score


class CorrelationEngine:
    def investigate(self, deploy_gap_minutes: int):

        score = deployment_score(deploy_gap_minutes)

        return {
            "possible_causes": [{"source": "Recent Deployment", "confidence": score}]
        }
"""