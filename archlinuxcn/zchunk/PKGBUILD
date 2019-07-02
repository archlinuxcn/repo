# Maintainer: Nikita Puzyryov <PuzyryovN@gmail.com>
pkgname=zchunk
pkgver=1.1.2
pkgrel=1
pkgdesc="A file format that allows easy deltas while maintaining good compression"
arch=(x86 x86_64)
url="https://github.com/zchunk/zchunk"
license=('BSD')
depends=('libcurl.so' 'zstd')
provides=('libzck.so')
makedepends=('meson')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('dcd7389ab9f947a53c83e32e842ba6ef69f931836bba585617a2bb7ec3cf900f')

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
