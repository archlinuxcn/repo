#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['oniguruma']
post_build = aur_post_build

def pre_build():
  aur_pre_build()

  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('depends=('):
        line = 'depends=("oniguruma" ' + line[len('depends=('):]
      elif line.lstrip().startswith('git describe'):
        line = line.replace('describe', 'describe --tags')
      print(line)

if __name__ == '__main__':
  single_main()
