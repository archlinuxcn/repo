# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: "UnCO" Lin <trash__box <_at_> 163.com>
# Contributor: Andreas Radke <andyrtr <_at_> archlinux.org>

pkgname=libgcrypt15
pkgver=1.5.6
pkgrel=1
pkgdesc="General purpose cryptographic library based on the code from GnuPG"
arch=('i686' 'x86_64')
url="http://www.gnupg.org"
license=('LGPL')
depends=('libgpg-error')
source=("ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-${pkgver}.tar."{gz,gz.sig})
sha512sums=('8fced63f1bb2f3b60d456df168479ebe77acf2a8963f5dc831a25e839e0930148e21568117e54a63c69cc40650026b1ad12cb50a71d2b8665cfde226041f490d'
            'SKIP')
validpgpkeys=('D8692123C4065DEA5E0F3AB5249B39D24F25E3B6') # Werner Koch <https://www.gnupg.org/signature_key.html>

build() {
  cd libgcrypt-${pkgver}
  ./configure --prefix=/usr \
    --enable-shared \
    --disable-static \
    --disable-padlock-support
  make
}

check() {
  cd libgcrypt-${pkgver}
  make check
}

package() {
  cd libgcrypt-${pkgver}
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,include,lib/libgcrypt.so,share}  
}
