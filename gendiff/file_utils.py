import json
from typing import Dict

import yaml


JSON_EXTENSION = '.json'
YAML_EXTENSION = '.yaml'
YML_EXTENSION = '.yml'


def read_json_file(path_file: str) -> Dict:
    with open(path_file, mode='r', encoding='utf8') as f:
        return json.load(f)


def read_yaml_file(path_file: str) -> Dict:
    with open(path_file, mode='r', encoding='utf8') as f:
        return yaml.safe_load(f)
