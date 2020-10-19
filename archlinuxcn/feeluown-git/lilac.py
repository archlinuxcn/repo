from lilaclib import *

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('groups=('):
            continue
    vcs_update()
