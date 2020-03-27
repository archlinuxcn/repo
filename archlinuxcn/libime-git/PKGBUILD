# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

pkgname=libime-git
pkgver=r153.a78efdf
pkgrel=1
pkgdesc="A library to support generic input method implementation"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/libime"
license=('GPL')
depends=('boost-libs' 'fcitx5-git')
makedepends=('boost' 'extra-cmake-modules' 'git' 'python')
conflicts=('libime')
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd libime
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd libime
  git submodule update --init
}

build(){
  cd libime

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd libime
  make DESTDIR="$pkgdir" install
}
