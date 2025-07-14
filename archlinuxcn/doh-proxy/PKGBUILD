# Author of software: jedisct1
# Maintainer of this package: Jan Ole Zabel <joz@spline.de>
# Package contributors: mys_721tx, dreieck
pkgname=doh-proxy
reponame=doh-server
pkgver=0.9.12
pkgrel=2
pkgdesc="A DNS-over-HTTP server proxy written in Rust by jedisct1"
arch=('x86_64' 'aarch64')
url="https://github.com/jedisct1/$reponame"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
source=("$url/archive/$pkgver.tar.gz")
sha512sums=('819de5eedc3a6a48dd77cace9eb2dd60b82db7df71e27127efa9e961a32f53a3f7b12d7c391564f25d00223aa48091b15afec8d317ccac0157fa5d6a568ea9f6')
options=('!lto')

prepare() {
	cd "$reponame-$pkgver"
	cargo fetch
}

build() {
	# Handle manually enabled LTO
	RUSTFLAGS="${RUSTFLAGS/-C lto/}"
	export RUSTFLAGS

	cd "$reponame-$pkgver"
	cargo build --frozen --release
}

package() {
	cd "$reponame-$pkgver"
	install -Dm755 "target/release/$pkgname" "$pkgdir/usr/bin/$pkgname"
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}

