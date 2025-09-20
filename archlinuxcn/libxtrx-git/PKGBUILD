# Maintainer: Alexander Couzens <lynxis@fe80.eu>
pkgname=libxtrx-git
pkgver=r77.acb0b1cf7ab9
pkgrel=2
pkgdesc="High level API for the xtrx SDR"
_gitname=libxtrx
arch=('any')
url="https://github.com/xtrx-sdr/libxtrx"
license=('LGPL')
makedepends=('git' 'cmake')
depends=('liblms7002m-xtrx'
         'libxtrxdsp'
         'libxtrxll'
         'qcustomplot'
         'soapysdr')
source=("git+$url")
md5sums=('SKIP')
provides=('libxtrx')
conflicts=('libxtrx')

pkgver() {
  cd "$srcdir"/$_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=12 HEAD)"
}

build() {
  cd "$srcdir/$_gitname"
  mkdir -p build
  cd build

  cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Debug

  make
}

package() {
  cd "$srcdir"/$_gitname/build

  make DESTDIR="$pkgdir" install
}

