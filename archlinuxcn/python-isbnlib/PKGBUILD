# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Francois Boulogne <fboulogne@april.org>

_pipname=isbnlib
pkgname=python-$_pipname
pkgver=3.10.14
pkgrel=4
pkgdesc='Extract, clean, transform, hyphenate and metadata for ISBNs'
arch=(any)
url="https://pypi.python.org/pypi/$_pipname"
license=(LGPL-3.0-only)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools)
_archive="$_pipname-$pkgver"
source=("https://github.com/xlcnd/$_pipname/archive/v$pkgver/$_archive.tar.gz")
sha256sums=('2aaed501b34a72c2f018b245358c0ef15772c1f3b9c2a8f407194e209b0f5804')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
