# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Maxime Gauduin <alucryd at archlinux dot org>
# Contributor: TheWaffleGuy <gvxq at hotmail dot com>
# Contributor: Andreas Radke <andyrtr at archlinux dot org>

pkgname=lib32-libgcrypt15
pkgver=1.5.4
pkgrel=1
pkgdesc='General purpose cryptographic library based on the code from GnuPG (32-bit)'
arch=('x86_64')
url='http://www.gnupg.org'
license=('LGPL')
depends=('lib32-libgpg-error')
makedepends=('gcc-multilib' 'libtool-multilib')
source=("ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-${pkgver}.tar.bz2"
		"debian_security_patches.patch")
sha512sums=('fe7e1d07eb10ee4ea8054bc955c35dc4b2109db645a08a6fa7757bf1e77a612e03c0838f9766086f04270b3621f34ccae0d6333f117cff204ccad9018c8a7908'
            'a5fe96bc83f830580391f3be92681f92057ca173407435f1800b3f05b8bfb6f87939dd573a0bf1d27afaf78f2e1fb3625b4c45ea5e9b1fddde0286ef4f3c69a6')

prepare() {
  cd libgcrypt-${pkgver}
  patch -Np1 -i "${srcdir}"/debian_security_patches.patch
  sed 's:path="amd64":path="i586 i386":' -i mpi/config.links
}

build() {
  cd libgcrypt-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --enable-shared \
    --disable-padlock-support \
    --disable-static
  make
}

package() {
  cd libgcrypt-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,include,lib32/libgcrypt.so,share}
}
