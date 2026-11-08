# Maintainer: graysky <therealgraysky AT protonmail DOT com>

pkgname=modprobed-db
pkgver=2.52
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
sha256sums=('bc721402a728a397e49c30d748e05f3fd63454bee3211110c3cb351d92952fcc')
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
