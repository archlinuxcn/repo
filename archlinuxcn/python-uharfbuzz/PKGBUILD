# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=uharfbuzz
pkgname=python-$_pyname
pkgver=0.39.3
pkgrel=1
pkgdesc='Streamlined Cython bindings for the harfbuzz shaping engine'
arch=(x86_64)
url="https://github.com/harfbuzz/$_project"
license=(Apache-2.0)
depends=(python)
makedepends=(cython
             python-{build,installer,wheel}
             python-setuptools-scm
             python-scikit-build)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.zip")
sha256sums=('1102d9fd371cdea6a859be380a3cc554237f4cf2933bc09e98aceaeae8a42229')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	pytest
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
