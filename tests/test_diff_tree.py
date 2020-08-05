from gendiff.diff_tree import build_diff_tree
from tests.fixtures.fixtures import diff_tree, content_before, content_after


def test_build_diff_tree(diff_tree, content_before, content_after):
    assert build_diff_tree(content_before, content_after) == diff_tree
