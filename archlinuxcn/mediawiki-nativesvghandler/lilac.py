from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'NativeSvgHandler',
    _G.newver,
    'Serves SVG images directly to clients',
    'GPL3',
  )

def post_build():
  mediawiki_post_build()
