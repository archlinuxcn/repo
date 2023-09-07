# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-xmldiff
_pyname=${pkgname#python-}
pkgver=2.6.3
pkgrel=1
pkgdesc='A libray and command line utility for diffing xml'
arch=(any)
url="https://$_pyname.readthedocs.io"
license=(BSD)
depends=(python
         python-lxml
         python-six)
makedepends=(python-{build,installer,wheel}
             python-setuptools)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('19b030b3fa37d1f0b5c5ad9ada9059884c3bf2c751c5dd8f1eb4ed49cfe3fc60')

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	python -m unittest discover
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.txt
}
