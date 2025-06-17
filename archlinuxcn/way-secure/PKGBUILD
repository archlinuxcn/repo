# Maintainer: Kimiblock Moe

pkgname="way-secure"
pkgver=0.2.0
pkgrel=1
pkgdesc='Create wayland security contexts'
arch=('x86_64')
url="https://git.sr.ht/~whynothugo/way-secure"
license=('ISC')
provides=()
depends=()
options=(lto)
makedepends=(git cargo rust)
source=(
	"$pkgname::git+https://git.sr.ht/~whynothugo/way-secure#tag=v${pkgver}"
)

function prepare() {
	cd "${pkgname}"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$CARCH-unknown-linux-gnu"
}

build() {
	cd "${pkgname}"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --release --frozen --all-features --locked
}

function package() {
	cd "${pkgname}"
	install -Dm 755 ./target/release/way-secure "${pkgdir}/usr/bin/way-secure"
}

sha256sums=('844d67b582f4d9e22d5bd0d11c80bbe25c21a58030bc6dfd3c2b65768754ce39')

