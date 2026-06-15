from app.models.incident import Incident


incident = Incident(
    incident_id="INC001",
    service="payment-service",
    severity="critical",
    timestamp="2026-05-31T10:00:00Z",
)

print(incident)
