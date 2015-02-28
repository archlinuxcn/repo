# $Id: PKGBUILD 122173 2014-11-07 23:22:36Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# Contributor: John Proctor <jproctor@prium.net>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxml2
pkgname=libx32-$_pkgbasename
pkgver=2.9.2
pkgrel=1.1
pkgdesc="XML parsing library, version 2 (x32 ABI)"
arch=(x86_64)
license=('custom')
depends=('libx32-zlib>=1.2.4' 'libx32-readline>=6.1' 'libx32-ncurses>=5.7' $_pkgbasename)
makedepends=(gcc-multilib-x32 autoconf automake libtool-multilib)
options=('!libtool')
url="http://www.xmlsoft.org/"
source=(ftp://ftp.xmlsoft.org/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz)
md5sums=('9e6a9aca9d155737868b3dc5fd82f788')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  autoreconf -fi
  ./configure --prefix=/usr --with-threads --with-history --libdir=/usr/libx32 --without-lzma --without-python
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin} "$pkgdir/usr/libx32/xml2Conf.sh"
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
