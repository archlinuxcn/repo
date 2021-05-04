# Maintainer: justforlxz <justforlxz@gmail.com>

pkgname=disomaster-git
pkgver=5.0.7.r1.gb65d359
pkgrel=1
pkgdesc='Library to manipulate DISC burning.'
arch=('x86_64')
url="https://github.com/linuxdeepin/disomaster"
license=('GPL3')
depends=('libisoburn')
makedepends=('git' 'qt5-tools')
groups=('deepin-git')
provides=('disomaster')
conflicts=('disomaster')
source=("$pkgname::git://github.com/linuxdeepin/disomaster")
sha512sums=('SKIP')

pkgver() {
    cd $pkgname
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd ${pkgname}
  qmake-qt5 PREFIX=/usr
  make
}

package() {
  cd ${pkgname}
  make INSTALL_ROOT="$pkgdir" install
}
