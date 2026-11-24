# Maintainer: George Hu <integral@archlinux.org>

pkgname=bilibili-tui
pkgver=1.1.0
pkgrel=1
pkgdesc="A terminal user interface (TUI) client for Bilibili"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/MareDevi/${pkgname}"
license=('MIT')
depends=('glibc' 'libgcc' 'mpv' 'openssl' 'yt-dlp')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('f6bd7bf097478406135310c66e8d590d61c0fde0535aeaa63c04c9fe255ba419')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target $(rustc --print host-tuple)
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	CFLAGS+=" -ffat-lto-objects" cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
