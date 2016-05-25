# $Id: PKGBUILD 99752 2013-10-30 23:29:49Z allan $
# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Judd Vinet <jvinet@zeroflux.org>

pkgname=gdk-pixbuf
pkgver=0.22.0
pkgrel=12
pkgdesc="Image loading and manipulation library"
arch=('i686' 'x86_64')
url="http://www.gtk.org/"
license=('GPL' 'LGPL')
depends=('gtk' 'libtiff' 'libpng')
makedepends=('libxt')
source=(ftp://ftp.gnome.org/pub/gnome/sources/${pkgname}/0.22/${pkgname}-${pkgver}.tar.bz2
	gdk-pixbuf-0.22.0-bmp_reject_corrupt.patch
	gdk-pixbuf-0.22.0-bmp_secure.patch
	gdk-pixbuf-0.22.0-loaders.patch
	gdk-pixbuf-0.22.0.patch
	libpng15.patch)
md5sums=('05fcb68ceaa338614ab650c775efc2f2'
         'd1fb93f1ae994875158a7e0c108c36f8'
         '5f59d5772b1482d885a180dbc581cf84'
         '3cf31ae0509747f72ac27a9fd96109c2'
         'e0f5f301ce958b7cea0be631ed7b8e56'
         '16db4dc83d507ebcf15d1beb753a77bc')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  export SED=/bin/sed
  patch -Np1 -i ${srcdir}/gdk-pixbuf-0.22.0-bmp_reject_corrupt.patch
  patch -Np0 -i ${srcdir}/gdk-pixbuf-0.22.0-bmp_secure.patch
  patch -Np1 -i ${srcdir}/gdk-pixbuf-0.22.0-loaders.patch
  patch -Np0 -i ${srcdir}/gdk-pixbuf-0.22.0.patch
  patch -Np1 -i ${srcdir}/libpng15.patch
  sed -i \
    -e 's|AM_CONFIG_HEADER|AC_CONFIG_HEADER|' \
    -e 's|AM_PROG_CC_STDC|AC_PROG_CC|' \
    configure.in
  libtoolize --force --copy --automake
  autoreconf --force --install
  ./configure --prefix=/usr --disable-gtk-doc
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make DESTDIR=${pkgdir} install
  rm -rf ${pkgdir}/usr/share/gnome
}
