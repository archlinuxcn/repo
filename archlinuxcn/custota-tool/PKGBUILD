# Maintainer: Integral <integral@member.fsf.org>

pkgname=custota-tool
_srcname=Custota
pkgver=6.1
pkgrel=1
pkgdesc="Android A/B OTA updater app for custom OTA servers"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/chenxiaolong/${_srcname}"
license=('GPL-3.0-or-later')
makedepends=('git' 'cargo')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('e7b7b527f769e55ca51d9a6088163a49b77ba8a3399171f1dd822595de8118a9')

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
