#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_provides(['libzvbi-chains.so', 'libzvbi.so'])

def post_build():
    aur_post_build()
