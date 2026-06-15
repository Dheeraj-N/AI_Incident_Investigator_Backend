from app.correlation.engine import CorrelationEngine


evidence = {
    "incident": {
        "incident_id": "INC-101",
        "service": "checkout-api",
        "severity": "SEV-1",
        "timestamp": "2026-06-04T14:13:00"
    },

    "deployments": [
        {
            "service": "checkout-api",
            "commit_sha": "abc123",
            "author": "john",
            "timestamp": "2026-06-04T14:05:00"
        }
    ],

    "metrics": [
        {
            "service": "checkout-api",
            "timestamp": "2026-06-04T14:12:00",
            "error_rate": 82,
            "latency_ms": 4200
        }
    ],

    "outages": [
        {
            "provider": "Stripe",
            "status": "degraded",
            "start_time": "2026-06-04T14:11:00",
            "end_time": "2026-06-04T14:30:00"
        }
    ]
}


engine = CorrelationEngine()

result = engine.investigate(evidence)

print(result)

"""from app.correlation.engine import CorrelationEngine

engine = CorrelationEngine()

result = engine.investigate(deploy_gap_minutes=5)

print(result)
"""