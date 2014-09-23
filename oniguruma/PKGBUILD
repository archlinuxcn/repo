# Contributor: Andreas Wagner <Andreas dot Wagner at em dot uni-frankfurt dot de>
# Contributor: Massimiliano Torromeo <massimiliano.torromeo@gmail.com>

pkgname=oniguruma
pkgver=5.9.5
pkgrel=1
pkgdesc="a regular expressions library"
arch=('i686' 'x86_64')
url="http://www.geocities.jp/kosako3/oniguruma/"
license=('BSD')
options=(!libtool)
source=("http://www.geocities.jp/kosako3/oniguruma/archive/onig-$pkgver.tar.gz")

build() {
	cd "$srcdir/onig-$pkgver"
	./configure --prefix=/usr
	make
}

package() {
	cd "$srcdir/onig-$pkgver"
	make DESTDIR="$pkgdir" install
}

md5sums=('970f98a4cd10021b545d84e34c34aae4')
