# Maintainer: George Hu <integral@archlinux.org>

pkgname=counts
pkgver=1.0.6
pkgrel=3
pkgdesc="A tool for ad hoc profiling"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/nnethercote/${pkgname}"
license=('Unlicense')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('4d3394b32afa98b91fd624a9c4df690d07fa1d6559cd87bb82a4bde6131fbc5f')

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
