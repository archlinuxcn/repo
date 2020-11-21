#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_provides(['libHalf-2_5.so', 'libHalf.so', 'libIex-2_5.so', 'libIex.so', 'libIexMath-2_5.so', 'libIexMath.so', 'libIlmImf-2_5.so', 'libIlmImf.so', 'libIlmImfUtil-2_5.so', 'libIlmImfUtil.so', 'libIlmThread-2_5.so', 'libIlmThread.so', 'libImath-2_5.so', 'libImath.so'])

def post_build():
    aur_post_build()
