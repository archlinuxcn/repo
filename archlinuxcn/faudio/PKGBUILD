# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=25.02
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(aarch64 x86_64)
url="https://github.com/FNA-XNA/FAudio"
license=('Zlib')
depends=('sdl3')
makedepends=('cmake')
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('1d93b0d167e23ea2f012ec10ca1227e05ff1b81aa9568ab35bb6335622a62bacb5ed33b788ef6e953050a3bfa7d15e6a9579821cf5e36c239998a0e1271c9c1e')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SDL3=ON
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
