# $Id: PKGBUILD 114599 2014-07-02 07:47:19Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Travis Willard <travis@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libpng
pkgname=libx32-$_pkgbasename
pkgver=1.6.12
_apngver=1.6.12
_libversion=16
pkgrel=1
pkgdesc="A collection of routines used to create PNG format graphics files (x32 ABI)"
arch=('x86_64')
url="http://www.libpng.org/pub/png/libpng.html"
license=('custom')
depends=('libx32-zlib' $_pkgbasename)
makedepends=(gcc-multilib-x32)
options=('!libtool')
source=("http://downloads.sourceforge.net/sourceforge/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.xz"{,.asc}
        "http://downloads.sourceforge.net/sourceforge/libpng-apng/libpng-${_apngver}-apng.patch.gz")
md5sums=('ee752da8aa75076500e4cf31318e636e'
         'SKIP'
         'f959e8b1cb9876ce946a2701e8aca519')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  # Add animated PNG (apng) support
  # see http://sourceforge.net/projects/libpng-apng/
  patch -p1 -i "${srcdir}/libpng-${_apngver}-apng.patch"

  ./configure --prefix=/usr --libdir=/usr/libx32 --program-suffix=-x32 --disable-static
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  make DESTDIR="${pkgdir}" install

  cd contrib/pngminus
  make PNGLIB="-L${pkgdir}/usr/libx32 -lpng" -f makefile.std png2pnm pnm2png

  rm -rf "${pkgdir}"/usr/{include,share}

  rm "$pkgdir/usr/bin/libpng-config"
  ln -s "libpng${_libversion}-config-x32" "$pkgdir/usr/bin/libpng-config-x32"

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
