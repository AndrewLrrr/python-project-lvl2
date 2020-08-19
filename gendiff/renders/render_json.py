import json
from typing import Dict


def render(diff: Dict) -> str:
    return json.dumps(diff)
