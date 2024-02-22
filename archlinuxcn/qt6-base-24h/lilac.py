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

  in_prepare = False
  in_build_qt6_base = False
  checks = ''
  variant = '-24h'
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgrel='):
      line = line + '.3'
    elif line.startswith('pkgbase='):
      line = f"pkgbase=qt6-base{variant}"
      checks = checks + 'f'
    elif line.startswith('pkgname='):
      if line == "pkgname=(qt6-base qt6-xcb-private-headers)":
        line = f"pkgname=(qt6-base{variant})"
        checks = checks + '1'
      else:
        raise ValueError('PKGBUILD pkgname mismatch with preset')
    elif in_build_qt6_base and line.strip().startswith('pkgdesc='):
      line = "pkgdesc='A cross-platform application and UI framework. This package uses 24-hour notation in all locales.'"
      checks = checks + 'b'
    elif line.startswith('makedepends=('):
      line = line.replace('(', "(python ")
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
      oldherl-24h.patch
      'https://build.archlinuxcn.org/~oldherl/files/cldr/44/core.zip'
      'https://iso639-3.sil.org/sites/iso639-3/files/downloads/iso-639-3.tab'
      ''')
      checks = checks + '6'
    elif line.startswith('sha256sums=('):
      line = line.replace('=(', '''=(
      '6ab571d50f0c17d31ed33bb2ebf6eadf41c18cbf2dd8cb5260b939915a139a28'
      'bd7f70adfe8a999cfa0f5d96145bf0a095b1a099024e4f451fa1afccf6e4aee6'
      '9660ebcab661e7a6bbb194a6c031fb89bea532af4f34fa5d99d653c20d9562cb'
      ''')
      checks = checks + '7'
    elif line.startswith('prepare('):
      in_prepare = True
      checks = checks + '8'
    elif in_prepare and line.startswith('}'):
      line = '''
  cd $_pkgfn
  patch -p1 -i ../oldherl-24h.patch
  cd util/locale_database
  echo "This is slow. It takes about 4 minutes on my desktop."
  ./cldr2qlocalexml.py ../../../ > ./24h.xml
  ./qlocalexml2cpp.py ./24h.xml ../../../iso-639-3.tab ../..
''' + line
      in_prepare = False
      checks = checks + '9'
    elif in_build_qt6_base and line.startswith('}'):
      in_build_qt6_base = False
      checks = checks + 'e'
    elif line.startswith('package_qt6-base('):
      line = line.replace('(', f'{variant}(')
      in_build_qt6_base = True
      checks = checks + 'd'
    elif line.startswith('package_'):
      # other split packages. do not build them.
      line = 'no' + line
      logger.info('removed: %s', line)
    elif line.startswith('depends=('):
      # let it conflict with incompatable icu versions, @q234rty
      line = line.replace('=(', '=(libicui18n.so ')
      checks = checks + 'c'
    print(line)
  if len(checks) != 13:
    raise ValueError('PKGBUILD editing not completed. checks=' + checks)

def post_build():
  git_add_files(g.files)
  git_commit()

#if __name__ == '__main__':
#  single_main()
