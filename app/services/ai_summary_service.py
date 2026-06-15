class AISummaryService:

    async def generate_summary(
        self,
        correlation_result: dict,
        timeline: list
    ):

        top_cause = (
            correlation_result["possible_causes"][0]
        )

        source = top_cause["source"]

        confidence = (
            top_cause["confidence"]
        )

        evidence = (
            top_cause["evidence"]
        )

        evidence_text = "; ".join(
            evidence
        )

        timeline_text = " → ".join(
            [
                item["event"]
                for item in timeline
            ]
        )

        if "Outage" in source:

            recommendation = (
                "Review provider status page "
                "and enable service failover."
            )

        elif "Deployment" in source:

            recommendation = (
                "Review recent deployment "
                "and consider rollback."
            )

        elif "Error Rate" in source:

            recommendation = (
                "Inspect application logs "
                "and failing requests."
            )

        else:

            recommendation = (
                "Perform additional investigation."
            )

        summary = (
            f"Investigation indicates "
            f"that {source} is the most "
            f"likely root cause with "
            f"confidence {confidence:.0%}. "
            f"Supporting evidence: "
            f"{evidence_text}. "
            f"Timeline observed: "
            f"{timeline_text}."
        )

        return {
            "summary": summary,
            "root_cause": source,
            "confidence": confidence,
            "recommendation": recommendation
        }


"""class AISummaryService:

    async def generate_summary(
        self,
        correlation_result: dict,
        timeline: list
    ):

        top_cause = (
            correlation_result
            ["possible_causes"][0]
        )

        source = top_cause["source"]

        confidence = (
            top_cause["confidence"]
        )

        timeline_text = " → ".join(
            [
                item["event"]
                for item in timeline
            ]
        )

        summary = (
            f"Investigation indicates "
            f"that {source} is the "
            f"most likely root cause "
            f"with confidence "
            f"{confidence:.0%}. "
            f"Timeline observed: "
            f"{timeline_text}."
        )

        return {
            "summary": summary,
            "root_cause": source,
            "confidence": confidence
        }
        """