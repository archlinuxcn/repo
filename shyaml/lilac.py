#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  ver = run_cmd(['sh', '-c', "git ls-remote --tags https://github.com/0k/shyaml | sed -n '${s#^.*tags\/##p}'"]).rstrip()
  run_cmd(['sh', '-c', 'sed -i "/pkgver/s/^.*$/pkgver=' + ver + '/" PKGBUILD'])

  sha256sums = run_cmd(['sh', '-c', 'makepkg -g 2> /dev/null']).rstrip()
  run_cmd(['sh', '-c', 'sed -i "/sha256sums/s/^.*$/' + sha256sums + '/" PKGBUILD'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit

if __name__ == '__main__':
  single_main()
