#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libmbedcrypto.so'])
    add_provides(['libdislocker.so'])

def post_build():
    aur_post_build()
