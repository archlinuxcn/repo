# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: FadeMind <fademind at gmailn dot com>
# Contributor: alucryd <alucryd at gmail dot com>
# Contributor: Balló György <ballogyor+arch at gmail dot com>

pkgname=libdbusmenu-gtk2
pkgver=12.10.2
pkgrel=4
pkgdesc="A library for passing menus over DBus"
arch=('i686' 'x86_64')
url="https://launchpad.net/libdbusmenu"
license=('GPL3')
depends=('gtk2' 'libdbusmenu-glib')
makedepends=('gnome-doc-utils' 'gobject-introspection' 'intltool' 'vala')
options=('!emptydirs')
source=("http://launchpad.net/dbusmenu/${pkgver%.*}/${pkgver}/+download/${pkgname%-*}-${pkgver}.tar.gz")
sha512sums=('cf2e50dc3adbf35d0a4ccdd62a3efd9fae2d079b8d06e6522b70f077f89ac2cf72188e380f476e38d184b69549e90b801bf1e32174fa94bbe612dd52aec94496')

build() {
  cd ${pkgname%-*}-${pkgver}

  export HAVE_VALGRIND_TRUE='#'
  export HAVE_VALGRIND_FALSE=''
  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-{dumper,static,tests} --with-gtk='2'
  make
}

package() {
  cd ${pkgname%-*}-${pkgver}

  make -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall
}
