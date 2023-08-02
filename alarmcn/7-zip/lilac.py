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
