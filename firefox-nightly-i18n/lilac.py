#!/usr/bin/python3

import datetime

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  version, dt = _G.newver.split(None, 1)
  dt = datetime.datetime.strptime(dt, '%d-%b-%Y %H:%M').strftime('%Y%m%d.%H')

  for l in edit_file('PKGBUILD'):
    if l.startswith('pkgver='):
      l = f'pkgver={version}_{dt}'
    elif l.startswith('_pkgver='):
      l = f'_pkgver={version}'
    print(l)

  run_cmd(['updpkgsums'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
