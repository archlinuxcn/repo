# Maintainer: Integral <integral@member.fsf.org>

pkgname=tunet-rust
pkgver=0.12.1
pkgrel=1
pkgdesc="A Rust-based client for network authentication at Tsinghua University | 清华大学校园网 Rust 客户端"
url="https://github.com/Berrysoft/${pkgname}"
arch=('x86_64' 'aarch64')
license=('MIT')
depends=('openssl' 'curl' 'freetype2' 'hicolor-icon-theme' 'qt6-base')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('1ab7f9c66fa61c2a82dbeff23e325b2f3b8b31da4c3b54ec9df7a1f1d8e080e8')
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
	install -Dm755 target/release/tunet -t "${pkgdir}/usr/bin/"

	# Desktop file
	install -Dm644 "tunet/io.github.berrysoft.tunet.desktop" -t "${pkgdir}/usr/share/applications/"

	# Icon
	install -Dm644 "logo.png" "${pkgdir}/usr/share/icons/hicolor/256x256/apps/tunet.png"

	# Service
	install -Dm644 tunet-service/tunet{,-dbus}.service -t "${pkgdir}/usr/lib/systemd/user/"

	# License
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
