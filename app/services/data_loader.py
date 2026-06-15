import json

from pathlib import Path


BASE_DIR = Path(
    __file__
).parent.parent

MOCK_DIR = (
    BASE_DIR / "mock_data"
)


def load_json(
    filename: str
):
    with open(
        MOCK_DIR / filename
    ) as f:
        return json.load(f)