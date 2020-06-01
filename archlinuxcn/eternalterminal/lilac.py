#!/usr/bin/env python3

from lilaclib import *
import re

def pre_build():
  update_pkgver_and_pkgrel(re.sub('^[^0-9]*', '', _G.newver))
