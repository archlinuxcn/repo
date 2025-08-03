# Maintainer: TTsdzb <ttsdzboutlook dot com>
# Maintainer: Jia Yin<lok-ation at outlook dot com>

pkgname=uni-updater
pkgver=0.2.4
pkgrel=1
pkgdesc='Helper program that updates everything on your system.'
arch=('x86_64')
url="https://codeberg.org/TTsdzb/uni-updater"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
source=("${pkgname}-${pkgver}-${pkgrel}.tar.gz::https://codeberg.org/TTsdzb/uni-updater/archive/$pkgver.tar.gz"
	)
sha512sums=('33a35ac7617257cde78bf574c5896593a2a2f70efb74690d6403ba6ce282cd4362a5089adef1b3ccea83ae7530c4643803e697b1ece898b82da33ec7c239bc7b')
prepare() {
	cd "$pkgbase"
	cargo update
	cargo fetch --locked --target "$CARCH-unknown-linux-gnu"
}

build() {
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cd "$pkgbase"
	cargo build --release --frozen --all-features
}

package() {
	cd "$pkgbase"
	install -Dm755 -t "$pkgdir/usr/bin" target/release/uni-updater
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}
