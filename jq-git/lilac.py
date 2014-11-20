#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  aur_pre_build(do_vcs_update=False)

  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('depends=('):
        line = 'depends=("oniguruma" ' + line[len('depends=('):]
      elif line.lstrip().startswith('git describe'):
        line = line.replace('describe', 'describe --tags')
      print(line)

  vcs_update()

if __name__ == '__main__':
  single_main()
