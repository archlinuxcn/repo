#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['rkcf'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('install -Dm644 LICENSE'):
            print('install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"')
        print(line)
