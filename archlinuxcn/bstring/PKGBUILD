# Maintainer: Denis Yantarev <denis dot yantarev at gmail dot com>

pkgname=bstring
pkgver=1.0.2
pkgrel=1
pkgdesc='Better String Library'
url='https://mike.steinert.ca/bstring'
license=('BSD-3-Clause')

source=("https://github.com/msteinert/bstring/releases/download/v${pkgver}/bstring-${pkgver}.tar.xz")

md5sums=('549f0edb795d3acf4ce047303d131da7')

arch=('x86_64' 'i686' 'pentium4' 'armv6h' 'armv7h' 'aarch64')

makedepends=()

depends=()

optdepends=()

conflicts=()

backup=()

build() {
  cd "${srcdir}/${pkgname}-${pkgver}" || exit 1
  autoreconf -i
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}" || exit 1
  mkdir -p ${pkgdir}/usr/lib/pkgconfig "${pkgdir}/usr/include/bstring"
  install -m 0644 ./bstring/.libs/libbstring.so "${pkgdir}/usr/lib/"
  ln -s libbstring.so "${pkgdir}/usr/lib/libbstring.so.0"
  ln -s libbstring.so "${pkgdir}/usr/lib/libbstring.so.0.1.0"
  install -m 0644 ./bstring/{bstraux,bstrlib}.h "${pkgdir}/usr/include/bstring/"
  install -m 0644 ./bstring.pc "${pkgdir}/usr/lib/pkgconfig/"
}

