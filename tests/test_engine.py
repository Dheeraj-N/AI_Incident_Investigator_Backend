from app.correlation.engine import (
    CorrelationEngine
)


def test_investigation():

    engine = CorrelationEngine()

    result = engine.investigate(
        deploy_gap_minutes=5
    )

    assert (
        result["possible_causes"][0]
        ["confidence"]
        == 0.8
    )