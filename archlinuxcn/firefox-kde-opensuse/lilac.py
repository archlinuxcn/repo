#!/usr/bin/env python3
from lilaclib import *
from pyalpm import vercmp

build_prefix = 'extra-x86_64'
time_limit_hours = 4

def pre_build():
    aur_pre_build()
    # add_into_array('options', "'debug'")

if __name__ == '__main__':
    single_main(build_prefix)
