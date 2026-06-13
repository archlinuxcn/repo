# Maintainer: graysky <therealgraysky AT protonmail DOT com>

pkgname=modprobed-db
pkgver=2.50
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
sha256sums=('8cd9b490896a5e1e3eddf9c5a7dd771de8627965ffad0ca6426d25c886d904ee')
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
