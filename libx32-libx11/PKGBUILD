# $Id: PKGBUILD 129545 2015-03-18 18:27:18Z lcarlier $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libx11
pkgname=libx32-$_pkgbasename
pkgver=1.6.3
pkgrel=1.1
pkgdesc="X11 client-side library (x32 ABI)"
arch=(x86_64)
url="http://xorg.freedesktop.org/"
depends=('libx32-libxcb' $_pkgbasename)
makedepends=('xorg-util-macros' 'xextproto' 'xtrans' 'inputproto' 'gcc-multilib-x32')
options=('!libtool')
license=('custom:XFREE86')
source=(${url}/releases/individual/lib/libX11-${pkgver}.tar.bz2{,.sig})
sha256sums=('cf31a7c39f2f52e8ebd0db95640384e63451f9b014eed2bb7f5de03e8adc8111'
            'SKIP')
validpgpkeys=('4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E')

build() {
  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/libX11-${pkgver}"
  ./configure --prefix=/usr --disable-static --disable-xf86bigfont \
      --libdir=/usr/libx32 --disable-specs
  make
}

check() {
  cd "${srcdir}/libX11-${pkgver}"

  make check
}

package() {
  cd "${srcdir}/libX11-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
