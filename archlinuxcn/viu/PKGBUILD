# Maintainer: orhun <orhunparmaksiz@gmail.com>
# Contributor: Wesley Moore <wes@wezm.net>
# https://github.com/orhun/pkgbuilds

pkgname=viu
pkgver=1.2.1
pkgrel=2
pkgdesc="Simple terminal image viewer"
arch=('x86_64')
url="https://github.com/atanunq/viu"
license=('MIT')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('22d8a4260552d49e8cf269a52262b40f02f4be84e799aab111cdac4ff57e2998ed6c61975ed7e90ecd25ad163aee4c3c9662720c119fb9134452396b76c21665')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release --locked --all-features
}

check() {
  cd "$pkgname-$pkgver"
  cargo test --release --locked
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm 755 "target/release/$pkgname" -t "$pkgdir/usr/bin"
  install -Dm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm 644 LICENSE-MIT -t "$pkgdir/usr/share/licenses/$pkgname"
}
