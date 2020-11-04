# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: schuay <jakob.gruber@gmail.com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: Kazuo Teramoto <kaz.rag at gmail dot com>
# Contributor: damir <damir@archlinux.org>

pkgname=lib32-libcdio
pkgver=2.0.0
pkgrel=3
pkgdesc="GNU Compact Disc Input and Control Library (32-bit)"
arch=("x86_64")
license=("GPL3")
url="https://www.gnu.org/software/${pkgname#lib32-*}/"
depends=("lib32-gcc-libs" "${pkgname#lib32-*}")
source=(https://ftp.gnu.org/gnu/${pkgname#lib32-*}/${pkgname#lib32-*}-${pkgver}.tar.gz{,.sig})
sha256sums=("1b481b5da009bea31db875805665974e2fc568e2b2afa516f4036733657cf958"
            "1ca33fe6e86266f7829f0d4cdef36e0268144484c86090d6608fa53da782e8ac")
validpgpkeys=("DAA63BC2582034A02B923D521A8DE5008275EC21") # R. Bernstein

prepare() {
  cd "${pkgname#lib32-*}-${pkgver}"
  autoreconf -fi
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd "${pkgname#lib32-*}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --disable-vcd-info \
    --enable-cpp-progs \
    --libdir=/usr/lib32 \
    --without-cd-drive \
    --without-cd-info \
    --without-cdda-player \
    --without-cd-read \
    --without-iso-info \
    --without-iso-read \
    --disable-cddb
  make
}

package() {
  cd "${pkgname#lib32-*}-${pkgver}"
  make -j1 DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}/usr/bin" "${pkgdir}/usr/include" "${pkgdir}/usr/share"
}
