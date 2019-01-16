pkgname=ydcv-rs-git
_pkgname="ydcv-rs"
pkgdesc="A Rust version of ydcv."
pkgver=0.3.11.120
pkgrel=1
arch=('i686' 'x86_64')
conflicts=("ydcv")
provides=("ydcv")
url="https://github.com/farseerfc/ydcv-rs"
license=('GPL2')
depends=("openssl" "libdbus" "libxcb")
optdepends=()
makedepends=('git' 'cargo' 'python')
source=('git://github.com/farseerfc/ydcv-rs.git')
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
	install -D -m755 "$srcdir/$_pkgname/target/release/ydcv-rs" "$pkgdir/usr/bin/ydcv"
}
