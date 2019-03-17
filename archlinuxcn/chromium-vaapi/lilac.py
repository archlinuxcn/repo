from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('local _flags=('):
            print(line)
            print("    'use_jumbo_build = true'")
        else:
            print(line)


