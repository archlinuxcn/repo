# Maintainer: George Hu <integral@archlinux.org>

pkgname=meka
pkgver=0.29.0
pkgrel=1
pkgdesc="A general-purpose AI agent harness"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://docs.${pkgname}.so"
license=('MIT')
depends=('glibc' 'libgcc' 'sqlite')
makedepends=('cargo')
optdepends=('bubblewrap: sandbox support')
provides=('agsh')
replaces=('agsh')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/k4yt3x/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('d4a997df7185c21e654b8e5a0a8778be8eac544cce0e17a33bdc5f52c0a4d913')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	export CFLAGS+=" -ffat-lto-objects"
	cargo build --frozen --release --all-features
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 "target/release/${pkgname}" -t "${pkgdir}/usr/bin/"
	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
	install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
}
