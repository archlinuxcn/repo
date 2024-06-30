pkgname=nyaa
pkgver=0.9.1
pkgrel=1
pkgdesc="A tui tool for browsing and downloading torrents"
url='https://github.com/Beastwick18/nyaa/'
arch=(x86_64)
license=('GPL-3.0-or-later')
makedepends=(rustup)
source=("$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate")
conflicts=('nyaa')
provides=('nyaa')
b2sums=('64a14832668dcf464abfd255ed699d297409074009a1ddf7e537022f13d48eedbb3321ed43586e93c1020e536c4f415830f9a186e4e038752c2bd274186e6967')
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
	cargo build --frozen --release
}

check() {
	cd $pkgname-$pkgver
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen
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
