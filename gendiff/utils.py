import ntpath
import json
import sys
from typing import Dict

import yaml


def read_json_file(path_file):
    with open(path_file, mode='r', encoding='utf8') as f:
        return json.load(f)


def read_yaml_file(path_file):
    with open(path_file, mode='r', encoding='utf8') as f:
        return yaml.safe_load(f)


def get_file_extension(file_path):
    file = ntpath.basename(file_path)
    try:
        return file.split('.')[1]
    except IndexError:
        pass


def compare(before, after):
    diff = {}
    for key, value in before.items():
        if key in after and value == after[key]:
            diff.setdefault('same', {})[key] = value
        elif key in after and value != after[key]:
            if isinstance(value, Dict):
                diff.setdefault('children', {})[key] = compare(
                    value, after[key]
                )
            else:
                diff.setdefault('diff', {})[key] = [value, after[key]]
        else:
            diff.setdefault('minus', {})[key] = value

    new_keys = after.keys() - before.keys()

    for key in new_keys:
        diff.setdefault('plus', {})[key] = after[key]

    return diff


def print_diff(diff, prefix='', tab='', output=sys.stdout):
    diff_keys = ('same', 'children', 'diff', 'plus', 'minus')

    diff_tabs = {
        'children': '    ',
        'plus': '    + ',
        'minus': '    - ',
        'same': '    ',
    }

    bool_values = {
        True: 'true',
        False: 'false',
    }

    output.write(prefix + '{\n')
    for key in diff_keys:
        if key not in diff:
            continue
        for field, value in diff[key].items():
            if isinstance(value, bool):
                value = bool_values[value]
            if key == 'diff':
                output.write(f'{tab}{diff_tabs["plus"]}{field}: {value[1]}\n')
                output.write(f'{tab}{diff_tabs["minus"]}{field}: {value[0]}\n')
            else:
                new_tab = tab + diff_tabs["same"]
                prefix = f'{tab}{diff_tabs[key]}{field}: '
                if key == 'children':
                    print_diff(
                        value, prefix=prefix, tab=new_tab, output=output)
                elif key in ['same', 'plus', 'minus']:
                    if isinstance(value, Dict):
                        print_diff(
                            {'same': value},
                            prefix=prefix,
                            tab=new_tab,
                            output=output,
                        )
                    else:
                        output.write(
                            f'{tab}{diff_tabs[key]}{field}: {value}\n')
    output.write(tab + '}\n')
