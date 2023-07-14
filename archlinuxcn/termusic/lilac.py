#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['orhun'])

    for line in edit_file('PKGBUILD'):
        print (line.replace('3bf9cacb01ccaaa2415e0296d8870408b5d5b231dfc798236fa114fb1b61d9c3c03af4fedb2cdd98fa3a33f518b0b83f0636a2bfae8fa370a36bb33a378faa24','67f0b06ff37dbc3d16c77c6bdd0163dc547fbea1a25b3a7574b4540a4ad3a2059dc547d49411803fd9aa162d4f432ff5b99bef1e0f5c362342943fa76985f443'))
