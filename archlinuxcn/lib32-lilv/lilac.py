#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libserd-0.so', 'libsord-0.so', 'libsratom-0.so'])
    add_provides(['liblilv-${pkgver%%.*}.so'])

def post_build():
    aur_post_build()
