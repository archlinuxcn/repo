from lilaclib import *

def pre_build():
    aur_pre_build()
    update_pkgrel()

def post_build():
    aur_post_build()

