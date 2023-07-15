from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'CodeMirror',
    _G.newver,
    'Provides syntax highlighting in wikitext editor',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
