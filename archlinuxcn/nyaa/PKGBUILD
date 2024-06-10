pkgname=nyaa
pkgver=0.9.0
pkgrel=1
pkgdesc="A tui tool for browsing and downloading torrents"
url='https://github.com/Beastwick18/nyaa/'
arch=(x86_64)
license=('GPL-3.0-or-later')
makedepends=(rustup)
source=("$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate")
conflicts=('nyaa')
provides=('nyaa')
b2sums=('b5dac8ea829c80e60d4a9e106db68143b5c307220daee69ef67263034fb44ed70f74a6c67af0b5c20e48d80fe62bb78e3c266ccd264f0441b76ba61f4838c454')
options=(!lto)

prepare() {
	cd $pkgname-$pkgver
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd $pkgname-$pkgver
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

check() {
	cd $pkgname-$pkgver
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd $pkgname-$pkgver
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
	install -Dm0644 -t "$pkgdir/usr/share/doc/nyaa/" "README.md"
	install -Dm0644 -t "$pkgdir/usr/share/doc/nyaa/" "CHANGELOG.md"
	install -d "${pkgdir}/usr/share/doc/nyaa/docs"
	cp -r ./docs/* "${pkgdir}/usr/share/doc/nyaa/docs"
	install -Dm0644 -t "$pkgdir/usr/share/licenses/nyaa/" "LICENSE"
}
