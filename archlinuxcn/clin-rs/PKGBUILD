# Maintainer: Integral <integral@archlinuxcn.org>

pkgname=clin-rs
pkgver=0.13.2
pkgrel=1
pkgdesc="Feature-packed TUI note management app inspired by Obsidian"
arch=('x86_64' 'aarch64' 'riscv64')
url="https://github.com/reekta92/${pkgname}"
license=('GPL-3.0-only')
depends=('glibc' 'hicolor-icon-theme' 'libgcc' 'libgit2')
makedepends=('cargo')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('7a0ae7c0f60d81b05ac3e9f08981642838bd89f2c14ad421f846b093cc7d13ce')
options=('!lto')

prepare() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export LIBGIT2_NO_VENDOR=1
	cargo build --frozen --release --all-features
}

check() {
	cd "${pkgname}-${pkgver}/"
	export RUSTUP_TOOLCHAIN=stable
	export LIBGIT2_NO_VENDOR=1
	cargo test --frozen --all-features
}

package() {
	cd "${pkgname}-${pkgver}/"
	install -Dm755 target/release/clin -t "${pkgdir}/usr/bin/"
	install -Dm644 assets/clin.desktop -t "${pkgdir}/usr/share/applications/"
	install -Dm644 assets/clin.png -t "${pkgdir}/usr/share/icons/hicolor/256x256/apps/"
	install -Dm644 {README,CHANGELOG}.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
}
