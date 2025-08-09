#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['exu', 'ruahcra'])

    for line in edit_file('PKGBUILD'):
        print(line)

    print('''
_filename=Feishin-linux
source=("feishin.desktop")
source_x86_64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-x64.tar.xz")
source_aarch64=("https://github.com/jeffvli/feishin/releases/download/v${pkgver//_/-}/${_filename}-arm64.tar.xz")
sha256sums=('ef112b1a9ef80d8bf27f721fdbb12de0a195da4e464dbf27282503ba398bef8d')
sha256sums_x86_64=('592b403bfd362229ff4e9348ad5d605b94805f660f40895da3cd068dd6df9658')
sha256sums_aarch64=('52a3a02f5bb52bc6330bc3777661fd0e75a297d6058864187d38e55d40b05522')
    ''')
