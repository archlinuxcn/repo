from lilaclib import *

def pre_build():
    aur_pre_build()
    update_pkgver_and_pkgrel(_G.newver.split('-')[0])
