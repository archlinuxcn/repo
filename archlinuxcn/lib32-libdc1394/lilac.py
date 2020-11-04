#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libusb-1.0.so'])
    add_provides(['libdc1394.so'])

def post_build():
    aur_post_build()
