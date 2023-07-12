#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['lsf'])

    for line in edit_file('PKGBUILD'):
        print(line.replace("$(uname -r)", "${KERNEL_VER}"))
        if line.strip().startswith('build()'):
            print("KERNEL_VER=$(pacman -Si linux-headers | grep Version | awk '{print $3}' | sed 's/.arch/-arch/')")
