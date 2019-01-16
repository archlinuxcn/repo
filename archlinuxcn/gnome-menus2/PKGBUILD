# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: alucryd <alucryd at gmail dot com>
# Contributor: Balló György <ballogyor+arch at gmail dot com>
# Contributor: Jan de Groot <jan at archlinux dot org>

pkgname=gnome-menus2
pkgver=3.0.1
pkgrel=4
pkgdesc='Library for the Desktop Menu Specification (legacy version)'
arch=('i686' 'x86_64')
url='http://www.gnome.org/'
license=('LGPL')
depends=('glib2')
optdepends=('python2')
makedepends=('gobject-introspection' 'intltool')
source=("http://ftp.gnome.org/pub/gnome/sources/${pkgname%2}/${pkgver%.*}/${pkgname%2}-${pkgver}.tar.bz2")
sha256sums=('579c119c26f37781f66708e867ea45b3c37589b3b69e5b32d33e9bdb944165f0')

build() {
  cd ${pkgname%2}-$pkgver

  export PYTHON='/usr/bin/python2'
  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' --disable-static
  make
}

package(){
  cd ${pkgname%2}-$pkgver

  make -C libmenu DESTDIR="${pkgdir}" install
  make -C python DESTDIR="${pkgdir}" install
}

# vim: ts=2 sw=2 et:
