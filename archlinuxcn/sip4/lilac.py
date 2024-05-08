#!/usr/bin/python

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['daizhirui'])

    for line in edit_file('PKGBUILD'):
        if not ((line.strip().startswith("provides=(python-sip4")) or line.strip().startswith("replaces=(python-sip4")):
            print (line)
