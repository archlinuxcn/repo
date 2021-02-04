# Trimmed lilac.py
#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():
  g.files = download_official_pkgbuild('wget')

  prepare = False
  sumwhich = 0
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
    elif line.startswith('sha256sums='):
      sumwhich = 0
    elif line.startswith('b2sums='):
      sumwhich = 1
    elif "'SKIP')" in line:
      if sumwhich == 0:
        line = line.replace(')', ' aa28cf8532f6b7cc1fe689eb253b0453102990eb725a6583704ca4f3e665c9b0)')
      elif sumwhich == 1:
        line = line.replace(')', ' c6a292c1be5606c007d1dcd25f02b3760ac98e86f2c1de30b50847b65c5ecfdb5cd89a482ab1e6a5b5978d38057c21d671b72ec45f10f6e59c5596519cecdf2e)')
    if '${pkgname}' in line:
      line = line.replace('${pkgname}', 'wget')
    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()

#if __name__ == '__main__':
#  single_main()
