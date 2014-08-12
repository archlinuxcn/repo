# $Id: PKGBUILD 109537 2014-04-15 14:55:45Z bluewind $
# Maintainer:  Ionut Biru <ibiru@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=glib2
pkgname=libx32-$_pkgbasename
pkgver=2.40.0
pkgrel=1
pkgdesc="Common C routines used by GTK+ 2.4 and other libs (x32 ABI)"
url="http://www.gtk.org/"
arch=('x86_64')
license=('LGPL')
depends=('libx32-pcre' 'libx32-zlib' 'libx32-libdbus' libx32-libffi $_pkgbasename)
makedepends=('gcc-multilib-x32' python2)
options=('!libtool' '!docs')
source=(http://ftp.gnome.org/pub/GNOME/sources/glib/${pkgver%.*}/glib-${pkgver}.tar.xz)
sha256sums=('0d27f195966ecb1995dcce0754129fd66ebe820c7cd29200d264b02af1aa28b5')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/glib-${pkgver}"

  PYTHON=/usr/bin/python2 ./configure --prefix=/usr --sysconfdir=/etc --libdir=/usr/libx32 \
      --enable-static --enable-shared --with-pcre=system --disable-fam
  make
}

package() {
  cd "${srcdir}/glib-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/{etc,usr/{share,include}}

  cd "${pkgdir}"/usr/bin
  mv gio-querymodules gio-querymodules-x32
  rm -f gdbus glib* gobject-query gsettings gtester*
  rm -rf "$pkgdir"/usr/libx32/gdbus-2.0
  find "$pkgdir/usr/bin" -type f -not -name gio-querymodules-x32 -delete
}
