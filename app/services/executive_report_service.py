import json

from app.services.gemini_service import (
    GeminiService
)


class ExecutiveReportService:

    def __init__(self):

        self.gemini = (
            GeminiService()
        )

    def _build_prompt(
        self,
        timeline,
        root_cause,
        recommendations,
        ai_analysis
    ):

        return f"""
You are an Engineering Director.

Generate an executive incident report.

Timeline:
{timeline}

Root Cause:
{root_cause}

Investigation Analysis:
{ai_analysis}

Recommendations:
{recommendations}

Return ONLY valid JSON.

{{
  "incident_summary": "...",
  "business_impact": "...",
  "root_cause": "...",
  "actions_taken": [],
  "preventive_actions": [],
  "executive_recommendation": "..."
}}
"""

    async def generate(
        self,
        timeline,
        root_cause,
        recommendations,
        ai_analysis
    ):

        prompt = (
            self._build_prompt(
                timeline,
                root_cause,
                recommendations,
                ai_analysis
            )
        )

        response = await (
            self.gemini.generate(
                prompt
            )
        )

        cleaned = response.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        if not cleaned:
            raise ValueError("Empty response from Gemini")
        report = json.loads(cleaned)

       # report = json.loads(response)
        

        return report



"""class ExecutiveReportService:

    async def generate(
        self,
        correlation_result: dict,
        recommendations: list,
        timeline: list
    ):

        top_cause = (
            correlation_result[
                "possible_causes"
            ][0]
        )

        root_cause = (
            top_cause["source"]
        )

        incident_summary = (
            "A critical production "
            "incident impacted "
            "checkout operations "
            "and triggered an "
            "automated investigation."
        )

        business_impact = (
            "Customers experienced "
            "checkout disruptions "
            "which may have affected "
            "transaction completion."
        )

        actions_taken = [
            item["action"]
            for item in recommendations[:3]
        ]

        preventive_actions = [
            "Improve monitoring coverage",
            "Enhance vendor failover strategy",
            "Review incident response process"
        ]

        executive_recommendation = (
            "Prioritize resilience "
            "improvements for critical "
            "payment dependencies."
        )

        return {
            "incident_summary":
                incident_summary,

            "business_impact":
                business_impact,

            "root_cause":
                root_cause,

            "actions_taken":
                actions_taken,

            "preventive_actions":
                preventive_actions,

            "executive_recommendation":
                executive_recommendation
        }
"""