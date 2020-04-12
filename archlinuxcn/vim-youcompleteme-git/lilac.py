#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    run_cmd(['sh', '-c', 'sed \'/vim-plugins/d\' -i PKGBUILD'])
