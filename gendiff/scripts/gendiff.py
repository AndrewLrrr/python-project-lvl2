import argparse
import sys

from gendiff import utils


class FileExtensionError(Exception):
    pass


class FormatTypeError(Exception):
    pass


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('first_file')
        parser.add_argument('second_file')
        parser.add_argument('-f', '--format', help='set format of output')

        args = parser.parse_args()

        files_data = []

        format_ = args.format

        if format_ and format_ not in ('json', 'plain'):
            raise FormatTypeError(f'Format `{format_}` not allowed')

        for file_path in [args.first_file, args.second_file]:
            first_ext = utils.get_file_extension(file_path)
            if first_ext is None:
                raise FileExtensionError(
                    f'File extension is not specified in `{file_path}`')
            if first_ext == 'json':
                data = utils.read_json_file(file_path)
            elif first_ext in ['yml', 'yaml']:
                data = utils.read_yaml_file(file_path)
            else:
                raise FileExtensionError(
                    f'Unsupported extension `{first_ext}`')
            files_data.append(data)

        diff = utils.compare(*files_data)

        if format_ == 'plain':
            utils.print_diff_plain(diff)
        elif format_ == 'json':
            pass
        else:
            utils.print_diff(diff)

    except (FileExtensionError, FileNotFoundError, FormatTypeError) as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
