# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-cffsubr
_pyname=${pkgname#python-}
pkgver=0.2.9.post1
pkgrel=2
pkgdesc='Standalone CFF subroutinizer based on AFDKO tx'
arch=(x86_64)
url="https://github.com/adobe-type-tools/$_pyname"
license=(Apache)
depends=(python
         python-fonttools)
makedepends=(python-{build,installer,wheel}
             python-setuptools-git-ls-files
             python-setuptools-scm)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('6b31412dcf49c8fa84664bda867e2eddc55b6fe6fa696ff253c4f13a9ff2fc5c')

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	local _pyver=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
	export PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$_pyver"
	pytest tests
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
