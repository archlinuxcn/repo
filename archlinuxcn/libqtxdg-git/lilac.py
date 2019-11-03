from lilaclib import aur_pre_build, update_pkgrel


def pre_build():
    update_pkgrel()
    aur_pre_build()
