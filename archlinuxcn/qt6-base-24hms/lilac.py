#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():
  g.files = download_official_pkgbuild('qt6-base')

  conflict_string=""
  for line in open('qt6-pkgs').readlines():
    p = line.strip()
    conflict_string = conflict_string + '"' + p + '>$pkgver" '

  prepare = False
  checks = ''
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgrel='):
      line = line + '.1'
    elif line.startswith('pkgname='):
      line = 'pkgname=qt6-base-24hms'
      checks = checks + '1'
    elif line.startswith('pkgdesc='):
      line = "pkgdesc='A cross-platform application and UI framework. This package uses 24-hour notation HH:mm:ss in all locales.'"
      checks = checks + 'b'
    elif line.startswith('makedepends=('):
      line = line.replace('(', "(python 'zstd>=1.5.2-7' ")
      checks = checks + '2'
    elif line.startswith('groups=('):
      line = '''
provides=("qt6-base=$pkgver")
conflicts=(qt6-base ''' + conflict_string + ")" # remove official groups
      checks = checks + '4'
    elif line.startswith('_pkgfn='):
      line = line.replace('${pkgname/6-/}', 'qtbase')
      checks = checks + '5'
    elif line.startswith('source=('):
      line = line.replace('=(', '''=(
      oldherl-24hms.patch
      'https://build.archlinuxcn.org/~oldherl/files/cldr/36/core.zip'
      'https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3.tab'
      ''')
      checks = checks + '6'
    elif line.startswith('sha256sums=('):
      line = line.replace('=(', '''=(
      '97ab390edb9b8f452f42138f9dfb2184e5a2bf0a2dddd02c3b6afbc448bd6997'
      '07279e56c1f4266d140b907ef3ec379dce0a99542303a9628562ac5fe460ba43'
      '9660ebcab661e7a6bbb194a6c031fb89bea532af4f34fa5d99d653c20d9562cb'
      ''')
      checks = checks + '7'
    elif line.startswith('prepare('):
      prepare = True
      checks = checks + '8'
    elif prepare and line.startswith('}'):
      line = '''
  cd $_pkgfn
  patch -p1 -i ../oldherl-24hms.patch
  cd util/locale_database
  echo "This is slow. It takes about 4 minutes on my desktop."
  ./cldr2qlocalexml.py ../../../ > ./24h.xml
  ./qlocalexml2cpp.py ./24h.xml ../../../iso-639-3.tab ../..
''' + line
      prepare = False
      checks = checks + '9'
    elif line.startswith('package_'):
      # other split packages. do not build them.
      line = 'no' + line
      logger.info('removed: %s', line)
    print(line)
  if len(checks) != 9:
    raise ValueError('PKGBUILD editing not completed. checks=' + checks)

def post_build():
  git_add_files(g.files)
  git_commit()

#if __name__ == '__main__':
#  single_main()
