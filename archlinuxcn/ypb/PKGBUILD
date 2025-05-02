# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=ypb
pkgver=0.2.6
pkgrel=1
pkgdesc="Yet another PasteBin"
url="https://github.com/st0nie/${pkgname}"
license=('AGPL-3.0-or-later')
arch=('x86_64' 'aarch64' 'riscv64')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.zip")
sha256sums=('b7d1f702ac0a613c74f800a6ce493a1a5ff577c0991dbb924613aad357199802')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --release --all-features
}

package() {
	cd "${pkgname}-${pkgver}"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"

	sed -i '/ExecStart=/s|/local||' "install/${pkgname}.service"
	install -Dm644 "install/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
}
