# Maintainer: Andrew Sun <adsun701 at gmail dot com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Laszlo Papp <djszapi2 at gmail dot com>
# Contributor: Shinlun Hsieh <yngwiexx at yahoo dot com dot tw>

pkgname=gxemul
pkgver=0.7.0
pkgrel=1
pkgdesc='Instruction-level machine emulator'
arch=('i686' 'x86_64')
url='http://gavare.se/gxemul/'
license=('GPL')
depends=('libx11' 'sh')
source=("http://gavare.se/gxemul/src/gxemul-${pkgver}.tar.gz")
sha256sums=('79c4437c6f8ca904f46d33ac36062a65fdcf4a92a248478e408ab11295cf8e83')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  CFLAGS="$CFLAGS -std=gnu99 -fgnu89-inline" ./configure
  sed -i 's|$(DESTDIR)$(MANDIR)/man1|$(PREFIX)/share/man/man1|g' Makefile

  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make PREFIX=${pkgdir}/usr install
}
