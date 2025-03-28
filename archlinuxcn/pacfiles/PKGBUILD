# Maintainer: Integral <integral@member.fsf.org>

pkgname=pacfiles
pkgver=0.2.7
pkgrel=2
pkgdesc="A pacman -F alternative that runs blazingly fast"
url="https://github.com/lilydjwg/${pkgname}"
license=('GPL-2.0-only')
arch=('x86_64' 'aarch64' 'riscv64')
depends=('libarchive' 'gcc-libs' 'plocate' 'pacman')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('b59b071532abdb43d2818ee878512ec14d885c6104fcc79906c8639d37b7e31d')

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
