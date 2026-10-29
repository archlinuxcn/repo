# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: lorim <lorimz@gmail.com>

pkgname=lib32-libtiff4
pkgver=3.9.7
pkgrel=6
pkgdesc='Library for manipulation of TIFF images'
arch=(x86_64)
url=http://www.simplesystems.org/libtiff/
license=(custom)
depends=(
  lib32-gcc-libs
  lib32-glibc
  lib32-libjpeg-turbo
  lib32-zlib
)
makedepends=(git)
source=(
  git+https://gitlab.com/libtiff/libtiff.git#tag=v${pkgver}
  libtiff4-soname.patch
)
sha256sums=('b4fe4a431427dcabeac32374419271fc249453748c7e21b73c63928e668c1e54'
            'e6246631f6d943715b612b4ddd2279c946ff90c9e8d755fa639e8051a6eb3488')

prepare() {
  cd libtiff

  # Rename 3.9.7 to 4.3.7, 3.6.x was the first release with the unintentional ABI change
  patch -Np1 -i ../libtiff4-soname.patch

  ./autogen.sh
}

build() {
  cd libtiff

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH=/usr/lib32/pkgconfig

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32'
  make
}

package() {
  make DESTDIR="${pkgdir}" -C libtiff install
  rm -rf "${pkgdir}"/usr/{bin,include,lib32/libtiff{,xx}.{a,so},share}
  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s libtiff4 "${pkgdir}"/usr/share/licenses/lib32-libtiff4
}

# vim: ts=2 sw=2 et:
