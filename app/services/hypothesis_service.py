import json
import logging

from app.services.gemini_service import (
    GeminiService
)

logger = logging.getLogger(__name__)


class HypothesisService:

    def __init__(self):

        self.gemini = GeminiService()

    def _build_prompt(
        self,
        timeline: list,
        possible_causes: list
    ) -> str:

        return f"""
You are a Principal Incident Commander.

Analyze the incident evidence.

Timeline:
{json.dumps(timeline, indent=2)}

Possible Causes:
{json.dumps(possible_causes, indent=2)}

IMPORTANT RULES:

1. The FIRST cause in Possible Causes is already the
most likely root cause determined by the correlation engine.

2. Do NOT change the root cause.

3. Do NOT invent timeline events.

4. Do NOT invent evidence.

5. Only use the provided data.

Generate:

- Primary Hypothesis explanation
- Alternative Hypotheses

Return ONLY valid JSON.

Schema:

{{
  "primary_hypothesis": {{
      "cause": "",
      "confidence": 0.0,
      "reasoning": "",
      "supporting_evidence": []
  }},
  "alternative_hypotheses": [
      {{
          "cause": "",
          "confidence": 0.0,
          "reasoning": "",
          "supporting_evidence": []
      }}
  ]
}}
"""

    async def analyze(
        self,
        timeline: list,
        possible_causes: list
    ) -> dict:

        if not possible_causes:

            return {
                "primary_hypothesis": {
                    "cause": "Unknown",
                    "confidence": 0.0,
                    "reasoning":
                        "No causes were available.",
                    "supporting_evidence": []
                },
                "alternative_hypotheses": []
            }

        prompt = self._build_prompt(
            timeline,
            possible_causes
        )

        try:

            response = await self.gemini.generate(
                prompt
            )

            cleaned = response.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            if not cleaned:
                    raise ValueError("Empty response from Gemini")
            analysis = json.loads(cleaned)
           
            #analysis = json.loads(response)

            return {
                "primary_hypothesis": {
                    "cause":
                        analysis[
                            "primary_hypothesis"
                        ]["cause"],

                    "confidence":
                        analysis[
                            "primary_hypothesis"
                        ]["confidence"],

                    "reasoning":
                        analysis[
                            "primary_hypothesis"
                        ]["reasoning"],

                    "supporting_evidence":
                        analysis[
                            "primary_hypothesis"
                        ].get(
                            "supporting_evidence",
                            []
                        )
                },

                "alternative_hypotheses":
                    analysis.get(
                        "alternative_hypotheses",
                        []
                    )
            }

        except Exception as exc:

            logger.exception(
                "Hypothesis generation failed"
            )

            primary = possible_causes[0]

            return {

                "primary_hypothesis": {

                    "cause":
                        primary.get(
                            "source",
                            "Unknown"
                        ),

                    "confidence":
                        primary.get(
                            "confidence",
                            0.0
                        ),

                    "reasoning":
                        (
                            "Fallback hypothesis "
                            "generated because "
                            "Gemini analysis "
                            "failed."
                        ),

                    "supporting_evidence":
                        primary.get(
                            "evidence",
                            []
                        )
                },

                "alternative_hypotheses": [

                    {
                        "cause":
                            cause.get(
                                "source",
                                "Unknown"
                            ),

                        "confidence":
                            cause.get(
                                "confidence",
                                0.0
                            ),

                        "reasoning":
                            (
                                "Alternative "
                                "hypothesis "
                                "derived from "
                                "correlation results."
                            ),

                        "supporting_evidence":
                            cause.get(
                                "evidence",
                                []
                            )
                    }

                    for cause in possible_causes[1:]
                ]
            }

"""class HypothesisService:

    async def analyze(
        self,
        possible_causes: list
    ):

        sorted_causes = sorted(
            possible_causes,
            key=lambda cause:
                cause["confidence"],
            reverse=True
        )

        primary = (
            sorted_causes[0]
        )

        primary_hypothesis = {
            "cause":
                primary["source"],

            "confidence":
                primary["confidence"]
        }

        alternatives = []

        for cause in sorted_causes[1:]:

            alternatives.append(
                {
                    "cause":
                        cause["source"],

                    "confidence":
                        cause["confidence"]
                }
            )

        return {
            "primary_hypothesis":
                primary_hypothesis,

            "alternative_hypotheses":
                alternatives
        }
"""