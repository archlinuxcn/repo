#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def post_build():
  os.chdir('vim')
  run_cmd(["git", "push"])

if __name__ == '__main__':
  single_main()
