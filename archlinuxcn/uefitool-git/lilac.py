from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('arch='):
            line = 'arch=("x86_64")'
        print(line)

