# $Id: PKGBUILD 116430 2014-07-27 16:12:15Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxext
pkgname=libx32-$_pkgbasename
pkgver=1.3.3
pkgrel=1
pkgdesc="X11 miscellaneous extensions library (x32 ABI)"
arch=(x86_64)
url="http://xorg.freedesktop.org/"
license=('custom')
depends=('libx32-libx11' $_pkgbasename)
makedepends=('xorg-util-macros' 'gcc-multilib-x32')
options=('!libtool')
source=(${url}/releases/individual/lib/libXext-${pkgver}.tar.bz2)
sha256sums=('b518d4d332231f313371fdefac59e3776f4f0823bcb23cf7c7305bfb57b16e35')

build() {
  cd "${srcdir}/libXext-${pkgver}"

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --sysconfdir=/etc --disable-static --libdir=/usr/libx32
  make
}

package() {
  cd "${srcdir}/libXext-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname" 
}
