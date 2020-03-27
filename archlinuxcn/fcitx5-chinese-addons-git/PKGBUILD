# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_pkgname=fcitx5-chinese-addons
pkgname=${_pkgname}-git
pkgver=r159.a52a51d
pkgrel=1
pkgdesc="Addons related to Chinese, including IME previous bundled inside fcitx4"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5-chinese-addons"
license=('GPL')
depends=('curl' 'libime-git' 'qt5-webengine' 'fcitx5-qt5-git' 'boost-libs' 'opencc' 'fcitx5-git')
makedepends=('boost' 'extra-cmake-modules' 'git')
provides=(${_pkgname})
conflicts=(${_pkgname})
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd fcitx5-chinese-addons
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd fcitx5-chinese-addons

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd fcitx5-chinese-addons
  make DESTDIR="$pkgdir" install
}
