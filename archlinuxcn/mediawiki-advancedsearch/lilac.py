from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'AdvancedSearch',
    _G.newver,
    'Creating an improved advanced search interface for MediaWiki and aiming for a user friendly integration of search keywords',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
