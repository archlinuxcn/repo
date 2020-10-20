# Maintainer: Wesley Moore <wes@wezm.net>

pkgname=viu
pkgver=1.1.0
_pkgver=1.1
pkgrel=1
pkgdesc='A command-line application to view images from the terminal written in Rust'
arch=('x86_64')
url='https://github.com/atanunq/viu'
license=('MIT')
depends=()
conflicts=('viu-git')
makedepends=('cargo')
source=("$pkgver.tar.gz::$url/archive/v$_pkgver.tar.gz")
sha256sums=('22699390fd9501394e10fcd81a3d6a8633e9b7c9d2083529c7edbae27229bbc6')

build() {
  cd "$pkgname-$_pkgver"
  cargo build --release --locked
}

package() {
  install -Dm755 "$srcdir/$pkgname-$_pkgver/target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$_pkgver/LICENSE-MIT" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
