pkgname=ydcv-rs-git
_pkgname="ydcv-rs"
pkgdesc="A Rust version of ydcv."
pkgver=0.6.1.203
pkgrel=2
arch=('i686' 'x86_64')
conflicts=("ydcv")
provides=("ydcv")
url="https://github.com/farseerfc/ydcv-rs"
license=('GPL2')
depends=("openssl" "libdbus" "libxcb")
optdepends=()
makedepends=('git' 'cargo' 'python')
source=('git+https://github.com/farseerfc/ydcv-rs.git')
sha256sums=('SKIP')

#disable lto for https://github.com/briansmith/ring/issues/1444
options=('!lto')

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
