#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('firefox')

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=firefox-gtk2'
    elif line.startswith('depends=('):
      line = line.replace("'gtk3' ", "")
      line = """conflicts=('firefox')
provides=("firefox=${pkgver}-${pkgrel}")\n""" + line

    print(line)

  for line in edit_file('mozconfig'):
    if 'gtk3' in line:
      continue
    print(line)

  run_cmd(['updpkgsums'])

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  single_main()
