# Contributor: Andre Klitzing <aklitzing () gmail () com>

pkgname=msitools
pkgver=0.99
pkgrel=1
pkgdesc="Set of programs to inspect and build Windows Installer (.MSI) files"
arch=('i686' 'x86_64')
url="https://wiki.gnome.org/msitools"
license=('GPL')
depends=('libgsf' 'gcab')
makedepends=('intltool' 'vala')
source=(http://ftp.gnome.org/pub/GNOME/sources/msitools/${pkgver}/${pkgname}-${pkgver}.tar.xz)
sha256sums=('d475939a5e336b205eb3137bac733de8099bc74829040e065b01b15f6c8b3635')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  sed -i 's|LIBTOOL = $(SHELL) $(top_builddir)/libtool|LIBTOOL = /usr/bin/libtool|g' Makefile
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make install DESTDIR="${pkgdir}"
}

