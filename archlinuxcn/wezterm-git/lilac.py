#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['wez', 'xiota'])
    for line in edit_file('PKGBUILD'):
        # terminfo file conflicts with ncurse
        # https://github.com/archlinuxcn/repo/issues/3838
        if "/usr/share/terminfo/w/wezterm" in line:
            line = ""
        print(line)
