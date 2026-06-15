from app.correlation.scoring import (
    deployment_score
)


def test_recent_deployment():

    result = deployment_score(5)

    assert result == 0.8


def test_old_deployment():

    result = deployment_score(60)

    assert result == 0.1