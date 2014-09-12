#!/usr/bin/env python3

import fileinput

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['python2-netlib-git']
post_build = aur_post_build

patch = '''\
  lilyver=$(pacman -Q linux-lily-headers | awk '{print $2}')
  mkdir -p libau/linux
  cp "/lib/modules/${lilyver}-lily/build/include/uapi/linux/aufs_type.h" libau/linux
  sed -i 's/__user//g' libau/linux/aufs_type.h
  mkdir -p fhsm/libau/linux
  cp libau/linux/aufs_type.h fhsm/libau/linux
  sed -i 's/-lrt -L. -lfhsm -L.. -lautil/-L. -lfhsm -L.. -lautil -lrt/' fhsm/Makefile

'''

def pre_build():
  aur_pre_build()
  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.strip() == 'make':
        line = patch + line
      elif line.startswith('pkgname='):
        line = 'pkgname=aufs3-util-lily-git'
      elif line.startswith('makedepends'):
        line = "makedepends=('linux-lily-headers' 'git')"
      print(line)

if __name__ == '__main__':
  single_main()
