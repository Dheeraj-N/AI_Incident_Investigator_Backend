import json

from app.services.gemini_service import (
    GeminiService
)


class AIInvestigationService:

    def __init__(self):

        self.gemini = (
            GeminiService()
        )

    def _build_prompt(
        self,
        possible_causes,
        timeline
    ):

        return f"""
You are a Principal Site Reliability Engineer.

Analyze the production incident.

Timeline:
{timeline}

Possible Causes:
{possible_causes}

Generate JSON:

{{
  "root_cause": "...",
  "confidence": 0.0,
  "reasoning": [
      "...",
      "..."
  ],
  "conclusion": "..."
}}

Return ONLY JSON.
"""

    async def analyze(
        self,
        correlation_result,
        timeline
    ):

        possible_causes = (
            correlation_result[
                "possible_causes"
            ]
        )

        prompt = (
            self._build_prompt(
                possible_causes,
                timeline
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
        analysis = json.loads(cleaned)
        
        #analysis = json.loads(response)

        

        return {
            "root_cause":
                analysis["root_cause"],

            "confidence":
                analysis["confidence"],

            "reasoning":
                analysis["reasoning"],

            "conclusion":
                analysis["conclusion"]
        }

"""
class AIInvestigationService:

    async def analyze(
        self,
        correlation_result: dict,
        timeline: list
    ):

        top_cause = (
            correlation_result[
                "possible_causes"
            ][0]
        )

        source = (
            top_cause["source"]
        )

        confidence = (
            top_cause["confidence"]
        )

        evidence = (
            top_cause["evidence"]
        )

        reasoning = []

        reasoning.extend(
            evidence
        )

        reasoning.extend(
            [
                event["event"]
                for event in timeline
            ]
        )

        conclusion = (
            f"The available evidence "
            f"strongly suggests that "
            f"{source} is the most "
            f"likely root cause."
        )

        return {
            "root_cause": source,
            "confidence": confidence,
            "reasoning": reasoning,
            "conclusion": conclusion
        }
"""