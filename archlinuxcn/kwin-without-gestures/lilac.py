#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newver.split("-", 1)[0])

def post_build():
    update_aur_repo()
