# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=uharfbuzz
pkgname=python-$_pyname
pkgver=0.53.6
pkgrel=1
pkgdesc='Streamlined Cython bindings for the harfbuzz shaping engine'
arch=(x86_64)
url="https://github.com/harfbuzz/$_project"
license=(Apache-2.0)
depends=(python)
makedepends=(cython
             python-{build,installer,wheel}
             python-pkgconfig
             python-setuptools-scm
             python-scikit-build)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('d5bbf33ea5bcb0bfda5436e2ada91b39d4a63cc29fa81022932209aafefba28e')

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
