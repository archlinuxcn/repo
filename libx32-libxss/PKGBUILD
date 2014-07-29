# $Id: PKGBUILD 115616 2014-07-12 17:35:28Z fyan $
# Maintainer: Florian Pritz <flo@xssn.at>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Alexander Baldeck <alexander@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxss
pkgname=libx32-$_pkgbasename
pkgver=1.2.2
pkgrel=2
pkgdesc="X11 Screen Saver extension library (x32 ABI)"
arch=(x86_64)
license=('custom')
url="http://xorg.freedesktop.org/"
depends=('libx32-libxext' $_pkgbasename)
makedepends=('xorg-util-macros' gcc-multilib-x32)
options=('!libtool')
source=(${url}/releases/individual/lib/libXScrnSaver-${pkgver}.tar.bz2)
sha1sums=('7b8298eec371c33a71232e3653370a98f03c6c88')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/libXScrnSaver-${pkgver}"
  ./configure --prefix=/usr --sysconfdir=/etc \
    --libdir=/usr/libx32
  make
}

package() {
  cd "${srcdir}/libXScrnSaver-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
