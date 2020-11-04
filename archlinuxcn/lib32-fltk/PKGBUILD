# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: xw258
# Contributor: genesis66

pkgname=lib32-fltk
pkgver=1.3.5
pkgrel=1
pkgdesc="Graphical user interface toolkit for X (32-bit)"
arch=('x86_64')
url="https://www.fltk.org"
license=('custom:LGPL')
depends=("${pkgname#lib32-}" 'lib32-glu' 'lib32-libjpeg-turbo' 'lib32-libxcursor' 'lib32-libxinerama' 'lib32-libxft')
makedepends=('cmake' 'lib32-alsa-lib' 'libxft')
options=('staticlibs')
source=("${pkgname#lib32-}-${pkgver}.tar.gz::https://github.com/fltk/fltk/archive/release-${pkgver}.tar.gz"
        "${pkgname#lib32-}-fix-lib-mess.patch")
sha512sums=('35732df4d66573fdabf95f57069c5a2df63b0029d7b904d4ac02bd4c3ab3e5b287d4f06998b67129e8195c42c0b39e137e5d4f10baf4d73992077bb5ae0bef6c'
            '14592ba5616483df1b36f6e2b8309a3d1e898c5c4dcf0ddfbb374bbd1332eca6ba3490569fc8f903023a069b7771ed06baddef36140253e2e81eb409892bbba5')

prepare() {
  mv -v "${pkgname#lib32-}-release-${pkgver}" "${pkgname#lib32-}-${pkgver}"
  cd "${pkgname#lib32-}-${pkgver}"
  # fix bizarre renaming of shared libraries
  # https://github.com/fltk/fltk/issues/20
  patch -Np1 -i ../${pkgname#lib32-}-fix-lib-mess.patch
  mkdir -v build
}

build() {
  # Modify environment to generate 32-bit ELF. Respects flags defined in makepkg.conf
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export LDFLAGS="-m32 ${LDFLAGS}"
  export PKG_CONFIG_LIBDIR='/usr/lib32/pkgconfig'

  cd "${pkgname#lib32-}-${pkgver}/build"
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
        -DFLTK_LIBDIR=/usr/lib32 \
        -DOPTION_CREATE_LINKS=ON \
        -DOPTION_BUILD_SHARED_LIBS=ON \
        ..
  make VERBOSE=1
}

package() {
  cd "${pkgname#lib32-}-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}/usr/"{bin,include,share}
  install -vDm 644 ../COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
