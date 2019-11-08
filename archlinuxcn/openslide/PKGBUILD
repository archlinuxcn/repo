# Maintainer: pingplug < aur at pingplug dot me >

pkgname=openslide
pkgver=3.4.1
pkgrel=2
pkgdesc="Library that provides a simple interface to read whole-slide images"
arch=('x86_64')
url="http://openslide.org"
license=('LGPL')
depends=('openjpeg2'
         'cairo'
         'gdk-pixbuf2'
         'sqlite')
source=("https://github.com/openslide/openslide/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.xz")
sha256sums=('9938034dba7f48fadc90a2cdf8cfe94c5613b04098d1348a5ff19da95b990564')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

# vim:set ts=2 sw=2 et:
