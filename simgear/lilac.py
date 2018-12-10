from lilaclib import *
import os

depends = []

def pre_build():
    for line in edit_file('PKGBUILD'): 
        if line.startswith('depends='):
            line = "depends=('glut')"
        if line.startswith('makedepends='):
            line = "makedepends=('boost' 'cmake' 'mesa' 'openscenegraph34' 'plib' 'freealut' 'glu')"

