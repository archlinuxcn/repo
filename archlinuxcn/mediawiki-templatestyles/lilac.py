from lilaclib import *

def pre_build():
  mediawiki_pre_build(
    'TemplateStyles',
    _G.newver,
    'Allows for loading sanitized CSS stylesheets from a template',
    'GPL',
  )

def post_build():
  mediawiki_post_build()
