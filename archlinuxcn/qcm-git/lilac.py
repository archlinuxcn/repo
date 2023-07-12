#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Kimiblock'])

    for line in edit_file('PKGBUILD'):
        print(line)
        if line.strip().startswith('function build()'):
            print('export TERM=xterm')
