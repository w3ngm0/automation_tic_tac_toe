# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------
import os 
import sys
# Add the path to your modules to sys.path
sys.path.insert(0, os.path.abspath('..'))

# Example intersphinx mapping 
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'sphinx': ('https://www.sphinx-doc-org/en/master/', None)
                       }

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tic-tac-bug-toe'
copyright = '2024, Kelden Wangmo'
author = 'Kelden Wangmo'
release = '23/03/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']

templates_path = ['_templates']
exclude_patterns = []

language = 'english'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
