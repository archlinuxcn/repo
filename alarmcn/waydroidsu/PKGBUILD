# Maintainer: George Hu <integral@archlinux.org>

pkgname=waydroidsu
_srcname=WaydroidSU
pkgver=0.1.2
pkgrel=1
pkgdesc="CLI Magisk manager and installer for Waydroid written in Rust"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/mistrmochov/${_srcname}"
license=('GPL-3.0-or-later')
depends=('gcc-libs' 'openssl' 'dbus' 'waydroid')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('bfc1341b7d2c9649ba1a87fd97472ab9c83edc711b3edd5c6733616bd09256ad')

prepare() {
	cd "${_srcname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${_srcname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

package() {
	cd "${_srcname}-${pkgver}/"
	install -Dm755 target/release/wsu -t "${pkgdir}/usr/bin/"
	install -Dm644 docs/* -t "${pkgdir}/usr/share/doc/${pkgname}/"
}
