# Maintainer: TTsdzb <ttsdzb at outlook dot com>
# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=uni-updater
pkgver=0.3.0
pkgrel=1
pkgdesc='Helper program that updates everything on your system.'
arch=('x86_64')
url="https://codeberg.org/TTsdzb/uni-updater"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
source=("${pkgname}-${pkgver}-${pkgrel}.tar.gz::https://codeberg.org/TTsdzb/uni-updater/archive/$pkgver.tar.gz"
	)
sha512sums=('db49f4e74fedaa2027cc9b82fc8c58d1ef66bee0e6d13b5abc4d2460471b27ad96e6b463b42e8768177496ea839711bc092e6ba61b3fa7db89e2fb2c2b952f64')
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
