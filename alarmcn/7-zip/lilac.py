#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['post-factum'])
    add_arch(['aarch64'])

    in_uasm_src = False

    for line in edit_file('meson.build'):
        if not in_uasm_src:
            print(line)
        elif line.strip().startswith(']'):
            in_uasm_src = False

        if line.strip().startswith('uasm_src'):
            in_uasm_src = True
            print("\'Asm/arm64/7zAsm.S\',")
            print("\'Asm/arm64/LzmaDecOpt.S\',")
            print(']')

    for line in edit_file('PKGBUILD'):
        print (line.replace('211a57a476943e654de7408145b8d626a4dc242e74a3dcb8fc3afd0620792a03','SKIP'))
