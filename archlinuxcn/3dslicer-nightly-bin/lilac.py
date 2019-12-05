#!/usr/bin/env python3

from lilaclib import *


def pre_build():
    version, revision = _G.newvers
    newver = version + '.r' + revision
    update_pkgver_and_pkgrel(newver)


def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

# vim:set ts=2 sw=2 et:
