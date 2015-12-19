# $Id: PKGBUILD 126747 2015-01-29 15:09:32Z alucryd $
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-db
pkgver=5.3.28
pkgrel=2.1
pkgdesc="The Berkeley DB embedded database system (x32 ABI)"
arch=('x86_64')
url='http://www.oracle.com/technology/software/products/berkeley-db/index.html'
license=('custom')
depends=("db=${pkgver}" 'libx32-gcc-libs')
makedepends=('gcc-multilib-x32')
source=("http://download.oracle.com/berkeley-db/db-${pkgver}.tar.gz")
sha256sums=('e0a992d740709892e81f9d93f06daf305cf73fb81b545afe72478043172c3628')

build() {
  cd db-${pkgver}/build_unix

  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'

  ../dist/configure \
    --prefix='/usr' \
    --libdir='/usr/libx32' \
    --enable-compat185 \
    --enable-cxx \
    --enable-dbm \
    --enable-shared
  make LIBSO_LIBS='-lpthread'
}

package() {
  cd db-${pkgver}/build_unix

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,docs,include,share}

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s db "${pkgdir}"/usr/share/licenses/libx32-db
}

# vim: ts=2 sw=2 et:
