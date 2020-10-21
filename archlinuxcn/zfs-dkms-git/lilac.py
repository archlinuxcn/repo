#!/usr/bin/env python3

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('depends='):
            print('depends=("zfs-utils-git" "lsb-release" "dkms")')
        else:
            print(line)

