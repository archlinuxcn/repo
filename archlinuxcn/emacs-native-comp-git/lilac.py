#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('emacs-git', maintainers=['toropisco'])
    checks = ''
    for line in edit_file('PKGBUILD'):
        if 'pkgdesc=' in line:
            line = 'pkgdesc="GNU Emacs. Development master branch. AOT&JIT enabled."'
        if 'pkgname=' in line:
            line = '  pkgname="emacs-native-comp-git"'
        if line.startswith('replaces='):
            line = ''

        #disable all flags
        if '="YES"' in line:
            line = line.replace('="YES"', '=')

        if line.startswith('JIT='):
            line = 'JIT="YES"'
            checks = checks + '3'
        if line.startswith('AOT='):
            line = 'AOT="YES"'
            checks = checks + '4'

        #if line.startswith('XWIDGETS='):
        #    line = 'XWIDGETS="YES"'
        #    checks = checks + '5'

        # enable tree-sitter, request from #3094
        if line.startswith('SITTER='):
            line = 'SITTER="YES"'
            checks = checks + '8'

        if line.startswith('install='):
            line = 'install=emacs-git.install'
            checks = checks + '6'

        #if line.startswith('source='):
        #    line = 'source=("emacs-git::git+https://github.com/emacs-mirror/emacs.git")'
        #    checks = checks + '3'
        if '../configure' in line:
            line = f'{line}\n  make bootstrap'


        print(line)

    # make sure PKGBUILD is modified
    if len(checks) != 4:
        raise ValueError('PKGBUILD editing not completed. checks=' + checks)
