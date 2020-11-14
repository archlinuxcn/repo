#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():
  origname = 'xf86-input-libinput'
  myname = origname + '-oldherl'
  g.files = download_official_pkgbuild(origname)

  checks = ''
  for line in edit_file('PKGBUILD'):
    line = line.replace('${pkgname}', '${_pkgname}')
    if line.startswith('pkgname='):
      line = 'pkgname=' + myname + '\n' + '_pkgname=' + origname
      checks = checks + '0'
    elif line.startswith('pkgrel='):
      line = line + '.1'
      checks = checks + '1'
    elif line.startswith('pkgdesc='):
      line = line + '" Patched by oldherl."'
      checks = checks + '2'
    elif line.startswith('conflicts=('):
      line = line.replace('(', '(${_pkgname} ')
      checks = checks + '2'
    elif line.startswith('groups=('):
      line = 'provides=("' + origname + '=$pkgver")'  # remove official groups
      checks = checks + '3'
    elif line.startswith('source=('):
      # remove gpg keys and add patch
      line = line.replace('{,.sig}', '''
      0001-scroll-scale.patch
      ''')
      checks = checks + '4'
    elif line.startswith('validpgpkeys=('):
      line = ''  # remove gpg keys
      checks = checks + '5'
    elif line.startswith('build('):
      line = '''
prepare() {
  cd ${_pkgname}-${pkgver}
  patch -p1 -i ../0001-scroll-scale.patch
}
''' + line
      checks = checks + '6'
    print(line)
  if len(checks) != 7:
    raise ValueError('PKGBUILD editing not completed. checks=' + checks)

def post_build():
  git_add_files(g.files)
  git_commit()

#if __name__ == '__main__':
#  single_main()
