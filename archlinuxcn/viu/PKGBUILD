# Maintainer: Wesley Moore <wes@wezm.net>

pkgname=viu
pkgver=1.2.1
_pkgver=1.2.1
pkgrel=1
pkgdesc='A command-line application to view images from the terminal written in Rust'
arch=('x86_64')
url='https://github.com/atanunq/viu'
license=('MIT')
depends=()
conflicts=('viu-git')
makedepends=('cargo')
source=("$pkgver.tar.gz::$url/archive/v$_pkgver.tar.gz")
sha256sums=('e4055c66b90173c51311a9c9868bba9e6cca80489c121b305905f930948b17a0')

build() {
  cd "$pkgname-$_pkgver"
  cargo build --release --locked
}

package() {
  install -Dm755 "$srcdir/$pkgname-$_pkgver/target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
  install -Dm644 "$srcdir/$pkgname-$_pkgver/LICENSE-MIT" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
