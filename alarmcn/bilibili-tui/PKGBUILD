# Maintainer: George Hu <integral@archlinux.org>

pkgname=bilibili-tui
pkgver=1.0.6
pkgrel=1
pkgdesc="A terminal user interface (TUI) client for Bilibili"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://maredevi.moe/projects/${pkgname}"
license=('MIT')
depends=('gcc-libs' 'mpv' 'yt-dlp')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/MareDevi/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('356aba215b202468e22fed0b1d617229a0c17afd317fa6e23b170d5a515fdf17')

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
