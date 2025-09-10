# Maintainer: Kimiblock Moe

pkgname=autopush-rs
pkgver=1.75.10
pkgrel=2
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
sha256sums=('824459fb6b5e095907acecfee0df156ec3a62ee76c7eb20fcffcc54436dac8e8')

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
