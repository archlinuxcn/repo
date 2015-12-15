#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  info = get_pypi_info('tldextract')
  pkgver = info['info']['version']
  release = [x for x in info['releases'][pkgver] if x['packagetype'] == 'sdist'][0]
  md5sum = release['md5_digest']
  url = release['url']

  oldver = None
  for line in edit_file('PKGBUILD'):
    line = line.rstrip('\n')
    if line.startswith('pkgver='):
      oldver = line.split('=', 1)[-1]
      line = 'pkgver=' + pkgver
    elif line.startswith('pkgrel='):
      oldrel = int(line.split('=', 1)[-1])
      if oldver != pkgver:
        line = 'pkgrel=1'
        # else we're rebuilding, leave as it is
    elif line.startswith('source='):
      line = 'source=(%s)' % url
    elif line.startswith('md5sums='):
      line = 'md5sums=(%s)' % md5sum
    print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
