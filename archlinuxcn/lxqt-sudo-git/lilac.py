from lilaclib import aur_pre_build, add_makedepends


def pre_build():
    aur_pre_build()
    add_makedepends(['lxqt-build-tools-git'])
