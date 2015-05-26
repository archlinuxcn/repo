#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('wget')

  prepare = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=wget-lily'
    elif line.startswith('optdepends=('):
      line = line + '''
conflicts=('wget')
provides=("wget=$pkgver")'''
    elif line.startswith('prepare('):
      prepare = True
    elif prepare and line.startswith('}'):
      line = '  patch -p1 -i "${srcdir}/wget.patch"\n' + line
      prepare = False
    elif line.startswith('source=('):
      line = line.replace(')', ' wget.patch)')
    elif "'SKIP')" in line:
      line = line.replace(')', ' 50d39b440b755ab411cf30128cd001bf4233c329)')
    if '${pkgname}' in line:
      line = line.replace('${pkgname}', 'wget')
    print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  single_main()
