# Maintainer: graysky <therealgraysky AT protonmail DOT com>

pkgname=modprobed-db
pkgver=2.46
pkgrel=1
pkgdesc='Keeps track of EVERY kernel module ever used - useful for make localmodconfig'
arch=('any')
license=('MIT')
depends=('kmod')
optdepends=('sudo: needed for recall function')
replaces=('modprobed_db')
conflicts=('modprobed_db')
url="https://wiki.archlinux.org/index.php/Modprobed-db"
source=("$pkgname-$pkgver.tar.gz::https://github.com/graysky2/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('34a0cd3fa67efea8a2ba657d90ce2f5e3ef480babb7f3bcae6c13bac1eb4eeab')
install=readme.install

build() {
	cd "$pkgname-$pkgver"
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
	install -Dm644 MIT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
