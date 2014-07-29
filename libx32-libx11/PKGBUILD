# $Id: PKGBUILD 97276 2013-09-16 07:35:05Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libx11
pkgname=libx32-$_pkgbasename
pkgver=1.6.2
pkgrel=1
pkgdesc="X11 client-side library (x32 ABI)"
arch=(x86_64)
url="http://xorg.freedesktop.org/"
depends=('libx32-libxcb' $_pkgbasename)
makedepends=('xorg-util-macros' 'xextproto' 'xtrans' 'inputproto' 'gcc-multilib-x32')
options=('!libtool')
license=('custom:XFREE86')
source=(${url}/releases/individual/lib/libX11-${pkgver}.tar.bz2)
sha256sums=('2aa027e837231d2eeea90f3a4afe19948a6eb4c8b2bec0241eba7dbc8106bd16')

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
