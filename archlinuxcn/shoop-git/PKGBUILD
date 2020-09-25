# Maintainer: Jiachen YANG <farseerfc@gmail.com>

pkgname=shoop-git
_pkgname="shoop"
pkgdesc="high-speed encrypted file transfer tool reminiscent of scp, written in rust"
pkgver=0.1.1.210
pkgrel=1
arch=('x86_64')
conflicts=("${_pkgname}")
provides=("${_pkgname}")
url="https://github.com/mcginty/shoop"
license=('GPL2')
depends=("openssl")
optdepends=()
makedepends=('git' 'cargo')
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
	cd $_pkgname
	echo $(grep '^version =' Cargo.toml|head -n1|cut -d\" -f2).$(git rev-list --count HEAD)
}

build() {
	cd $_pkgname
	cargo build --release
}

check() {
	cd $_pkgname
	cargo test --release
}

package() {
	cd $_pkgname
	install -D -m755 "$srcdir/$_pkgname/target/release/shoop" "$pkgdir/usr/bin/shoop"
}
