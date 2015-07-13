# Maintainer: Antonio Rojas

pkgname=kwayland-git
pkgver=r238.0eca1f7
pkgrel=1
pkgdesc='Qt-style Client and Server library wrapper for the Wayland libraries'
arch=('i686' 'x86_64')
url='http://www.kde.org'
license=('LGPL')
depends=('qt5-base')
makedepends=('extra-cmake-modules' 'git')
provides=('kwayland')
conflicts=('kwayland')
source=('git://anongit.kde.org/kwayland.git')
md5sums=('SKIP')

pkgver() {
  cd kwayland
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake ../kwayland \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DLIB_INSTALL_DIR=lib
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
