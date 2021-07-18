# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: damir <damir.archlinux.org>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=lib32-muparser
pkgver=2.3.2
pkgrel=2
pkgdesc="Fast math parser library (32 bit)"
arch=('x86_64')
url="http://muparser.beltoforion.de/"
license=('MIT')
depends=('muparser' 'lib32-gcc-libs')
makedepends=('gcc-multilib' 'cmake')
source=(muparser-$pkgver.tar.gz::"https://github.com/beltoforion/muparser/archive/v$pkgver.tar.gz")
sha512sums=('8ef5c8b3834da3995a782b7364a4eb4197fb706bee4cadabe5511d2a9cf2912c3db6de422a91eff7f9690f8c9c355b9900335e940749d5c243cb732ac1992aef')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  cmake -B build -S muparser-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_LIBDIR=lib32 \
    -DCMAKE_INSTALL_INCLUDEDIR=include
  VERBOSE=1 cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  # remove headers already present in muparser package
  rm -rf "$pkgdir"/usr/include
  # license
  install -d "$pkgdir"/usr/share/licenses
  ln -s muparser "$pkgdir"/usr/share/licenses/$pkgname
}
