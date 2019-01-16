# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# Contributor: Maribu <leonidas200@web.de>

pkgname=lib32-gdbm
pkgver=1.12
pkgrel=1
pkgdesc='GNU database library'
arch=('x86_64')
url='http://www.gnu.org/software/gdbm/gdbm.html'
license=('GPL')
depends=('gdbm' 'lib32-glibc')
makedepends=('gcc-multilib')
source=("ftp://ftp.gnu.org/gnu/gdbm/gdbm-${pkgver}.tar.gz"
        'gdbm-1.10-zeroheaders.patch')
options=('!makeflags')
sha256sums=('d97b2166ee867fd6ca5c022efee80702d6f30dd66af0e03ed092285c3af9bcea'
            'fb4b3b3c05e85584c2d8f1af38c63219a3fb2aa152743ae6a6396e6952becc5c')

prepare() {
  cd gdbm-${pkgver}

  patch -Np1 -i ../gdbm-1.10-zeroheaders.patch
}

build() {
  cd gdbm-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --enable-libgdbm-compat
  make
}

package() {
  cd gdbm-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,share,include}
}

# vim: ts=2 sw=2 et:
