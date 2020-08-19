import json

from gendiff.renders import render, JSON_FORMAT, PRETTY_FORMAT, PLAIN_FORMAT
from tests.fixtures.fixtures import (
    diff_tree_no_need_order,
    pretty_render,
    plain_render,
    json_render
)


def test_pretty_render(diff_tree_no_need_order, pretty_render):
    assert render(diff_tree_no_need_order, PRETTY_FORMAT) == pretty_render


def test_plain_render(diff_tree_no_need_order, plain_render):
    assert render(diff_tree_no_need_order, PLAIN_FORMAT) == plain_render


def test_json_render(diff_tree_no_need_order, json_render):
    output = render(diff_tree_no_need_order, JSON_FORMAT)
    assert json.loads(output) == json.loads(json_render)
