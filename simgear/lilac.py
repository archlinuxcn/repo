from lilaclib import *
import os

depends = []

build_prefix = 'extra-x86_64'

def pre_build():
    for line in edit_file('PKGBUILD'): 
        if line.startswith('depends='):
            print("depends=('glut')")
            continue
        if line.startswith('makedepends='):
            print("makedepends=('boost' 'cmake' 'mesa' 'openscenegraph34' 'plib' 'freealut' 'glu')")
            continue
        else:
            print(line) 

# if __name__ == '__main__':
#     single_main('extra-x86_64')
