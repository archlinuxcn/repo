
from lilaclib import *

def pre_build():
  add_depends(["ruby-rails-dom-testing"])
  update_pkgver_and_pkgrel(_G.newver)
