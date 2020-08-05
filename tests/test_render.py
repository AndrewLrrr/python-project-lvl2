import json

from gendiff.render import (
    render,
    render_default_output,
    render_plain_output,
    render_json_output,
)

from tests.fixtures.fixtures import (
    diff_tree_no_need_order,
    default_render,
    plain_render,
    json_render
)


def test_default_render(diff_tree_no_need_order, default_render):
    assert render(diff_tree_no_need_order, handler=render_default_output) == default_render


def test_plain_render(diff_tree_no_need_order, plain_render):
    assert render(diff_tree_no_need_order, handler=render_plain_output) == plain_render


def test_json_render(diff_tree_no_need_order, json_render):
    output = render(diff_tree_no_need_order, handler=render_json_output)
    assert json.loads(output) == json.loads(json_render)
