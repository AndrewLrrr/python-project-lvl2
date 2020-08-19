from typing import Dict, Union

from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, SAME


MESSAGES = {
    ADDED: "Property '{}' was added with value: '{}'",
    REMOVED: "Property '{}' was removed",
    CHANGED: "Property '{}' was changed. From '{}' to '{}'",
}


def map_complex_value(value: Union[str, Dict]) -> str:
    if isinstance(value, Dict):
        return 'complex value'
    return value


def render(diff: Dict, keys: str = '') -> str:
    output = []

    for diff_node in sorted(diff.keys() - {SAME}):
        for key, value in diff[diff_node].items():
            current_key = f'{keys}.{key}'.lstrip('.')
            if diff_node == NESTED:
                output.append(render(value, keys=current_key))
            else:
                if diff_node == CHANGED:
                    diff_data = [current_key, value[0], value[1]]
                elif diff_node == ADDED:
                    diff_data = [current_key, value]
                else:
                    diff_data = [current_key]

                output.append(MESSAGES[diff_node].format(
                    *map(map_complex_value, diff_data))
                )

    return '\n'.join(output)
