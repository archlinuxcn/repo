#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'extra-x86_64'

def _get_new_version():
  new_verion = s.get("https://api.github.com/repos/slgobinath/uget-chrome-wrapper/tags").json()[0]
  return new_verion['name'][1:]

def pre_build():
  aur_pre_build()
  ver = _get_new_version()
  with fileinput.input(files=('PKGBUILD'), inplace=1) as f:
    for l in f:
      l = l.rstrip('\n')
      if l.startswith('pkgver='):
        l = 'pkgver=' + ver
      print(l)

def post_build():
  git_add_files("PKGBUILD")
  git_commit()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
