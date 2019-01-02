#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  oldver, oldrel = _G.oldver.split('-', 1)
  ver, rel = _G.newver.split('-', 1)
  need_update_pkgrel = False

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver='):
      print('pkgver=%s' % ver)
      continue
    elif line.startswith('pkgrel='):
      if oldver == ver:
        need_update_pkgrel = True
        print(line)
      else:
        print('pkgrel=1')
      continue

    print(line)

  if need_update_pkgrel:
    update_pkgrel()

  run_cmd(['updpkgsums'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
