#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='RavuAlHemio')
    add_provides(['libgsm.so'])

def post_build():
    aur_post_build()
