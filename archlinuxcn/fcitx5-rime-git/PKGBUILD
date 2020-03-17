# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

pkgname=fcitx5-rime-git
pkgver=r116.bd08374
pkgrel=4
pkgdesc="RIME input method for fcitx5"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5-rime"
license=('LGPL')
depends=('boost-libs' 'curl' 'fcitx5-git' 'librime' 'opencc' 'librime-data')
makedepends=('boost' 'extra-cmake-modules' 'git')
conflicts=('fcitx-rime' 'fcitx5-rime')
provides=('fcitx5-rime')
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd fcitx5-rime
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd fcitx5-rime

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd fcitx5-rime
  make DESTDIR="$pkgdir" install
}
