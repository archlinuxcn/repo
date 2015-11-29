# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>

pkgname=lib32-libvpx
pkgver=1.4.0
pkgrel=4
pkgdesc='VP8 and VP9 codec'
arch=('x86_64')
url='http://www.webmproject.org/'
license=('BSD')
depends=('lib32-gcc-libs' 'libvpx')
makedepends=('gcc-multilib' 'git' 'yasm')
source=("https://storage.googleapis.com/downloads.webmproject.org/releases/webm/libvpx-${pkgver}.tar.bz2")
sha256sums=('f582d9b2d60a592a4a3d8c32965ca2d2167e9ade38c6c30bac8801ff66a118e4')

build() {
  cd libvpx-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --target='x86-linux-gcc' \
    --enable-pic \
    --enable-postproc \
    --enable-runtime-cpu-detect \
    --enable-shared \
    --enable-vp{8,9} \
    --disable-install-{bins,docs,srcs}
  make
}

package() {
  cd libvpx-${pkgver}

  make DIST_DIR="${pkgdir}/usr" install
  rm -rf "${pkgdir}"/usr/include

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s libvpx "${pkgdir}"/usr/share/licenses/lib32-libvpx
}

# vim: ts=2 sw=2 et:
