#!/usr/bin/env python3

import fileinput
from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  json = s.get('https://rubygems.org/api/v1/versions/rak.json').json()

  pkgver = json[0]['number']
  run_cmd(['sh', '-c', 'sed -i "/^pkgver/s/^.*$/pkgver=' + pkgver + '/" PKGBUILD'])

  run_cmd(['sh', '-c', 'updpkgsums'])

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
