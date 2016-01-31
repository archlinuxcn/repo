# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>

pkgname=lib32-libvpx
pkgver=1.5.0
pkgrel=1
pkgdesc='VP8 and VP9 codec'
arch=('x86_64')
url='http://www.webmproject.org/'
license=('BSD')
depends=('lib32-gcc-libs' 'libvpx')
makedepends=('gcc-multilib' 'git' 'yasm')
source=("https://storage.googleapis.com/downloads.webmproject.org/releases/webm/libvpx-${pkgver}.tar.bz2")
sha256sums=('306d67908625675f8e188d37a81fbfafdf5068b09d9aa52702b6fbe601c76797')

build() {
  cd libvpx-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --target='x86-linux-gcc' \
    --enable-vp{8,9} \
    --enable-postproc \
    --enable-runtime-cpu-detect \
    --enable-shared \
    --enable-pic \
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
