#!/usr/bin/env python3
#
# This file is the most simple lilac.py file.
#

from lilaclib import *

def pre_build():
    update_pkgver_and_pkgrel(_G.newver.lstrip('v'))

# vim:set ts=4 sw=4 et:
