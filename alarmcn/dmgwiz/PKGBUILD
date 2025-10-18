# Maintainer: George Hu <integral@archlinux.org>

pkgname=dmgwiz
pkgver=1.1.0
pkgrel=1
pkgdesc="Extract filesystem data from DMG files"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/citruz/${pkgname}"
license=('MIT')
depends=('gcc-libs' 'bzip2')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('c2cdea92bcb934aaeea4f1797cf15e85bdb3e7b6da577cc8c974869753d11601')

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

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	CFLAGS+=" -ffat-lto-objects" cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}
