#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build('google-drive-ocamlfuse-opam', do_vcs_update=True)
    for line in edit_file('PKGBUILD'):
        line = line.replace('google-drive-ocamlfuse-opam', 'google-drive-ocamlfuse')
        print(line)
