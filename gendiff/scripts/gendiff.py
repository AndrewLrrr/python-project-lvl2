import argparse
import sys

from gendiff import utils


class GenDiffError(Exception):
    pass


def json_handler(first_file, second_file):
    before = utils.read_json_file(first_file)
    after = utils.read_json_file(second_file)
    return utils.compare(before, after)


def yml_handler(first_file, second_file):
    return {}


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('first_file')
        parser.add_argument('second_file')
        parser.add_argument('-f', '--format', help='set format of output')

        args = parser.parse_args()

        first_ext = utils.get_file_extension(args.first_file)
        second_ext = utils.get_file_extension(args.second_file)

        if first_ext != second_ext:
            raise GenDiffError('File extension must be the same')

        if first_ext == 'json':
            diff = json_handler(args.first_file, args.second_file)
        elif first_ext == 'yml':
            diff = yml_handler(args.first_file, args.second_file)
        else:
            raise GenDiffError(f'Unsupported extension `{first_ext}`')
        utils.print_diff(diff)
    except (GenDiffError, utils.FileExtensionError, FileNotFoundError) as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
