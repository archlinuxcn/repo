# Maintainer: Nikita Puzyryov <PuzyryovN@gmail.com>
pkgname=zchunk
pkgver=1.1.3
pkgrel=1
pkgdesc="A file format that allows easy deltas while maintaining good compression"
arch=(x86 x86_64)
url="https://github.com/zchunk/zchunk"
license=('BSD')
depends=('libcurl.so' 'zstd')
provides=('libzck.so')
makedepends=('meson')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('4972d488f2e035b7b6ebe2484ac5123a49ce616c2a4bcca8112841c5ed94b8b7')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  arch-meson build/
  ninja -C build/
}

check() {
  cd "$srcdir/$pkgname-$pkgver/build"
  meson test
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  DESTDIR="$pkgdir/" ninja -C build/ install
}
