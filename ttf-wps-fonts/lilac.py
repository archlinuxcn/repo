#!/usr/bin/env python3
from lilaclib import *
import datetime

build_prefix = 'extra-x86_64'

def pre_build():
    if str(datetime.datetime.now())[:8] < '20180704':
        run_cmd('rm -rf ttf-wps-fonts'.split(' '))

    aur_pre_build()

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
