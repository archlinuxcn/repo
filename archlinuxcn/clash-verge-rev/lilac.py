#!/usr/bin/python3

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newvers[0])

    for line in edit_file('PKGBUILD'):
        if line.startswith('_ipc_ver='):
            line = f'_ipc_ver={_G.newvers[1]}'

        print(line)

    run_protected(["updpkgsums"])

