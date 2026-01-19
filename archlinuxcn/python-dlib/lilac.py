#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['zen'])
    for line in edit_file('PKGBUILD'):
        if '--no DLIB_USE_CUDA' in line:
            line += ' --no USE_SSE4_INSTRUCTIONS --no USE_AVX_INSTRUCTIONS'

        print(line)
