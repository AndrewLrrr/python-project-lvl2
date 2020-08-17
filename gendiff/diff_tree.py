from typing import Dict


NESTED = 'nested'
CHANGED = 'changed'
SAME = 'same'
ADDED = 'added'
REMOVED = 'removed'


def build_diff_tree(before: Dict, after: Dict) -> Dict:
    diff = {}

    for key in before.keys() & after.keys():
        if before[key] == after[key]:
            diff.setdefault(SAME, {})[key] = before[key]
        elif isinstance(before[key], Dict) and isinstance(after[key], Dict):
            diff.setdefault(NESTED, {})[key] = build_diff_tree(before[key], after[key])  # noqa: E501
        else:
            diff.setdefault(CHANGED, {})[key] = [before[key], after[key]]

    for key in before.keys() - after.keys():
        diff.setdefault(REMOVED, {})[key] = before[key]

    for key in after.keys() - before.keys():
        diff.setdefault(ADDED, {})[key] = after[key]

    return diff
