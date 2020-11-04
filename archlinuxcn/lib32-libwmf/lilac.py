#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libfreetype.so', 'libglib-2.0.so', 'libgobject-2.0.so'])
    add_provides(['libwmf.so', 'libwmflite.so'])

def post_build():
    aur_post_build()
