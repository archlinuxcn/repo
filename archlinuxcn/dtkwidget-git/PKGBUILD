# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkwidget-git
pkgver=5.4.1.r41.g8a7765e5
pkgrel=1
pkgdesc='Deepin graphical user interface library'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkwidget"
license=('LGPL3')
depends=('deepin-qt-dbus-factory-git' 'dtkcore-git' 'dtkgui-git' 'librsvg' 'qt5-multimedia' 'qt5-svg'
         'qt5-x11extras' 'startup-notification')
makedepends=('git' 'qt5-tools' 'gtest')
provides=('dtkwidget')
conflicts=('dtkwidget')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dtkwidget.git")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd $pkgname
  sed -i 's/5\.5//g' examples/dwidget-examples/collections/collections.pro
  sed -i 's/5\.5//g' tests/tests.pro
  sed -i 's/5\.5//g' tools/svgc/svgc.pro
  sed -i 's/5\.5//g' src/src.pro
}

build() {
  cd $pkgname
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd $pkgname
  make INSTALL_ROOT="$pkgdir" install
}
