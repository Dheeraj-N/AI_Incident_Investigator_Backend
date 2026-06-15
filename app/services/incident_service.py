from app.correlation.engine import CorrelationEngine

from app.services.evidence_service import EvidenceService

from app.services.ai_summary_service import AISummaryService

from app.services.hypothesis_service import (
    HypothesisService
)

from app.services.ai_investigation_service import (
    AIInvestigationService
)

from app.timeline.builder import (
    TimelineBuilder
)

from app.services.recommendation_service import (
    RecommendationService
)

from app.services.executive_report_service import (
    ExecutiveReportService
)

from app.core.logger import logger

_report_cache: dict[str, dict] = {}


class IncidentService:
    def __init__(self):

        self.evidence_service = EvidenceService()

        self.correlation_engine = CorrelationEngine()

        self.ai_summary_service = AISummaryService()

        self.timeline_builder = (TimelineBuilder())

    async def investigate(self, incident_id: str):

        logger.info(f"Starting investigation for {incident_id}")

        logger.info("Collecting evidence")

        evidence = await self.evidence_service.collect(incident_id)

        logger.info("Running correlation engine")

        correlation_result = self.correlation_engine.investigate(evidence)

        timeline = (
    self.timeline_builder
    .build(
        evidence
    )
)
        ai_investigation_service = (
    AIInvestigationService()
)
        analysis = (
    await ai_investigation_service
    .analyze(
        correlation_result,
        timeline
    )
)
        hypothesis_service = (
    HypothesisService()
)
        hypothesis_analysis = (
    await hypothesis_service
    .analyze(
        timeline,
        correlation_result[
            "possible_causes"
        ]
    )
)
        

        logger.info("Generating summary")

        summary = (
    await self.ai_summary_service
    .generate_summary(
        correlation_result, timeline
    )
)
        recommendation_service = (
    RecommendationService()
)
        recommendations = (
    recommendation_service.generate(
        correlation_result[
            "possible_causes"
        ]
    )
)

        executive_report_service = (
    ExecutiveReportService()
)
        root_cause = (
    analysis[
        "root_cause"
    ]
)

        executive_report = (
    await executive_report_service
    .generate(
        timeline,
        root_cause,
        recommendations,
        analysis
    )
)
        
        report = {
    "incident_id": incident_id,

    "timeline": timeline,

    "possible_causes":
        correlation_result[
            "possible_causes"
        ],

    "ai_analysis":
    analysis, 

    "hypothesis_analysis":
    hypothesis_analysis,

    "ai_summary":
        summary["summary"],

    "recommendations": recommendations, 

    "executive_report":
    executive_report
}

        _report_cache[incident_id] = report
        return report

    @staticmethod
    def get_cached_report(incident_id: str) -> dict | None:
        return _report_cache.get(incident_id)
