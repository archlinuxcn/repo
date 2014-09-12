#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
post_build = aur_post_build

def pre_build():
  aur_pre_build()
  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('license='):
        line += '\ndepends=("ca-certificates")'
      elif line.lstrip() == '}':
        line = '''\
  # use system-wide certificates
  ln -sf ../../../etc/ssl/certs/ca-certificates.crt "${pkgdir}"/opt/prince/etc/curl-ca-bundle.crt
}'''
      print(line)

if __name__ == '__main__':
  single_main()
