from lilaclib import *

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('makedepends='):
            line = "makedepends=('jdk8-openjdk' 'ant>=1.9.0'"
        print(line)

