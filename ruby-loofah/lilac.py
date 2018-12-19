
from lilaclib import *

def pre_build():
  add_makedepends(["ruby-rdoc"])
  add_depends(["ruby-crass"])
  update_pkgver_and_pkgrel(_G.newver)

