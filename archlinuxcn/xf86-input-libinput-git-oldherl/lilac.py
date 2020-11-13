#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():

  aur_pre_build(name='xf86-input-libinput-git', do_vcs_update=True)
  checks = ''
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgname='):
      line = 'pkgname=xf86-input-libinput-git-oldherl'
      checks = checks + '0'
    elif line.startswith('pkgrel='):
      line = line + '.1'
      checks = checks + '1'
    elif line.startswith('pkgdesc='):
      line = 'pkgdesc="Generic input driver for the X.Org server based on libinput. With patch for setting scroll scale."'
      checks = checks + '2'
    elif line.startswith('groups=('):
      line = '' # remove official groups
      checks = checks + '3'
    elif line.startswith('source=('):
      line = line.replace('=(', '''=(
      0001-scroll-scale.patch
      ''')
      checks = checks + '4'
    elif line.startswith('sha256sums=('):
      line = line.replace('=(', '''=(
'934fd1e21ae8330bbaa1189c8b3858fc0e26724dea3d24dae62c5b569457e55f221db12ccc78b14a9c755bc69f59ab949bdce02ffb0f2329bef1a3d4c2c116a0'
      ''')
      checks = checks + '5'
    elif line.startswith('pkgver('):
      line = '''
prepare() {
  cd xf86-input-libinput
  git config user.name "builduser"
  git config user.email "builduser@example.com"
  git am ../0001-scroll-scale.patch
}

''' + line
      checks = checks + '6'
    elif line.startswith('validpgpkeys'):
      line = ''
      checks = checks + '7'
    elif line.startswith('makedepends=('):
      line = line.replace('=(', '=(\'git\' ')
      checks = checks + '8'
    print(line)
  if len(checks) != 9:
    raise ValueError('PKGBUILD editing not completed. checks=' + checks)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
