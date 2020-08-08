# Maintainer: Haruyuki lxz <lxz@ilxz.me>

pkgname=dtkwidget-git
pkgver=5.2.2.3.r3.g4750dbfe
pkgrel=2
pkgdesc='Deepin graphical user interface library'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkwidget"
license=('LGPL3')
depends=('deepin-qt-dbus-factory' 'dtkcore' 'dtkgui' 'librsvg' 'qt5-multimedia' 'qt5-svg'
         'qt5-x11extras' 'startup-notification')
makedepends=('git' 'qt5-tools')
replaces=('dtkwidget')
conflicts=('dtkwidget')
provides=('dtkwidget')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dtkwidget.git")
sha512sums=('SKIP')

pkgver() {
    cd dtkwidget
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd dtkwidget
  sed -i '/#include <QPainter>/a #include <QPainterPath>' src/util/dwidgetutil.cpp
}

build() {
  cd dtkwidget
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd dtkwidget
  make INSTALL_ROOT="$pkgdir" install
}
