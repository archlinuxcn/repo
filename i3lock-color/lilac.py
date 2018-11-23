#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  aur_pre_build()
  add_depends(["xcb-util-xrm"])

