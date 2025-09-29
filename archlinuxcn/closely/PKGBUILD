# Maintainer: George Hu <integral@archlinux.org>

pkgname=closely
pkgver=0.1.23
pkgrel=1
pkgdesc="Subscribe to updates from people you follow, from any platform to any platform"
arch=('x86_64' 'aarch64')
url="https://github.com/SpriteOvO/${pkgname}"
license=('AGPL-3.0-only')
depends=('openssl')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('bcf1e1b94c61401edad024dc70cfcc2b62c1f014e2617a1891a03351bde55fd4')

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

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
}
