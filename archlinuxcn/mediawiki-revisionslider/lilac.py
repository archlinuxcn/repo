from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'RevisionSlider',
    _G.newver,
    'Adds a slider interface to the diff view allowing to easily move between revisions',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
