import argparse

from gendiff.render import DEFAULT_FORMAT, PLAIN_FORMAT, JSON_FORMAT


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        nargs='?',
        default=DEFAULT_FORMAT,
        choices=(DEFAULT_FORMAT, PLAIN_FORMAT, JSON_FORMAT),
        help='set format of output',
    )

    return parser.parse_args()
