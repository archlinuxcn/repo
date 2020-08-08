# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=dtkgui-git
pkgver=5.2.2.1.r1.gb227464
pkgrel=1
pkgdesc='Deepin Toolkit, gui module for DDE look and feel'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkgui"
license=('LGPL3')
depends=('dtkcore' 'librsvg' 'qt5-x11extras')
makedepends=('git' 'qt5-tools')
conflicts=('dtkgui')
replaces=('dtkgui')
provides=('dtkgui')
groups=('deepin-git')
source=('git://github.com/linuxdeepin/dtkgui')
sha512sums=('SKIP')

pkgver() {
    cd dtkgui
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd dtkgui
  qmake-qt5 PREFIX=/usr DTK_VERSION=$pkgver LIB_INSTALL_DIR=/usr/lib
  make
}

package() {
  cd dtkgui
  make INSTALL_ROOT="$pkgdir" install
}
