import os
from unittest import TestCase

from gendiff.utils import (
    compare,
    generate_output,
    read_json_file,
    get_file_extension,
    read_yaml_file,
    generate_plain_output,
    generate_json_output,
)


class TestUtils(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_get_file_extension(self):
        self.assertEqual('json', get_file_extension('/path/to/file.json'))
        self.assertEqual('yaml', get_file_extension('/path/to/file.yaml'))
        self.assertIsNone(get_file_extension('/path/to/file'))

    def assert_diff_files(self, before, after):
        expected = {
            'children': {
                'common': {
                    'children': {
                        'group5': {
                            'children': {
                                'group6': {
                                    'diff': {
                                        'foo': ['bar', 'baz'],
                                    },
                                },
                            },
                        },
                    },
                    'diff': {
                        'setting3': [False, True],
                    },
                    'plus': {
                        'setting4': 'blah blah',
                        'setting5': {
                            'key5': 'value5',
                        },
                    },
                    'minus': {
                        'setting2': '200',
                        'setting6': {
                            'key': 'value',
                        },
                    },
                    'same': {
                        'setting1': 'Value 1',
                    },
                },
                'group1': {
                    'diff': {
                        'baz': ['bas', 'bars'],
                    },
                    'same': {
                        'foo': 'bar',
                    },
                },
            },
            'diff': {
                'timeout': [50, 20],
                'protocol': ['http', 'https'],
            },
            'plus': {
                'verbose': True,
                'format': 'json',
                'group3': {
                    'fee': '100500',
                },
            },
            'minus': {
                'proxy': '123.234.53.22',
                'group2': {
                    'abc': '12345',
                },
            },
            'same': {
                'host': 'hexlet.io',
            },
        }

        self.assertDictEqual(expected, compare(before, after))

    def test_compare_json_files(self):
        dirname = os.path.dirname(__file__)
        before = read_json_file(os.path.join(dirname, 'fixtures/before.json'))
        after = read_json_file(os.path.join(dirname, 'fixtures/after.json'))
        self.assert_diff_files(before, after)

    def test_compare_yaml_files(self):
        dirname = os.path.dirname(__file__)
        before = read_yaml_file(os.path.join(dirname, 'fixtures/before.yaml'))
        after = read_yaml_file(os.path.join(dirname, 'fixtures/after.yaml'))
        self.assert_diff_files(before, after)

    def assert_print(self, fn, fixture_file_path):
        diff = {
            'children': {
                'common': {
                    'children': {
                        'group5': {
                            'children': {
                                'group6': {
                                    'diff': {
                                        'foo': ['bar', 'baz'],
                                    },
                                },
                            },
                        },
                    },
                    'same': {
                        'setting1': 'Value 1',
                    },
                    'plus': {
                        'group3': {
                            'fee': '100500',
                        },
                    },
                    'minus': {
                        'group2': {
                            'abc': '12345',
                        },
                    },
                },
            },
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

        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, fixture_file_path)) as f:
            expected_output = f.read()

        self.assertEqual(expected_output, fn(diff))

    def test_generate_output(self):
        self.assert_print(generate_output, 'fixtures/expected.txt')

    def test_generate_plain_output(self):
        self.assert_print(generate_plain_output, 'fixtures/expected_plain.txt')

    def test_generate_json_output(self):
        self.assert_print(generate_json_output, 'fixtures/expected_json.json')
