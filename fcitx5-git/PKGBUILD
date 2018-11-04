# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

pkgname=fcitx5-git
pkgver=r407.7ccf3f6
pkgrel=1
pkgdesc="Next generation of fcitx"
arch=('i686' 'x86_64')
url="https://gitlab.com/fcitx/fcitx5"
license=('GPL')
depends=('cairo' 'enchant' 'iso-codes' 'libgl' 'libxkbcommon-x11' 'pango' 'systemd' 'wayland'
         'wayland-protocols' 'xcb-imdkit-git' 'xcb-util-wm' 'libxkbfile'
    	 'fmt' 'libxkbfile' 'gdk-pixbuf2')
makedepends=('extra-cmake-modules' 'git')
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd fcitx5
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd fcitx5

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd fcitx5
  make DESTDIR="$pkgdir" install
}
