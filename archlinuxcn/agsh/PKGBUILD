# Maintainer: George Hu <integral@archlinux.org>

pkgname=agsh
pkgver=0.21.1
pkgrel=1
pkgdesc="An agentic shell where you speak human, not bash"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://docs.${pkgname}.sh"
license=('MIT')
depends=('glibc' 'libgcc' 'sqlite')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/k4yt3x/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('a6c028e4031bbfc987860a6b2eb86cba63d75ae05c5093bcc9500fe83f3797c4')

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
