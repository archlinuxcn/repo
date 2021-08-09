# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Vlad M. <vlad@archlinux.net>
# Contributor: Ankit R Gadiya <arch@argp.in>

pkgname=alert-after
pkgver=1.5.1
pkgrel=1
pkgdesc="Get a desktop notification after a command finishes executing"
arch=('i686' 'x86_64')
url="https://github.com/frewsxcv/alert-after"
license=('MIT' 'Apache')
depends=('libdbus')
makedepends=('cargo')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('f40dd43f667735741be95f753e52d3ec36731fcb3c3217084ad07e70dbac7a2a')

build() {
	cd "${pkgname}-${pkgver}"
	cargo build --release --all-features --target-dir=target
}

check() {
	cd "$pkgname-$pkgver"
	cargo test --release --locked --target-dir=target
}

package() {
	cd "$pkgname-$pkgver"
	install -Dm 755 target/release/aa -t "$pkgdir/usr/bin/"
}
