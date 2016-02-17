#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver='):
      line = 'pkgver=' + s.get('https://rubygems.org/api/v1/versions/rak.json').json()[0]['number']
    print(line)
    run_cmd(['sh', '-c', 'makepkg -g >> PKGBUILD'])

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
