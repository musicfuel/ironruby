# -*- coding: utf-8 -*-
"""
    sphinx.quickstart
    ~~~~~~~~~~~~~~~~~

    Quickly setup documentation source to work with Sphinx.

    :copyright: Copyright 2007-2009 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import sys, os, time
from os import path

TERM_ENCODING = getattr(sys.stdin, 'encoding', None)

from sphinx.util import make_filename
from sphinx.util.console import purple, bold, red, turquoise, \
     nocolor, color_terminal
from sphinx.util import texescape


PROMPT_PREFIX = '> '

QUICKSTART_CONF = '''\
# -*- coding: utf-8 -*-
#
# %(project)s documentation build configuration file, created by
# sphinx-quickstart on %(now)s.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [%(extensions)s]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['%(dot)stemplates']

# The suffix of source filenames.
source_suffix = '%(suffix)s'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = '%(master_str)s'

# General information about the project.
project = u'%(project_str)s'
copyright = u'%(copyright_str)s'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '%(version_str)s'
# The full version, including alpha/beta/rc tags.
release = '%(release_str)s'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%%B %%d, %%Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = [%(exclude_trees)s]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['%(dot)sstatic']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%%b %%d, %%Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = '%(project_fn)sdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('%(master_str)s', '%(project_fn)s.tex', u'%(project_doc_texescaped_str)s',
   u'%(author_texescaped_str)s', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
'''

INTERSPHINX_CONFIG = '''

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
'''

MASTER_FILE = '''\
.. %(project)s documentation master file, created by
   sphinx-quickstart on %(now)s.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to %(project)s's documentation!
===========%(underline)s=================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

'''

MAKEFILE = '''\
# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = %(rbuilddir)s

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) \
$(SPHINXOPTS) %(rsrcdir)s

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes \
linkcheck doctest

help:
\t@echo "Please use \\`make <target>' where <target> is one of"
\t@echo "  html      to make standalone HTML files"
\t@echo "  dirhtml   to make HTML files named index.html in directories"
\t@echo "  pickle    to make pickle files"
\t@echo "  json      to make JSON files"
\t@echo "  htmlhelp  to make HTML files and a HTML help project"
\t@echo "  qthelp    to make HTML files and a qthelp project"
\t@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
\t@echo "  changes   to make an overview of all changed/added/deprecated items"
\t@echo "  linkcheck to check all external links for integrity"
\t@echo "  doctest   to run all doctests embedded in the documentation \
(if enabled)"

clean:
\t-rm -rf $(BUILDDIR)/*

html:
\t$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
\t@echo
\t@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
\t$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
\t@echo
\t@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

pickle:
\t$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
\t@echo
\t@echo "Build finished; now you can process the pickle files."

json:
\t$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
\t@echo
\t@echo "Build finished; now you can process the JSON files."

htmlhelp:
\t$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
\t@echo
\t@echo "Build finished; now you can run HTML Help Workshop with the" \\
\t      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
\t$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
\t@echo
\t@echo "Build finished; now you can run "qcollectiongenerator" with the" \\
\t      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
\t@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/%(project_fn)s.qhcp"
\t@echo "To view the help file:"
\t@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/%(project_fn)s.qhc"

latex:
\t$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
\t@echo
\t@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
\t@echo "Run \\`make all-pdf' or \\`make all-ps' in that directory to" \\
\t      "run these through (pdf)latex."

changes:
\t$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
\t@echo
\t@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
\t$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
\t@echo
\t@echo "Link check complete; look for any errors in the above output " \\
\t      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
\t$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
\t@echo "Testing of doctests in the sources finished, look at the " \\
\t      "results in $(BUILDDIR)/doctest/output.txt."
'''

BATCHFILE = '''\
@ECHO OFF

REM Command file for Sphinx documentation

set SPHINXBUILD=sphinx-build
set BUILDDIR=%(rbuilddir)s
set ALLSPHINXOPTS=-d %%BUILDDIR%%/doctrees %%SPHINXOPTS%% %(rsrcdir)s
if NOT "%%PAPER%%" == "" (
\tset ALLSPHINXOPTS=-D latex_paper_size=%%PAPER%% %%ALLSPHINXOPTS%%
)

if "%%1" == "" goto help

if "%%1" == "help" (
\t:help
\techo.Please use `make ^<target^>` where ^<target^> is one of
\techo.  html      to make standalone HTML files
\techo.  dirhtml   to make HTML files named index.html in directories
\techo.  pickle    to make pickle files
\techo.  json      to make JSON files
\techo.  htmlhelp  to make HTML files and a HTML help project
\techo.  qthelp    to make HTML files and a qthelp project
\techo.  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter
\techo.  changes   to make an overview over all changed/added/deprecated items
\techo.  linkcheck to check all external links for integrity
\techo.  doctest   to run all doctests embedded in the documentation if enabled
\tgoto end
)

if "%%1" == "clean" (
\tfor /d %%%%i in (%%BUILDDIR%%\*) do rmdir /q /s %%%%i
\tdel /q /s %%BUILDDIR%%\*
\tgoto end
)

if "%%1" == "html" (
\t%%SPHINXBUILD%% -b html %%ALLSPHINXOPTS%% %%BUILDDIR%%/html
\techo.
\techo.Build finished. The HTML pages are in %%BUILDDIR%%/html.
\tgoto end
)

if "%%1" == "dirhtml" (
\t%%SPHINXBUILD%% -b dirhtml %%ALLSPHINXOPTS%% %%BUILDDIR%%/dirhtml
\techo.
\techo.Build finished. The HTML pages are in %%BUILDDIR%%/dirhtml.
\tgoto end
)

if "%%1" == "pickle" (
\t%%SPHINXBUILD%% -b pickle %%ALLSPHINXOPTS%% %%BUILDDIR%%/pickle
\techo.
\techo.Build finished; now you can process the pickle files.
\tgoto end
)

if "%%1" == "json" (
\t%%SPHINXBUILD%% -b json %%ALLSPHINXOPTS%% %%BUILDDIR%%/json
\techo.
\techo.Build finished; now you can process the JSON files.
\tgoto end
)

if "%%1" == "htmlhelp" (
\t%%SPHINXBUILD%% -b htmlhelp %%ALLSPHINXOPTS%% %%BUILDDIR%%/htmlhelp
\techo.
\techo.Build finished; now you can run HTML Help Workshop with the ^
.hhp project file in %%BUILDDIR%%/htmlhelp.
\tgoto end
)

if "%%1" == "qthelp" (
\t%%SPHINXBUILD%% -b qthelp %%ALLSPHINXOPTS%% %%BUILDDIR%%/qthelp
\techo.
\techo.Build finished; now you can run "qcollectiongenerator" with the ^
.qhcp project file in %%BUILDDIR%%/qthelp, like this:
\techo.^> qcollectiongenerator %%BUILDDIR%%\\qthelp\\%(project_fn)s.qhcp
\techo.To view the help file:
\techo.^> assistant -collectionFile %%BUILDDIR%%\\qthelp\\%(project_fn)s.ghc
\tgoto end
)

if "%%1" == "latex" (
\t%%SPHINXBUILD%% -b latex %%ALLSPHINXOPTS%% %%BUILDDIR%%/latex
\techo.
\techo.Build finished; the LaTeX files are in %%BUILDDIR%%/latex.
\tgoto end
)

if "%%1" == "changes" (
\t%%SPHINXBUILD%% -b changes %%ALLSPHINXOPTS%% %%BUILDDIR%%/changes
\techo.
\techo.The overview file is in %%BUILDDIR%%/changes.
\tgoto end
)

if "%%1" == "linkcheck" (
\t%%SPHINXBUILD%% -b linkcheck %%ALLSPHINXOPTS%% %%BUILDDIR%%/linkcheck
\techo.
\techo.Link check complete; look for any errors in the above output ^
or in %%BUILDDIR%%/linkcheck/output.txt.
\tgoto end
)

if "%%1" == "doctest" (
\t%%SPHINXBUILD%% -b doctest %%ALLSPHINXOPTS%% %%BUILDDIR%%/doctest
\techo.
\techo.Testing of doctests in the sources finished, look at the ^
results in %%BUILDDIR%%/doctest/output.txt.
\tgoto end
)

:end
'''


def mkdir_p(dir):
    if path.isdir(dir):
        return
    os.makedirs(dir)


class ValidationError(Exception):
    """Raised for validation errors."""

def is_path(x):
    if path.exists(x) and not path.isdir(x):
        raise ValidationError("Please enter a valid path name.")
    return x

def nonempty(x):
    if not x:
        raise ValidationError("Please enter some text.")
    return x

def choice(*l):
    def val(x):
        if x not in l:
            raise ValidationError('Please enter one of %s.' % ', '.join(l))
        return x
    return val

def boolean(x):
    if x.upper() not in ('Y', 'YES', 'N', 'NO'):
        raise ValidationError("Please enter either 'y' or 'n'.")
    return x.upper() in ('Y', 'YES')

def suffix(x):
    if not (x[0:1] == '.' and len(x) > 1):
        raise ValidationError("Please enter a file suffix, "
                              "e.g. '.rst' or '.txt'.")
    return x

def ok(x):
    return x


def do_prompt(d, key, text, default=None, validator=nonempty):
    while True:
        if default:
            prompt = purple(PROMPT_PREFIX + '%s [%s]: ' % (text, default))
        else:
            prompt = purple(PROMPT_PREFIX + text + ': ')
        x = raw_input(prompt)
        if default and not x:
            x = default
        if x.decode('ascii', 'replace').encode('ascii', 'replace') != x:
            if TERM_ENCODING:
                x = x.decode(TERM_ENCODING)
            else:
                print turquoise('* Note: non-ASCII characters entered '
                                'and terminal encoding unknown -- assuming '
                                'UTF-8 or Latin-1.')
                try:
                    x = x.decode('utf-8')
                except UnicodeDecodeError:
                    x = x.decode('latin1')
        try:
            x = validator(x)
        except ValidationError, err:
            print red('* ' + str(err))
            continue
        break
    d[key] = x


def inner_main(args):
    d = {}
    texescape.init()

    if not color_terminal():
        nocolor()

    print bold('Welcome to the Sphinx quickstart utility.')
    print '''
Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).'''

    print '''
Enter the root path for documentation.'''
    do_prompt(d, 'path', 'Root path for the documentation', '.', is_path)

    while path.isfile(path.join(d['path'], 'conf.py')) or \
          path.isfile(path.join(d['path'], 'source', 'conf.py')):
        print
        print bold('Error: an existing conf.py has been found in the '
                   'selected root path.')
        print 'sphinx-quickstart will not overwrite existing Sphinx projects.'
        print
        do_prompt(d, 'path', 'Please enter a new root path (or just Enter '
                  'to exit)', '', is_path)
        if not d['path']:
            sys.exit(1)

    print '''
You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.'''
    do_prompt(d, 'sep', 'Separate source and build directories (y/N)', 'n',
              boolean)

    print '''
Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.'''
    do_prompt(d, 'dot', 'Name prefix for templates and static dir', '_', ok)

    print '''
The project name will occur in several places in the built documentation.'''
    do_prompt(d, 'project', 'Project name')
    do_prompt(d, 'author', 'Author name(s)')
    print '''
Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
just set both to the same value.'''
    do_prompt(d, 'version', 'Project version')
    do_prompt(d, 'release', 'Project release', d['version'])
    print '''
The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.'''
    do_prompt(d, 'suffix', 'Source file suffix', '.rst', suffix)
    print '''
One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.'''
    do_prompt(d, 'master', 'Name of your master document (without suffix)',
              'index')

    while path.isfile(path.join(d['path'], d['master']+d['suffix'])) or \
          path.isfile(path.join(d['path'], 'source', d['master']+d['suffix'])):
        print
        print bold('Error: the master file %s has already been found in the '
                   'selected root path.' % (d['master']+d['suffix']))
        print 'sphinx-quickstart will not overwrite the existing file.'
        print
        do_prompt(d, 'master', 'Please enter a new file name, or rename the '
                  'existing file and press Enter', d['master'])

    print '''
Please indicate if you want to use one of the following Sphinx extensions:'''
    do_prompt(d, 'ext_autodoc', 'autodoc: automatically insert docstrings '
              'from modules (y/N)', 'n', boolean)
    do_prompt(d, 'ext_doctest', 'doctest: automatically test code snippets '
              'in doctest blocks (y/N)', 'n', boolean)
    do_prompt(d, 'ext_intersphinx', 'intersphinx: link between Sphinx '
              'documentation of different projects (y/N)', 'n', boolean)
    do_prompt(d, 'ext_todo', 'todo: write "todo" entries '
              'that can be shown or hidden on build (y/N)', 'n', boolean)
    do_prompt(d, 'ext_coverage', 'coverage: checks for documentation '
              'coverage (y/N)', 'n', boolean)
    do_prompt(d, 'ext_pngmath', 'pngmath: include math, rendered '
              'as PNG images (y/N)', 'n', boolean)
    do_prompt(d, 'ext_jsmath', 'jsmath: include math, rendered in the '
              'browser by JSMath (y/N)', 'n', boolean)
    if d['ext_pngmath'] and d['ext_jsmath']:
        print '''Note: pngmath and jsmath cannot be enabled at the same time.
pngmath has been deselected.'''
    do_prompt(d, 'ext_ifconfig', 'ifconfig: conditional inclusion of '
              'content based on config values (y/N)', 'n', boolean)
    print '''
A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.'''
    do_prompt(d, 'makefile', 'Create Makefile? (Y/n)', 'y', boolean)
    do_prompt(d, 'batchfile', 'Create Windows command file? (Y/n)',
              'y', boolean)

    d['project_fn'] = make_filename(d['project'])
    d['now'] = time.asctime()
    d['underline'] = len(d['project']) * '='
    d['extensions'] = ', '.join(
        repr('sphinx.ext.' + name)
        for name in ('autodoc', 'doctest', 'intersphinx', 'todo', 'coverage',
                     'pngmath', 'jsmath', 'ifconfig')
        if d['ext_' + name])
    d['copyright'] = time.strftime('%Y') + ', ' + d['author']
    d['author_texescaped'] = unicode(d['author']).\
                             translate(texescape.tex_escape_map)
    d['project_doc'] = d['project'] + ' Documentation'
    d['project_doc_texescaped'] = unicode(d['project'] + ' Documentation').\
                                  translate(texescape.tex_escape_map)

    # escape backslashes and single quotes in strings that are put into
    # a Python string literal
    for key in ('project', 'copyright', 'author_texescaped',
                'project_doc_texescaped', 'version', 'release', 'master'):
        d[key + '_str'] = d[key].replace('\\', '\\\\').replace("'", "\\'")

    if not path.isdir(d['path']):
        mkdir_p(d['path'])

    srcdir = d['sep'] and path.join(d['path'], 'source') or d['path']

    mkdir_p(srcdir)
    if d['sep']:
        builddir = path.join(d['path'], 'build')
        d['exclude_trees'] = ''
    else:
        builddir = path.join(srcdir, d['dot'] + 'build')
        d['exclude_trees'] = repr(d['dot'] + 'build')
    mkdir_p(builddir)
    mkdir_p(path.join(srcdir, d['dot'] + 'templates'))
    mkdir_p(path.join(srcdir, d['dot'] + 'static'))

    conf_text = QUICKSTART_CONF % d
    if d['ext_intersphinx']:
        conf_text += INTERSPHINX_CONFIG

    f = open(path.join(srcdir, 'conf.py'), 'w')
    f.write(conf_text.encode('utf-8'))
    f.close()

    masterfile = path.join(srcdir, d['master'] + d['suffix'])
    f = open(masterfile, 'w')
    f.write((MASTER_FILE % d).encode('utf-8'))
    f.close()

    if d['makefile']:
        d['rsrcdir'] = d['sep'] and 'source' or '.'
        d['rbuilddir'] = d['sep'] and 'build' or d['dot'] + 'build'
        f = open(path.join(d['path'], 'Makefile'), 'w')
        f.write((MAKEFILE % d).encode('utf-8'))
        f.close()

    if d['batchfile']:
        d['rsrcdir'] = d['sep'] and 'source' or '.'
        d['rbuilddir'] = d['sep'] and 'build' or d['dot'] + 'build'
        f = open(path.join(d['path'], 'make.bat'), 'w')
        f.write((BATCHFILE % d).encode('utf-8'))
        f.close()

    print
    print bold('Finished: An initial directory structure has been created.')
    print '''
You should now populate your master file %s and create other documentation
source files. ''' % masterfile + ((d['makefile'] or d['batchfile']) and '''\
Use the Makefile to build the docs, like so:
   make builder
''' or '''\
Use the sphinx-build command to build the docs, like so:
   sphinx-build -b builder %s %s
''' % (srcdir, builddir)) + '''\
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
'''


def main(argv=sys.argv):
    try:
        return inner_main(argv)
    except (KeyboardInterrupt, EOFError):
        print
        print '[Interrupted.]'
        return

