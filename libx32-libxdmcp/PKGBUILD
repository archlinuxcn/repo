# $Id: PKGBUILD 130202 2015-03-29 19:25:46Z bluewind $
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxdmcp
pkgname=libx32-$_pkgbasename
pkgver=1.1.2
pkgrel=1.1
pkgdesc="X11 Display Manager Control Protocol library (x32 ABI)"
arch=(x86_64)
url="http://xorg.freedesktop.org/"
license=('custom')
depends=('libx32-glibc' $_pkgbasename)
makedepends=('xorg-util-macros' 'gcc-multilib-x32')
options=('!libtool')
source=(${url}/releases/individual/lib/libXdmcp-${pkgver}.tar.bz2{,.sig})
sha1sums=('3c09eabb0617c275b5ab09fae021d279a4832cac'
          'SKIP')
validpgpkeys=('4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E') # Alan Coopersmith <alan.coopersmith@oracle.com>

build() {
  cd ${srcdir}/libXdmcp-${pkgver}

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --sysconfdir=/etc --disable-static \
              --libdir=/usr/libx32
  make
}

package() {
  cd ${srcdir}/libXdmcp-${pkgver}

  make DESTDIR=${pkgdir} install

  rm -rf "${pkgdir}"/usr/{include,share}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname" 
}
