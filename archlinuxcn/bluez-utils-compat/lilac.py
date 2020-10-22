#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libdbus-1.so', 'libglib-2.0.so', 'libjson-c.so', 'libreadline.so', 'libudev.so'])

def post_build():
    aur_post_build()
