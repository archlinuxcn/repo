from lilaclib import *

def pre_build():
  add_depends(["ruby-rdoc"])
  update_pkgver_and_pkgrel(_G.newver)

