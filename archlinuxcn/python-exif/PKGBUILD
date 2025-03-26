# Maintainer: Caleb Maclennan <caleb@alerque.com>

_py_name=exif
pkgname=python-$_py_name
pkgver=1.6.1
pkgrel=2
pkgdesc='Read and modify image EXIF metadata'
arch=(any)
url="https://gitlab.com/TNThieding/$_py_name"
license=(MIT)
_pydeps=(plum)
depends=(python
         "${_pydeps[@]/#/python-}")
_archive="$_py_name-$pkgver"
makedepends=(python-{build,installer,wheel}
             python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_py_name::1}/$_py_name/$_archive.tar.gz")
sha256sums=('763599b89b9b67495713060a703f32d1874abf8f0628c9d77711c2c06a5f44c8')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
