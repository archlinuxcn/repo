# Maintainer: justforlxz <justforlxz@gmail.com>
# Contributor: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-qt-dbus-factory-git
pkgver=5.3.0.20.r8.g8e1181f
pkgrel=1
pkgdesc='A repository stores auto-generated Qt5 dbus code (libdframeworkdbus)'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-qt-dbus-factory"
license=('GPL3')
depends=('qt5-base')
makedepends=('git' 'dtkcore-git' 'python')
conflicts=('deepin-qt-dbus-factory')
provides=('deepin-qt-dbus-factory')
groups=('deepin-git')
source=("$pkgname::git://github.com/linuxdeepin/dde-qt-dbus-factory.git")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
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
