# Maintainer: George Hu <integral@archlinux.org>

pkgname=dmgwiz
pkgver=1.1.1
pkgrel=1
pkgdesc="Extract filesystem data from DMG files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/citruz/${pkgname}"
license=('MIT')
depends=('bzip2' 'libgcc' 'openssl')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('dcc75eaf9042ac488cf7ef9e856418f800a88afaea2b99d66f47d2329af2202e')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export OPENSSL_NO_VENDOR=1
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export OPENSSL_NO_VENDOR=1
	CFLAGS+=" -ffat-lto-objects" cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
