# Maintainer: Integral <integral@member.fsf.org>

pkgname=custota-tool
_srcname=Custota
pkgver=6.2
pkgrel=1
pkgdesc="Android A/B OTA updater app for custom OTA servers"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/chenxiaolong/${_srcname}"
license=('GPL-3.0-or-later')
makedepends=('git' 'cargo')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('dd6cd614da2bcce86d67dc05b131de5c46b22db38f6b2082d09a5b98bff2c639')

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
