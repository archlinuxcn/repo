from lilaclib import *


def pre_build():
    update_pkgver_and_pkgrel(_G.newver)


def post_build():
    pypi_post_build()
    update_aur_repo()
