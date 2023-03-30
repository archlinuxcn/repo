#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['grufo'])
    add_depends(['gtk4', 'libadwaita'])
