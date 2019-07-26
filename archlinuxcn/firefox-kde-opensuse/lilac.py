#!/usr/bin/env python3
from lilaclib import *
from pyalpm import vercmp

build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    oldver, oldpkgrel = _G.oldver.split('-')
    newver, newpkgrel = _G.newver.split('-')
    if vercmp(newver, oldver) >= 0:
        update_pkgver_and_pkgrel(newver, updpkgsums=True)
    else:
        update_pkgver_and_pkgrel(oldver, updpkgsums=True)


post_build = git_pkgbuild_commit

if __name__ == '__main__':
    single_main(build_prefix)
