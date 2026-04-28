# Maintainer: Jax Young <jaxvanyang@gmail.com>
pkgname=dotbackup
_name="$pkgname.rs"
pkgver=2.1.0
pkgrel=1
pkgdesc='Dotfile backup utility'
arch=('x86_64')
url='https://github.com/jaxvanyang/dotbackup.rs'
license=('MIT')
depends=('gcc-libs' 'glibc')
makedepends=('cargo' 'just' 'scdoc')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('6a3b54932044c8dbc3f5fa4c7cb2b2a6d1d90d46c11168b74234e757c93f553b')

prepare() {
	cd "$_name-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
	cd "$_name-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	cargo build --frozen --release --all-features
	just doc
}

check() {
	cd "$_name-$pkgver"
	export RUSTUP_TOOLCHAIN=stable
	cargo test --frozen --all-features
}

package() {
	cd "$_name-$pkgver"
	just prefix="$pkgdir/usr" install
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
