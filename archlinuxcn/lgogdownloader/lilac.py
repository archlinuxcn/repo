from lilaclib import *

def pre_build():
    aur_prebuild()
    update_pkgver_and_pkgrel(_G.newver.split('-')[0])
