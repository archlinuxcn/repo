from lilaclib import update_pkgrel, vcs_update


def pre_build():
    update_pkgrel()
    vcs_update()
