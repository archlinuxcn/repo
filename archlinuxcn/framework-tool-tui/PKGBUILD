# Maintainer: George Hu <integral@archlinux.org>

pkgname=framework-tool-tui
pkgver=0.5.7
pkgrel=1
pkgdesc="TUI for controlling and monitoring Framework Computers hardware built in Rust"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/grouzen/${pkgname}"
license=('MIT')
depends=('gcc-libs')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('cc97341ba72dcf3aeedfce7435c2e72be198bceef9ce97231f3d5c0743c00800')

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
