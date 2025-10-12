# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=25.10
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(aarch64 x86_64)
url="https://github.com/FNA-XNA/FAudio"
license=('Zlib')
depends=('sdl3')
makedepends=('cmake')
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('08f4f8ca74c2c8d885b88388d420691358ca357b1f3f03bb1aa778cb0b9115e4ed7446fedaaa83c5b95e8a306ad596acb090fe6dfa11055b7588a342f8bf185c')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
