# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from docutils import nodes
from ferrocene_spec.utils import is_fls_id
from ferrocene_spec.definitions import DefIdNode

def check(app, raise_error):
    for document in app.env.found_docs:
        doctree = app.env.get_doctree(document)
        if document in app.config.lint_no_paragraph_ids:
            check_does_not_have_ids(doctree, raise_error)
        else:
            check_has_ids(doctree, raise_error)


def check_has_ids(node, raise_error):
    is_paragraph = nodes.paragraph is type(node)

    if is_paragraph and nodes.section is type(node.parent):
        should_have_id(node, "paragraph", raise_error)
    elif is_paragraph and nodes.list_item is type(node.parent):
        should_have_id(node, "list item", raise_error)
    elif is_paragraph and nodes.entry is type(node.parent):
        if node.parent.parent.index(node.parent) == 0:
            should_have_id(node, "first cell of a table row", raise_error)
        else:
            should_not_have_id(
                node,
                "second or later cell of a table row",
                raise_error,
            )
    elif nodes.section is type(node):
        if not any(is_fls_id(name) for name in node["names"]):
            raise_error("section should have an id", location=node)
    else:
        should_not_have_id(node, type(node).__name__, raise_error)

    for child in node.children:
        check_has_ids(child, raise_error)


def check_does_not_have_ids(node, raise_error):
    if nodes.section is type(node):
        if any(is_fls_id(name) for name in node["names"]):
            raise_error("section should not have an id", location=node)
    else:
        should_not_have_id(node, type(node).__name__, raise_error)

    for child in node.children:
        check_does_not_have_ids(child, raise_error)


def should_have_id(node, what, raise_error):
    if any(is_definition(child) for child in node.children[1:]):
        raise_error(f"id in {what} is not the first element", location=node)
    elif not len(node.children) or not is_definition(node.children[0]):
        raise_error(f"{what} should have an id", location=node)


def should_not_have_id(node, what, raise_error):
    if any(is_definition(child) for child in node.children):
        raise_error(f"{what} should not have an id", location=node)


def is_definition(node):
    return (
        DefIdNode is type(node)
        and node["def_kind"] == "paragraph"
        and is_fls_id(node["def_id"])
    )
