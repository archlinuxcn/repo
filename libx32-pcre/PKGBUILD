# $Id: PKGBUILD 109541 2014-04-15 14:58:31Z bluewind $
# Maintainer: Ionut Biru <ibiru@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=pcre
pkgname=libx32-$_pkgbasename
pkgver=8.35
pkgrel=1
pkgdesc="A library that implements Perl 5-style regular expressions (x32 ABI)"
arch=('x86_64')
url="http://pcre.sourceforge.net"
license=('custom')
depends=('libx32-gcc-libs' $_pkgbasename)
makedepends=('gcc-multilib-x32')
source=(ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/${_pkgbasename}-${pkgver}.tar.bz2{,.sig})
md5sums=('6aacb23986adccd9b3bc626c00979958'
         'SKIP')

build() {
  cd "${srcdir}"/${_pkgbasename}-${pkgver}
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --libdir=/usr/libx32 \
    --enable-utf --enable-unicode-properties --enable-pcre16 --enable-pcre32 --enable-jit
  make
}

check() {
  cd "${srcdir}"/${_pkgbasename}-${pkgver}

  make -j1 check
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
