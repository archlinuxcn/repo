# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Sergej Pupykin <arch+pub@sergej.pp.ru>

pkgname=nextcloud-app-tasks-git
pkgver=0.13.6.r612.g977efa0b
pkgrel=1
pkgdesc="Enhanced task app for NextCloud"
arch=('any')
url="https://github.com/nextcloud/tasks"
license=('AGPL')
depends=('nextcloud')
makedepends=('npm' 'zip' 'git' 'rsync')
provides=("nextcloud-app-tasks=$pkgver")
conflicts=('nextcloud-app-tasks')
options=('!strip')
source=("git+https://github.com/nextcloud/tasks.git")
sha512sums=('SKIP')

pkgver() {
  cd "${srcdir}/tasks"
  git describe --tags --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
}

build() {
  cd "${srcdir}/tasks" 

  make -j1 npm-init
  make -j1 all appstore
}

package() {
  cd "${srcdir}/tasks" 

  install -Ddm755 "${pkgdir}/usr/share/webapps/nextcloud/apps"
  cp -dr --no-preserve=ownership build/appstore/tasks "${pkgdir}/usr/share/webapps/nextcloud/apps"
}
