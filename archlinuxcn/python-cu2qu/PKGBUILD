# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

_pyname=cu2qu
pkgname=python-$_pyname
pkgver=1.6.7.post2
pkgrel=4
pkgdesc='Cubic-to-quadratic bezier curve conversion'
arch=(any)
url="https://github.com/googlefonts/$_pyname"
license=(Apache-2.0)
_pydeps=(defcon
         fonttools
         fs)
depends=(python
         "${_pydeps[@]/#/python-}")
makedepends=(cython
             python-{build,installer,wheel}
             python-setuptools-scm)
checkdepends=(python-coverage
              python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.zip")
sha256sums=('1df562d99bd6059226088f443702bf51cfdd8cc63623f23137459a78d7bf5808')

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	# Wants deprecated pytest-runner stuff
	# pytest
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}

