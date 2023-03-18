#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['Eragon'])
    add_depends(['playerctl'])
