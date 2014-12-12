#!/usr/bin/env python3

from lilaclib import *

build_prefix = ['extra-x86_64', 'extra-i686']
post_build = aur_post_build

def pre_build():
  # delete old source files as they have same names each version
  run_cmd(["rm", "-f", "android-ndk_x86_64.bin", "android-ndk_i686.bin"])
  aur_pre_build()

if __name__ == '__main__':
  single_main()
