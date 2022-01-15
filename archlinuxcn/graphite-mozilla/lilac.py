#!/usr/bin/env python3
from lilaclib import *
from pyalpm import vercmp

def pre_build():
    aur_pre_build()
    # add_into_array('options', "'debug'")

if __name__ == '__main__':
    single_main(build_prefix)
