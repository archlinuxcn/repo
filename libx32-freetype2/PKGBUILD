# $Id: PKGBUILD 148309 2015-12-04 05:30:35Z fyan $
# Maintainer: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=freetype2
pkgname=libx32-$_pkgbasename
pkgver=2.6.2
pkgrel=1.1
pkgdesc="TrueType font rendering library (x32 ABI)"
arch=(x86_64)
license=('GPL')
url="http://www.freetype.org/"
# adding harfbuzz for improved OpenType features auto-hinting
# introduces a cycle dep to harfbuzz depending on freetype wanted by upstream
depends=('libx32-zlib' 'libx32-bzip2' 'libx32-libpng' 'libx32-harfbuzz' $_pkgbasename)
makedepends=(gcc-multilib-x32)
source=(http://download.savannah.gnu.org/releases/freetype/freetype-${pkgver}.tar.bz2{,.sig}
        0001-Enable-table-validation-modules.patch
        0002-Enable-subpixel-rendering.patch
        0003-Enable-subpixel-hinting.patch
        0004-Mask-subpixel-hinting-with-an-env-var.patch)
sha1sums=('29c22b85b77cb22cf95c13e7062e21f39fe6b17a'
          'SKIP'
          '1c7bc438df0428a63f881e7e4343b22c5b09ecb1'
          'e2d2b8c4847ab9cfd497179c7140835e99ece711'
          'ebe3d7a6fc41304a77c23cb56e94dc718146d963'
          'f50c70080f3fbee45b9c4264d8ae37eb4f1ac335')
validpgpkeys=('58E0C111E39F5408C5D3EC76C1A60EACE707FDA5')

prepare() {
  cd "${srcdir}/freetype-${pkgver}"
  patch -Np1 -i "${srcdir}/0001-Enable-table-validation-modules.patch"
  patch -Np1 -i "${srcdir}/0002-Enable-subpixel-rendering.patch"

  # https://bugs.archlinux.org/task/35274
  patch -Np1 -i "${srcdir}/0003-Enable-subpixel-hinting.patch"
  # Provide a way to enable the above patch at runtime.
  # Hopefully just a temporary measure until fontconfig picks up
  # the necessary configurables.
  patch -Np1 -i "${srcdir}/0004-Mask-subpixel-hinting-with-an-env-var.patch"
}

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/freetype-${pkgver}"
  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

check() {
  cd "${srcdir}/freetype-${pkgver}"
  make -k check
}

package() {
  cd "${srcdir}/freetype-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -r "${pkgdir}"/usr/{include,share,bin}
}
