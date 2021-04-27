# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkcore-git
pkgver=5.4.0.r35.g511d1dd
pkgrel=1
pkgdesc='DTK core modules'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkcore"
license=('LGPL3')
depends=('dconf' 'deepin-desktop-base-git' 'python' 'gsettings-qt' 'lshw')
makedepends=('git' 'qt5-tools' 'gtest' 'dtkcommon-git')
conflicts=('dtkcore')
provides=('dtkcore')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dtkcore.git")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $pkgname
  qmake-qt5 PREFIX=/usr DTK_VERSION=$pkgver LIB_INSTALL_DIR=/usr/lib
  make
}

package() {
  cd $pkgname
  make INSTALL_ROOT="$pkgdir" install
}
