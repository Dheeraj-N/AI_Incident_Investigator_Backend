from app.correlation.scoring import (
    weighted_confidence
)

print(
    weighted_confidence(
        0.8,
        0.8,
        0.95
    )
)