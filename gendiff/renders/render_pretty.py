from typing import Dict

from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, SAME


TABS = {
    NESTED: '    ',
    ADDED: '    + ',
    REMOVED: '    - ',
    SAME: '    ',
}

BOOL_VALUES = {
    True: 'true',
    False: 'false',
}


def render(diff: Dict, tab: str = '', inline: bool = False) -> str:
    output = []

    if not inline:
        output.append('{')

    for diff_node in sorted(diff.keys()):
        for key, value in diff[diff_node].items():
            if isinstance(value, bool):
                value = BOOL_VALUES[value]

            if diff_node == CHANGED:
                value = {
                    ADDED: {key: value[1]},
                    REMOVED: {key: value[0]},
                }
                output.append(render(value, tab=tab, inline=True))
            else:
                new_tab = tab + TABS[NESTED]
                if diff_node == NESTED:
                    value = render(value, tab=new_tab)
                elif isinstance(value, Dict):
                    value = render({SAME: value}, tab=new_tab)
                output.append(f'{tab}{TABS[diff_node]}{key}: {value}')

    if not inline:
        output.append(tab + '}')

    return '\n'.join(output)
