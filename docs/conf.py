# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import sys
from shutil import copyfile

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sphinx_rtd_theme  # noqa: F401

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "otupy"
copyright = "2024, Matteo Repetto"
author = "Matteo Repetto <mattereppe@gmail.com>"


# -- General configuration ---------------------------------------------------

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx_copybutton",
    "sphinx_issues",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.autoprogram",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.spelling",
]

# Copy needed files from parent directory.
for filename in ["LICENSE", "CONTRIBUTING.md", "CHANGELOG.md"]:
    copyfile(f"../{filename}", f"./{filename}")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_favicon = "../logo.ico"
html_theme = "sphinx_rtd_theme"

#issues_github_path = "guard-project/lcp"

nitpick_ignore = [("any", "falcon.Request"), ("any", "falcon.Response")]
