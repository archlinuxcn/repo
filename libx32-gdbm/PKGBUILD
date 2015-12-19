# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: Maribu <leonidas200@web.de>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-gdbm
pkgver=1.11
pkgrel=1.1
pkgdesc="GNU database library (x32 ABI)"
arch=('x86_64')
url='http://www.gnu.org/software/gdbm/gdbm.html'
license=('GPL')
depends=('gdbm' 'libx32-glibc')
makedepends=('gcc-multilib-x32')
source=("ftp://ftp.gnu.org/gnu/gdbm/gdbm-${pkgver}.tar.gz"
        'gdbm-1.10-zeroheaders.patch')
options=('!makeflags')
sha256sums=('8d912f44f05d0b15a4a5d96a76f852e905d051bb88022fcdfd98b43be093e3c3'
            'fb4b3b3c05e85584c2d8f1af38c63219a3fb2aa152743ae6a6396e6952becc5c')

prepare() {
  cd gdbm-${pkgver}

  patch -Np1 -i ../gdbm-1.10-zeroheaders.patch
}

build() {
  cd gdbm-${pkgver}

  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/libx32' \
    --enable-libgdbm-compat
  make
}

package() {
  cd gdbm-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,share,include}
}

# vim: ts=2 sw=2 et:
