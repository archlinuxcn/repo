# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Maxime Gauduin <alucryd at archlinux dot org>
# Contributor: FadeMind <fademind at gmail dot com>
# Contributor: Balló György <ballogyor+arch at gmail dot com>
# Contributor: Branchini Massimo <max.bra.gtalk at gmail dot com

pkgbase=libdbusmenu
pkgname=("${pkgbase}-glib" "${pkgbase}-gtk"{2,3})
pkgver=12.10.3.15.04.20150410.2
pkgrel=2
pkgdesc="A library for passing menus over DBus"
arch=('i686' 'x86_64')
url="https://launchpad.net/libdbusmenu"
license=('GPL3')
makedepends=('docbook-xsl' 'gnome-common' 'gnome-doc-utils' 'gobject-introspection' 'gtk2' 'gtk3' 'intltool' 'vala')
options=('!emptydirs')
source=("https://launchpad.net/ubuntu/+archive/primary/+files/${pkgbase}_12.10.3+15.04.20150410.2.orig.tar.gz")
sha512sums=('c15b79464bc6498cb1e912efbe648606b7bf3b5c521c4d4e5c7decf002b4e8362444177922a5abd8a057a803a8cc00e72de6e36209189eb255efb83e2ded0b06')

prepare() {
  cd "${srcdir}"
  [ -d "${pkgbase}-gtk2-12.10.3+15.04.20150410.2" ] && rm -rf "${pkgbase}-gtk2-12.10.3+15.04.20150410.2"
  cp -a "${pkgbase}-12.10.3+15.04.20150410.2" "${pkgbase}-gtk2-12.10.3+15.04.20150410.2"
}

build() {
  export HAVE_VALGRIND_TRUE='#'
  export HAVE_VALGRIND_FALSE=''

  cd "${srcdir}/${pkgbase}-12.10.3+15.04.20150410.2"
  ./autogen.sh --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-{dumper,static,tests}
  make

  cd "${srcdir}/${pkgbase}-gtk2-12.10.3+15.04.20150410.2"
  ./autogen.sh --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-{dumper,static,tests} --with-gtk='2'
  make
  
}

package_libdbusmenu-glib() {
depends=('glib2')

  cd "${srcdir}/${pkgbase}-12.10.3+15.04.20150410.2"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
}

package_libdbusmenu-gtk2() {
depends=('gtk2' 'libdbusmenu-glib')

  cd "${srcdir}/${pkgbase}-gtk2-12.10.3+15.04.20150410.2"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall
}

package_libdbusmenu-gtk3() {
depends=('gtk3' 'libdbusmenu-glib')

  cd "${srcdir}/${pkgbase}-12.10.3+15.04.20150410.2"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall
}
