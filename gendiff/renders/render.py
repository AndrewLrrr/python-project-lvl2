from typing import Dict

from gendiff.renders import render_json, render_plain, render_pretty


JSON_FORMAT = 'json'
PLAIN_FORMAT = 'plain'
PRETTY_FORMAT = 'pretty'


RENDERS = {
    JSON_FORMAT: render_json,
    PLAIN_FORMAT: render_plain,
    PRETTY_FORMAT: render_pretty,
}


class RenderError(Exception):
    pass


def render(diff: Dict, render_format: str) -> str:
    try:
        handler = RENDERS[render_format]
    except KeyError:
        raise RenderError(f'Unsupported format `{render_format}`')
    else:
        return handler.render(diff)
