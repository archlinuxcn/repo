# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=modcrawl
pkgver=0.6.2
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
sha256sums=('03c72aa0536ddb32b29192eb183d5ccfad16708eb77b6a69ed21d51cd53b7717')

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
