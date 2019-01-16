#!/usr/bin/env python3

from datetime import datetime

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  version, dt = _G.newver.split(None, 1)
  dt = datetime.strptime(dt, '%d-%b-%Y %H:%M').strftime('%Y%m%d.%H')

  for line in edit_file('PKGBUILD'):
    if line.startswith('_version='):
      line = f'_version={version}'
    elif line.startswith('_filename_prefix='):
      line = f'_filename_prefix="{dt}-"'

    print(line)

  update_pkgver_and_pkgrel(f'{version}.{dt}')
  run_cmd(['updpkgsums'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
