# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Maxime Gauduin <alucryd at archlinux dot org>
# Contributor: FadeMind <fademind at gmail dot com>
# Contributor: Balló György <ballogyor+arch at gmail dot com>
# Contributor: Branchini Massimo <max.bra.gtalk at gmail dot com

pkgbase=libdbusmenu
pkgname=("${pkgbase}-glib" "${pkgbase}-gtk"{2,3})
pkgver=16.04.0
pkgrel=1
pkgdesc="A library for passing menus over DBus"
arch=('i686' 'x86_64')
url="https://launchpad.net/libdbusmenu"
license=('GPL3' 'LGPL2.1' 'LGPL3')
makedepends=('gnome-common' 'gnome-doc-utils' 'gobject-introspection' 'gtk2' 'gtk3' 'intltool' 'vala' 'valgrind')
options=('!emptydirs')
source=("https://launchpad.net/${pkgbase}/${pkgver%.?}/${pkgver}/+download/${pkgbase}-${pkgver}.tar.gz")
sha512sums=('ee9654ac4ed94bdebc94a6db83b126784273a417a645b2881b2ba676a5f67d7fc95dd2bb37bfb0890aa47299ed73cb21ed7de8b75f3fed6b69bfd39065062241')

prepare() {
  [ -d "${pkgbase}-gtk2-${pkgver}" ] && rm -rf "${pkgbase}-gtk2-${pkgver}"
  cp -a "${pkgbase}-${pkgver}" "${pkgbase}-gtk2-${pkgver}"
}

build() {
  export HAVE_VALGRIND_TRUE='#'
  export HAVE_VALGRIND_FALSE=''

  cd "${srcdir}/${pkgbase}-${pkgver}"
  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-{dumper,static,tests}
  make

  cd "${srcdir}/${pkgbase}-gtk2-${pkgver}"
  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-{dumper,static,tests} --with-gtk='2'
  make
  
}

package_libdbusmenu-glib() {
depends=('glib2')

  cd "${pkgbase}-${pkgver}"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
}

package_libdbusmenu-gtk2() {
depends=("${pkgbase}-glib" 'gtk2')

  cd "${pkgbase}-gtk2-${pkgver}"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall
}

package_libdbusmenu-gtk3() {
depends=("${pkgbase}-glib" 'gtk3')

  cd "${pkgbase}-${pkgver}"

  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-gtk DESTDIR="${pkgdir}" install
  make -j1 -C libdbusmenu-glib DESTDIR="${pkgdir}" uninstall
}
