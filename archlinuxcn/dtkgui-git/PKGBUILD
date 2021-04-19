# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkgui-git
pkgver=5.4.0.r38.g5fcda3f
pkgrel=1
pkgdesc='Deepin Toolkit, gui module for DDE look and feel'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkgui"
license=('LGPL3')
depends=('dtkcore-git' 'librsvg' 'qt5-x11extras')
makedepends=('git' 'qt5-tools' 'dtkcore-git' 'librsvg' 'qt5-x11extras' 'gtest' 'gmock')
conflicts=('dtkgui')
provides=('dtkgui')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dtkgui")
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
