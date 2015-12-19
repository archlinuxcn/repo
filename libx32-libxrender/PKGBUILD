# $Id: PKGBUILD 133791 2015-05-19 09:10:33Z bluewind $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxrender
pkgname=libx32-$_pkgbasename
pkgver=0.9.9
pkgrel=1.1
pkgdesc="X Rendering Extension client library (x32 ABI)"
arch=('x86_64')
url="http://xorg.freedesktop.org/"
license=('custom')
depends=('libx32-libx11>=1.3.4' $_pkgbasename)
makedepends=('pkgconfig' 'gcc-multilib-x32' renderproto)
options=('!libtool')
source=(${url}/releases/individual/lib/libXrender-${pkgver}.tar.bz2{,.sig})
sha256sums=('fc2fe57980a14092426dffcd1f2d9de0987b9d40adea663bd70d6342c0e9be1a'
            'SKIP')
validpgpkeys=('4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E') #Alan Coopersmith <alan.coopersmith@oracle.com>

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
