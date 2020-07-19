import ntpath
import json

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
    diff = {
        'same': {},
        'diff': {},
        'plus': {},
        'minus': {},
    }
    for key, value in before.items():
        if key in after and value == after[key]:
            diff['same'][key] = value
        elif key in after and value != after[key]:
            diff['diff'][key] = [value, after[key]]
        else:
            diff['minus'][key] = value

    new_keys = after.keys() - before.keys()

    for key in new_keys:
        diff['plus'][key] = after[key]

    return diff


def print_diff(diff, prefix='', tab=''):
    diff_keys = ('same', 'diff', 'plus', 'minus')

    diff_tabs = {
        'plus': '    + ',
        'minus': '    - ',
        'same': '    ',
    }

    bool_values = {
        True: 'true',
        False: 'false',
    }

    print(prefix + '{')
    for key in diff_keys:
        for field, value in diff[key].items():
            if isinstance(value, bool):
                value = bool_values[value]
            if key != 'diff':
                print(f'{tab}{diff_tabs[key]}{field}: {value}')
            else:
                print(f'{tab}    + {field}: {value[1]}')
                print(f'{tab}    - {field}: {value[0]}')
    print(tab + '}')
