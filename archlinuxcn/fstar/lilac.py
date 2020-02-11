from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        print(line.replace("z3-git", "z3"))
