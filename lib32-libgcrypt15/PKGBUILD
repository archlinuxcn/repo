# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Maxime Gauduin <alucryd at archlinux dot org>
# Contributor: TheWaffleGuy <gvxq at hotmail dot com>
# Contributor: Andreas Radke <andyrtr at archlinux dot org>

pkgname=lib32-libgcrypt15
pkgver=1.5.6
pkgrel=2
pkgdesc='General purpose cryptographic library based on the code from GnuPG (32-bit)'
arch=('x86_64')
url='http://www.gnupg.org'
license=('LGPL')
depends=('lib32-libgpg-error')
makedepends=('gcc-multilib' 'libtool-multilib')
source=("ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-${pkgver}.tar."{gz,gz.sig})
sha512sums=('8fced63f1bb2f3b60d456df168479ebe77acf2a8963f5dc831a25e839e0930148e21568117e54a63c69cc40650026b1ad12cb50a71d2b8665cfde226041f490d'
            'SKIP')
validpgpkeys=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6') # Werner Koch <https://www.gnupg.org/signature_key.html>

prepare() {
  cd libgcrypt-${pkgver}
  sed 's:path="amd64":path="i586 i386":' -i mpi/config.links
}

build() {
  # Modify environment to generate 32-bit ELF. Respects flags defined in makepkg.conf
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export LDFLAGS+=' -m32'
  export PKG_CONFIG_LIBDIR='/usr/lib32/pkgconfig'

  cd libgcrypt-${pkgver}
  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --enable-shared \
    --disable-padlock-support \
    --disable-static
  make
}

check() {
  cd libgcrypt-${pkgver}
  make check
}

package() {
  cd libgcrypt-${pkgver}
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,include,lib32/libgcrypt.so,share}
}
