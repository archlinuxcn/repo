# Maintainer: George Hu <integral@archlinux.org>

pkgname=agsh
pkgver=0.15.1
pkgrel=1
pkgdesc="An agentic shell where you speak human, not bash"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://docs.${pkgname}.sh"
license=('MIT')
depends=('glibc' 'libgcc' 'sqlite')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/k4yt3x/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('b657a4d1732e42a79abfa3f97b998193ec676b18df95ec0bd4ee7a577d0c86aa')

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
