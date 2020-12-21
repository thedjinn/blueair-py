# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys

# Add the parent directory to the module path
sys.path.insert(0, os.path.abspath(os.pardir))

# -- Project information -----------------------------------------------------

project = 'Blueair'
copyright = '2020, Emil Loer'
author = 'Emil Loer'

from blueair import __version__ as blueair_version

# The short X.Y version.
version = '.'.join(blueair_version.split('.')[:2])

# The full version, including alpha/beta/rc tags
release = blueair_version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]

# Sort members by the source order instead of alphabetically.
autodoc_member_order = 'bysource'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python3=('https://docs.python.org/3', None)
)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options = {
    "show_powered_by": False,
    "github_user": "thedjinn",
    "github_repo": "blueair-py",
    "github_banner": True,
    "show_related": False,
    "note_bg": "#FFF59C",
}

html_sidebars = {
    "index": [
        "sidebarintro.html",
        "localtoc.html",
        "sourcelink.html",
        "searchbox.html"
    ],
    "**": [
        "sidebarintro.html",
        "localtoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html"
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
