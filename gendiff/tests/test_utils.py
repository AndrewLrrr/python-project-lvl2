import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from gendiff.utils import (
    compare,
    print_diff,
    read_json_file,
    get_file_extension,
)


class TestUtils(TestCase):
    def test_get_file_extension(self):
        self.assertEqual('json', get_file_extension('/path/to/file.json'))
        self.assertEqual('yaml', get_file_extension('/path/to/file.yaml'))

        with self.assertRaises(Exception) as ctx:
            get_file_extension('/path/to/file')
            self.assertEqual(
                'File extension is not specified in `/path/to/file`',
                ctx.exception,
            )

    def test_compare_json_files(self):
        dirname = os.path.dirname(__file__)
        before = read_json_file(os.path.join(dirname, 'fixtures/before.json'))
        after = read_json_file(os.path.join(dirname, 'fixtures/after.json'))

        expected = {
            'diff': {
                'timeout': [50, 20],
                'protocol': ['http', 'https'],
            },
            'plus': {
                'verbose': True,
                'format': 'json',
            },
            'minus': {
                'proxy': '123.234.53.22',
            },
            'same': {
                'host': 'hexlet.io',
            },
        }

        self.assertDictEqual(expected, compare(before, after))

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_diff(self, mock_stdout):
        diff = {
            'same': {
                'host': 'hexlet.io',
            },
            'diff': {
                'timeout': [50, 20],
            },
            'plus': {
                'verbose': True,
            },
            'minus': {
                'proxy': '123.234.53.22',
            },
        }

        lines = [
            'host: hexlet.io',
            '+ timeout: 20',
            '- timeout: 50',
            '+ verbose: true',
            '- proxy: 123.234.53.22',
        ]

        expected = '{\n    ' + '\n    '.join(lines) + '\n}\n'

        print_diff(diff)

        self.assertEqual(expected, mock_stdout.getvalue())