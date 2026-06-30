# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.11.1
pkgrel=1
pkgdesc="A Rust-based client for network authentication at Tsinghua University | 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/${pkgname}"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'curl' 'freetype2' 'hicolor-icon-theme' 'qt6-base')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('8e3ef776d9220dea9a0b86ec21cc3f44e9110c583b9bc778fdbb1704250e5c0b')
options=('!lto')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target $(rustc --print host-tuple) # --locked
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --workspace --exclude native
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features --workspace --exclude native
}

package() {
	cd "${pkgname}-${pkgver}/"

	# Binaries
	install -Dm755 target/release/tunet{,-{gui,service}} -t "${pkgdir}/usr/bin/"

	# Desktop file
	install -Dm644 "tunet/io.github.berrysoft.tunet.desktop" -t "${pkgdir}/usr/share/applications/"

	# Icon
	install -Dm644 "logo.png" "${pkgdir}/usr/share/icons/hicolor/256x256/apps/tunet.png"

	# Service
	install -Dm644 "tunet-service/tunet@.service" -t "${pkgdir}/usr/lib/systemd/system/"

	# License
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
