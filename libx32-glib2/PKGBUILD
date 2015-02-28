# $Id: PKGBUILD 122984 2014-11-23 10:25:53Z bluewind $
# Maintainer:  Ionut Biru <ibiru@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=glib2
pkgname=libx32-$_pkgbasename
pkgver=2.42.1
pkgrel=1.1
pkgdesc="Common C routines used by GTK+ 2.4 and other libs (x32 ABI)"
url="http://www.gtk.org/"
arch=('x86_64')
license=('LGPL')
depends=('libx32-dbus' 'libx32-libffi' 'libx32-pcre' 'libx32-zlib' "$_pkgbasename")
makedepends=('gcc-multilib-x32' 'python2')
options=('!docs')
source=("http://ftp.gnome.org/pub/GNOME/sources/glib/${pkgver%.*}/glib-${pkgver}.tar.xz"
        'revert-warn-glib-compile-schemas.patch')
sha256sums=('8f3f0865280e45b8ce840e176ef83bcfd511148918cc8d39df2ee89b67dcf89a'
            '049240975cd2f1c88fbe7deb28af14d4ec7d2640495f7ca8980d873bb710cc97')

prepare() {
  cd "${srcdir}/glib-${pkgver}"
  patch -Rp1 -i ../revert-warn-glib-compile-schemas.patch
}

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/glib-${pkgver}"
  PYTHON=/usr/bin/python2 ./configure --prefix=/usr --sysconfdir=/etc \
      --libdir=/usr/libx32 --with-pcre=system --disable-fam
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
