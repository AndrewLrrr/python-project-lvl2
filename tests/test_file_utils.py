import os

from gendiff.file_utils import read_json_file, read_yaml_file
from tests.fixtures.fixtures import diff_tree, content_before, content_after


def test_read_json_file(content_before, content_after):
    dirname = os.path.dirname(__file__)
    assert read_json_file(os.path.join(dirname, 'fixtures/files/before.json')) == content_before
    assert read_json_file(os.path.join(dirname, 'fixtures/files/after.json')) == content_after


def test_read_yaml_file(content_before, content_after):
    dirname = os.path.dirname(__file__)
    assert read_yaml_file(os.path.join(dirname, 'fixtures/files/before.yaml')) == content_before
    assert read_yaml_file(os.path.join(dirname, 'fixtures/files/after.yaml')) == content_after
