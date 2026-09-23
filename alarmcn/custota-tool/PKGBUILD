# Maintainer: Integral <integral@member.fsf.org>

pkgname=custota-tool
_srcname=Custota
pkgver=6.6
pkgrel=1
pkgdesc="Android A/B OTA updater app for custom OTA servers"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/chenxiaolong/${_srcname}"
license=('GPL-3.0-or-later')
makedepends=('git' 'cargo')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('b8c3f3bbe3243bf1ae8956cd69062a78c375d9e5961d64b5c41d60112793d6a8')

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
