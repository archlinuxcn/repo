# Maintainer: mark.blakeney at bullet-systems dot net
# Contributor: David Birks <david@birks.dev>
# Contributor: David Stark <david@starkers.org>

pkgname=dive
pkgver=0.10.0
pkgrel=2
pkgdesc="A tool for exploring each layer in a docker image"
url="https://github.com/wagoodman/$pkgname"
arch=("x86_64")
license=("MIT")
makedepends=("go")
conflicts=("dive-git")
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('293e3ae853c8e7f77e4891addb4504a057ed3b6d97934cc97201031bcaa30b53')

build() {
  cd $pkgname-$pkgver
  go build \
    -trimpath \
    -ldflags "-X main.version=$pkgver" \
    -o bin/dive \
    .
}

package() {
  install -Dm 755 "$srcdir/$pkgname-$pkgver/bin/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
