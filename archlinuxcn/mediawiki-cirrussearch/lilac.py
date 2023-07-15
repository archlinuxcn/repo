from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'CirrusSearch',
    _G.newver,
    'Implements searching for MediaWiki using Elasticsearch',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
