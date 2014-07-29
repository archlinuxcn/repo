# $Id: PKGBUILD 92732 2013-06-14 06:38:04Z lcarlier $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxrender
pkgname=libx32-$_pkgbasename
pkgver=0.9.8
pkgrel=1
pkgdesc="X Rendering Extension client library (x32 ABI)"
arch=('x86_64')
url="http://xorg.freedesktop.org/"
license=('custom')
depends=('libx32-libx11>=1.3.4' $_pkgbasename)
makedepends=('pkgconfig' 'gcc-multilib-x32' renderproto)
options=('!libtool')
source=(${url}/releases/individual/lib/libXrender-${pkgver}.tar.bz2)
sha256sums=('1d14b02f0060aec5d90dfdcf16a996f17002e515292906ed26e3dcbba0f4fc62')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/libXrender-${pkgver}"
  ./configure --prefix=/usr --disable-static --libdir=/usr/libx32
  make
}

package() {
  cd "${srcdir}/libXrender-${pkgver}"

  make DESTDIR=${pkgdir} install
  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
