from app.services.data_loader import (
    load_json
)

data = load_json(
    "incidents.json"
)

print(data)