# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: damir <damir.archlinux.org>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=lib32-muparser
_pkgname=muparser
pkgver=2.3.3
pkgrel=2
pkgdesc="Fast math parser library (32 bit)"
arch=('x86_64')
url="http://muparser.beltoforion.de/"
license=('MIT')
depends=('muparser' 'lib32-gcc-libs')
makedepends=('gcc-multilib' 'cmake')
source=(https://github.com/beltoforion/muparser/archive/v$pkgver-1/$_pkgname-$pkgver.tar.gz)
sha512sums=('f7e01c83f6ffe71e240653c47fdb8f3152d7fdf61b5997a3c717dec50d0175065c4fc4241ec95fb35b60b968c5c965a820009163ebe84f0fa57d64b3a23226b4')

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  cmake -B build -S muparser-$pkgver-1 \
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
  install -D -m644 $_pkgname-$pkgver-1/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
