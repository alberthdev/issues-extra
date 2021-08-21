#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = '@alberthdev'
SITENAME = 'Issues'
SITEURL = ''

THEME = 'themes/bootstrap-next'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins', 'plugins/mdx_include', 'plugins/pelican-plugins']
PLUGINS = ['i18n_subsites']
STATIC_PATHS = ['libraries/colorbox']
BOOTSTRAP_THEME = "sandstone"
BANNER_ALL_PAGES = False
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_CATEGORIES_ON_MENU = False

SITE_URL = "https://alberthdev.github.io/issues-extra"

# FS hierarchy: https://github.com/getpelican/pelican/issues/686#issuecomment-48603981
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}/index.html'

READERS = {'html': None}

MARKDOWN = {
    'extensions': ['mdx_include', 'attr_list', 'fenced_code'],
    'extension_configs': {
        'mdx_include': {
            "base_path": "content"
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {}
    },
    'output_format': 'html5',
}

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('GitHub', 'https://github.com/alberthdev'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True