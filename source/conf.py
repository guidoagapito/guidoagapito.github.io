# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Guido Agapito'
copyright = '2026, Guido Agapito'
author = 'Guido Agapito'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# Aggiungi l'estensione alla lista (se non c'è già)
extensions = [
    'sphinxcontrib.bibtex',
]

# Specifica il nome esatto del tuo file .bib (aggiungi questa riga in fondo al file)
bibtex_bibfiles = ['bibliography.bib']