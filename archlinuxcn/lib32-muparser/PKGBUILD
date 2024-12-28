# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Ronald van Haren <ronald.archlinux.org>
# Contributor: damir <damir.archlinux.org>
# Maintainer: heavysink <winstonwu91 at gmail>

pkgname=lib32-muparser
_pkgname=muparser
pkgver=2.3.5
pkgrel=1
pkgdesc="Fast math parser library (32 bit)"
arch=('x86_64')
url="http://muparser.beltoforion.de/"
license=('MIT')
depends=('muparser' 'lib32-gcc-libs')
makedepends=('gcc-multilib' 'cmake')
source=(https://github.com/beltoforion/muparser/archive/v$pkgver/$_pkgname-$pkgver.tar.gz)
sha512sums=('48610dd112b5c8e1ea7615e29c9f9ca185091392b651794de039c14edfad4c62a6ae1d087393fdfd8d03a99f94a6e71275b86ddc8027234d322030bc7c25223e')

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
