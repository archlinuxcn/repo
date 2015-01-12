#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('build()'):
      line = 'package() {'
    elif line.startswith('pkgver='):
      line = 'pkgver=' + s.get('https://rubygems.org/api/v1/versions/text.json').json()[0]['number']
    elif line.startswith(('sha256sums=', 'md5sums=')):
      continue
    print(line)
  run_cmd(['sh', '-c', 'makepkg -g >> PKGBUILD'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
