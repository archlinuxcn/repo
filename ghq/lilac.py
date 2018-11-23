#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'


def pre_build():
    update_pkgver_and_pkgrel(_G.newver)
