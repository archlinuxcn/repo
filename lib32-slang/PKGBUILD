# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

pkgname=lib32-slang
pkgver=2.2.4
pkgrel=2
pkgdesc='S-Lang is a powerful interpreted language'
arch=('x86_64')
url='http://www.jedsoft.org/slang/'
license=('GPL')
depends=('lib32-pcre' 'lib32-zlib' 'slang')
makedepends=('gcc-multilib')
options=('!makeflags')
source=("ftp://ftp.fu-berlin.de/pub/unix/misc/slang/v${pkgver%.*}/slang-${pkgver}.tar.bz2")
sha256sums=('9a8257a9a2a55099af858b13338dc8f3a06dd2069f46f0df2c9c3bb84a01d5db')

build() {
  cd slang-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --sysconfdir='/etc' \
    --with-onig='no'
  make
}

package() {
  cd slang-${pkgver}

  make DESTDIR="${pkgdir}" install-all
  rm -rf "${pkgdir}"/{etc,usr/{bin,include,share}}
}

# vim: ts=2 sw=2 et:
