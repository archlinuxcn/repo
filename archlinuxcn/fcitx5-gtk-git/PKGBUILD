# $Id: PKGBUILD 226039 2017-04-27 13:52:30Z felixonmars $
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: csslayer <wengxt AT gmail com>

_pkgname=fcitx5-gtk
pkgname=${_pkgname}-git
pkgver=r38.22d30ef
pkgrel=1
pkgdesc="Gtk im module for fcitx5 and glib based dbus client library"
arch=('i686' 'x86_64')
url="https://github.com/fcitx/fcitx5-gtk"
license=('GPL')
depends=('fcitx5-git' 'gtk2' 'gtk3')
makedepends=('extra-cmake-modules' 'gobject-introspection' 'git')
provides=(${_pkgname})
conflicts=(${_pkgname})
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
  cd fcitx5-gtk
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build(){
  cd fcitx5-gtk

  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=/usr/lib .
  make
}

package() {
  cd fcitx5-gtk
  make DESTDIR="$pkgdir" install
}
