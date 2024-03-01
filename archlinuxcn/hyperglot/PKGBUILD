# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=hyperglot
pkgver=0.6.1
pkgrel=1
pkgdesc='A database and tools for detecting language support in fonts'
arch=(any)
url="https://github.com/rosettatype/$pkgname"
license=(GPL-3.0-only)
_py_deps=(click
          colorlog
          fonttools
          unicodedata2
          yaml)
depends=(python
         "${_py_deps[@]/#/python-}")
makedepends=(python-{build,installer,wheel}
             python-setuptools)
_archive="$pkgname-$pkgver"
source=("$_archive.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('9f959bd8b497bc91749f7e66fd8f6e49c85ef65035143c29f0b6af896a8f4ce7')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
