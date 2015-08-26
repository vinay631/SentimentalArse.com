#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SentimenalArse'
SITENAME = u'Sentimental Arse'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = './pelican-themes/greda-theme/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'liquid_tags.notebook', 'pelican_dynamic', 'render_math']

GOOGLE_ANALYTICS = 'UA-66840105-1'
DOMAIN = 'sentimentalarse.com'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
