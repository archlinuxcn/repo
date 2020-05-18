# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Jakob Matthes <jakob.matthes@gmail.com>

pkgname=python-markdown2
pkgver=2.3.8
pkgrel=2
pkgdesc='A fast and complete implementation of Markdown in Python'
url="https://github.com/trentm/$pkgname"
license=('MIT')
arch=('any')
depends=('python')
makedepends=('python-setuptools')
source=("$pkgname-$pkgver.tgz::$url/archive/${pkgver}.tar.gz")
sha256sums=('8cfd0738fc63e59fd895715c4c53e3b9024070d1497f7fa1bde7468f04f23c27')

build() {
	cd "$pkgname-$pkgver"
	python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
