# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.10.8
pkgrel=1
pkgdesc="A Rust-based client for network authentication at Tsinghua University | 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/${pkgname}"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'curl' 'freetype2' 'hicolor-icon-theme' 'qt6-base')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('662782624bf2c77b7a08c8ce176fc544e29c1cc85ebbdf69274e83f3d4c73e0f')
options=('!lto')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target $(rustc --print host-tuple)
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
