#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libfontconfig.so', 'libfreetype.so', 'libgio-2.0.so', 'libglib-2.0.so', 'libgobject-2.0.so', 'libharfbuzz.so', 'libpango-1.0.so', 'libpangocairo-1.0.so', 'libpangoft2-1.0.so', 'libsndfile.so'])

def post_build():
    aur_post_build()
