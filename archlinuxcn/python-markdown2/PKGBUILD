# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jakob Matthes <jakob.matthes@gmail.com>

pkgname=python-markdown2
pkgver=2.3.9
pkgrel=1
pkgdesc='A fast and complete implementation of Markdown in Python'
url="https://github.com/trentm/$pkgname"
license=('MIT')
arch=('any')
depends=('python')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tgz::$url/archive/${pkgver}.tar.gz")
sha256sums=('dc2fa66e2866dd9fcbecd98fbcd3d3f8a3edc0bf7ff28ee2d5435dd0fbca6f38')

build() {
	cd "$pkgname-$pkgver"
	python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
