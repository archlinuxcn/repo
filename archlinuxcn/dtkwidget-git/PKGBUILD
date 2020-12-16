# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=dtkwidget-git
pkgver=5.4.1.r6.gd678ffe2
pkgrel=1
pkgdesc='Deepin graphical user interface library'
arch=('x86_64')
url="https://github.com/linuxdeepin/dtkwidget"
license=('LGPL3')
depends=('deepin-qt-dbus-factory-git' 'dtkcore-git' 'dtkgui-git' 'librsvg' 'qt5-multimedia' 'qt5-svg'
         'qt5-x11extras' 'startup-notification')
makedepends=('git' 'qt5-tools')
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
  sed -i '/#include <QPainter>/a #include <QPainterPath>' src/util/dwidgetutil.cpp
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
