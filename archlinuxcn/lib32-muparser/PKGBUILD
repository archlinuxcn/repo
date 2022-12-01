# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: damir <damir.archlinux.org>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=lib32-muparser
_pkgname=muparser
pkgver=2.3.4
pkgrel=2
pkgdesc="Fast math parser library (32 bit)"
arch=('x86_64')
url="http://muparser.beltoforion.de/"
license=('MIT')
depends=('muparser' 'lib32-gcc-libs')
makedepends=('gcc-multilib' 'cmake')
source=(https://github.com/beltoforion/muparser/archive/v$pkgver/$_pkgname-$pkgver.tar.gz)
sha512sums=('5226fd666eaf3ff7e661bbf72e60114d0ceed10491ffa4ed2dd34cd669c6c21c037eff0388402d6b9d60b0a5a27b03ca35153e0c048328abc75dfd1eaf38ceca')

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
  install -D -m644 $_pkgname-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
