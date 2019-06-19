#!/usr/bin/python3

from lilaclib import *

def pre_build():

    aur_pre_build()
    
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('source='):
            print(line)
            print("        'fixforgcc9.patch::https://686982.bugs.gentoo.org/attachment.cgi?id=578490'")
        elif line.strip().startswith('cd "$srcdir/chromium-$pkgver"'):
            print(line)
            print()
            print('  #https://bugs.gentoo.org/686982')
            print('  patch -Np1 -i "$srcdir/fixforgcc9.patch"')
            print()
        elif line.strip().startswith('local _flags=('):
            print(line)
            print("    'use_jumbo_build = true'")
        else:
            print(line)
    
    run_cmd(["updpkgsums"])


#if __name__ == '__main__':
#    single_main('extra-x86_64')

