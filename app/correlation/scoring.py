def deployment_score(
    gap_minutes: int
) -> float:
    """
    Score deployment correlation
    based on time difference between
    deployment and incident.
    """

    if gap_minutes <= 10:
        return 0.80

    if gap_minutes <= 30:
        return 0.60

    if gap_minutes <= 60:
        return 0.40

    return 0.10


def metric_score(
    error_rate: int,
    latency_ms: int
) -> float:
    """
    Score based on system health metrics.
    """

    score = 0.0

    if error_rate > 70:
        score += 0.50

    if latency_ms > 3000:
        score += 0.30

    return min(score, 1.0)


def outage_score(
    status: str
) -> float:
    """
    Score based on third-party outage state.
    """

    if status == "degraded":
        return 0.95

    return 0.0


def weighted_confidence(
    deployment_score_value: float,
    metric_score_value: float,
    outage_score_value: float
) -> float:
    """
    Weighted confidence calculation.

    Deployment = 30%
    Metrics    = 40%
    Outages    = 30%
    """

    confidence = (
        deployment_score_value * 0.30
        + metric_score_value * 0.40
        + outage_score_value * 0.30
    )

    return round(confidence, 2)

"""def deployment_score(deploy_gap_minutes: int) -> float:

    if deploy_gap_minutes <= 10:
        return 0.8

    if deploy_gap_minutes <= 30:
        return 0.4

    return 0.1
"""