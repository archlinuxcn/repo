# Maintainer: Kimiblock Moe

pkgname=autopush-rs
pkgver=1.81.0
pkgrel=1
pkgdesc="Push Server in Rust"
arch=('x86_64')
provides=('autopush' 'autopush-rs' 'sunup-server')
conflicts=('autopush' 'autopush-rs' 'sunup-server')
url="https://github.com/mozilla-services/autopush-rs"
license=('MPL-2.0')
depends=('gcc-libs' 'openssl' 'pypy' 'libffi' 'grpc')
makedepends=('rustup' 'git' 'cmake3' 'python-virtualenv' 'clang')
options=(!lto)
source=("git+$url.git#tag=${pkgver}")
sha256sums=('ff90661db9d8476bf351ccf2efa909b81d5bf3d31dd94795cb04bef0eab8d63f')

prepare() {
	rustup default stable
	cd "$srcdir/autopush-rs"
	cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "$srcdir/autopush-rs"
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --target-dir target
}

package() {
	cd "$srcdir/autopush-rs"
	install -Dm755 "target/release/autoconnect" "$pkgdir/usr/bin/autoconnect"
	install -Dm755 "target/release/autoendpoint" -t "$pkgdir/usr/bin/"

	# These are missing
	#install -Dm755 "target/release/endpoint_diagnostic" -t "$pkgdir/usr/bin/"
	#install -Dm755 "target/release/autokey" -t "$pkgdir/usr/bin/"
}
