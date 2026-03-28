#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build('emacs-git', maintainers=['toropisco'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('replaces='):
            continue
        #if line.startswith('source='):
        #    line = 'source=("emacs-git::git+https://github.com/emacs-mirror/emacs.git")'

        # enable svg
        # make sure librsvg is present so emacs can build the support
        # https://github.com/emacs-mirror/emacs/blob/e6c1e87c1e06b44cfffd2f0fd7ee00bb714a1854/INSTALL#L380-L390
        if line.startswith('depends'):
            line = line.replace(')', " 'librsvg')")

        # disable build flags
        if '="YES"' in line:
            line = line.replace('="YES"', '=')

        #if line.startswith('XWIDGETS='):
        #    line = 'XWIDGETS="YES"'

        if line.startswith('SITTER='):
            line = 'SITTER="YES"'

        print(line)
