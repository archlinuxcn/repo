# Maintainer: Integral <integral@member.fsf.org>

pkgname=live-server
pkgver=0.11.1
pkgrel=1
pkgdesc="Launch a local network server with live reload feature for static pages"
arch=('x86_64' 'aarch64')
url="https://github.com/lomirus/${pkgname}"
license=('MIT')
makedepends=('cargo')
checkdepends=('chromium')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('0501e8b5c2f3819033fd645b5011554b88a6ff96e5bd02ab17922dbee8c88bd1')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
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
	export CFLAGS+=" -ffat-lto-objects"
	cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
