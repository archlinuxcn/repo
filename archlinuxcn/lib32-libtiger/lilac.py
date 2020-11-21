#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libglib-2.0.so', 'libgobject-2.0.so', 'libharfbuzz.so', 'libkate.so', 'libpango-1.0.so', 'libpangocairo-1.0.so'])
    add_provides(['libtiger.so'])

def post_build():
    aur_post_build()
