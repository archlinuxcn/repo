# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=modcrawl
pkgver=0.9.1
pkgrel=1
pkgdesc="Detect, inspect, and analyze Minecraft mods and plugins from JARs"
arch=('x86_64')
url="https://github.com/SirCesarium/modcrawl"
license=('MIT')
depends=(libgcc glibc)
makedepends=(cargo zstd cbindgen)
provides=("lib$pkgname")
options=(!lto)
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('740454db987437a75eaa5bced14a5bc4cfc2a40e9119eafb2fac567dfcd47221')

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
    cbindgen --config cbindgen.toml --crate "$pkgname" --output "target/release/$pkgname.h"
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
    install -Dm644 -t "$pkgdir/usr/include/" "target/release/$pkgname.h"
    install -Dm644 -t "$pkgdir/usr/lib/" "target/release/lib$pkgname."{so,a}
}
