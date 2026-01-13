# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>

pkgname=python-cffsubr
_pyname=${pkgname#python-}
pkgver=0.4.0
pkgrel=2
pkgdesc='Standalone CFF subroutinizer based on AFDKO tx'
arch=(any)
url="https://github.com/adobe-type-tools/$_pyname"
license=(Apache-2.0)
depends=(afdko
         python
         python-fonttools)
makedepends=(python-{build,installer,wheel}
             python-setuptools-git-ls-files
             python-setuptools-scm)
checkdepends=(python-pytest)
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz"
        devendor-tx.patch)
sha256sums=('2c321b6807bd95856d921ed9dce8506495cf49fc7a89a63cb942e8bece13addd'
            '10ec393d97b10ab33ed475bcf6a2c9a5308ac1c82eccd1dd96c21f8e9da77e53')

prepare() {
	cd "$_archive"
	rm -rf external _custom_build
	patch -p0 -i ../devendor-tx.patch
}

build() {
	cd "$_archive"
	python -m build -wn
}

check() {
	cd "$_archive"
	export PYTHONPATH="./src"
	pytest tests
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
}
