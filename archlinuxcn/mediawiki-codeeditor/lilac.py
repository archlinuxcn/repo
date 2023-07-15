from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'CodeEditor',
    _G.newver,
    'Provides a syntax-highlighting code editor for site & user JS, CSS and Lua pages, integrating with advanced edit toolbar',
    ['GPL', 'BSD-3-Clause'],
  )

def post_build():
  mediawiki_post_build()
