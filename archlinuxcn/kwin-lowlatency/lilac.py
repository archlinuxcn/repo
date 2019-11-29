#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    vcs_update() # Avoid lilac cache for git sources
