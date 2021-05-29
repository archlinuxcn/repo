#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='adam900710')
    add_depends(['lib32-gcc-libs'])
    add_provides(['libfftw3.so', 'libfftw3_omp.so', 'libfftw3_threads.so', 'libfftw3f.so', 'libfftw3f_omp.so', 'libfftw3f_threads.so', 'libfftw3l.so', 'libfftw3l_omp.so', 'libfftw3l_threads.so'])

def post_build():
    check_library_provides()
    aur_post_build()
