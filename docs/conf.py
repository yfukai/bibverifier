"""Sphinx configuration."""
project = "Bibverifier"
author = "Yohsuke T. Fukai"
copyright = "2024, Yohsuke T. Fukai"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
