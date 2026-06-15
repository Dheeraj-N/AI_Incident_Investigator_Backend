GET_INCIDENT = """
SELECT *
FROM incidents
WHERE incident_id = :incident_id
"""


GET_DEPLOYMENTS = """
SELECT *
FROM deployments
WHERE service = :service
"""


GET_METRICS = """
SELECT *
FROM metrics
WHERE service = :service
"""


GET_OUTAGES = """
SELECT *
FROM outages
"""
