from lilaclib import *

def pre_build():
  aur_pre_build(maintainers='masterkorp')
  add_makedepends(["python2"])
