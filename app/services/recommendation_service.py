class RecommendationService:

    def generate(
        self,
        possible_causes: list
    ) -> list[dict]:

        recommendations = []

        for cause in possible_causes:

            source = cause["source"]

            if "Outage" in source:

                recommendations.extend(
                    [
                        {
                            "action":
                                "Check provider status dashboard"
                        },
                        {
                            "action":
                                "Enable service failover"
                        },
                        {
                            "action":
                                "Review dependency timeout settings"
                        }
                    ]
                )

            if "Deployment" in source:

                recommendations.extend(
                    [
                        {
                            "action":
                                "Review deployment changes"
                        },
                        {
                            "action":
                                "Consider rollback"
                        },
                        {
                            "action":
                                "Verify feature flags"
                        }
                    ]
                )

            if "Error Rate" in source:

                recommendations.extend(
                    [
                        {
                            "action":
                                "Inspect application logs"
                        },
                        {
                            "action":
                                "Review failing requests"
                        }
                    ]
                )

            if "Latency" in source:

                recommendations.extend(
                    [
                        {
                            "action":
                                "Review slow dependencies"
                        },
                        {
                            "action":
                                "Check database performance"
                        }
                    ]
                )

        unique_actions = set()

        deduplicated = []

        for recommendation in recommendations:

            action = recommendation["action"]

            if action not in unique_actions:

                unique_actions.add(action)

                deduplicated.append(
                    recommendation
                )

        return deduplicated