# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=24.10
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(x86_64)
url="https://github.com/FNA-XNA/FAudio/"
license=('Zlib')
depends=('sdl2' 'gst-libav')
makedepends=('cmake')
source=(https://github.com/FNA-XNA/FAudio/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('e0b2031ba8452aa0696bc841013db5558c97f87a0071cf5fb48dd668363980d6d7d1adbc22d051e5019f32ee4aaf5553ebb80d37b87e9bcde153b828be5ff127')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
