from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'Popups',
    _G.newver,
    'Displays popups when users hover over article links and footnote markers',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
