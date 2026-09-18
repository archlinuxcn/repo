# Maintainer: Kimiblock Moe

pkgname=portable-packer
pkgver=1.0.4
pkgrel=1
pkgdesc="Packaging utility for Portable"
arch=("x86_64")
url="https://github.com/Kimiblock/stashpak"
license=("GPL-3.0-or-later")
depends=("glibc" coreutils desktop-file-utils git)

makedepends=('rust' 'git')
checkdepends=(portable)
backup=()
source=("source::git+https://github.com/Kimiblock/portable-packer.git#tag=${pkgver}")
sha256sums=('326ebe33ab7122abe01caeac5c701f3287e096cd6f925d5f49603d4de066a05d')

conflicts+=("portable<14.99")

function prepare() {
	cd source
	git submodule update --init --recursive
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

function build() {
	cd source
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release
}

function check() {
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cd source
	cargo test --frozen
}

function package() {
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	install \
		-vDm755 \
		"${srcdir}/source/target/release/portable-packer" \
		"${pkgdir}/usr/bin/portable-packer"
}
