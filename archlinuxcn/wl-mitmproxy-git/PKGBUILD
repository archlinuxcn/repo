# Maintainer: Vita Yuzu <vita.yuzupon at gmail dot com>
pkgname=wl-mitmproxy-git
pkgver=v0.1.0.r4.g1302e7e
pkgrel=4
pkgdesc="Wayland intercepting proxy for modifying protocol messages"
arch=('x86_64')
url="https://github.com/5andr0/wl-mitmproxy"
license=('GPL-3.0-only' 'MIT' 'Apache-2.0')
depends=('gcc-libs' 'glibc')
makedepends=('cargo' 'git')
options=('!lto')
provides=('wl-mitmproxy')
conflicts=('wl-mitmproxy')
source=("$pkgname::git+https://github.com/5andr0/wl-mitmproxy.git")
sha256sums=('SKIP')

pkgver() {
	cd "$pkgname"
	git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "$pkgname"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --locked --target host-tuple
}

build() {
	cd "$pkgname"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	export RUSTFLAGS="-C force-frame-pointers=yes"
	cargo build --frozen --release
}

package() {
	cd "$pkgname"
	install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/wl-mitmproxy"

	install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	install -Dm0644 crates/wl-mitmproxy/LICENSE-MIT \
		"$pkgdir/usr/share/licenses/$pkgname/LICENSE-MIT"
	install -Dm0644 crates/wl-mitmproxy/LICENSE-APACHE \
		"$pkgdir/usr/share/licenses/$pkgname/LICENSE-APACHE"
}
