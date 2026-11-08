# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=modcrawl
pkgver=0.12.4
pkgrel=1
pkgdesc="Detect, inspect, and analyze Minecraft mods and plugins from JARs"
arch=('x86_64')
url="https://github.com/SirCesarium/modcrawl"
license=('MIT')
depends=(libgcc glibc)
makedepends=(cargo zstd)
options=(!lto)
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('c4cd8518c58d4a2149e97468ca32f8fd803eaf14333382a993aa04cdbf85b5ae')

prepare() {
	cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target host-tuple
}

build() {
	cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features
}

check() {
	cd "$pkgname-$pkgver"
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
	cd "$pkgname-$pkgver"
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
