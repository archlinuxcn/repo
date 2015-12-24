# Maintainer: Dave Reisner <d@falconindy.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Andrej Gelenberg <andrej.gelenberg@udo.edu>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=yajl
pkgname=libx32-$_pkgbasename
pkgver=2.1.0
pkgrel=1.1
pkgdesc='Yet Another JSON Library (x32 ABI)'
arch=('x86_64')
url='http://lloyd.github.com/yajl/'
license=('ISC')
makedepends=('cmake')
depends=('libx32-glibc' "${_pkgbasename}")
source=("$_pkgbasename-$pkgver.tar.gz::https://github.com/lloyd/$_pkgbasename/archive/$pkgver.tar.gz")
md5sums=('6887e0ed7479d2549761a4d284d3ecb0')

build() {
  cd "$_pkgbasename-$pkgver"

  export CC='gcc -mx32'
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=x32 .

  make
}

package() {
  cd "$_pkgbasename-$pkgver"

  make DESTDIR="$pkgdir" install

  mkdir -p "${pkgdir}/usr/libx32/pkgconfig/"
  mv "${pkgdir}"/usr/share/pkgconfig/* "${pkgdir}/usr/libx32/pkgconfig/"

  install -d -m755 "${pkgdir}/usr/share/licenses/"
  ln -s ${_pkgbasename} "${pkgdir}/usr/share/licenses/${pkgname}"

  # Clean up libx32 package
  rm -rf "${pkgdir}"/usr/{bin,include,share/pkgconfig}
}
