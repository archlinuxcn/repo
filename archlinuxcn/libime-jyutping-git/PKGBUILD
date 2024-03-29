# Maintainer: Rocket Aaron <i at rocka dot me>

_pkgname=libime-jyutping
pkgname=${_pkgname}-git
pkgver=1.0.10.r1.g773251a
pkgrel=1
pkgdesc="A library make use of libime to implement jyutping (粵拼) input method, also includes engine for fcitx 5 (git version)"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/libime-jyutping"
license=('LGPL-2.1-or-later')
depends=('fcitx5-chinese-addons-git')
makedepends=('boost' 'extra-cmake-modules' 'fmt' 'ninja' 'git')
source=("git+https://github.com/fcitx/libime-jyutping.git")
sha512sums=('SKIP')

pkgver() {
  cd ${_pkgname}
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd ${_pkgname}
  git submodule update --init --recursive
}

build(){
  cmake -B build -GNinja -S ${_pkgname} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
