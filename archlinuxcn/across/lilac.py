#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    run_cmd(["sh", "-c", 'curl -sSO https://raw.githubusercontent.com/ArkToria/ACross/master/pkgbuild/arch/across/PKGBUILD'])
    run_cmd(["updpkgsums"])

def post_build():
    git_pkgbuild_commit()
    update_aur_repo()
