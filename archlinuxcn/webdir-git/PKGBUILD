pkgname=webdir-git
pkgver=0.1.0.68.g78f51b3
pkgrel=1
pkgdesc="A simple asynchronous static file server"
arch=('x86_64' 'i686')
url="https://github.com/Tyzzer/webdir"
license=('MIT')
depends=()
makedepends=('cargo')
optdepends=()
provides=('webdir')
conflicts=('webdir')
source=($pkgname::git+https://github.com/Tyzzer/webdir)
sha256sums=('SKIP')

pkgver() {
	cd $pkgname
	echo $(grep '^version =' Cargo.toml|head -n1|cut -d\" -f2).$(git rev-list --count HEAD).g$(git describe --always)
}

build() {
	cd $pkgname
	cargo build --release --features sendfile
}

package() {
	cd $pkgname
	install -D -m755 "$srcdir/$pkgname/target/release/webdir" "$pkgdir/usr/bin/webdir"
}
