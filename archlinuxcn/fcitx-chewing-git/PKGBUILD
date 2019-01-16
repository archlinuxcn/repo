# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from community/fcitx-chewing; original contributors:
# Contributor: Felix Yan <felixonmars@gmail.com>

_pkgname=fcitx-chewing
pkgname=$_pkgname-git
pkgver=0.2.3.r4.ge4bb273
pkgrel=4
pkgdesc='Fcitx Wrapper for chewing'
arch=(i686 x86_64)
url='https://gitlab.com/fcitx/fcitx-chewing'
license=(GPL2)
depends=(libchewing-git fcitx)
makedepends=(cmake git)
source=("git+https://gitlab.com/fcitx/fcitx-chewing.git")
md5sums=('SKIP')
conflicts=("$_pkgname")
provides=("$_pkgname=$pkgver")

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd $_pkgname

  mkdir -p build
}

build() {
  cd $_pkgname/build

  cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    ..

  make
}

package() {
  cd $_pkgname/build

  make DESTDIR="$pkgdir" install
}
