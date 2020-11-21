#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libgio-2.0.so', 'libglib-2.0.so', 'libgmodule-2.0.so', 'libgobject-2.0.so', 'libgssdp-1.2.so', 'libuuid.so'])
    add_provides(['libgupnp-1.2.so'])

def post_build():
    aur_post_build()
