# $Id: PKGBUILD 121059 2014-10-20 10:54:34Z alucryd $
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Balló György <ballogyor+arch@gmail.com>
# Contributor: Branchini Massimo <max.bra.gtalk@gmail.com

pkgbase=lib32-libdbusmenu
_pkgbasename=libdbusmenu
pkgname=('lib32-libdbusmenu-glib' 'lib32-libdbusmenu-gtk3')
pkgver=12.10.2
pkgrel=3
pkgdesc="A library for passing menus over DBus"
arch=('i686' 'x86_64')
url="https://launchpad.net/libdbusmenu"
license=('GPL3')
makedepends=('gnome-doc-utils' 'gobject-introspection' 'lib32-gtk3' 'intltool' 'vala')
options=('!emptydirs')
source=("http://launchpad.net/dbusmenu/${pkgver%.?}/${pkgver}/+download/${_pkgbasename}-${pkgver}.tar.gz")
sha256sums=('9d6ad4a0b918b342ad2ee9230cce8a095eb601cb0cee6ddc1122d0481f9d04c9')

build() {
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  cd ${_pkgbasename}-${pkgver}

  export HAVE_VALGRIND_TRUE='#'
  export HAVE_VALGRIND_FALSE=''

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libdir=/usr/lib32 --disable-{dumper,static,tests}
  make
}

package_lib32-libdbusmenu-glib() {
depends=('lib32-glib2' 'libdbusmenu-glib')

  cd ${_pkgbasename}-${pkgver}

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
}

package_lib32-libdbusmenu-gtk3() {
depends=('lib32-gtk3' 'lib32-libdbusmenu-glib' 'libdbusmenu-gtk3')

  cd ${_pkgbasename}-${pkgver}

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall

  rm -rf "${pkgdir}"/usr/{include,share,bin}
}

# vim: ts=2 sw=2 et:
