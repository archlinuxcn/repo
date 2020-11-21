#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libserd-0.so'])
    add_provides(['libsord-0.so'])

def post_build():
    aur_post_build()
