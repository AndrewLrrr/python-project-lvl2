import json
from typing import Dict, Callable, Union

from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, SAME


DEFAULT_FORMAT = 'default'
JSON_FORMAT = 'json'
PLAIN_FORMAT = 'plain'


def render(diff: Dict, *, handler: Callable) -> str:
    return handler(diff)


def render_default_output(diff: Dict, prefix: str = '',
                          tab: str = '', inline: bool = False) -> str:
    output = []

    tabs = {
        NESTED: '    ',
        ADDED: '    + ',
        REMOVED: '    - ',
        SAME: '    ',
    }

    bool_values = {
        True: 'true',
        False: 'false',
    }

    if not inline:
        output.append(prefix + '{')

    for diff_node in (SAME, NESTED, CHANGED, ADDED, REMOVED):
        if diff_node not in diff:
            continue

        for key, value in diff[diff_node].items():
            if isinstance(value, bool):
                value = bool_values[value]

            if diff_node == CHANGED:
                output.append(render_default_output(
                            {ADDED: {key: value[1]}}, tab=tab, inline=True))
                output.append(render_default_output(
                            {REMOVED: {key: value[0]}}, tab=tab, inline=True))
            else:
                new_tab = tab + tabs[NESTED]
                prefix = f'{tab}{tabs[diff_node]}{key}: '
                if diff_node == NESTED:
                    output.append(render_default_output(
                        value, prefix=prefix, tab=new_tab))
                elif diff_node in [SAME, ADDED, REMOVED]:
                    if isinstance(value, Dict):
                        output.append(render_default_output(
                            {SAME: value}, prefix=prefix, tab=new_tab))
                    else:
                        output.append(
                            f'{tab}{tabs[diff_node]}{key}: {value}')

    if not inline:
        output.append(tab + '}')

    return '\n'.join(output)


def map_complex_value(value: Union[str, Dict]) -> str:
    if isinstance(value, Dict):
        return 'complex value'
    return value


def render_plain_output(diff: Dict, keys: str = '') -> str:
    output = []

    messages = {
        ADDED: "Property '{}' was added with value: '{}'",
        REMOVED: "Property '{}' was removed",
        CHANGED: "Property '{}' was changed. From '{}' to '{}'",
    }

    for diff_node in (NESTED, CHANGED, ADDED, REMOVED):
        if diff_node not in diff:
            continue

        for key, value in diff[diff_node].items():
            current_key = f'{keys}.{key}'.lstrip('.')
            if diff_node == NESTED:
                output.append(render_plain_output(value, keys=current_key))
            else:
                if diff_node == CHANGED:
                    diff_data = [current_key, value[0], value[1]]
                elif diff_node == ADDED:
                    diff_data = [current_key, value]
                else:
                    diff_data = [current_key]

                output.append(messages[diff_node].format(
                    *map(map_complex_value, diff_data))
                )

    return '\n'.join(output)


def render_json_output(diff: Dict) -> str:
    return json.dumps(diff, indent=4)
