from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'AbuseFilter',
    _G.newver,
    'Allows specific behavior-based restrictions to be placed on wiki activity',
    'GPL-2.0-or-later',
  )

def post_build():
  mediawiki_post_build()
