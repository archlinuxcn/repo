#!/usr/bin/env python3

from lilaclib import *
import datetime


def pre_build():
    newver = _G.newvers[0] + '.r' + datetime.datetime.today().strftime('%Y%m%d')
    update_pkgver_and_pkgrel(newver)


def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

# vim:set ts=2 sw=2 et:
