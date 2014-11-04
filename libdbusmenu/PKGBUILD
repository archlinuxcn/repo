# Maintainer: alucryd <alucryd at gmail dot com>
# Contributor: Balló György <ballogyor+arch at gmail dot com>
# Contributor: Branchini Massimo <max dot bra dot gtalk at gmail dot com

pkgname=libdbusmenu
pkgver=12.10.2
pkgrel=2
pkgdesc="A library for passing menus over DBus"
arch=('i686' 'x86_64')
url="https://launchpad.net/libdbusmenu"
license=('LGPL')
depends=('gtk2' 'gtk3' 'json-glib' 'python2')
makedepends=('gnome-doc-utils' 'gobject-introspection' 'intltool' 'vala')
options=('!libtool' '!emptydirs')
source=("http://launchpad.net/dbusmenu/${pkgver%.?}/${pkgver}/+download/${pkgname}-${pkgver}.tar.gz")
sha256sums=('9d6ad4a0b918b342ad2ee9230cce8a095eb601cb0cee6ddc1122d0481f9d04c9')

prepare() {
  cd ${pkgname}-${pkgver}

  sed -i 's/install-libdbusmenu_gtkincludeHEADERS install-pkgconfigDATA/install-pkgconfigDATA/g' libdbusmenu-gtk/Makefile.in
  sed -i '/g_type_init();/d' $(grep -rl 'g_type_init();')
  sed -i 's|^#!.*python$|#!/usr/bin/python2|' tools/dbusmenu-bench
}

build() {
  cd ${pkgname}-${pkgver}

  export PYTHON=python2
  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --libexecdir="/usr/lib/${pkgname}" --disable-static
  make
}

package() {
  cd ${pkgname}-${pkgver}

  make DESTDIR="${pkgdir}" install
  make -C libdbusmenu-gtk DESTDIR="${pkgdir}" uninstall
}

# vim: ts=2 sw=2 et:
