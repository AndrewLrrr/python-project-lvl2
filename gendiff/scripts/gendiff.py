import argparse
import sys

from gendiff.diff_tree import build_diff_tree
from gendiff.file_utils import load_file, FileLoadError
from gendiff.renders import render, PRETTY_FORMAT, RENDERS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        nargs='?',
        default=PRETTY_FORMAT,
        choices=sorted(RENDERS.keys()),
        help='set format of output',
    )

    args = parser.parse_args()

    try:
        files_data = []
        for file_path in (args.first_file, args.second_file):
            files_data.append(load_file(file_path))
    except FileLoadError as e:
        print(e, file=sys.stderr)
    else:
        diff = build_diff_tree(*files_data)
        output = render(diff, args.format)
        print(output)


if __name__ == '__main__':
    main()
