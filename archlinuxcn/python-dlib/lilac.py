#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['petronny', 'AutoUpdateBot'])
    for line in edit_file('PKGBUILD'):
        line = line.replace('gcc-14', 'gcc').replace('g++-14', 'g++'))
        if '--no DLIB_USE_CUDA' in line:
            line += ' --no USE_SSE4_INSTRUCTIONS --no USE_AVX_INSTRUCTIONS'

        print(line)
