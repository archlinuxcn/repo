# Maintainer: Kimiblock Moe
# Contributor: AlphaLynx

pkgname=continuwuity
pkgdesc="a very cool, featureful fork of conduit (rust matrix homeserver)"
url="https://forgejo.ellis.link/continuwuation/continuwuity"
license=("Apache-2.0")
arch=("x86_64" "aarch64")
pkgver=26.7.3
pkgrel=1
epoch=2
makedepends=("rust" "cargo" "git" "clang")
depends=("gcc-libs" "glibc" "liburing" "jemalloc" "zstd")
source=("git+https://forgejo.ellis.link/continuwuation/continuwuity.git#tag=v$(echo ${pkgver} | sed 's|_|-|g')")
sha256sums=('fe6f8b9dfe76f71a3177fbaa29239da150cb928fba5a9ce6e56f9f414978cb15')
provides=("conduwuit" "continuwuity")
conflicts=("conduwuit" "continuwuity")
options=(!lto)
backup=("etc/conduwuit/conduwuit.toml")

#function pkgver() {
#	cd continuwuity
#	echo "$(grep '^version =' Cargo.toml|head -n1|cut -d\" -f2|cut -d\- -f1).$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
#}

function prepare() {
	export JEMALLOC_OVERRIDE=/usr/lib/libjemalloc.so
	export CARGO_FEATURE_UNPREFIXED_MALLOC_ON_SUPPORTED_PLATFORMS=1
	export ZSTD_SYS_USE_PKG_CONFIG=1
	cd "${srcdir}/continuwuity"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
	export CONDUWUIT_VERSION_EXTRA=$(git rev-parse --short HEAD)
}

function build() {
	export JEMALLOC_OVERRIDE=/usr/lib/libjemalloc.so
	export CARGO_FEATURE_UNPREFIXED_MALLOC_ON_SUPPORTED_PLATFORMS=1
	export ZSTD_SYS_USE_PKG_CONFIG=1
	cd "${srcdir}/continuwuity"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --locked
}

function check() {
	export JEMALLOC_OVERRIDE=/usr/lib/libjemalloc.so
	export CARGO_FEATURE_UNPREFIXED_MALLOC_ON_SUPPORTED_PLATFORMS=1
	export ZSTD_SYS_USE_PKG_CONFIG=1
	cd "${srcdir}/continuwuity"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --locked
}

function package() {
	install -Dm755 "${srcdir}/continuwuity/target/release/conduwuit" "${pkgdir}/usr/bin/conduwuit"
	install -Dm644 "${srcdir}/continuwuity/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	install -Dm600 "${srcdir}/continuwuity/conduwuit-example.toml" "${pkgdir}/etc/conduwuit/conduwuit.toml"
	install -Dm644 "${srcdir}/continuwuity/pkg/conduwuit.service" "${pkgdir}/usr/lib/systemd/system/continuwuity.service"
}
