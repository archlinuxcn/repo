# Maintainer: Martin Hundebøll <martin@hundeboll.net>
pkgname=tio
pkgver=1.44
pkgrel=1
pkgdesc="The simple TTY terminal I/O application"
url="http://tio.github.io/"
arch=('x86_64' 'i686' 'arm' 'armv7h' 'armv6h' 'aarch64')
license=('GPLv2')
depends=('glibc' 'libinih')
makedepends=('meson')
source=("https://github.com/tio/tio/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz")
sha256sums=('3d3e20ecc44ed674816d2d0421cce42c1a7af96753d3b3bc1d7b7f6b03192cd0')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  meson --prefix=/usr --buildtype=plain . build
  meson compile -C build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  meson install -C build --destdir "$pkgdir"
}

# vim:set ts=2 sw=2 et:
