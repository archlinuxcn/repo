from lilaclib import *

def pre_build():
    if _G.newver is not None:
        update_pkgver_and_pkgrel(_G.newver)
    else:
        raise Exception("nvchecker failed (newver is None)")


def post_build():
    aur_post_build()
    update_aur_repo()

