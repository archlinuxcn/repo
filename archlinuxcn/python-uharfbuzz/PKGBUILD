# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=uharfbuzz
pkgname=python-$_pyname
pkgver=0.51.2
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
sha256sums=('f5f344668155502bfdc68b0f4bf4ee683d956ec9a31467a597b9f3c0312d638d')

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
