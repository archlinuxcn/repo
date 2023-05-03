#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Kimiblock'])
    add_depends(['qt6-quick3d'])
