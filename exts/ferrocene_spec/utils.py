# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Ferrocene Developers

from docutils import nodes

def is_fls_id(id):
    """
    Annotations in the Ferrocene Language Specification have ids starting with 'fls_'.
    However, Sphinx (and in particular Myst) normalizes these to `fls-` on occassion.
    This function accepts either, but use `normalize_fls_id` to convert to `fls_`.
    """
    return id.startswith("fls-") or id.startswith("fls_")

def normalize_fls_id(id):
    """
    Normalize `fls_` or `fls-` annotations to the `fls_` form.
    """
    if id.startswith("fls-"):
        return id.replace("fls-", "fls_", 1)
    else:
        return id

def section_id_and_anchor(section):
    if "names" in section:
        try:
            id = [normalize_fls_id(name) for name in section["names"] if is_fls_id(name)][0]
        except IndexError:
            print(f"section names={repr(section['names'])}")
            raise NoSectionIdError()
    else:
        raise NoSectionIdError()

    if section.parent is not None and isinstance(section.parent, nodes.document):
        anchor = ""
    else:
        anchor = "#" + section["ids"][0]

    return id, anchor


class NoSectionIdError(RuntimeError):
    pass
