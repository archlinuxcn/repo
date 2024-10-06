# Maintainer: Yigid BALABAN <fyb at fybx.dev> 
pkgname=protoc-gen-prost
pkgver=0.3.1
pkgrel=1
pkgdesc="Protocol Buffers compiler plugin powered by Prost!"
arch=('any')
url="https://github.com/neoeinstein/protoc-gen-prost"
license=('Apache-2.0')
depends=(protobuf)
makedepends=(cargo)
provides=(protoc-gen-prost)
source=("$pkgname-$pkgver.tar.gz"::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate)
sha256sums=('e810847124cb9a1d4ccefb1aabc80ccaba67f4af047e60dc1c0f2e145494bb85')

prepare() {
	cd "$pkgname-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
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
}
