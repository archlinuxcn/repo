# Maintainer: Alexander Couzens <lynxis@fe80.eu>
pkgname=liblms7002m-xtrx-git
_gitname="liblms7002m"
pkgver=r10.b07761b73861
pkgrel=1
pkgdesc="A Compact LMS7002 library suitable for MCU. Use by the xtrx sdr."
arch=('armv7h' 'i686' 'x86_64')
url="https://github.com/xtrx-sdr/liblms7002m"
license=('LGPL')
makedepends=('git' 'cmake' 'python-cheetah3')
source=("git+$url")
md5sums=('SKIP')
provides=('liblms7002m-xtrx')

pkgver() {
  cd "$srcdir"/$_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=12 HEAD)"
}

build() {
  mkdir -p "$srcdir"/$_gitname/build
  cd "$srcdir"/$_gitname/build

  cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release

  make
}

package() {
  cd "$srcdir"/$_gitname/build

  make DESTDIR="$pkgdir" install
}

