from lilaclib import *
import os

repo_depends = ["simgear", "flightgear-data"]

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            print("depends=('libxmu' 'openscenegraph34' 'openal' 'qt5-svg')")
            continue
        if line.startswith('makedepends='):
            print("makedepends=('boost' 'cmake' 'mesa' 'sharutils' 'simgear' 'qt5-base' 'qt5-declarative' 'plib' 'glu' 'libxrandr' 'subversion')")
            continue
        else:
            print(line)

# if __name__ == '__main__':
#     single_main('extra-x86_64')

