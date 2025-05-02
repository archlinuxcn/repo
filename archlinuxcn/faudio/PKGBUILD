# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=25.05
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(aarch64 x86_64)
url="https://github.com/FNA-XNA/FAudio"
license=('Zlib')
depends=('sdl3')
makedepends=('cmake')
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('5fef113376e8989990413e49e41de8a47941e56fd579267aaf895701f7edb13af1490dcc5c101fd4caf3f183c3e5c2162332c75a45dffd53e3a787d3903b762c')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
