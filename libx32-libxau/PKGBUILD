# $Id: PKGBUILD 91755 2013-05-27 09:10:06Z bluewind $
# Maintainer: Alexander Baldeck <alexander@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>
_pkgbasename=libxau
pkgname=libx32-$_pkgbasename
pkgver=1.0.8
pkgrel=1
pkgdesc="X11 authorisation library (x32 ABI)"
arch=(x86_64)
url="http://xorg.freedesktop.org/"
depends=('libx32-glibc' $_pkgbasename)
makedepends=('pkgconfig' 'xproto>=7.0.15' 'gcc-multilib-x32')
license=('custom')
options=('!libtool')
source=(${url}/releases/individual/lib/libXau-${pkgver}.tar.bz2)
sha1sums=('d9512d6869e022d4e9c9d33f6d6199eda4ad096b')

build() {
  cd "${srcdir}/libXau-${pkgver}"

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --sysconfdir=/etc --libdir=/usr/libx32
  make
}

package() {
  cd "${srcdir}/libXau-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
