# Maintainer: Integral <integral@member.fsf.org>

pkgname=pacfiles
pkgver=0.3.0
pkgrel=1
pkgdesc="A pacman -F alternative that runs blazingly fast"
url="https://github.com/lilydjwg/${pkgname}"
license=('GPL-2.0-only')
arch=('x86_64' 'aarch64' 'riscv64')
depends=('libarchive' 'gcc-libs' 'plocate' 'pacman')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('684c8567eea28aa020c61502ee1b50f8b56603a63cfead81a1ead45fac5b9f49')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	install -Dm755 "${pkgname}-${pkgver}/target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
}
