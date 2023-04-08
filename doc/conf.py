# -*- coding: utf-8 -*-
#
# joblib documentation build configuration file, created by
# sphinx-quickstart on Thu Oct 23 16:36:51 2008.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# The contents of this file are pickled, so don't put values in the
# namespace that aren't pickleable (module imports are okay,
# they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

import joblib

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
# ys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.imgmath', 'numpydoc',
              'sphinx.ext.autosummary', 'sphinx.ext.coverage',
              'sphinx.ext.intersphinx', 'sphinx_gallery.gen_gallery']

autosummary_generate = True

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(
        sys.version_info), None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'distributed': ('https://distributed.readthedocs.io/en/latest/', None),
}

# sphinx-gallery configuration
sphinx_gallery_conf = {
    'default_thumb_file': '_static/joblib_logo_examples.png',
    'doc_module': 'joblib',
    'filename_pattern': '',
    'ignore_pattern': 'utils.py',
    'backreferences_dir': os.path.join('generated'),
    'reference_url': {
        'joblib': None}
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# ource_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'joblib'
copyright = '2008-2021, Joblib developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = joblib.__version__
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# anguage = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# oday = ''
# Else, today_fmt is used as the format for a strftime call.
# oday_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# nused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
# efault_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# dd_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# dd_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# how_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Avoid '+DOCTEST...' comments in the docs
trim_doctest_flags = True

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# tml_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# tml_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# tml_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# tml_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# tml_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# tml_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}


# Additional templates that should be rendered to pages, maps page names to
# template names.
# tml_additional_pages = {}

# If false, no module index is generated.
# tml_use_modindex = True

# If false, no index is generated.
# tml_use_index = True

# If true, the index is split into individual pages for each letter.
# tml_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
# tml_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# tml_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# tml_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'joblibdoc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
# atex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# atex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# document class [howto/manual]).
latex_documents = [
  ('index', 'joblib.tex', 'joblib Documentation',
   'Gael Varoquaux', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# atex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# atex_use_parts = False

# Additional stuff for the LaTeX preamble.
# atex_preamble = ''

# Documents to append as an appendix to all manuals.
# atex_appendices = []

# If false, no module index is generated.
# atex_use_modindex = True

html_theme = 'alabaster'

html_theme_options = {
    'logo': 'joblib_logo.svg',
    'github_repo': 'joblib/joblib',
    'github_button': 'true',
    'link': '#aa560c',
    'show_powered_by': 'false',
    # "relbarbgcolor": "#333",
    # "sidebarlinkcolor": "#e15617",
    # "sidebarbgcolor": "#000",
    # "sidebartextcolor": "#333",
    # "footerbgcolor": "#111",
    # "linkcolor": "#aa560c",
    # "headtextcolor": "#643200",
    # "codebgcolor": "#f5efe7",
}


##############################################################################
# Hack to copy the CHANGES.rst file
import shutil
try:
    shutil.copyfile('../CHANGES.rst', 'CHANGES.rst')
    shutil.copyfile('../README.rst', 'README.rst')
except IOError:
    pass
    # This fails during the testing, as the code is ran in a different
    # directory

numpydoc_show_class_members = False

suppress_warnings = ['image.nonlocal_uri']
