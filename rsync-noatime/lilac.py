#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.files = download_official_pkgbuild('rsync')

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=rsync-noatime'
    elif line.startswith('depends=('):
      line = line + '''
conflicts=('rsync')
provides=("rsync=$pkgver")'''
    elif line.startswith('build('):
      line = '''\
prepare() {
	cd "$srcdir/rsync-$pkgver"
	patch -p1 -i "${srcdir}/noatime.diff"
}

''' + line
    elif line.startswith('source=('):
      line = f'{line}\n\t"noatime.diff"'
    elif "'SKIP'" in line:
      line = f'{line}\n\t"7509ab5faf85dddea671d40e379c8b03b3aef41270df33cc51399017238a9fe4"'
    if '$pkgname' in line:
      line = line.replace('$pkgname', 'rsync')
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  single_main()
