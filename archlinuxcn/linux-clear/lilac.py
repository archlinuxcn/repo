#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['JeremyStarTM'])
    add_replaces(["linux-clear-x64-v3", "linux-clear-x64-v4"])
    add_provides(["linux-clear-x64-v3", "linux-clear-x64-v4"])
    add_makedepends(['pv'])
