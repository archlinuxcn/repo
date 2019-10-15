from lilaclib import *

def pre_build():
    vcs_update()
    update_pkgver_and_pkgrel(get_pkgver_and_pkgrel()[0])
