from lilaclib import *

def pre_build():
  aur_pre_build()
  add_makedepends(['lxqt-build-tools-git'])

post_build = aur_post_build
