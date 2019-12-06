from lilaclib import *

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('makedepends='):
            line = "makedepends=('jdk8-openjdk' 'ant>=1.9.0'"
        if line.strip().startswith('./configure'):
            line = '  ./configure --with-jdk=/usr/lib/jvm/java-8-openjdk/ \\'
        print(line)

