#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    run_cmd(['sh', '-c', 'sed \'/vim-plugins/d\' -i PKGBUILD'])
    run_cmd(['sh', '-c', 'sed \'s/_use_system_clang="OFF"/_use_system_clang="ON"/\' -i PKGBUILD'])
