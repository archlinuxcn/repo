# $Id: PKGBUILD 107112 2014-03-12 16:52:44Z bluewind $
# Maintainer: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=freetype2
pkgname=libx32-$_pkgbasename
pkgver=2.5.3
pkgrel=1
pkgdesc="TrueType font rendering library (x32 ABI)"
arch=(x86_64)
license=('GPL')
url="http://freetype.sourceforge.net"
depends=('libx32-zlib' 'libx32-bzip2' 'libx32-libpng' 'libx32-harfbuzz' $_pkgbasename)
makedepends=(gcc-multilib-x32)
options=('!libtool')
source=(http://downloads.sourceforge.net/sourceforge/freetype/freetype-${pkgver}.tar.bz2{,.sig}
        freetype-2.5.1-enable-spr.patch
        freetype-2.2.1-enable-valid.patch)
md5sums=('d6b60f06bfc046e43ab2a6cbfd171d65'
         'SKIP'
         '80a14cce234f3f190cd936ca9060c398'
         '214119610444c9b02766ccee5e220680')

prepare() {
  cd "${srcdir}/freetype-${pkgver}"
  patch -Np1 -i "${srcdir}/freetype-2.5.1-enable-spr.patch"
  patch -Np1 -i "${srcdir}/freetype-2.2.1-enable-valid.patch"
}

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/freetype-${pkgver}"

  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

package() {
  cd "${srcdir}/freetype-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
}
