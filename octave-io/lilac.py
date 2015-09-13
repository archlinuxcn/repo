#!/usr/bin/env python3

from lilaclib import *
import fileinput
import re

build_prefix = 'archlinuxcn-x86_64'

post_build = aur_post_build

_pkg = 'io'

def _get_new_version():
  web = s.get('http://octave.sourceforge.net/%s/index.html' % _pkg)
  return re.search(r'\d\.\d\.\d', web.text).group()

def pre_build():
  aur_pre_build()
  ver = _get_new_version()
  with fileinput.input(files=('PKGBUILD'), inplace=1) as f:
    for l in f:
      l = l.rstrip('\n')
      if l.startswith('pkgver='):
        l = 'pkgver=' + ver
      print(l)

  run_cmd(['updpkgsums'])


if __name__ == '__main__':
  single_main(build_prefix)
