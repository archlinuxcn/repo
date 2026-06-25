# Maintainer: Kimiblock Moe

pkgname=bawn
pkgver=0.0.2
pkgrel=1
pkgdesc='Bawn is a transient Portable sandbox generator'
url='https://github.com/Kimiblock/bawn'
license=(GPL-3.0-or-later)
makedepends=('cargo' 'git')
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=(git+https://github.com/Kimiblock/bawn.git#tag=${pkgver})
sha256sums=('c1498fcbec4c0f227466f4434b768e78d43860a75e7b57a69991b4870eab60e1')
depends=(glibc libgcc)

prepare() {
	cd bawn
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd bawn
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
}

check() {
	cd bawn
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	package+=(portable)
	cd bawn
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/bawn"
	# for custom license, e.g. MIT
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
