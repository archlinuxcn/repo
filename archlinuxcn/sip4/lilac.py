#!/usr/bin/python

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['daizhirui'])

    for line in edit_file('PKGBUILD'):
        stripped = line.strip()
        if not (stripped.startswith("provides=(sip4") or stripped.startswith("provides=(python-sip4") or stripped.startswith("replaces=(python-sip4")):
            print (line)
