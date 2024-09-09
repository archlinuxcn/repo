# Maintainer: opale95
# Contributor: Namarrgon
pkgname=lebiniou-data
pkgver=3.67.0
pkgrel=1
pkgdesc="Data files for lebiniou"
arch=('any')
url="https://biniou.lenain.info/"
license=('GPL')
source=("https://gitlab.com/lebiniou/lebiniou-data/-/archive/version-$pkgver/lebiniou-data-version-$pkgver.tar.gz")
sha256sums=('19b83dbcbf60cdc5ab6dd9cf42cd1442d32075219c70553b2b3d7bf05acac81c')

build() {
	cd "$pkgname-version-$pkgver"

	./bootstrap
	./configure --prefix=/usr
}

package() {
	cd "$pkgname-version-$pkgver"

	make DESTDIR="$pkgdir/" install
}

