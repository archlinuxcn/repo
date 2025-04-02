# Maintainer: Echo J. <aidas957 at gmail dot com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrew Eikum

pkgname=faudio
pkgver=25.04
pkgrel=1
pkgdesc="XAudio2 reimplementation"
arch=(aarch64 x86_64)
url="https://github.com/FNA-XNA/FAudio"
license=('Zlib')
depends=('sdl3')
makedepends=('cmake')
source=($url/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha512sums=('191b4947c43161c74f32da0208d752f492bcc48eb4ce5bd94824fe541ce0446ff522bfed45fdde29eb05f6938ed814dba3bde31fd06abed4bccf6a79cf334eac')

build() {
  cmake -B build -S FAudio-$pkgver --fresh \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 FAudio-$pkgver/LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
}
