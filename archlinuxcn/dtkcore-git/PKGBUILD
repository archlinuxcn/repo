# Maintainer: Haruyuki lxz <lxz@ilxz.me>

pkgname=dtkcore-git
pkgver=5.2.2.3.r0.g3241d4d
pkgrel=1
pkgdesc='DTK core modules'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkcore"
license=('LGPL3')
depends=('dconf' 'deepin-desktop-base' 'python' 'gsettings-qt' 'lshw')
makedepends=('git' 'qt5-tools')
conflicts=('dtkcore')
replaces=('dtkcore')
provides=('dtkcore')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dtkcore.git")
sha512sums=('SKIP')

pkgver() {
    cd dtkcore
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd dtkcore
  qmake-qt5 PREFIX=/usr DTK_VERSION=$pkgver LIB_INSTALL_DIR=/usr/lib
  make
}

package() {
  cd dtkcore
  make INSTALL_ROOT="$pkgdir" install
}
