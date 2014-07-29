# Maintainer: Sven-Hendrik Haase <sh@lutzhaase.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>
_pkgbasename=libxslt
pkgname=libx32-libxslt
pkgver=1.1.28
pkgrel=2
pkgdesc="XML stylesheet transformation library (x32 ABI)"
arch=('x86_64')
url="http://xmlsoft.org/XSLT/"
license=('custom')
depends=('libx32-libxml2' 'libx32-libgcrypt' 'libxslt')
makedepends=(gcc-multilib-x32)
options=(!libtool)
source=(ftp://xmlsoft.org/libxslt/${_pkgbasename}-${pkgver}.tar.gz)
md5sums=('9667bf6f9310b957254fdcf6596600b7')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  sed -e 's|/usr/bin/python -u|/usr/bin/python2 -u|g' -e 's|/usr/bin/python$|/usr/bin/python2|g' -i python/tests/*.py
  ./configure --prefix=/usr --libdir=/usr/libx32 --without-python
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -d "${pkgdir}"/usr/share/licenses
  ln -s ${_pkgbasename} "${pkgdir}"/usr/share/licenses/${pkgname}

  rm -rf "${pkgdir}"/usr/{include,share,bin}
  rm -f "${pkgdir}"/usr/lib/python*/site-packages/*.a
}
