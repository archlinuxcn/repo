# Maintainer: George Hu <integral@archlinux.org>

pkgname=framework-tool-tui
pkgver=0.8.6
pkgrel=1
pkgdesc="TUI for controlling and monitoring Framework Computers hardware built in Rust"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/grouzen/${pkgname}"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('a648a5f2cb8c2c0312ea02a2ae8904353072a61d41d23207fc4cc0fb8212181f')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

# check() {
# 	cd "${pkgname}-${pkgver}/"
# 	export RUSTUP_TOOLCHAIN=stable
# 	CFLAGS+=" -ffat-lto-objects" cargo test --frozen --all-features
# }

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
	install -d "${pkgdir}/usr/share/doc/${pkgname}/"
	cp -a docs/* "${pkgdir}/usr/share/doc/${pkgname}/"
}
