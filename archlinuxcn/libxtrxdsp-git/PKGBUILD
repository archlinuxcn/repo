# Maintainer: Alexander Couzens <lynxis@fe80.eu>
pkgname=libxtrxdsp-git
_gitname=libxtrxdsp
pkgver=r11.eec28640c0eb
pkgrel=4
pkgdesc="DSP specific function for SDR in general and XTRX in specific"
arch=('armv7h' 'i686' 'x86_64')
url="https://github.com/xtrx-sdr/libxtrxdsp"
license=('LGPL')
makedepends=('git' 'cmake')
source=("git+$url")
md5sums=('SKIP')
provides=('libxtrxdsp')
conflicts=('libxtrxdsp')

pkgver() {
  cd "$srcdir"/$_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=12 HEAD)"
}

build() {
  cd "$srcdir/$_gitname"
  mkdir -p build
  cd build
  if [ "$CARCH" = 'i686' ]; then
    FORCE_ARCH="-DFORCE_ARCH=x86"
  fi

  cmake .. \
    ${FORCE_ARCH} \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release

  make
}

package() {
  cd "$srcdir"/$_gitname/build

  make DESTDIR="$pkgdir" install
}
