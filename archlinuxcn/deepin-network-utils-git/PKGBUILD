# Maintainer: DingYuan Zhang <justforlxz@gmail.com>

pkgname=deepin-network-utils-git
pkgver=5.1.0.2.r2.gd15232e
pkgrel=1
pkgdesc='DDE network utils'
arch=('x86_64')
url="https://github.com/linuxdeepin/dde-network-utils"
license=('GPL3')
depends=('deepin-qt-dbus-factory-git')
makedepends=('git' 'qt5-tools')
conflicts=('deepin-network-utils')
replaces=('deepin-network-utils')
provides=('deepin-network-utils')
groups=('deepin-git')
source=("git://github.com/linuxdeepin/dde-network-utils.git")
sha512sums=('SKIP')

pkgver() {
    cd dde-network-utils
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd dde-network-utils
  # Use our own url instead of third-party commercial company's homepage
  sed -i '/www.baidu.com/i \    "https://www.archlinux.org/favicon.ico",' connectivitychecker.cpp
}

build(){
  cd dde-network-utils
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd dde-network-utils
  make INSTALL_ROOT="$pkgdir" install
}
