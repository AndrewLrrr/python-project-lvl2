import os

import pytest

from gendiff.diff_tree import ADDED, CHANGED, NESTED, REMOVED, SAME


@pytest.fixture
def diff_tree():
    return {
        NESTED: {
            'common': {
                NESTED: {
                    'group5': {
                        NESTED: {
                            'group6': {
                                CHANGED: {
                                    'foo': ['bar', 'baz'],
                                },
                            },
                        },
                    },
                },
                CHANGED: {
                    'setting3': [False, True],
                },
                ADDED: {
                    'setting4': 'blah blah',
                    'setting5': {
                        'key5': 'value5',
                    },
                },
                REMOVED: {
                    'setting2': '200',
                    'setting6': {
                        'key': 'value',
                    },
                },
                SAME: {
                    'setting1': 'Value 1',
                },
            },
            'group1': {
                CHANGED: {
                    'baz': ['bas', 'bars'],
                },
                SAME: {
                    'foo': 'bar',
                },
            },
        },
        CHANGED: {
            'timeout': [50, 20],
            'protocol': ['http', 'https'],
        },
        ADDED: {
            'verbose': True,
            'format': 'json',
            'group3': {
                'fee': '100500',
            },
        },
        REMOVED: {
            'proxy': '123.234.53.22',
            'group2': {
                'abc': '12345',
            },
        },
        SAME: {
            'host': 'hexlet.io',
        },
    }


@pytest.fixture
def diff_tree_no_need_order():
    return {
        NESTED: {
            'common': {
                NESTED: {
                    'group5': {
                        NESTED: {
                            'group6': {
                                CHANGED: {
                                    'foo': ['bar', 'baz'],
                                },
                            },
                        },
                    },
                },
                SAME: {
                    'setting1': 'Value 1',
                },
                ADDED: {
                    'group3': {
                        'fee': '100500',
                    },
                },
                REMOVED: {
                    'group2': {
                        'abc': '12345',
                    },
                },
            },
        },
        SAME: {
            'host': 'hexlet.io',
        },
        CHANGED: {
            'timeout': [50, 20],
        },
        ADDED: {
            'verbose': True,
        },
        REMOVED: {
            'proxy': '123.234.53.22',
        },
    }


@pytest.fixture
def content_before():
    return {'common': {'group5': {'group6': {'foo': 'bar'}},
                       'setting1': 'Value 1',
                       'setting2': '200',
                       'setting3': False,
                       'setting6': {'key': 'value'}},
            'group1': {'baz': 'bas', 'foo': 'bar'},
            'group2': {'abc': '12345'},
            'host': 'hexlet.io',
            'protocol': 'http',
            'proxy': '123.234.53.22',
            'timeout': 50}


@pytest.fixture
def content_after():
    return {'common': {'group5': {'group6': {'foo': 'baz'}},
                       'setting1': 'Value 1',
                       'setting3': True,
                       'setting4': 'blah blah',
                       'setting5': {'key5': 'value5'}},
            'format': 'json',
            'group1': {'baz': 'bars', 'foo': 'bar'},
            'group3': {'fee': '100500'},
            'host': 'hexlet.io',
            'protocol': 'https',
            'timeout': 20,
            'verbose': True}


@pytest.fixture
def pretty_render():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'files/expected.txt')) as f:
        yield f.read()


@pytest.fixture
def plain_render():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'files/expected_plain.txt')) as f:
        yield f.read()


@pytest.fixture
def json_render():
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'files/expected_json.json')) as f:
        yield f.read()
