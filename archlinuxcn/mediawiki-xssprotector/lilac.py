from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'XSSProtector',
    _G.newver,
    'Add an extra layer of defense against XSS',
    'GPL-2.0-or-later',
  )

def post_build():
  mediawiki_post_build()
