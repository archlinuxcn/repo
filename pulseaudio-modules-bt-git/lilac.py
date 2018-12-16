from lilaclib import *
import os

depends = ["libldac"]

build_prefix = 'extra-x86_64'

def pre_build():
    for line in edit_file('PKGBUILD'):
        # Don't replace any official package
        if line.startswith('replaces=') or line.startswith('provides='):
            continue
        else:
            print(line)
