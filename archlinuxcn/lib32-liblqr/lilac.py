#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libglib-2.0.so'])
    add_provides(['liblqr-1.so'])

def post_build():
    aur_post_build()
