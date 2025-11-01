# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=25.11
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(aarch64 x86_64)
url="https://github.com/FNA-XNA/FAudio"
license=('Zlib')
depends=('sdl3')
makedepends=('cmake')
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('00a3b6d7eb1fa91547f06fc0ec9bd9e7f956d2244568da3ba5144641113a6040c94c0b1d0b32da37ac1a4b51de8322afb8947c5d8817dc1e6de3214f086ee554')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
