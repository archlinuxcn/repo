# $Id: PKGBUILD 143653 2015-10-11 15:22:32Z alucryd $
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: jtts <jussaar@mbnet.fi>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Federico Quagliata <quaqo@despammed.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-cracklib
pkgver=2.9.4
pkgrel=1.1
pkgdesc='Password Checking Library (x32 ABI)'
arch=('x86_64')
url='http://sourceforge.net/projects/cracklib'
license=('GPL')
depends=('cracklib' 'libx32-zlib')
makedepends=('gcc-multilib-x32')
source=("http://downloads.sourceforge.net/sourceforge/cracklib/cracklib-${pkgver}.tar.gz")
sha256sums=('f2a866b4b9808344228ea6d68b69e3ba9a8a99210e23dfd718d4b95c60be8958')

build() {
  cd cracklib-${pkgver}

  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/libx32' \
    --sbindir='/usr/bin' \
    --without-python
  make
}

package() {
  cd cracklib-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{include,bin,share}
}

# vim: ts=2 sw=2 et:
