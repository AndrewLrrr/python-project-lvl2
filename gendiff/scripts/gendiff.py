import os
import sys

from gendiff.arg_parser import arg_parse
from gendiff.diff_tree import build_diff_tree
from gendiff.file_utils import (
    JSON_EXTENSION,
    YML_EXTENSION,
    YAML_EXTENSION,
    read_json_file,
    read_yaml_file,
)
from gendiff.render import (
    DEFAULT_FORMAT,
    PLAIN_FORMAT,
    JSON_FORMAT,
    render,
    render_default_output,
    render_plain_output,
    render_json_output,
)


FORMAT_HANDLERS = {
    DEFAULT_FORMAT: render_default_output,
    PLAIN_FORMAT: render_plain_output,
    JSON_FORMAT: render_json_output,
}


FILE_READERS = {
    JSON_EXTENSION: read_json_file,
    YML_EXTENSION: read_yaml_file,
    YAML_EXTENSION: read_yaml_file,
}


class FileExtensionError(Exception):
    pass


def main():
    args = arg_parse()

    try:
        files_data = []
        for file_path in (args.first_file, args.second_file):
            _, first_ext = os.path.splitext(file_path)
            try:
                files_data.append(FILE_READERS[first_ext](file_path))
            except KeyError:
                raise FileExtensionError(f'Unsupported file extension `{first_ext}`')  # noqa: E501
    except (FileExtensionError, FileNotFoundError) as e:
        print(e, file=sys.stderr)
    else:
        diff = build_diff_tree(*files_data)
        output = render(diff, handler=FORMAT_HANDLERS[args.format])
        print(output)


if __name__ == '__main__':
    main()
