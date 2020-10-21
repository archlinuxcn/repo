# Maintainer: Jonathon Fernyhough <jonathon_at_m2x+dev>
# Contributor: Valentin Huélamo (birdtray.desktop, now upstreamed)
# Contributor: Kr1ss <kr1ss.x#yandex#com> (cmake)
# Contributor: Dmitry Valter <dvalter"protonmail"com>

pkgname=birdtray
pkgver=1.9.0
pkgrel=1
pkgdesc="Run Thunderbird with a system tray icon."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/gyunaev/birdtray"
license=('GPL-3.0')
depends=(qt5-svg qt5-x11extras)
optdepends=('qt5-translations: Support for translations')
makedepends=(cmake qt5-tools)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
b2sums=('acc6593116fa735311f62405406192ad43e8af6481eac1d09298f846f5fab9a0dff575caefe9490d0a183c464fab763515e20e5725649fe4a800e575f712067b')

build() {
  mkdir -p build && cd build
  cmake ../$pkgname-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release
  make
}

package() {
  make -C build DESTDIR="$pkgdir" install
  install -Dm644 -t "$pkgdir"/usr/share/doc/$pkgname/ $pkgname-$pkgver/README.md
}
