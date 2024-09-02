# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=24.09
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(x86_64)
url="https://github.com/FNA-XNA/FAudio/"
license=('Zlib')
depends=('sdl2' 'gst-libav')
makedepends=('cmake')
source=(https://github.com/FNA-XNA/FAudio/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('f74282a7df749f50026bb07309ca20fb12b098cc24b003f8b93f4f6868a3d6f4343d4bd06b947b17d9ec6c1d08f88e477da259397d745f9cc41321f7c5722448')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
