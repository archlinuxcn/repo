#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('emacs-git', maintainers=['toropisco'])
    checks = ''
    for line in edit_file('PKGBUILD'):
        if 'pkgdesc=' in line:
            line = 'pkgdesc="GNU Emacs. Development master branch. AOT&JIT&PGTK enabled."'
        if 'pkgname=' in line:
            line = '  pkgname="emacs-native-comp-pgtk-git"'
        if line.startswith('replaces='):
            line = ''

        # enable svg
        # make sure librsvg is present so emacs can build the support
        # https://github.com/emacs-mirror/emacs/blob/e6c1e87c1e06b44cfffd2f0fd7ee00bb714a1854/INSTALL#L380-L390
        if line.startswith('depends'):
            line = line.replace(')', " 'librsvg')")

        # disable all flags
        if '="YES"' in line:
            line = line.replace('="YES"', '=')

        if line.startswith('JIT='):
            line = 'JIT="YES"'
            checks = checks + '3'
        if line.startswith('AOT='):
            line = 'AOT="YES"'
            checks = checks + '4'

        if line.startswith('PGTK='):
            line = 'PGTK="YES"'
            checks = checks + '5'

        #if line.startswith('XWIDGETS='):
        #    line = 'XWIDGETS="YES"'
        #    checks = checks + '6'

        # enable tree-sitter, request from #3094
        if line.startswith('SITTER='):
            line = 'SITTER="YES"'
            checks = checks + '8'

        if line.startswith('install='):
            line = 'install=emacs-git.install'
            checks = checks + '7'

        #if line.startswith('source='):
        #    line = 'source=("emacs-git::git+https://github.com/emacs-mirror/emacs.git")'
        #    checks = checks + '3'

        print(line)

    # make sure PKGBUILD is modified
    if len(checks) != 5:
        raise ValueError('PKGBUILD editing not completed. checks=' + checks)
