import json
import os
from typing import Dict

import yaml


FILE_READERS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}


class FileLoadError(Exception):
    pass


def load_file(file_path: str) -> Dict:
    _, first_ext = os.path.splitext(file_path)
    with open(file_path, mode='r', encoding='utf8') as f:
        try:
            reader = FILE_READERS[first_ext]
        except KeyError:
            raise FileLoadError(f'Unsupported file extension `{first_ext}`')
        except FileNotFoundError:
            raise FileLoadError(f'File not found `{file_path}`')
        else:
            return reader(f)
