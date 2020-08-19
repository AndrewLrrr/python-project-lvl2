import os

from gendiff.file_utils import load_file
from tests.fixtures import diff_tree, content_before


def test_load_json_file(content_before):
    dirname = os.path.dirname(__file__)
    assert load_file(os.path.join(dirname, 'fixtures/files/before.json')) == content_before


def test_load_yaml_file(content_before):
    dirname = os.path.dirname(__file__)
    assert load_file(os.path.join(dirname, 'fixtures/files/before.yaml')) == content_before
