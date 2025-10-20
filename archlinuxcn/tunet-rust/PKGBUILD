# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.10.6
pkgrel=1
pkgdesc="A Tsinghua University network authentication client for Linux, written in Rust. 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/${pkgname}"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'freetype2' 'hicolor-icon-theme' 'qt6-base')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('f7998f9a901af3e501c2d29b414e5fb4bfdfbdba6df4e7fd5b6354c3c6779aef')
options=('!lto')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
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
