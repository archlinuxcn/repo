#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('emacs-git', maintainers=['vorbote'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('replaces='):
            continue
        if line.startswith('source='):
            line = 'source=("emacs-git::git://github.com/emacs-mirror/emacs.git")'
        # fix libxpm
        if line.startswith('depends='):
            line = 'depends=("${depends_nox[@]}" "harfbuzz" "libxpm")'
        print(line)
