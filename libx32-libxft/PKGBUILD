# $Id: PKGBUILD 112785 2014-06-07 11:59:09Z bluewind $
# Maintainer: Ionut Biru <ibiru@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>
_pkgbasename=libxft
pkgname=libx32-$_pkgbasename
pkgver=2.3.2
pkgrel=1
pkgdesc="FreeType-based font drawing library for X (x32 ABI)"
arch=('x86_64')
license=('custom')
url="http://xorg.freedesktop.org/"
depends=('libx32-fontconfig' 'libx32-libxrender')
makedepends=('gcc-multilib-x32')
options=('!libtool')
source=(${url}/releases/individual/lib/libXft-${pkgver}.tar.bz2)
sha256sums=('f5a3c824761df351ca91827ac221090943ef28b248573486050de89f4bfcdc4c')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd ${srcdir}/libXft-${pkgver}
  ./configure --prefix=/usr \
    --libdir=/usr/libx32 --disable-static
  make
}

package() {
  cd "${srcdir}/libXft-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{bin,include,share}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
