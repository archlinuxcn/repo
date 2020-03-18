# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_pkgname=xcb-imdkit
pkgname=${_pkgname}-git
pkgver=r68.db6cfd4
pkgrel=1
pkgdesc="Input method development support for xcb"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/xcb-imdkit"
license=('GPL')
depends=('xcb-util' 'xcb-util-keysyms')
makedepends=('extra-cmake-modules' 'git')
provides=(${_pkgname})
conflicts=(${_pkgname})
source=("git+https://github.com/fcitx/xcb-imdkit.git")
sha512sums=('SKIP')

pkgver() {
  cd xcb-imdkit
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd xcb-imdkit

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd xcb-imdkit
  make DESTDIR="$pkgdir" install
}
