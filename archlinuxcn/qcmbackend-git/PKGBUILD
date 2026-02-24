# Maintainer: Integral <integral@member.fsf.org>

pkgname=qcmbackend-git
_pkgname=${pkgname%-git}
pkgver=r217.5bfb635
pkgrel=2
pkgdesc="Qcm backend with Rust"
url="https://github.com/hypengw/QcmBackend"
arch=('x86_64' 'aarch64' 'riscv64')
license=('MPL-2.0')
depends=('protobuf' 'openssl' 'libgcc' 'sqlite')
makedepends=('git' 'cargo')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
	cd QcmBackend
	(
		set -o pipefail
		git describe --long --abbrev=7 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
			printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
	)
}

prepare() {
	cd QcmBackend
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd QcmBackend
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	CFLAGS+=" -ffat-lto-objects" cargo build --frozen --release --all-features
}

check() {
	cd QcmBackend
	export RUSTUP_TOOLCHAIN=stable
	export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
	CFLAGS+=" -ffat-lto-objects" cargo test --frozen --all-features --workspace
}

package() {
	install -Dm755 QcmBackend/target/release/QcmBackend -t "${pkgdir}/usr/bin/"
}
