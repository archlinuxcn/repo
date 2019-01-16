# Contributor: Andre Klitzing <aklitzing () gmail () com>

pkgname=msitools
pkgver=0.98
pkgrel=1
pkgdesc="Set of programs to inspect and build Windows Installer (.MSI) files"
arch=('i686' 'x86_64')
url="https://wiki.gnome.org/msitools"
license=('GPL')
depends=('libgsf' 'gcab')
makedepends=('intltool' 'vala')
source=(http://ftp.gnome.org/pub/GNOME/sources/msitools/${pkgver}/${pkgname}-${pkgver}.tar.xz)
sha256sums=('4c7198c82a6b2116515fb6f7b6e4c3cae9aeec0f6e6090e532ec4e6e871d8ba7')

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

