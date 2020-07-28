import ntpath
import json
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


def generate_output(diff, prefix='', tab=''):
    output = []

    diff_types = ('same', 'children', 'diff', 'plus', 'minus')

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

    output.append(prefix + '{')
    for diff_type in diff_types:
        if diff_type not in diff:
            continue

        for key, value in diff[diff_type].items():
            if isinstance(value, bool):
                value = bool_values[value]

            if diff_type == 'diff':
                output.append(f'{tab}{diff_tabs["plus"]}{key}: {value[1]}')
                output.append(f'{tab}{diff_tabs["minus"]}{key}: {value[0]}')
            else:
                new_tab = tab + diff_tabs["same"]
                prefix = f'{tab}{diff_tabs[diff_type]}{key}: '
                if diff_type == 'children':
                    output.append(generate_output(
                        value, prefix=prefix, tab=new_tab))
                elif diff_type in ['same', 'plus', 'minus']:
                    if isinstance(value, Dict):
                        output.append(generate_output(
                            {'same': value}, prefix=prefix, tab=new_tab))
                    else:
                        output.append(
                            f'{tab}{diff_tabs[diff_type]}{key}: {value}')
    output.append(tab + '}')

    return '\n'.join(output)


def generate_plain_output(diff, keys=''):
    output = []

    diff_types = ('children', 'diff', 'plus', 'minus')

    diff_messages = {
        'plus': "Property '{}' was added with value: '{}'",
        'minus': "Property '{}' was removed",
        'diff': "Property '{}' was changed. From '{}' to '{}'",
    }

    for diff_type in diff_types:
        if diff_type not in diff:
            continue

        for key, value in diff[diff_type].items():
            current_key = f'{keys}.{key}'.lstrip('.')
            if diff_type == 'children':
                output.append(generate_plain_output(value, keys=current_key))
            else:
                if isinstance(value, Dict):
                    value = 'complex value'

                if diff_type == 'diff':
                    diff_data = [current_key, value[0], value[1]]
                elif diff_type == 'plus':
                    diff_data = [current_key, value]
                else:
                    diff_data = [current_key]

                output.append(diff_messages[diff_type].format(*diff_data))

    return '\n'.join(output)


def generate_json_output(diff):
    return json.dumps(diff, indent=4, sort_keys=True)
