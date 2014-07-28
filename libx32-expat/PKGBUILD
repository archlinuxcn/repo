# $Id: PKGBUILD 115436 2014-07-11 10:22:04Z bluewind $
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=expat
pkgname=libx32-${_pkgbasename}
pkgver=2.1.0
pkgrel=2
pkgdesc="An XML Parser library written in C (x32 ABI)"
arch=('x86_64')
url="http://expat.sourceforge.net/"
license=('custom')
makedepends=('gcc-multilib-x32')
depends=('libx32-glibc' "${_pkgbasename}")
options=('!libtool')
source=(http://downloads.sourceforge.net/sourceforge/expat/${_pkgbasename}-${pkgver}.tar.gz)
md5sums=('dd7dab7a5fea97d2a6a43f511449b7cd')

build() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  export CC='gcc -mx32'
  export PKG_CONFIG_PATH=/usr/libx32/pkgconfig
  ./configure --prefix=/usr --libdir=/usr/libx32 --mandir=/usr/share/man 
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  install -d -m755 "${pkgdir}/usr/share/licenses/"
  ln -s ${_pkgbasename} "${pkgdir}/usr/share/licenses/${pkgname}"

  # Clean up libx32 package
  rm -rf "${pkgdir}"/usr/{bin,include,share/man}
}
