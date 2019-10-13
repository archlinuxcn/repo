from lilaclib import *

def pre_build():
    vcs_update()
    update_pkgver_and_pkgrel(_G.newver.split('-')[0])
