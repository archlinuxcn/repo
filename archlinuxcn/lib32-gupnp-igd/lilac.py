#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='rodrigo21')
    add_depends(['libglib-2.0.so', 'libgobject-2.0.so', 'libgssdp-1.2.so', 'libgupnp-1.2.so'])
    add_provides(['libgupnp-igd-1.0.so'])

def post_build():
    aur_post_build()
