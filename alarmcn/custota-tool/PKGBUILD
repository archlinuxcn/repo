# Maintainer: Integral <integral@member.fsf.org>

pkgname=custota-tool
_srcname=Custota
pkgver=5.21
pkgrel=1
pkgdesc="Android A/B OTA updater app for custom OTA servers"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/chenxiaolong/${_srcname}"
license=('GPL-3.0-or-later')
makedepends=('git' 'cargo')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('15f7a4a683ee4b6be1868e69f6af5a351bcacbd7ed10cb5664b73bd167786b6b')

prepare() {
	cd "${_srcname}/${pkgname}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${_srcname}/${pkgname}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

package() {
	install -Dm755 "${_srcname}/${pkgname}/target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
}
